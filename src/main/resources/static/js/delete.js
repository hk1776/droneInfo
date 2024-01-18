//1분간 접속이 없다면 removeData 함수 호출 하여 해당 Drone 정보 삭제
setInterval(() => {
    const currentTime = new Date().getTime();
    droneInfo.forEach((data, key) => {
        if (currentTime - data.lastUpdate >= 60000) {
            //removeData(key);
        }
    });
}, 1000);
function removeData(key) {
    var footer = document.getElementById("footer");
    var tree = document.getElementById("treeContainer");
    droneLocation.get(key).setMap(null);
    footer.style.display = "none"
    tree.style.display = "none"
    mapKey = null;
    missionLocation.forEach((value, key)=>{
        for(let i =0;i<value.length;i++){
            value[i].setMap(null);
        }
    });
    dotMap.forEach((value, key)=>{
        for(let i =0;i<value.length;i++){
            value[i].setMap(null);
        }
    });
    lineMap.get(key).setMap(null);
    lineMap.delete(key);
    droneInfo.delete(key);
    droneLocation.delete(key);
    altMap.delete(key);
    altMap2.delete(key);
    speedMap.delete(key);
    missionMap.delete(key);
    missionLocation.delete(key);
    dotMap.delete(key);
    createSidebarList();
}
