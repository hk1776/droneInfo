// 요청할 URL과 요청 본문 데이터를 설정
var interval =null;
var timer = 2000;
var index = 0;
var videoDroneId = document.getElementById("videoDroneId");
var simulId = document.getElementById("simulId");
var simuldate = document.getElementById("simuldate");
var jsonStr;
var data;
var fileIndex = 0;
var next = false;
var oneX = document.getElementById("oneX");
var twoX = document.getElementById("twoX");
var threeX = document.getElementById("threeX");
function getLog() {

    fetch('/log', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(fileIndex),
    })
    .then(response => response.json())
    .then(e => {
        // 서버로부터 받은 응답 데이터(data)를 처리
       //
        var law = JSON.stringify(e);
        data = JSON.parse(law)
    })
    .catch(error => {
        console.error('에러 발생:', error);
    });
}
function startTimer() {
    if (interval === null) {
        interval =setInterval(function() {
            if(index<data.length){
                console.log("timeout" + index);
                console.log("msg : "+data[index].msg);
                if(data[index].msg==="mission_file"){
                    jsonStr = JSON.stringify(data[index].mission_info)
                    var data2= JSON.parse(jsonStr.substring(1,jsonStr.length-1));
                    settings(data2);
                    index++;
                }else if(data[index].msg==="x"){
                    fileIndex = 0;
                    index=0;
                    next =true;
                    getLog()
                    stopTimer();

                }
                else{
                    jsonStr = JSON.stringify(data[index].drone_stat)
                    var data2= JSON.parse(jsonStr.substring(1,jsonStr.length-1));
                    simulKey = data2.drone_id;
                    mapKey = simulKey;
                    droneIdNo = simulKey;
                    videoDroneId.textContent = simulKey;
                    simulId.textContent = simulKey;
                    console.log("데이터 길이"+data.length);
                    simuldate.textContent = data[index].date;
                    panTo(data2.lat,data2.lon);
                    settings(data2);
                    settingFoot();
                    index++;
                }

            }else{
               fileIndex++;
               index = 0;
               next =true;
               console.log("시뮬 미션 :"+missionLocation.get(simulKey));
                missionLocation.forEach((value, key)=>{
                    for(let i =0;i<value.length;i++){
                        value[i].setMap(null);
                    }
                });
               missionMap.delete(simulKey);
               missionLocation.delete(simulKey);
               stopTimer();
               getLog();
            }
        }, timer);
    }
}

oneX.addEventListener("mouseover", () => {
    oneX.src = "../images/new/1x2.png";
});

oneX.addEventListener("mouseout", () => {
    oneX.src = "../images/new/1x.png";
});
twoX.addEventListener("mouseover", () => {
    twoX.src = "../images/new/2x2.png";
});

twoX.addEventListener("mouseout", () => {
    twoX.src = "../images/new/2x.png";
});
threeX.addEventListener("mouseover", () => {
    threeX.src = "../images/new/3x2.png";
});

threeX.addEventListener("mouseout", () => {
    threeX.src = "../images/new/3x.png";
});

oneX.addEventListener("click",()=>{
    console.log("click 1");
    oneX.src = "../images/new/1x2.png";
    twoX.src = "../images/new/2x.png";
    threeX.src = "../images/new/3x.png";
    if(timer != 1000){
        timer = 2000;
        stopTimer();
        startTimer();
    }
});
twoX.addEventListener("click",()=>{
    oneX.src = "../images/new/1x.png";
    twoX.src = "../images/new/2x2.png";
    threeX.src = "../images/new/3x.png";
    console.log("click 2");
    if(timer != 600){
        timer = 1000;
        stopTimer();
        startTimer();
    }
});
threeX.addEventListener("click",()=>{
    oneX.src = "../images/new/1x.png";
    twoX.src = "../images/new/2x.png";
    threeX.src = "../images/new/3x2.png";
    console.log("click 3");
    if(timer != 300){
        timer = 600;
        stopTimer();
        startTimer();
    }
});
function stopTimer() {
    if (interval !== null) {
        clearInterval(interval);
        interval = null; // 타이머 ID 초기화
        if(next === true){
            next=false;
            startTimer();
        }
    }
}
