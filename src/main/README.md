
# ⚙Source Code
### ❗(주)두시텍 및 대전시 드론 하늘길 사업에 기밀이 담긴 데이터는 제거하였습니다.


## Server
<div align="left">
	<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Conda-Forge&logoColor=white" />
	<img src="https://img.shields.io/badge/jQuery-0769AD?style=flat&logo=jQuery&logoColor=white" />
	<img src="https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=Spring&logoColor=white" />
 <img src="https://img.shields.io/badge/Gradle-02303A?style=flat&logo=gradle&logoColor=white" />
	<img src="https://img.shields.io/badge/mongodb-47A248?style=flat&logo=mongodb&logoColor=white" />
	<img src="https://img.shields.io/badge/h2DB-4053D6?style=flat&logo=amazondynamodb&logoColor=black" />
	
</div>
<br>
AWS EC2 환경에서 Spring boot를 사용해서 개발하였습니다. Member Post 등에 대한 정보는 RDBMS인 H2DB에 저장하였고 채팅 기록 DTO인 ChatMessage는 MongoDB에 저장하였습니다. 각각의 DB는 SpringDataJPA ORM을 사용하여 CRUD 작업을 수행하였습니다.
각 기능은 MVC 패턴으로 개발을 하였으며 Repository, Service, Controller 세 부분으로 나눠 동작합니다. Repository 에서는 SpringDataJpa를 상속하여 DB에 직접적으로 접근해 Service에서 요청한 기능을 수행합니다. Service에서는 Controller에서 요청한 비즈니스 로직을 수행하며 DB에서 값을 가져오거나 수정해야할 상황이 발생할 시 Repository를 호출하여 해당 기능을 진행합니다. Service에서는 안드로이드에서 접근할 URL을 제공하며 Json 형식으로 안드로이드와 통신을 합니다. 또한 안드로이드에서 요청한 값을 Service 클래스를 호출하여 값을 반환받고 이를 안드로이드에 전송합니다.
그 밖에 Spring 프레임워크에서 제공하는 웹소켓 통신 기능을 활용해 채팅 서버를 제공합니다.

#### 사용한 Open Source SW & Library
- Java
- Spring & Spring Boot
- JPA & Spring Boot JPA
- Google gson
- H2 DB
- Mongo DB
- Firebase
- OKHttp
- lombok
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
