
# ⚙Source Code
### ❗ (주)두시텍 및 대전시 드론 하늘길 사업에 기밀이 담긴 데이터는 제거하였습니다.


## DrServer
<div align="left">
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
</div>

#### 제작 : (주)두시텍 이재헌 사원 <br>

드론 중계서버로 드론이 전송한 비행 데이터 및 미션 데이터 로그를 받고 이를 가공하여 다음 작업을 실행함.
현재 프로젝트에서는 비행 데이터 및 미션 데이터를 Json 형식으로 웹 소켓 서버에 전송함.

## 웹 서버
#### 제작 : 한밭대학교 컴퓨터 공학과 강홍규 <br>
- #### java/com/example/dusi

	<div align="left">
		<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Conda-Forge&logoColor=white" />
		<img src="https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=Spring&logoColor=white" />
		<img src="https://img.shields.io/badge/Gradle-02303A?style=flat&logo=gradle&logoColor=white" />
	</div>
	
	Spring 프레임워크를 사용하여 웹 소켓 서버를 생성하고 중계 서버로부터 비행 데이터 및 미션 데이터를 받은 뒤 <br>
	해당 데이터를 파싱하여 웹 페이지로 값을 넘김. <br>
	또한 서버에 저장된 이전 비행 기록의 데이터를 가져와 해당 기록을 파싱하여 웹 페이지로 전달함.

 - #### resources
   	<div align="left">
		<img src="https://img.shields.io/badge/html5-E34F26?style=flat&logo=html5&logoColor=white" />
		<img src="https://img.shields.io/badge/css3-1572B6?style=flat&logo=css3&logoColor=white" />
		<img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat&logo=javascript&logoColor=white" />
		<img src="https://img.shields.io/badge/bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white" />	
		
	</div>

	#### 사용한 Open Source SW & Library
	- Kakao Map Web API
	- Highcharts
	- Three.js

	<br>

   	HTML, CSS, JavaScript 및 BootStrap 사용해서 웹 페이지를 구성함. Kakao Map Web API를 사용해 지도와 마커를 기능을 구현하였고 Highcharts 라이브러리를 사용하여 고도 및 속도 차트를 생성하였으며, Three.js 라이브러리를 사용하여 3D 모델로 드론의 roll pitch yaw 상태를 나타냈다. <br> 영상 재생관련 코드는 (주)두시텍 및 드론 하늘길 사업과 관련있으므로 현재 게시물에서 제거하였다. 
 	
  
