# 실시간 드론 관제 웹
**(주)두시텍 인턴 프로젝트 #1**
<br>
제작기간 : 2023.07.04~2023.09.04

## <u>👨‍🔧Producer
- #### 드론 관제 웹 서버 제작
	한밭대학교 컴퓨터공학과 강홍규
- #### 드론 데이터 중계 서버 제작
	(주)두시텍 이재헌 사원
	

## </u> 🧐Project Background
<h3>프로젝트 배경</h3>
  대전시 '<strong>드론 하늘길 사업*</strong>'에 참여한 기업의 드론의 위치, 고도, 속도 등 실시간 비행 상태를 웹으로 확인하고자 제작
  <br>
  <br>

   <strong>*드론 하늘길 사업</strong> : 대전광역시는 대전의 3대 하천 상공에 드론하이웨이(드론하늘길)를 조성하여 일반시민 대상으로 4차 산업혁명 시대 최신 드론기
술을 실생활에 적용한 대시민 드론서비스를 실시함은 물론, 디지털 소외계층의 교육을 병행하여 수호천사 드론서비스를 구축하
고 한국판 뉴딜 시민 체감도를 제고하고 주민 편의를 증진할 계획이다.

  
## 💻System Design

<h3> Tech Stack </h3>
<div align="left">
	<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Conda-Forge&logoColor=white" />
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
	<img src="https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=Spring&logoColor=white" />
	<img src="https://img.shields.io/badge/Gradle-02303A?style=flat&logo=gradle&logoColor=white" />
  <img src="https://img.shields.io/badge/Intellij%20IDE-000000?style=flat&logo=intellijidea&logoColor=white" />
	<img src="https://img.shields.io/badge/Tomcat-F8DC75?style=flat&logo=ApacheTomcat&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
</div>
<br>

### System Requirements
   
![요구사항](https://github.com/hk1776/droneInfo/assets/77769783/2c852ebc-18cd-436f-8712-b2b42f97ee24)

<br><br>
## 📲Result
   ### 시스템 구성도
![요구 결과](https://github.com/hk1776/droneInfo/assets/77769783/10cf44f3-8e62-4068-9d68-470b8302577d)

   ### 주요기능
   - #### 현재 접속중인 드론 리스트
      - 소켓통신으로 현재 비행중인 드론의 id 기업명 등을 리스트로 표시<br>
     
       ![5](https://github.com/hk1776/droneInfo/assets/77769783/8bfeca32-aebb-4dfa-a885-d8201a0c2812)
<br><br>

   - #### 지도에 마커로 드론 위치 표시 및 영상 출력
      - 소켓통신으로 현재 비행중인 드론의 좌표값을 받아 지도에 표시
      - 지나간 경로는 점으로 표현
      - 마커 클릭 시 드론 기체 이름 표시
      - 좌측 하단에 실시간 드론 촬영 영상 재생 <br>
      
      ![1](https://github.com/hk1776/droneInfo/assets/77769783/f935a7e5-4ca9-4bfe-b2f6-2ba86a9a6716)

<br><br>
     
   - #### 그래프로 고도 속도 표시

      - Highcharts 라이브러리를 사용하여 고도 속도 그래프 표현
      - 드론의 지표면, 해수면 기준 고도를 그래프로 표시
   
      ![2](https://github.com/hk1776/droneInfo/assets/77769783/3cfb6eec-5458-491b-a774-42751c702c1d)

      - 드론의 속도를 그래프로 표시
   
      ![4](https://github.com/hk1776/droneInfo/assets/77769783/fd5d855a-eb41-4d6f-9e20-d62d1a980237)



<br><br>


   - #### 3D 모델로 드론의 상태 표시
      - 드론의 roll pitch yaw 상태를 3D 모델로 표현
      - 3D 모델은 (주)두시텍의 KNX2 모델을 사용하였고 Three.js 라이브러리를 사용하여 웹에 표현 <br>

   
      ![6](https://github.com/hk1776/droneInfo/assets/77769783/47d66bdd-4e55-4660-b339-4a65dcab0f8a)



<br><br>

  - #### 미션 데이터 표시
      - 조종기에서 특정 포인트를 지정해 드론이 이동할 경로를 지정하는 미션 데이터를 설정하면 웹에서도 미션 데이터가 표시됨
      - S : 시작지점
      - M : 미션 포인트
      - E : 종료 지점 <br>
         
      ![7](https://github.com/hk1776/droneInfo/assets/77769783/6cf2e03e-a9df-4396-a0dd-a598ff8ad723)


<br><br>

  - #### 드론 로그 시뮬레이션
      - 저장된 비행 로그 기록을 바탕으로 웹에 비행 시뮬레이션을 실행
      - 2배속 3배속으로 비행 기록을 재생 가능 <br>
         
      ![8](https://github.com/hk1776/droneInfo/assets/77769783/78d9f4d9-f645-4835-a744-fd2be78d9af4)
    
  
<br><br>
   
  ## 🎓Conclusion
	- (주)두시텍에서 드론 시연 및 연구용으로 사용 
 	
