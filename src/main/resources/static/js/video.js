/*stopBtn = document.getElementById('stop_btn');
startBtn = document.getElementById('start_btn');*/
ws_connected = 0;
var sm;
var flag = false;
let time;

function sleep(ms)
{
    const wakeUpTime = Date.now() + ms;
    while (Date.now() < wakeUpTime) {}
}
/*function setButton(startB, stopB)
{
    startBtn.disabled = startB;
    stopBtn.disabled = stopB;
}*/
function callback(m)
{
    if(m.type == "connect")
    {
        println(">> connected");
        ws_connected = 1;
        flag=true;
        console.log("커넥트 : "+flag)

        //setButton(false, true)
        sm.startStreaming();
    }
    else if(m.type == "streaming")
    {
        if(m.code == "1")
        {
            //setButton(true, false);
        }
        else
        {
           // setButton(false, true);
        }
    }
    else if(m.type == "close")
    {
       // close reason
        println(">> closed >> "+m.code+" :: "+m.data);
        time =setTimeout(function() {
            streamingStop();
            console.log("재접속 로그")
            streamingStart();
            if(flag){
                console.log("탈출 / "+flag);
                clearTimeout(time);
            }
        }, 10000);
       // setButton(false, true);
        ws_connected = 1;
    }
    else if(m.type == "error")
    {
        println(">> error >> "+m.data);
       // setButton(false, true);
        ws_connected = 0;
    }
    else if(m.type == "data")
    {
        println(">> gps data >> "+m.data);
    }
}

function connect()
{
    if(typeof sm == "undefined" || sm == null)
    {
        sm = new SM('socketUrl', droneIdNo, callback);
        sm.start();
    }
}

function disconnect()
{
    if(typeof sm != "undefined" && sm != null)
    {
        sm.close();
        sm = null;
    }
    setButton(false, true, true, true);
}

function streamingStart()
{
    console.log("드론Id2="+droneIdNo);
    clearTimeout(time);
    if(typeof sm == "undefined" || sm == null)
    {
        sm = new SM('socketUrl', droneIdNo, callback);
    }
    sm.start();

}

function streamingStop()
{
    flag=false;
    console.log("flag = "+flag);
    /*sm.stopStreaming();*/
    if(typeof sm != "undefined" && sm != null)
    {
        sm.close();
        sm = null;
    }
   // setButton(true, true);
}
/* function setDroneId(id)
 {
     droneIdNo = id;
 }*/

function getDroneId()
{
    return droneIdNo;
}
