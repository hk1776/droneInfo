function settings (data){
    console.log("settings : "+data)
    try {
            //let data = JSON.parse(e.data); // e.data로부터 JSON 문자열 파싱
            if(data.mi_name===undefined) {
                let organization = data.organization;
                let user_id = data.user_id;
                let droneId = data.drone_id;
                let status = data.status;
                let data_uid = data.data_uid;
                let flight_mode = data.flight_mode;
                let lat = data.lat;
                let lng = data.lon;
                let rel_alt = data.rel_alt * 0.1;
                let msl_alt = data.msl_alt * 0.001;
                let speed = data.speed;
                let roll = data.roll;
                let pitch = data.pitch;
                let heading = data.heading;
                let battery = Math.floor(volt(data.battery * 1000) * 100);
                const lastUpdate = new Date().getTime();
                const getDrone = new Drone(organization, user_id, droneId, status, data_uid, flight_mode, lat, lng, rel_alt, msl_alt, speed, roll, pitch, heading, battery,lastUpdate);
                console.log(droneId + "/" + lat + "/" + lng + "/msl:" + msl_alt);
                console.log("맵키 : "+mapKey);

                //해당 드론Id의 위치가 이미 저장되어 있을 때
                if (droneLocation.has(droneId)) {
                    console.log("이미 있는 키:" + droneId + "위치" + droneLocation.get(droneId));
                    droneLocation.get(droneId).setMap(null);//이전 위치의 드론 마커 삭제

                    //이전위치를 새로운 마커(dot)로 표시
                    const dotLocation = new kakao.maps.LatLng(droneInfo.get(droneId).lat, droneInfo.get(droneId).lon);
                    console.log("드론 이전 위치 : "+ dotLocation);
                    var marker = new kakao.maps.Marker({
                        position: dotLocation,
                        image : dotImage
                    });
                    if(dotMap.has(droneId)){
                        var newArr =dotMap.get(droneId);
                        if(newArr.length>10){
                            newArr[0].setMap(null);
                            newArr.shift();
                        }
                        newArr.push(marker);

                        dotMap.set(droneId,newArr);
                    }else{
                        var newArr = [marker];
                        dotMap.set(droneId,newArr);
                    }

                    console.log("드론 이전 위치2 : "+ marker.position);

                    marker.setMap(map);
                }
                //해당 드론Id의 고도와 속도 그래프 기록을 저장하기 위한 배열 생성과 배열을 Map에 드론Id별로 저장함
                if (!droneInfo.has(droneId)) {
                    var alt = [];
                    var alt2 = [];
                    var speedArr = [];

                    altMap.set(droneId, alt);
                    altMap2.set(droneId, alt2);
                    speedMap.set(droneId, speedArr);
                }
                //고도 속도 저장
                var reAlt = altMap.get(droneId);
                reAlt.push(rel_alt);
                altMap.set(droneId, reAlt);

                var reAlt2 = altMap2.get(droneId);
                reAlt2.push(msl_alt);
                altMap2.set(droneId, reAlt2);

                var reSpeed = speedMap.get(droneId);
                reSpeed.push(speed);
                speedMap.set(droneId, reSpeed);

                //고도 속도 그래프의 최대 길이 => 61
                if (reAlt.length > 61) {
                    reAlt.shift();
                }
                if (reAlt2.length > 61) {
                    reAlt2.shift();
                }
                if (reSpeed.length > 61) {
                    reSpeed.shift();
                }

                //새로운 드론 마커 맵에 표시
                let position = new kakao.maps.LatLng(lat, lng);

                droneInfo.set(droneId, getDrone);
                if(droneInfo.has(null)){
                    console.log("null삭제");
                    droneInfo.delete(null);
                }
                if(mapKey!=null){
                    if(droneInfo.has(mapKey)){
                        panTo(droneInfo.get(mapKey).lat, droneInfo.get(mapKey).lon);
                    }

                }
                addMarker(droneId, position);
                // refreshSide();
                createSidebarList();
                settingFoot();
            }else {
                console.log("미션");
                console.log("맵키 : "+mapKey);
                let organization = data.organization;
                let drone_id = data.drone_id;
                let mi_name = data.mi_name;
                let mi_desc = data.mi_desc;
                let home_lat = data.home_lat;
                let home_lon = data.home_lon;
                let mi_alt = data.mi_alt;
                let waypoint = data.waypoint;
                const mission = new Mission(organization, drone_id, mi_name, mi_desc, home_lat, home_lon, mi_alt, waypoint);

                missionMap.set(drone_id,mission);
                settingFoot();

            }
    } catch (err) {
        console.log(err);

    }
}
