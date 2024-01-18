function chargebattery(per) {
    console.log("배터리 ="+per)
    var a;
    a = document.getElementById("battery");
    //a.innerHTML = "&#xf244;";
    if(per === 0){
        a.innerHTML = "&#xf244;";
    }
    if(1<per && per<25){
        a.innerHTML = "&#xf243;";
    }
    if(24<per && per<51){
        a.innerHTML = "&#xf242;";
    }
    if(50<per && per<75){
        a.innerHTML = "&#xf241;";
    }
    if(74<per && per<101){
        a.innerHTML = "&#xf240;";
    }
}
