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
  대전시 '<strong>드론 하늘길 사업*</strong>'에 참여한 기업의 드론의 위치, 고도, 속도 등 실시간 비행 상태를 웹으로 확인하고자 제작하였습니다.
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

   - #### 지도에 마커로 드론 위치 표시
      - 소켓통신으로 현재 비행중인 드론의 좌표값을 받아 지도에 표시
      - 지나간 경로는 점으로 표현
      - 마커 클릭 시 드론 기체 이름 표시<br>
      
      ![1](https://github.com/hk1776/droneInfo/assets/77769783/f935a7e5-4ca9-4bfe-b2f6-2ba86a9a6716)


     
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

  - #### 카풀 게시물 확인
      - 카풀 세부 정보 확인(출발지, 운행 요일 및 시간, 세부옵션, 카풀 평점 등)
      - 카풀 게시물 등록자 정보 확인(사용자 정보 페이지로 이동)
      - 출발지 목적지 터치 시 지도에 위치 표시
      - 카풀 신청 기능 <br><br>
             <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/538c3449-4e66-4c22-84fc-d920d6ec30d0" width="200" height="450"/>


  - #### 등록된 카풀 리스트
      - 현재 자신이 소속된 카풀 리스트 확인
      - 카풀 게시물 등록자인 경우 게시물 관리자가 됨
      - 카풀 관리자인 경우 해당 카풀 신청자 리스트를 확인 가능
      - 카풀 관리자인 경우 해당 카풀에 공지사항 등록 가능
      - 카풀 관리자인 경우 해당 카풀에 새로운 유저 등록 및 기존 유저 탑승 일정 수정 및 삭제 가능
      - 카풀 운행 요일이 표로 나오며 해당 요일에 탑승자 명단과 운전자가 표시
      - 카풀 탑승객인 경우 1회 카풀 평점 등록 가능 <br><br>
        <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/7e4f5a57-d259-41ac-a57b-8fe345db178a" width="200" height="500"/>
  
  - #### 채팅 기능
      - 카풀 관리자는 카풀 신청자 리스트에서 신청자의 평점과 세부 정보확인 가능
      - 카풀 관리자는 신청자를 카풀에 등록시키기 전 채팅 가능
      - 채팅 버튼 누를 시 채팅 목록 페이지에 채팅방 생성
      - 소켓 통신으로 실시간 채팅 <br><br>
        
        <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/f4a76cb7-3b73-47ea-baba-853331d1c15a" width="200" height="400"/>

  - #### 마이페이지
    - 본인의 평점 확인 기능
    - 프로필 사진 등록 기능
    - 카풀 탑승 일정 시간표로 호가인 가능
    - 차량 사진과 정보 등록 기능
    - 가상 머니 충전, 송금 출금 기능
    - 회원 정보 수정 및 회원 탈퇴 기능 <br><br>
        <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/dcd59b11-9bbe-4c06-a676-babfbfee8011" width="200" height="400"/>

   
  ## 🎓Conclusion

  글로벌 카풀 시장의 규모가 148억 달러(2015)에서 701억 달러(2021)로 급증한 것에 비해 우리나라의 카풀 규모는 작은 편이지만 처음 서비스가 시작된 해에 6억 원(2011)에 불과하던 것과 비교하면 1800억 원(2017)으로 300배 성장했다. 전 세계적으로 공유 교통이 새로운 교통수단으로 자리 잡아가고 있고 우리나라 또한 택시대란을 해소하기 위해 국토교통부가 여객자동차운수사업법 개정 가능성을 논의하고 있다. 따라서 서비스를 공급하여 시장의 수요를 만들고 공유 교통을 더욱 대중화하는 것을 기대할 수 있다.
