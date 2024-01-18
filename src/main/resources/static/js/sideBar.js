var droneIdNo
function createSidebarList() {
    var listElement = document.getElementById("listItems");
    listElement.innerHTML="";
    const btn1 = document.getElementById("droneBtn");
    const btnInfo1 = document.getElementById("btnInfo1");
    const btn2 = document.getElementById("3dBtn");
    const btnInfo2 = document.getElementById("btnInfo2");
    const listDiv = document.getElementById("droneList");
    const btn3 = document.getElementById("chartBtn");
    const btnInfo3 = document.getElementById("btnInfo3");
    const btn4 = document.getElementById("logBtn");
    const btnInfo4 = document.getElementById("btnInfo4");
    var three3 = document.getElementById("treeContainer3");
    var firstFooter = document.getElementById("firstFooter");
    var footer = document.getElementById("footer");
    var three = document.getElementById("treeContainer");
    var threeCheckDiv = document.getElementById("threeCheckDiv");
    var threeDiv = document.getElementById("tree");
    var videoDroneId = document.getElementById("videoDroneId");
    var simulFooter = document.getElementById("simulFooter");
    var b1Flag = false;
    btn1.addEventListener("mouseover", () => {
        btnInfo1.style.display = "block";
    });

    btn1.addEventListener("mouseout", () => {
        btnInfo1.style.display = "none";
    });
    btn2.addEventListener("mouseover", () => {
        btnInfo2.style.display = "block";
    });

    btn2.addEventListener("mouseout", () => {
        btnInfo2.style.display = "none";
    });
    btn3.addEventListener("mouseover", () => {
        btnInfo3.style.display = "block";
    });

    btn3.addEventListener("mouseout", () => {
        btnInfo3.style.display = "none";
    });
    btn4.addEventListener("mouseover", () => {
        btnInfo4.style.display = "block";
    });
    btn4.addEventListener("mouseout", () => {
        btnInfo4.style.display = "none";
    });

    btn1.addEventListener("click", () => {
        if(b1Flag===false){
            listDiv.style.display = "block";
            btn4.style.display = "none";
            b1Flag=true;
        }else if(b1Flag===true){
            listDiv.style.display = "none";
            btn4.style.display = "block";
            b1Flag=false;
        }

    });
    btn4.addEventListener("click", () => {
        streamingStop();
        mapKey = simulKey;
        listDiv.style.display = "none";
        three3.style.display = "block";
        simulFooter.style.display="block";
        firstFooter.style.display="none";
        threeDiv.style.display = "none";
        threeCheckDiv.style.display = "none";
        threeDiv.style.background= "rgba(0, 0, 0, 0)"
        three.style.display = "none"
        threeDiv.style.border="rgba(0, 0, 0, 0)"
        footer.style.display = "none";
        btn2.style.display="block";
        btn3.style.display="block";
        btn4.style.display = "block";
        getLog();
        startTimer();
    });
    droneInfo.forEach(function (value, key) {
        if(key===simulKey){
            return;
        }
        console.log("사이드바 리스트")
        if(value.drone_id == null){
            return;
        }
        var listItem = document.createElement("button");
        listItem.className = "list-group-item list-group-item-action py-3 lh-sm";
        listItem.style.background = "#ffffff"
        listItem.style.borderRadius= "15px"
        listItem.style.paddingLeft="10px"
        listItem.style.paddingRight="10px"

        listItem.addEventListener("click",function (){
            panTo(value.lat,value.lon);//사이드바 아이템 클릭 시 해당 아이템의 drone 좌표로 지도 이동
            mapKey = value.drone_id;
            streamingStop();
            droneIdNo = mapKey;
            listDiv.style.display = "none"
            b1Flag = false;
            firstFooter.style.display="block"
            three3.style.display = "block";
            threeDiv.style.display = "none";
            threeCheckDiv.style.display = "none";
            threeDiv.style.background= "rgba(0, 0, 0, 0)"
            three.style.display = "none"
            threeDiv.style.border="rgba(0, 0, 0, 0)"
            footer.style.display = "none";
            videoDroneId.textContent = mapKey;
            btn2.style.display="block";
            btn3.style.display="block";
            btn4.style.display = "block";
            simulFooter.style.display="none";
            stopTimer();
            streamingStart();
            settingFoot();
        });

        var div1 = document.createElement("div");
        div1.className = "d-flex w-100 align-items-center justify-content-between";

        var strong = document.createElement("strong");
        strong.className = "mb-1";
        strong.textContent = String(value.drone_id);

        var small = document.createElement("small");
        small.className = "text-body-secondary";
        small.textContent = "배터리 : "+String(value.battery)+"%";
        small.id = "smallTxt";

        div1.appendChild(strong);
        div1.appendChild(small);

        var div2 = document.createElement("div");
        div2.className = "col-10 mb-1 small";
        div2.textContent = String(value.organization);


        listItem.appendChild(div1);
        listItem.appendChild(div2);
        listElement.appendChild(listItem);//사이드바에 drone별로 div 생성
    });

}
