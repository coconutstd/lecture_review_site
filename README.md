멀티캠퍼스 학생들을 위한 커뮤니티
=============================

![image](https://user-images.githubusercontent.com/38436013/106375519-1618bf00-63d0-11eb-936c-d258c452aa77.png)

- 메인 페이지 : 인기 강의평, 인기 설문조사, 오늘의 책을 추천받고, 게시글을 클릭하면 링크로 넘어가요~



## 프로젝트 개요 

- 멀티캠퍼스 1차 인터페이스 프로젝트

- 멀티캠퍼스 수강생에게 필요한 서비스를 제공하는 웹사이트

- 실제 수강하며 느꼈던 불편한 점이나 건의사항을 바탕으로 제작.

- 더 좋은 교육환경을 위한 의견 제출 수단을 제공하고 학습의지를 고무할 수 있는 서비스 제공.

  

## 기여 & 역할

2020.08.10 ~ 2020.09.03

삼성 멀티캠퍼스 [융복합 프로제트형 클라우드 서비스 개발] 과정 - 1차 웹 인터페이스 프로젝트 

GitHub repo⇒ [https://github.com/coconutstd/lecture_review_site](https://github.com/coconutstd/lecture_review_site)

멀티캠퍼스 학생들을 위한 커뮤니티 사이트 => http://ondjango.site/ (Server is always open.)

![image](https://user-images.githubusercontent.com/38436013/106375732-12863780-63d2-11eb-8fae-c9877430bce3.png)



#### [이민용](https://github.com/miniongo3o)

- 팀의 분위기 메이커

- 도서 추천 목록 구현(Web Scrapping)
- 채팅방 구현
- 로그인/회원 가입 구현
- 회원가입 시 고유한 닉네임 생성

#### [이준의](https://github.com/coconutstd) (팀장)

- 팀의 살림꾼
- 설문 조사 기능 구현
- 메인홈페이지 UI 구현
- 로그인/회원 가입 구현
- Frontend/Backend 총괄 매니저

#### [홍유진](https://github.com/redcarrot01)

- 프로젝트 아이디어 뱅크

- 강의 평가 기능 구현

- 게시판 기능 구현

- 강의평가, 게시판 UI 구현

- 프로젝트 소개 MD 파일 작성

  

## 개발 환경

![image](https://user-images.githubusercontent.com/38436013/106376001-6b56cf80-63d4-11eb-9c93-25ff5da8be4b.png)

- Front-end : Bootstrap, jquery, ajax, HTML
- Back-end : Python, Django, AWS, BS4
- Infra , Platform : AWS RDS, AWS S3, Vultr



## 제공 기능

![image](https://user-images.githubusercontent.com/38436013/106376351-ee2d5980-63d7-11eb-8660-47778c8be157.png)

#### 회원 가입/로그인 : 아래의 모든 기능은 로그인한 사용자에게 제공된다.





![image](https://user-images.githubusercontent.com/38436013/106376357-f9808500-63d7-11eb-8a0b-3eea1f6b3aa8.png)

![image](https://user-images.githubusercontent.com/38436013/106376363-043b1a00-63d8-11eb-83c9-5336a0a1a451.png)

#### 강의 평가 : 강의 평가를 등록하고, 조회 할 수 있다.





![image](https://user-images.githubusercontent.com/38436013/106376369-0ef5af00-63d8-11eb-9c73-8a25e9fc4bf7.png)

#### 도서 추천 목록 : 도서 분야를 선택하여 추천수 랭킹으로 제공된(왼쪽부터 추천수 내림차순) 도서를 확인할 수 있고, 도서를 클릭하면 구매링크로 넘어갈 수 있다.





![image](https://user-images.githubusercontent.com/38436013/106376370-1d43cb00-63d8-11eb-828b-1f2ce02c678a.png)

![image](https://user-images.githubusercontent.com/38436013/106376406-5a0fc200-63d8-11eb-8480-c97a79a2762c.png)

#### 설문 조사 : 매니저와 학생들의 원내 생활 중 건의 사항을 제시하여 투표할 수 있다.





![image](https://user-images.githubusercontent.com/38436013/106376418-7e6b9e80-63d8-11eb-8510-2e771d0d9307.png)

#### 자유 게시판 : 익명성 보장을 위해 닉네임을 이용해 게시판에 글을 게시하고 댓글을 달거나 삭제 할 수 있다.





![image](https://user-images.githubusercontent.com/38436013/106376426-93483200-63d8-11eb-823c-52002e25cd33.png)

#### 채팅방 : 반별로 채팅창에 입장하여 랜덤의 닉네임으로 인원 제한 없이 채팅 할 수 있다.



## 서비스 아키텍처

![image](https://user-images.githubusercontent.com/38436013/106376516-647e8b80-63d9-11eb-921f-6585143def46.png)



1. client는 브라우저에 “ondjango.site” 로 접속
2. vultr는 AWS RDS를 이용하여 서비스와 관련된 데이터(유저, 게시글 등)을 모두 저장 및 요청
3. vultr는 AWS S3를 이용하여 정적 파일(이미지, 스크립트 등) 저장 및 요청





![image](https://user-images.githubusercontent.com/38436013/106376525-7f510000-63d9-11eb-9cce-4e229d6fe7ca.png)

1. 위는 Vultr에서 서버를 빌려 애플리케이션을 실행시키는 모습

2. 아래는 데이터베이스(AWS RDS)와 정적파일저장소(AWS S3)가 원격에 위치한 모습

   => 클라우드 서버와 DB 활용으로 운용 및 모니터링을 확인할 수 있다.

   

## 트러블 슈팅

![image](https://user-images.githubusercontent.com/38436013/106376723-3bf79100-63db-11eb-83e0-8f51964f8a85.png)



| 트러블슈팅 | 문제              | 문제 기술                                     | 표면 원인                                                    | 근본 원인                                                    |
| ---------- | ----------------- | --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Django     | NoReverseMatch    | Argument not found                            | Views.py에서 argument이름을 urls.py와 맞추지 않거나, template에서 넘어오는 데이터가 일치하지 않을 때 생김 | MVC모델에 익숙치 않아서 생기는 실수                          |
| Django     | Page Not Found    | 페이지를 찾을 수 없음                         | Urls.py문제 이거나,루트 프로젝트 밑의 메인 프로젝트 settings.py의 urls.py에앱 urls.py 추가 해주지 않음 | MVC 모델에 익숙치 않아서 생기는 실수                         |
| Django     | Operational Error | “Unknown Column …”                            | Models.py에는 컬럼을 적었지만, 실제 DB에 적용해주지 않음     | 기능 개발에 집중한 나머지 실제 DB는 신경쓰지 않아서 생기는 실수 |
| 배포       | AWS S3            | Resource Forbidden 403Error                   | S3버킷 내부의 자원들을 따로 공개설정 해주어야 함             | 지식 부족                                                    |
| 배포       | AWS S3            | CORS                                          | 호스팅 서버와 S3의 도메인이 달라서 생기는 오류, CORS 설정에 다른 도메인 허용 추가 | 지식 부족                                                    |
| 배포       | Vultur 가상 서버  | ALLOWED_HOST                                  | 장고 앱에 가상 서버의 IP주소 추가                            | 지식 부족                                                    |
| 배포       | Vultur 가상 서버  | AWS키 노출-> 미국 시애틀의 아마존에서 전화 옴 | 장고 settings.py에 AWS IAM S3접근 권한 키, 패스워드를 환경변수로 주지 않음 | 서버 설정의 귀찮음, 코드 저장소 관리의 귀찮음                |





## 추후 개선할 점

![image](https://user-images.githubusercontent.com/38436013/106376905-95ac8b00-63dc-11eb-91b1-0410177994e0.png)

- 커뮤니티 이용률을 놓이기 위한 스톱워치 타이머 제공, 데이터간 기록을 통해 사용자간 랭킹 표시
- 쿠키나 세션을 활용해 브라우저 종료시 로그인 해제
- 강의평을 사용자 반별로 글을 게시할 수 있는 권한 설정, 좋아요 기능
- 회원가입시 제공할 수 있는 닉네임DB(유머포인트) 확장

## 라이센스

#### 멀티캠퍼스 학생들을 위한 커뮤니티는 Copyright (c) OnDjango 2020 All rights reserved 이다. 

#### 이 소프트웨어는 무료 소프트웨어로, License 파일에 지정된 조건에 따라 재배포될 수 있다.
