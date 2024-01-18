# 실시간 드론 관제 웹
**(주)두시텍 인턴 프로젝트**

## <u>👨‍🔧Producer
<h3>팀 구성</h3> 
<h4>- 드론 관제 웹 서버 제작</h4>
 한밭대학교 컴퓨터공학과 강홍규
   <br>
<h4>- 드론 데이터 관리 서버 제작</h4>
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
![project](https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/da36abb1-c58a-4f56-a4e8-b33c3a01292f)
   ### 주요기능
   - #### 로그인 기능
      - 세션을 활용한 자동 로그인기능 <br><br>
      	<img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/8ac89075-1000-4259-8a3e-7ece76e0843a" width="200" height="400"/>
     
   - #### 카풀 게시물 리스트
      - 게시물 검색 기능(출발지, 도착지, 운행요일, 세부 옵션 등으로 검색)
      - 회원 가입시 등록한 사용자의 거주지와 인접한 출발지를 가진 카풀 게시물만 보는 기능
      - 게시물 요약 정보 확인 (운전자, 별점, 출발지, 도착지, 출발시간)<br><br>
	<img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/4309219b-9fa3-40d8-9279-bad55ca3fb1e" width="200" height="400"/>
  	<img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/0f55ae73-bdf7-4bf1-988f-2dbec0b43aa6" width="200" height="400"/>   

   - #### 카풀 게시물 등록
      - 마이 페이지에서 차량을 등록한 사용자만 게시물 등록 가능
      - 네이버 지도 API를 사용하여 출발지와 목적지를 세밀하게 등록 가능
      - 카풀 운행 요일 및 시간 등록
      - 카풀 운행 거리에 따른 카풀 요금 추천
      - 카풀 탑승 세부 조건 등록 (성별, 흡연여부, 반려동물 탑승 가능 여부, 아이동반 탑승 가능여부, 화물 소지 가능 여부)
      - 최대 탑승 가능 인원 설정 
      - 추가 전달사항 등록 <br><br>
        <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/7a460606-3b36-482f-8690-b4dc18174198" width="200" height="450"/>
	        <img src="https://github.com/HBNU-SWUNIV/come-capstone23-pool/assets/77769783/5d41e566-e468-4675-9703-77c9a44a35d5" width="200" height="400"/>

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
