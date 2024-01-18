var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(36.4180054, 127.408598), // 지도의 중심좌표
        level: 4, // 지도의 확대 레벨
        mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
    };

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);
console.log('지도생성');
// 지도 타입 변경 컨트롤을 생성한다
var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도의 상단 우측에 지도 타입 변경 컨트롤을 추가한다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
map.relayout();
// 지도에 확대 축소 컨트롤을 생성한다
var zoomControl = new kakao.maps.ZoomControl();

// 지도의 우측에 확대 축소 컨트롤을 추가한다
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
map.setMaxLevel(13);

// 지도 중심 좌표 변화 이벤트를 등록한다
kakao.maps.event.addListener(map, 'center_changed', function () {
    console.log('지도의 중심 좌표는 ' + map.getCenter().toString() +' 입니다.');
});
// 마커 이미지의 주소
var markerImageUrl = '../images/new/icon-dron-grey.png',
    markerImageSize = new kakao.maps.Size(30,30), // 마커 이미지의 크기
    markerImageOptions = {
        offset : new kakao.maps.Point(20, 10)// 마커 좌표에 일치시킬 이미지 안의 좌표
    };
var dotImageUrl = '../images/new/dot.png',
    dotImageSize = new kakao.maps.Size(5,5), // 마커 이미지의 크기
    dotImageOptions = {
        offset : new kakao.maps.Point(8,-3)// 마커 좌표에 일치시킬 이미지 안의 좌표
    };
var MissionStartImageUrl = '../images/new/startMarker.png',
    markerMsImageSize = new kakao.maps.Size(20,20), // 마커 이미지의 크기
    markerMsImageOptions = {
        offset : new kakao.maps.Point(10, 10)// 마커 좌표에 일치시킬 이미지 안의 좌표
    };
var MissionImageUrl = '../images/new/missionMarker.png',
    markerMImageSize = new kakao.maps.Size(20,20), // 마커 이미지의 크기
    markerMImageOptions = {
        offset : new kakao.maps.Point(10, 10)// 마커 좌표에 일치시킬 이미지 안의 좌표
    };
var MissionEndImageUrl = '../images/new/endMarker.png',
    markerMeImageSize = new kakao.maps.Size(20,20), // 마커 이미지의 크기
    markerMeImageOptions = {
        offset : new kakao.maps.Point(10, 10)// 마커 좌표에 일치시킬 이미지 안의 좌표
    };
// 마커 이미지를 생성한다
var markerImage = new kakao.maps.MarkerImage(markerImageUrl, markerImageSize, markerImageOptions);
var dotImage = new kakao.maps.MarkerImage(dotImageUrl, dotImageSize, dotImageOptions);
var miMarkerStartImage = new kakao.maps.MarkerImage(MissionStartImageUrl, markerMsImageSize, markerMsImageOptions);
var miMarkerImage = new kakao.maps.MarkerImage(MissionImageUrl, markerMImageSize, markerMImageOptions);
var miMarkerEndImage = new kakao.maps.MarkerImage(MissionEndImageUrl, markerMeImageSize, markerMeImageOptions);

var droneLocation = new Map();//key: 드론Id / value : 위치
var droneInfo = new Map();// key: 드론Id / value : 드론 정보
var altMap = new Map();// key: 드론Id / value : 드론 지표면 기준 고도
var altMap2 = new Map();// key: 드론Id / value : 드론 해수면 기준 고도
var speedMap = new Map();// key: 드론Id / value : 드론 속도
var missionMap = new Map();// key: 드론Id / value : 드론 미션
var missionLocation = new Map();// key: 드론Id / value : 드론 미션 좌표
var mapKey = null;// 현재 선택한 드론의 Id로 Map에서 값 가져올때 사용
var simulKey = null;
var dotMap = new Map(); // key: 드론Id / value : 드론의 이동 기록
var lineMap = new Map();

//지도 중심 위치 변경 함수
function panTo(panLat, panLng) {
    console.log(panLat+"/"+panLng);
    // 이동할 위도 경도 위치를 생성합니다
    var moveLatLon = new kakao.maps.LatLng(panLat, panLng);

    // 지도 중심을 부드럽게 이동시킵니다
    // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
    map.setCenter(moveLatLon);
}
