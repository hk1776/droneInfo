function settingFoot() {
    var footer = document.getElementById("footer");
    var closeChart = document.getElementById("closeFoot");
    var altChartC = document.getElementById("myChart");
    var speedChartC = document.getElementById("myChart2");
    var hBattery = document.getElementById("hBattery");
    var hBatteryImg = document.getElementById("hBatteryImg");
    var hId = document.getElementById("hId");
    var chart1 = document.getElementById("chart1");
    var chart2 = document.getElementById("chart2");
    var three = document.getElementById("treeContainer");
    var three3 = document.getElementById("treeContainer3");
    var threeDiv = document.getElementById("tree");
    const btn2 = document.getElementById("3dBtn");
    var threeCheckDiv = document.getElementById("threeCheckDiv");
    var close3D = document.getElementById("close3D");
    const btn3 = document.getElementById("chartBtn")
    var map = document.getElementById("map");


    three3.style.display = "block"

    //버튼 누를 시 3d div 표시
    btn2.addEventListener("click", () => {
        threeDiv.style.display = "block";
        threeCheckDiv.style.display = "block";
        threeDiv.style.background = "white"
        three.style.display = "block"
        threeDiv.style.borderLeft = "5px solid #212529"
        threeDiv.style.borderRight = "5px solid #212529"
        threeDiv.style.borderTop = "5px solid #212529"
        footer.style.display = "none";
    });

    //배터리이미지 변경
    if (mapKey != null) {
        hId.style.display = "block";
        hId.textContent = mapKey;
        hBattery.style.display = "block";
        hBattery.textContent = droneInfo.get(mapKey).battery + "%";
        hBatteryImg.style.display = "block";
        var currentB = droneInfo.get(mapKey).battery;
        console.log("배터리는" + currentB)
        switch (true) {
            case currentB === 0:
                console.log("현재 배터리E" + currentB);
                hBatteryImg.src = "../images/new/batteryEmpty.png";
                break;
            case 1 <= currentB && currentB < 40:
                console.log("현재 배터리L" + currentB);
                hBatteryImg.src = "../images/new/batteryLow.png";
                break;
            case 40 <= currentB && currentB < 55:
                console.log("현재 배터리H" + currentB);
                hBatteryImg.src = "../images/new/batteryHalf.png";
                break;
            case 55 <= currentB && currentB < 100:
                console.log("현재 배터리" + currentB);
                hBatteryImg.src = "../images/new/battery.png";
                break;
            case currentB === 100:
                console.log("현재 배터리F" + currentB);
                hBatteryImg.src = "../images/new/batteryFull.png";
                break;
        }

        //3d Div 닫기
        close3D.addEventListener("click", function () {
            threeDiv.style.display = "none";
            //threeCheckDiv.style.display = "none";
            threeDiv.style.background = "rgba(0, 0, 0, 0)"
            three.style.display = "none"
            threeDiv.style.border = "rgba(0, 0, 0, 0)"
        });

        //차트 세팅
        altChart(droneInfo.get(mapKey).drone_id);
        speedChart(droneInfo.get(mapKey).drone_id);

        //차트 버튼 누를 시 차트 창 생성
        btn3.addEventListener("click", function () {
            console.log("차트버튼")
            footer.style.display = "block";
            threeDiv.style.display = "none";
            // threeCheckDiv.style.display = "none";
            threeDiv.style.background = "rgba(0, 0, 0, 0)"
            three.style.display = "none"
            threeDiv.style.border = "rgba(0, 0, 0, 0)"
        });
        //차트 창 닫기
        closeChart.addEventListener("click", function () {
            footer.style.display = "none";
        });

        //미션데이터 마커 초기화
        missionLocation.forEach((value, key) => {
            for (let i = 0; i < value.length; i++) {
                value[i].setMap(null);
            }
        });
        lineMap.forEach((value, key) => {
            value.setMap(null);
        });

        //고도 속도 차트 변환 체크박스
        const checkbox1 = document.getElementById("highCheck");
        const checkbox2 = document.getElementById("speedCheck");

        checkbox1.addEventListener("change", function () {
            if (this.checked) {
                checkbox2.checked = false;
                altChartC.style.display = "block";
                chart2.style.width = "46%";

                chart1.style.width = "0";
                speedChartC.style.display = "none";

            } else {
                checkbox2.checked = true;
                speedChartC.style.display = "block";
                chart1.style.width = "46%";
                chart2.style.width = "0";
                altChartC.style.display = "none";
            }
        });
        checkbox2.addEventListener("change", function () {
            if (this.checked) {
                checkbox1.checked = false;
                speedChartC.style.display = "block";
                chart1.style.width = "46%";
                chart2.style.width = "0";
                altChartC.style.display = "none";
            } else {
                checkbox1.checked = true;
                altChartC.style.display = "block";
                chart2.style.width = "46%";
                chart1.style.width = "0";
                speedChartC.style.display = "none";
            }
        });
        missionMakerControl();
        console.log(droneInfo.get(mapKey).drone_id + " / " + droneInfo.get(mapKey).flight_mode + " / " + droneInfo.get(mapKey).speed + " / " + droneInfo.get(mapKey).lat + " / " + droneInfo.get(mapKey).lon + " / " + droneInfo.get(mapKey).battery)

        //드론 3d 모델 회전값 변경
        let rotationX = -1 * (Math.PI * droneInfo.get(mapKey).pitch) / 180;//pitch
        let rotationY = (Math.PI * droneInfo.get(mapKey).heading) / 180;//heading
        let rotationZ = (Math.PI * droneInfo.get(mapKey).roll) / 180;//roll

        if(threeDiv.style.display==="block"){
            rotateObjectBasedOnCondition(rotationX, rotationY, rotationZ);
        }

        console.log("(setRotation)pitch : " + rotationX + " heading : " + rotationY + " roll : " + rotationZ);


    }
}
