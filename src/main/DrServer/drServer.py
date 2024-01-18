import asyncio
import copy
import datetime
import json
import socket
import threading
import time

import chardet
import websockets
from PyQt5.QtCore import pyqtSignal, QObject

import Util.drone_vo as drone_vo
import Util.logger as logger

BUFFER_SIZE = 8196
URI = "socketUrl"  # 웹 소켓 클라이언트 접속

LOOP = asyncio.get_event_loop()


class WebSocketClient:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.ws = None
        self.flg_ws_status = False
        self.flg_conn = False
        self.lock = asyncio.Lock()
        LOOP.run_until_complete(self.connect())

    """async def connect(self):
        try:
            async with self.lock:
                if self.ws is not None:
                    if self.ws.open:
                        return

                    if not self.flg_conn:
                        self.flg_conn = True
                        self.ws = await websockets.connect(URI)
                        while True:
                            if self.ws.open:
                                self.flg_ws_status = True
                                self.flg_conn = False
                                break
                            else:
                                self.ws = await websockets.connect(URI)
                                await asyncio.sleep(1)
                else:
                    if not self.flg_conn:
                        self.flg_conn = True
                        self.ws = await websockets.connect(URI)
                        while True:
                            if self.ws.open:
                                self.flg_ws_status = True
                                self.flg_conn = False
                                break
                            else:
                                self.ws = await websockets.connect(URI)
                                await asyncio.sleep(1)

        except Exception as e:
            self.flg_conn = False
            self.flg_ws_status = False
            print(e)
            """

    async def connect(self):
        async with self.lock:
            if self.ws is not None and self.ws.open:
                # 이미 열린 연결이 있으므로 반환
                return

            if self.flg_conn:
                # 이미 연결 시도 중이므로 반환
                return

            # 연결 시도 플래그 설정
            self.flg_conn = True
            retry_count = 5  # 연결 시도 횟수

            for _ in range(retry_count):
                try:
                    # 웹 소켓의 통로가 열려 있다면 닫고
                    # if self.ws is not None and not self.ws.closed:
                    #     self.ws.close()

                    self.ws = await websockets.connect(URI)
                    if self.ws.open:
                        self.flg_ws_status = True
                        break
                except Exception as e:
                    if self.ws is not None and not self.ws.closed:
                        await self.close_connect()
                    print(f"연결 중 오류 발생: {e}")
                await asyncio.sleep(1)  # 1초 후 재시도

            # 연결 시도 플래그 해제
            self.flg_conn = False

    async def send(self, _original_data):
        if self.ws and self.ws.open and self.flg_ws_status and not self.ws.closed:
            try:
                data_str = json.dumps(_original_data)
                await self.ws.send(data_str)
            except Exception as e:
                if self.ws is not None and not self.ws.closed:
                    await self.close_connect()
                print(e)
        else:
            await self.connect()
            if self.ws and self.ws.open and self.flg_ws_status and not self.ws.closed:
                try:
                    data_str = json.dumps(_original_data)
                    await self.ws.send(data_str)
                except Exception as e:
                    if self.ws is not None and not self.ws.closed:
                        await self.close_connect()
                    print(e)

    async def receive(self):
        return await self.ws.recv()

    async def close_connect(self):
        await self.ws.close()


