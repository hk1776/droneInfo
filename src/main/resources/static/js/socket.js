// 웹소켓 생성
const socket = new WebSocket("ws://localhost:8080/ws/drone");

socket.onopen = function (e) {
    console.log("소켓 실행");

    let data = {
        msg : "flight_info",
        drone_stat: [
            {
                status : "Web Connect"
            }
        ]
    };
    socket.send(JSON.stringify(data))
};
//var dateText = document.getElementById("simuldate");
// 데이터를 수신 받았을 때
socket.onmessage = async function (e) {
    let data = JSON.parse(e.data);
    settings(data);
};

// 에러가 발생했을 때
socket.onerror = function (e) {
    console.log(e);
};
