function addMarker(droneId,position) {
    console.log("addMarker실행")
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        position: position,
        image : markerImage,
        clickable: true
    });

    marker.setMap(map);
    var iwContent = `<div style="padding:5px;">${droneId}</div>`, // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
        iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

// 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable : iwRemoveable
    });

// 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커 위에 인포윈도우를 표시합니다
        infowindow.open(map, marker);
    });
    // marker.setImage()
    droneLocation.set(droneId,marker)
}

function addMissionMarker(status,droneId,position) {
    var marker;
    if(status === "start"){
        console.log("마킹:"+status);
        marker = new kakao.maps.Marker({
            position: position,
            image : miMarkerStartImage
        });
    }else if(status === "mission"){
        console.log("마킹:"+status);
        marker = new kakao.maps.Marker({
            position: position,
            image : miMarkerImage
        });
    }else if(status === "end"){
        console.log("마킹:"+status);
        marker = new kakao.maps.Marker({
            position: position,
            image : miMarkerEndImage
        });
    }
    // 마커를 생성합니다
    marker.setMap(map);
    console.log("미션마크");
    return marker;
    // marker.setImage()
}

function missionMakerControl() {
    var markers = [];
    var linePath = [];
    if (missionMap.has(mapKey)) {
        console.log("미션있음")
        var wayPoint = missionMap.get(mapKey).waypoint;
        console.log("미션 체크" + wayPoint.length)
        for (let i = 0; i < wayPoint.length; i++) {
            const waypoint = wayPoint[i];
            var lat = waypoint.lat;
            var lng = waypoint.lon;
            var index = waypoint.index;
            let position = new kakao.maps.LatLng(lat, lng);
            console.log("미션 포지션" + position);
            linePath.push(position);
            console.log("index" + index);
            if (index === 1) {
                markers.push(addMissionMarker("start", droneInfo.get(mapKey).drone_id, position));
            } else if (i === wayPoint.length - 1) {
                markers.push(addMissionMarker("end", droneInfo.get(mapKey).drone_id, position));
            } else {
                markers.push(addMissionMarker("mission", droneInfo.get(mapKey).drone_id, position));
            }
        }
        missionLocation.set(droneInfo.get(mapKey).drone_id, markers);
        var polyline = new kakao.maps.Polyline({
            path: linePath, // 선을 구성하는 좌표배열 입니다
            strokeWeight: 5, // 선의 두께 입니다
            strokeColor: '#ff00f2', // 선의 색깔입니다
            strokeOpacity: 0.7, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
            strokeStyle: 'solid' // 선의 스타일입니다
        });

        // 지도에 선을 표시합니다
        lineMap.set(mapKey, polyline);
        polyline.setMap(map);
    }
}