class DroneServer(QObject):
    # GUI 시그널 생성
    update_log_view = pyqtSignal(str, str)
    update_append_except_log = pyqtSignal(str, str)

    def __init__(self, ui):
        super().__init__()
        self.client_sockets = []  # 서버에 접속 되어 있는 클라이언트 정보
        self.ui = ui
        self.now = ""
        self.lock = asyncio.Lock()
        self.ws_client = WebSocketClient.instance()
        self.lock = threading.Lock()

    def send_json_data(self, json_data):
        LOOP.run_until_complete(self.ws_client.send(json_data))

    def read_response_messge(self):
        return LOOP.run_until_complete(self.ws_client.receive())

    def tcp_threaded(self, client_socket, addr, name):
        print('>> 연결된 드론의 주소:', addr[0])
        drone_id = []
        log = logger.Logger(name)
        self.now = datetime.datetime.now()
        dr_vo = []
        one_fist_update = False

        organization_map = {
            'DUSI': '두시텍',

        }

        dr_id = {
            'DUSI': 'dst_01',

        }

        # 클라이언트가 접속을 끊을 때 까지 반복
        while True:
            try:
                # 데이터 수신
                data = client_socket.recv(BUFFER_SIZE)

                if not data:
                    print(f'>> 클라이언트와 연결이 종료되었습니다 IP 정보 {addr[0]}')
                    break
                try:
                    jsons = self.split_jsons(data)
                    if jsons == "":
                        continue

                    if len(jsons) > 1:
                        if isinstance(jsons, bytes):
                            result = chardet.detect(jsons)
                            data_str = jsons.decode(result['encoding'])
                        else:
                            data_str = jsons

                        for index, item in enumerate(data_str):
                            dict_data = json.loads(item)
                            fist_key = list(dict_data.keys())[0]

                            value = ''
                            if dict_data.get('msg') != '':
                                value = dict_data.get('msg')

                            original_data = copy.deepcopy(dict_data)
                            dict_data['ip_addr'] = addr[0]

                            if fist_key == "drone_stat" or value == 'flight_info':
                                self.status_thread_start(name, original_data, dict_data, addr, drone_id,
                                                         organization_map, dr_id, dr_vo)

                            if fist_key == "mission_info" or value == 'mission_file':
                                self.mission_thread_start(name, original_data, dict_data, organization_map, dr_id,
                                                          dr_vo)
                    elif len(jsons) <= 1:
                        # 데이터를 JSON 형식으로 파싱 작업
                        # 데이터 인코딩 추정
                        result = chardet.detect(data)
                        if result == "":
                            continue
                        data_str = data.decode(result['encoding'])
                        dict_data = json.loads(data_str)

                        # 필요 데이터 변수 저장
                        fist_key = list(dict_data.keys())[0]
                        value = dict_data.get('msg')
                        original_data = copy.deepcopy(dict_data)
                        dict_data['ip_addr'] = addr[0]

                        if fist_key == "drone_stat" or value == 'flight_info':
                            self.status_thread_start(name, original_data, dict_data, addr, drone_id, organization_map,
                                                     dr_id, dr_vo)

                        elif fist_key == "mission_info" or value == 'mission_file':
                            self.mission_thread_start(name, original_data, dict_data, organization_map, dr_id, dr_vo)

                    if dr_vo and one_fist_update is not True:
                        log.fist_update_json(self.now, dr_vo)
                        one_fist_update = True

                    time.sleep(1)

                except (ValueError, TypeError, KeyError, socket.timeout, Exception) as e:
                    result = chardet.detect(data)
                    data_str = data.decode(result['encoding'])
                    print("data_str ERROR: ", data_str)
                    self.update_log_view.emit(organization_map[name], str(log.json_data))
                    self.update_append_except_log.emit(str(e), addr[0])
                    log.log_exception(e)
                    continue

            except (ConnectionResetError, socket.timeout) as e:
                print(f'>> 연결이 끊겼습니다 IP 정보 {addr[0]}')
                self.update_append_except_log.emit(str(e), addr[0])
                self.del_drone_info(name, self.ui)
                log.log_exception(e)
                log.logger.shutdown()
                break

        if client_socket in self.client_sockets:
            try:
                self.client_sockets.remove(client_socket)
                self.ui.delete_item(drone_id)
                self.del_drone_info(name, self.ui)
                print(f'클라이언트와 연결이 종료되었습니다 남은 클라이언트 리스트 : {len(self.client_sockets)}')
                log.log_exception('클라이언트와 연결이 종료되었습니다.')
            except Exception as e:
                log.log_exception(e)
                self.update_append_except_log.emit(str(e), addr[0])
                # log.end_update_json(self.now, dr_vo)
                # self.ui.append_except_log(e, addr[0])
                print("tcp_threaded Exception", e)

    def udp_threaded(self, _data, addr, name):
        drone_id = []
        log = logger.Logger(name)
        self.now = datetime.datetime.now()
        dr_vo = []
        one_fist_update = False

        organization_map = {
            'DUSI': '두시텍',

        }

        dr_id = {
            'DUSI': 'dst_01',

        }

        try:

            try:
                dict_data = json.loads(_data)
                value = ''
                if dict_data.get('msg') != '':
                    value = dict_data.get('msg')

                fist_key = list(dict_data.keys())[0]
                original_data = copy.deepcopy(dict_data)
                dict_data['ip_addr'] = addr[0]

                if fist_key == "drone_stat" or value == 'flight_info':
                    self.status_thread_start(name, original_data, dict_data, addr, drone_id, organization_map, dr_id,
                                             dr_vo)

                if fist_key == "mission_info" or value == 'mission_file':
                    self.mission_thread_start(name, original_data, dict_data, organization_map, dr_id, dr_vo)

                if dr_vo and one_fist_update is not True:
                    log.fist_update_json(self.now, dr_vo)

                # if len(drone_id) > 0:
                #     self.ui.delete_item(drone_id)
                # self.del_drone_info(name, self.ui)
                time.sleep(1)

            except (ValueError, TypeError, KeyError, socket.timeout, Exception) as e:
                self.update_append_except_log.emit(str(e), addr[0])
                # self.ui.append_except_log(e, addr[0])
                log.log_exception(e)

        except (ConnectionResetError, socket.timeout) as e:
            print(f'>> 연결이 끊겼습니다 IP 정보 {addr[0]}')
            self.update_append_except_log.emit(str(e), addr[0])
            # self.ui.append_except_log(e, addr[0])
            self.del_drone_info(name, self.ui)
            # log.end_update_json(self.now, dr_vo)
            log.log_exception(e)
            log.logger.shutdown()

        if _data in self.client_sockets:
            try:
                self.client_sockets.remove(_data)
                self.ui.delete_item(drone_id)
                self.del_drone_info(name, self.ui)
                print(f'클라이언트와 연결이 종료되었습니다 남은 클라이언트 리스트 : {len(self.client_sockets)}')
                log.log_exception('클라이언트와 연결이 종료되었습니다.')
            except Exception as e:
                log.log_exception(e)
                self.update_append_except_log.emit(str(e), addr[0])
                # self.ui.append_except_log(e, addr[0])
                print("udp_threaded Exception", e)

    """
    수신 받는 데이터의 버퍼가 상수 BUFFER_SIZE 보다 사이즈가 클때 data 변수에 나머지 데이터들을 넣음
    """

    def recevie_data(self, client_socket):
        data = b""
        while True:
            part = client_socket.recv(BUFFER_SIZE)
            data += part
            if len(part) < BUFFER_SIZE:
                break
        return data

    def split_jsons(self, data):
        try:
            jsons = []

            result = chardet.detect(data)
            data_str = data.decode(result['encoding'])

            bracket_count = 0
            start = 0
            i = 0
            length = len(data_str)

            while i < length:
                char = data_str[i]
                if char == '{':
                    if bracket_count == 0:
                        start = i
                    bracket_count += 1
                elif char == '}':
                    bracket_count -= 1
                    if bracket_count == 0:
                        jsons.append(data_str[start:i + 1])
                i += 1

            return jsons

        except Exception as e:
            # debugPrint(this=self.split_jsons)
            print(e)

    """
    Drone state thread Start
    """

    def mission_thread_start(self, name, original_data, dict_data, organization_map, dr_id, dr_vo):
        logs = logger.Logger(name)
        logs.json_data = original_data
        # db_conn = db.Db_conn()
        drone_mission_vo = drone_vo.DroneMissionVo()
        drone_mission_threading = threading.Thread(target=self.process_drone_mission_info,
                                                   args=(dict_data,
                                                         original_data,
                                                         drone_mission_vo,
                                                         logs,
                                                         organization_map,
                                                         name,
                                                         dr_id,
                                                         dr_vo))
        drone_mission_threading.daemon = True
        drone_mission_threading.start()

    def status_thread_start(self, name, original_data, dict_data, addr, drone_id, organization_map, dr_id, dr_vo):
        logs = logger.Logger(name)
        logs.json_data = original_data
        drone_vos = drone_vo.Drone_Vo()
        drone_flight_threading = threading.Thread(target=self.process_drone_flight_info,
                                                  args=(dict_data,
                                                        original_data,
                                                        name,
                                                        addr,
                                                        drone_id,
                                                        drone_vos,
                                                        logs,
                                                        organization_map,
                                                        dr_id,
                                                        dr_vo))
        drone_flight_threading.daemon = True
        drone_flight_threading.start()
        drone_flight_threading.join()

    def process_drone_flight_info(self, dict_data, original_data, name, addr, drone_id, drone_vos, log,
                                  organization_map, dr_id, dr_vo):
        try:
            drone_data = dict_data['drone_stat'][0]

            self.name_value_check(name, drone_data, original_data, organization_map, dr_id,
                                  self.process_drone_flight_info)

            with self.lock:
                self.send_json_data(original_data)

            # 최초에 한번만 addItem 함수를 통해 데이터의 기본 정보를 넘겨주어, hidden value 값을 추가하는 작업 Hidden value는 값을 삭제할때 사용하기 위함
            # 이 작업이 GUI에서 Organization, User_ID, Drone_id, IP Addr, 으로 추가 됨
            if len(drone_id) <= 0 and name != 'N':
                drone_id.append(drone_data)
                drone_id.append(addr[0])
                drone_id.append(name)
                self.ui.addItem(drone_id)

            if len(self.ui.drone_log) <= 0 or all(
                    name not in drone_log_item for drone_log_item in self.ui.drone_log):
                temp = {name: drone_data}
                self.ui.drone_log.append(temp)

            dr_id = drone_data['drone_id']
            dr_user = drone_data['user_id']
            dr_uid = drone_data['data_uid']

            dr_flight_mod = drone_data['flight_mode']
            dr_lat = drone_data['lat']
            dr_lon = drone_data['lon']
            dr_rel_alt = drone_data['rel_alt']
            dr_msl_alt = drone_data['msl_alt']
            dr_speed = drone_data['speed']
            dr_roll = drone_data['roll']
            dr_pitch = drone_data['pitch']
            dr_heading = drone_data['heading']
            dr_battery = drone_data['battery']
            dr_status = drone_data['status']

            # vo 객체 초기화
            drone_vos.set_data_uid(dr_uid)
            drone_vos.set_dr_id(dr_id)
            drone_vos.set_user_id(dr_user)
            drone_vos.set_flight_mode(dr_flight_mod)
            drone_vos.set_lat(dr_lat)
            drone_vos.set_lon(dr_lon)
            drone_vos.set_rel_alt(dr_rel_alt)
            drone_vos.set_msl_alt(dr_msl_alt)
            drone_vos.set_speed(dr_speed)
            drone_vos.set_status(dr_status)

            if 'roll' in drone_data:
                drone_vos.set_roll(dr_roll)

            if 'pitch' in drone_data:
                drone_vos.set_pitch(dr_pitch)

            if 'heading' in drone_data:
                drone_vos.set_heading(dr_heading)

            drone_vos.set_battery(dr_battery)
            drone_vos.set_addr(addr[0])

            self.update_log_view.emit(organization_map[name], str(log.json_data))
            if name != 'N':
                self.add_drone_info(name, drone_vos, self.ui, addr[0])

            # self.ui.append_log(organization_map[name], str(log.json_data))

            log.vo = drone_vos
            if len(dr_vo) <= 0:
                dr_vo.append(drone_vos)
            make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
            make_json_thread.daemon = True
            make_json_thread.start()
            # db_conn.insert_dr_info(drone_vos, log.file_path)
            log_info_thread = threading.Thread(target=log.log_info)
            log_info_thread.daemon = True
            log_info_thread.start()

            # "할당 해제"
            # make_json_thread.join()
            # log_info_thread.join()

        except Exception as e:
            print("process_drone_flight_info Exception", e)

    """
    Drone state thread Stop
    """

    """
    Drone Mission start
    """

    def process_drone_mission_info(self, dict_data, original_data, drone_mission_vo, log,
                                   organization_map, name, dr_id, dr_vo):
        mission_info = dict_data['mission_info'][0]

        self.name_value_check(name, mission_info, original_data, organization_map, dr_id,
                              self.process_drone_mission_info)

        mi_time = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

        original_data['mission_info'][0]['mi_time'] = mi_time
        original_data['mission_info'][0]['mi_name'] = f"{name}_{mi_time}"
        original_data['mission_info'][0]['mi_desc'] = f"{name}_MISSION"

        with self.lock:
            self.send_json_data(original_data)

        drone_mission_vo.set_dr_id(mission_info['drone_id'])
        drone_mission_vo.set_user_id(mission_info['user_id'])
        drone_mission_vo.set_mi_time(mission_info['mi_time'])
        drone_mission_vo.set_mi_name(mission_info['mi_name'])

        if mission_info['mi_desc'] is not None:
            drone_mission_vo.set_mi_desc(mission_info['mi_desc'])

        drone_mission_vo.set_home_lat(mission_info['home_lat'])
        drone_mission_vo.set_home_lon(mission_info['home_lon'])
        drone_mission_vo.set_mi_alt(mission_info['mi_alt'])
        drone_mission_vo.set_waypoint(mission_info['waypoint'])

        self.update_log_view.emit(organization_map[name], str(log.json_data))
        log.vo = drone_mission_vo
        if len(dr_vo) <= 0:
            dr_vo.append(drone_mission_vo)
        make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
        make_json_thread.daemon = True
        make_json_thread.start()
        log_info_thread = threading.Thread(target=log.log_mission_info, args=(drone_mission_vo.get_waypoint(),))
        log_info_thread.daemon = True
        log_info_thread.start()

        "할당 해제"
        # make_json_thread.join()
        # log_info_thread.join()

    """
    Drone Mission Stop
    """

    def name_value_check(self, _name, _json_data, _org_json_data, _organization_map, _dr_id, this):

        if this.__name__ == "process_drone_flight_info":
            if _name in _organization_map:
                _org_json_data['drone_stat'][0]['organization'] = _organization_map[_name]
                _json_data["organization"] = _organization_map[_name]

        elif this.__name__ == "process_drone_mission_info":
            if _name in _organization_map:
                _org_json_data['mission_info'][0]['organization'] = _organization_map[_name]
                _json_data["organization"] = _organization_map[_name]

        # ID 확인후 필요한 아이디 형식이 아니면 바꾸는 로직 구현 예정
        '''if _org_json_data['drone_stat'][0]['drone_id'] != f'{_dr_id[_name]}':
            _org_json_data['drone_stat'][0]['user_id'] = f"{_dr_id[_name]}"
            _org_json_data['drone_stat'][0]['drone_id'] = f"{_dr_id[_name]}"
            _json_data["user_id"] = f"{_dr_id[_name]}"
            _json_data["drone_id"] = f"{_dr_id[_name]}"

        if _org_json_data['drone_stat'][0]['user_id'] != f'{_dr_id[_name]}':
            _org_json_data['drone_stat'][0]['user_id'] = f'{_dr_id[_name]}'
            _org_json_data['drone_stat'][0]['drone_id'] = f'{_dr_id[_name]}'
            _json_data["user_id"] = f"{_dr_id[_name]}"
            _json_data["drone_id"] = f"{_dr_id[_name]}"'''

    def n_threaded(self, name, n_mavlink):
        drone_id = []
        log = logger.Logger(name)
        drone_vos = drone_vo.Drone_Vo()
        mission_vos = drone_vo.DroneMissionVo()
        self.now = datetime.datetime.now()
        n_json_data = {
            "msg": "flight_info",
            "drone_stat": [
                {
                    "organization": "나르마",
                    "drone_id": "nrm_01",
                    "user_id": "nrm_01",
                    "status": "",
                    "data_uid": 0,
                    "flight_mode": 0,
                    "lat": 0,
                    "lon": 0,
                    "rel_alt": 0,
                    "msl_alt": 0,
                    "speed": 0,
                    "roll": 0,
                    "pitch": 0,
                    "heading": 0,
                    "battery": 0
                }

            ]
        }
        n_mission_data = {
            "msg": "mission_file",
            "mission_info": [
                {
                    "organization": "나르마",
                    "drone_id": "nrm_01",
                    "user_id": "nrm01",
                    "mi_time": "",
                    "mi_name": "",
                    "mi_desc": "",
                    "home_lat": 0,
                    "home_lon": 0,
                    "mi_alt": 0,
                    "waypoint": []
                }

            ]
        }
        waypoint_item = []
        updated_flags = {
            'HEARTBEAT': False,
            'GLOBAL_POSITION_INT': False,
            'VFR_HUD': False,
            'ATTITUDE': False,
            'SYS_STATUS': False
        }
        n_stat = n_json_data.get("drone_stat")
        data_uid = 0
        mission_flg = False
        waypoint_flg = True
        last_update_data = 0
        flg_time_out = 30

        while True:
            try:
                msg = n_mavlink.recv_match()
                if msg:
                    last_update_data = time.time()
                    if msg.get_type() == 'HEARTBEAT':
                        if msg.base_mode == 29 and msg.custom_mode == 67371008 and waypoint_flg:
                            n_mavlink.waypoint_request_list_send()

                            msg = n_mavlink.recv_match(type=['MISSION_COUNT'], blocking=True)

                            waypoint_flg = msg.count

                            for i in range(waypoint_flg):
                                n_mavlink.waypoint_request_send(i)
                                msg = n_mavlink.recv_match(type=['MISSION_ITEM'], blocking=True)

                                waypoint_items = dict(index=0, lat=0, lon=0)
                                waypoint_items["index"] = i
                                waypoint_items["lat"] = msg.x
                                waypoint_items["lon"] = msg.y
                                waypoint_item.append(waypoint_items)

                            n_mavlink.mav.mission_ack_send(n_mavlink.target_system,
                                                               n_mavlink.target_component, 0)

                            n_mission_data["mission_info"][0]['waypoint'] = waypoint_item
                            mission_vos.set_waypoint(waypoint_item)

                            msg = n_mavlink.recv_match(type='HOME_POSITION', blocking=True)
                            if msg.latitude is not None:
                                n_mission_data['mission_info'][0]['home_lat'] = msg.latitude

                            if msg.longitude is not None:
                                n_mission_data['mission_info'][0]['home_lon'] = msg.longitude

                            mi_time = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
                            n_mission_data['mission_info'][0]['mi_time'] = mi_time
                            n_mission_data['mission_info'][0]['mi_name'] = f'{name}_{mi_time}'
                            n_mission_data['mission_info'][0]['mi_desc'] = f'{name}_MISSION'

                            if n_mission_data['mission_info'][0]['mi_alt'] == '':
                                n_mission_data['mission_info'][0]['mi_alt'] = msg.z
                                mission_vos.set_mi_alt(n_mission_data['mission_info'][0]['mi_alt'])

                            mission_vos.set_dr_id("nrm_01")
                            mission_vos.set_user_id("nrm_01")
                            mission_vos.set_mi_time(n_mission_data['mission_info'][0]['mi_time'])
                            mission_vos.set_mi_name(n_mission_data['mission_info'][0]['mi_name'])
                            mission_vos.set_mi_desc(n_mission_data['mission_info'][0]['mi_desc'])
                            mission_vos.set_home_lat(n_mission_data['mission_info'][0]['home_lat'])
                            mission_vos.set_home_lon(n_mission_data['mission_info'][0]['home_lon'])
                            mission_vos.set_home_lon(n_mission_data['mission_info'][0]['home_lon'])

                            mission_flg = True

                        else:
                            # status 정보 수신
                            if msg.system_status == 4:
                                n_stat[0]["status"] = "1"
                                updated_flags['HEARTBEAT'] = True
                                drone_vos.set_status(n_stat[0]["status"])
                            else:
                                n_stat[0]["status"] = "0"
                                updated_flags['HEARTBEAT'] = True
                                drone_vos.set_status(n_stat[0]["status"])

                            # updated_flags['HEARTBEAT'] = True

                    if msg.get_type() == 'GLOBAL_POSITION_INT':
                        n_stat[0]["lat"] = msg.lat / 1e7
                        n_stat[0]["lon"] = msg.lon / 1e7
                        n_stat[0]["alt"] = msg.alt / 1e3
                        n_stat[0]["rel_alt"] = msg.relative_alt / 1e3
                        n_stat[0]["msl_alt"] = msg.alt / 1e3
                        n_stat[0]["data_uid"] = data_uid

                        updated_flags['GLOBAL_POSITION_INT'] = True

                    if msg.get_type() == "VFR_HUD":
                        n_stat[0]["speed"] = msg.groundspeed
                        drone_vos.set_speed(n_stat[0]['speed'])

                        updated_flags['VFR_HUD'] = True

                    if msg.get_type() == "ATTITUDE":
                        n_stat[0]["roll"] = msg.roll
                        n_stat[0]["pitch"] = msg.pitch
                        n_stat[0]["heading"] = msg.yaw

                        drone_vos.set_roll(n_stat[0]['roll'])
                        drone_vos.set_pitch(n_stat[0]['pitch'])
                        drone_vos.set_heading(n_stat[0]['heading'])

                        updated_flags['ATTITUDE'] = True

                    if msg.get_type() == "SYS_STATUS":
                        n_stat[0]["battery"] = msg.battery_remaining
                        drone_vos.set_battery(n_stat[0]['battery'])

                        updated_flags['SYS_STATUS'] = True

                    drone_vos.set_dr_id("nrm_01")
                    drone_vos.set_user_id("nrm_01")
                    drone_vos.set_data_uid(data_uid)
                    drone_vos.set_lat(n_stat[0]['lat'])
                    drone_vos.set_lon(n_stat[0]['lon'])
                    drone_vos.set_rel_alt(n_stat[0]['rel_alt'])
                    drone_vos.set_msl_alt(n_stat[0]['msl_alt'])

                    drone_vos.set_addr(n_mavlink.address)

                    # 모든 플래그가 True 인지 (즉, 모든 메시지가 업데이트되었는지) 확인
                    if all(updated_flags.values()):
                        if len(drone_id) <= 0:
                            dr_json_data = n_json_data['drone_stat'][0]
                            drone_id.append(dr_json_data)
                            drone_id.append(self.client_sockets[0])
                            drone_id.append(name)
                            self.ui.addItem(drone_id)

                        log.json_data = n_json_data
                        self.update_log_view.emit(name, str(log.json_data))
                        log.vo = drone_vos
                        log.log_info()

                        # self.send_json_data(n_json_data)
                        with self.lock:
                            self.send_json_data(n_json_data)
                        make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
                        make_json_thread.daemon = True
                        make_json_thread.start()

                        data_uid += 1

                        # 플래그 초기화
                        for key in updated_flags:
                            updated_flags[key] = False

                    elif mission_flg:
                        log.json_data = n_mission_data
                        self.ui.append_log(name, str(log.json_data))
                        log.vo = mission_vos
                        log.log_mission_info(mission_vos.get_waypoint())

                        # self.send_json_data(n_mission_data)
                        with self.lock:
                            self.send_json_data(n_mission_data)
                        waypoint_item.clear()
                        n_mission_data["mission_info"][0]['waypoint'] = []

                        make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
                        make_json_thread.daemon = True
                        make_json_thread.start()

                        mission_flg = False
                        waypoint_flg = False
                        continue

                time_out_check = time.time() - last_update_data
                if time_out_check > flg_time_out:
                    if drone_id:
                        self.ui.delete_item(drone_id)

                    if n_mavlink.address in self.client_sockets:
                        try:
                            self.client_sockets.remove(n_mavlink.address)
                            print(f'클라이언트와 연결이 종료되었습니다 남은 클라이언트 리스트 : {len(self.client_sockets)}')
                            self.update_append_except_log.emit(str(name + ' time out'), str(n_mavlink.address))
                        except Exception as e:
                            print("나르마 클라이언트 제거 중 오류 발생 : ", e)
                            self.update_append_except_log.emit(str(e), str(n_mavlink.address))
                    n_mavlink.close()
                    break

            except Exception as e:
                log.log_exception(e)
                self.update_append_except_log.emit(str(e), str(n_mavlink.address))
                # self.ui.append_except_log(e, n_mavlink.address)
                self.ui.delete_item(drone_id)
                print("n_threaded Exception : ", e)

    def n_threaded_two(self, name, n_mavlink):
        drone_id = []
        log = logger.Logger(name)
        drone_vos = drone_vo.Drone_Vo()
        mission_vos = drone_vo.DroneMissionVo()
        self.now = datetime.datetime.now()
        n_json_data = {
            "msg": "flight_info",
            "drone_stat": [
                {
                    "organization": "나르마",
                    "drone_id": "nrm_02",
                    "user_id": "nrm_02",
                    "status": "",
                    "data_uid": 0,
                    "flight_mode": 0,
                    "lat": 0,
                    "lon": 0,
                    "rel_alt": 0,
                    "msl_alt": 0,
                    "speed": 0,
                    "roll": 0,
                    "pitch": 0,
                    "heading": 0,
                    "battery": 0
                }

            ]
        }
        n_mission_data = {
            "msg": "mission_file",
            "mission_info": [
                {
                    "organization": "나르마",
                    "drone_id": "nrm_02",
                    "user_id": "nrm02",
                    "mi_time": "",
                    "mi_name": "",
                    "mi_desc": "",
                    "home_lat": 0,
                    "home_lon": 0,
                    "mi_alt": 0,
                    "waypoint": []
                }

            ]
        }
        waypoint_item = []
        updated_flags = {
            'HEARTBEAT': False,
            'GLOBAL_POSITION_INT': False,
            'VFR_HUD': False,
            'ATTITUDE': False,
            'SYS_STATUS': False
        }
        n_stat = n_json_data.get("drone_stat")
        data_uid = 0
        mission_flg = False
        waypoint_flg = True
        last_update_data = 0
        flg_time_out = 30

        while True:
            try:
                msg = n_mavlink.recv_match()
                if msg:
                    last_update_data = time.time()
                    if msg.get_type() == 'HEARTBEAT':
                        if msg.base_mode == 29 and msg.custom_mode == 67371008 and waypoint_flg:
                            n_mavlink.waypoint_request_list_send()

                            msg = n_mavlink.recv_match(type=['MISSION_COUNT'], blocking=True)

                            waypoint_flg = msg.count

                            for i in range(waypoint_flg):
                                n_mavlink.waypoint_request_send(i)
                                msg = n_mavlink.recv_match(type=['MISSION_ITEM'], blocking=True)

                                waypoint_items = dict(index=0, lat=0, lon=0)
                                waypoint_items["index"] = i
                                waypoint_items["lat"] = msg.x
                                waypoint_items["lon"] = msg.y
                                waypoint_item.append(waypoint_items)

                            n_mavlink.mav.mission_ack_send(n_mavlink.target_system,
                                                               n_mavlink.target_component, 0)

                            n_mission_data["mission_info"][0]['waypoint'] = waypoint_item
                            mission_vos.set_waypoint(waypoint_item)

                            msg = n_mavlink.recv_match(type='HOME_POSITION', blocking=True)
                            if msg.latitude is not None:
                                n_mission_data['mission_info'][0]['home_lat'] = msg.latitude

                            if msg.longitude is not None:
                                n_mission_data['mission_info'][0]['home_lon'] = msg.longitude

                            mi_time = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
                            n_mission_data['mission_info'][0]['mi_time'] = mi_time
                            n_mission_data['mission_info'][0]['mi_name'] = f'{name}_{mi_time}'
                            n_mission_data['mission_info'][0]['mi_desc'] = f'{name}_MISSION'

                            if n_mission_data['mission_info'][0]['mi_alt'] == '':
                                n_mission_data['mission_info'][0]['mi_alt'] = msg.z
                                mission_vos.set_mi_alt(n_mission_data['mission_info'][0]['mi_alt'])

                            mission_vos.set_dr_id("nrm_01")
                            mission_vos.set_user_id("nrm_01")
                            mission_vos.set_mi_time(n_mission_data['mission_info'][0]['mi_time'])
                            mission_vos.set_mi_name(n_mission_data['mission_info'][0]['mi_name'])
                            mission_vos.set_mi_desc(n_mission_data['mission_info'][0]['mi_desc'])
                            mission_vos.set_home_lat(n_mission_data['mission_info'][0]['home_lat'])
                            mission_vos.set_home_lon(n_mission_data['mission_info'][0]['home_lon'])
                            mission_vos.set_home_lon(n_mission_data['mission_info'][0]['home_lon'])

                            mission_flg = True

                        else:
                            # status 정보 수신
                            if msg.system_status == 4:
                                n_stat[0]["status"] = "1"
                                updated_flags['HEARTBEAT'] = True
                                drone_vos.set_status(n_stat[0]["status"])
                            else:
                                n_stat[0]["status"] = "0"
                                updated_flags['HEARTBEAT'] = True
                                drone_vos.set_status(n_stat[0]["status"])

                            # updated_flags['HEARTBEAT'] = True

                    if msg.get_type() == 'GLOBAL_POSITION_INT':
                        n_stat[0]["lat"] = msg.lat / 1e7
                        n_stat[0]["lon"] = msg.lon / 1e7
                        n_stat[0]["alt"] = msg.alt / 1e3
                        n_stat[0]["rel_alt"] = msg.relative_alt / 1e3
                        n_stat[0]["msl_alt"] = msg.alt / 1e3
                        n_stat[0]["data_uid"] = data_uid

                        updated_flags['GLOBAL_POSITION_INT'] = True

                    if msg.get_type() == "VFR_HUD":
                        n_stat[0]["speed"] = msg.groundspeed
                        drone_vos.set_speed(n_stat[0]['speed'])

                        updated_flags['VFR_HUD'] = True

                    if msg.get_type() == "ATTITUDE":
                        n_stat[0]["roll"] = msg.roll
                        n_stat[0]["pitch"] = msg.pitch
                        n_stat[0]["heading"] = msg.yaw

                        drone_vos.set_roll(n_stat[0]['roll'])
                        drone_vos.set_pitch(n_stat[0]['pitch'])
                        drone_vos.set_heading(n_stat[0]['heading'])

                        updated_flags['ATTITUDE'] = True

                    if msg.get_type() == "SYS_STATUS":
                        n_stat[0]["battery"] = msg.battery_remaining
                        drone_vos.set_battery(n_stat[0]['battery'])

                        updated_flags['SYS_STATUS'] = True

                    drone_vos.set_dr_id("nrm_01")
                    drone_vos.set_user_id("nrm_01")
                    drone_vos.set_data_uid(data_uid)
                    drone_vos.set_lat(n_stat[0]['lat'])
                    drone_vos.set_lon(n_stat[0]['lon'])
                    drone_vos.set_rel_alt(n_stat[0]['rel_alt'])
                    drone_vos.set_msl_alt(n_stat[0]['msl_alt'])

                    drone_vos.set_addr(n_mavlink.address)

                    # 모든 플래그가 True 인지 (즉, 모든 메시지가 업데이트되었는지) 확인
                    if all(updated_flags.values()):
                        if len(drone_id) <= 0:
                            dr_json_data = n_json_data['drone_stat'][0]
                            drone_id.append(dr_json_data)
                            drone_id.append(self.client_sockets[0])
                            drone_id.append(name)
                            self.ui.addItem(drone_id)

                        log.json_data = n_json_data
                        self.update_log_view.emit(name, str(log.json_data))
                        log.vo = drone_vos
                        log.log_info()

                        # self.send_json_data(n_json_data)
                        with self.lock:
                            self.send_json_data(n_json_data)
                        make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
                        make_json_thread.daemon = True
                        make_json_thread.start()

                        data_uid += 1

                        # 플래그 초기화
                        for key in updated_flags:
                            updated_flags[key] = False

                    elif mission_flg:
                        log.json_data = n_mission_data
                        self.ui.append_log(name, str(log.json_data))
                        log.vo = mission_vos
                        log.log_mission_info(mission_vos.get_waypoint())

                        # self.send_json_data(n_mission_data)
                        with self.lock:
                            self.send_json_data(n_mission_data)
                        waypoint_item.clear()
                        n_mission_data["mission_info"][0]['waypoint'] = []

                        make_json_thread = threading.Thread(target=log.make_json_data, args=(self.now,))
                        make_json_thread.daemon = True
                        make_json_thread.start()

                        mission_flg = False
                        waypoint_flg = False
                        continue

                time_out_check = time.time() - last_update_data
                if time_out_check > flg_time_out:
                    if drone_id:
                        self.ui.delete_item(drone_id)

                    if n_mavlink.address in self.client_sockets:
                        try:
                            self.client_sockets.remove(n_mavlink.address)
                            print(f'클라이언트와 연결이 종료되었습니다 남은 클라이언트 리스트 : {len(self.client_sockets)}')
                            self.update_append_except_log.emit(str(name + ' time out'), str(n_mavlink.address))
                        except Exception as e:
                            print("나르마 클라이언트 제거 중 오류 발생 : ", e)
                            self.update_append_except_log.emit(str(e), str(n_mavlink.address))
                    n_mavlink.close()
                    break

            except Exception as e:
                log.log_exception(e)
                self.update_append_except_log.emit(str(e), str(n_mavlink.address))
                # self.ui.append_except_log(e, n_mavlink.address)
                self.ui.delete_item(drone_id)
                print("n_threaded_two Exception : ", e)

    def add_drone_info(self, name, drone_info, ui, addr):

        if name in ['DUSI']:
            self.del_drone_info(name, ui)
            drone_list = getattr(ui, f'dr_{name.lower()}')
            drone_list.append(drone_info)
            drone_list.append(name)
            drone_list.append(addr)
            # print(f'{name} : {drone_list}')

    def del_drone_info(self, name, ui):
        if name in ['DUSI',]:
            if name != 'N':
                drone_list = getattr(ui, f'dr_{name.lower()}')
                drone_list.clear()
