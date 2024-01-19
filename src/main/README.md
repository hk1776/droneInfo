
# ⚙Source Code
### ❗ (주)두시텍 및 대전시 드론 하늘길 사업에 기밀이 담긴 데이터는 제거하였습니다.


## DrServer
<div align="left">
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
</div>
<br>

#### 제작 :  (주)두시텍 이제헌 사원 <br>

드론 중계서버로 드론이 전송한 비행 데이터 및 미션 데이터 로그를 받고 이를 가공하여 다음 작업을 실행함.
현재 프로젝트에서는 비행 데이터 및 미션 데이터를 Json 형식으로 웹 소켓 서버에 전송함.

## Android
<div align="left">
	<img src="https://img.shields.io/badge/Figma-F24E1E?style=flat&logo=figma&logoColor=white" />
	<img src="https://img.shields.io/badge/Android-3DDC84?style=flat&logo=android&logoColor=white" />
	<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Conda-Forge&logoColor=white" />
</div>
<br>
안드로이드 스튜디오를 사용하여 개발을 진행하였습니다. 서버와 Rest API 통신을 위해 Retrofit2 라이브러리를 사용하였습니다. 앱 UI는 xml으로 구성하였고, 각 인터페이스의 동작은 Java를 사용해서 구현하였습니다.<br>
출발지와 목적지 세부 설정 기능을 위해 네이버 지도 API와 구글 Geocoder를 사용하였으며 사용자 알림시스템 구현을 위해 구글 파이어베이스 FCM 기능을 사용하였습니다. 그밖에 사용자 프로필 사진 등록과 불러오기 기능은 Glide 라이브러리를 사용하였고
핸드폰 권한설정 관련 기능은 TedPermission 라이브러리를 사용하여 구현했습니다.

#### 사용한 Open Source SW & Library
- Java
- Android Studio
- Retrofit2
- Naver maps
- Google Geocoder
- Firebase FCM
- Glide
- TedPermission
