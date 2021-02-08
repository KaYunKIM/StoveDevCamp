# TweetDeck 클론 발표영상 요약

## 발표 영상

### 프론트

- React (scaffolding ?)

- Socket 통신

- Column 별 드래그앤드롭

- MSA

### 백엔드

- 게이트웨이

- 인증

- 피드 서버

→ 스프링 처음

- 어려운 점

   - Real-time

- DB

   - Cassandra, Redis

### 빅데이터, 트렌드 분석

- 의미 있는 데이터를 어떻게 ?

   - 인기 트윗 랭킹 : 30초 주기로 가장 많이 리트윗 되고 있는 트윗 목록

   - 해시태그 랭킹 : 30초 주기로 가장 많이 언급되는 hashtag 분석

- Spark에서 메모리 기반 병렬처리를 통해 빠르게 처리

   - 30초간 가장 많이 언급되는 Top10을 보여줌

   - Favorite, Quoted, Retweet 등과 조합하여 새로운 데이터 프레임

   - 카산드라로부터 30초 주기로 쌓인 데이터들을 스파크로 가져와 전처리 후 새로운 데이터 프레임 생성, 그 후 Favorite, Quoted, Retweet, 카운트를 합산 하여 결과값이 큰 순서로 정렬, group by 연산으로 중복된 id의 트윗 제거 → Redis에 저장하여 빠르게 클라이언트에 제공 가능

- 해시태그의 불필요한 데이터 제거 

   - [불용어(stopword)](https://wikidocs.net/22530#:~:text=%EA%B0%96%EA%B3%A0%20%EC%9E%88%EB%8A%94%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%90%EC%84%9C%20%EC%9C%A0%EC%9D%98%EB%AF%B8%ED%95%9C,%EB%90%98%EC%A7%80%20%EC%95%8A%EB%8A%94%20%EB%8B%A8%EC%96%B4%EB%93%A4%EC%9D%84%20%EB%A7%90%ED%95%A9%EB%8B%88%EB%8B%A4.) 제거 (자연어 처리 관련)

   - 유사어 하나로

- Spark가 가장 어려웠다. (최적화, 성능 테스트, 메모리 최적화)

### 분산 클러스터를 활용한 데이터 파이프라인 구축

- 트위터 API로 계속 가져와서 카프카 메시지 큐에 쌓음

- 쌓인 메시지를 스파크에서 실시간으로 읽어들여 데이터를 처리하고 분산형 디비에 저장하게 된다

- Consumer인 Spark 앱에 필요한 데이터 형태로 필터링 및 변형되어 DB에 저장

### 트렌드 분석 도구

[Google 트렌드](https://trends.google.co.kr/trends/?geo=KR)

![TweetDeck-클론-발표영상-요약-image-0](images/TweetDeck-클론-발표영상-요약-image-0.png)

[](https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F06qd3&gl=US&ceid=US%3Aen)



[네이버 데이터랩](https://datalab.naver.com/)

### 인스타그램 분석 도구

- impression : 얼마나 오래 그 포스트에 머물렀는지를 측정

- reach : 게시물이 얼마나 많은 사람에게 퍼졌는지

[Instagram Analytics for Business Accounts](https://youtu.be/ziC31bTUD18)

[SNS분석 < 시각화통계 < 문화셈터](https://stat.mcst.go.kr/mcst/WebPortal/public/visual/snsBigdata.html)

### 느낀점

- 프론트엔드 적 관점의 TweetDeck

   - DragNDrop

   - Redux를 활용한 전역 상태관리

   - 실시간(Real-Time)을 위한 Socket 통신 구현

→ 결국 구현하기 위한 기술은 복잡했지만, 결과물 상으로는 TweetDeck 클론, 부족한 기능 구현으로 아쉬워 보임

- `트렌드 분석` 에 초점? 통합에 초점?

- 어느 수준의 데이터를 보관할 것인지?

   - 스크롤 위치, 커서 위치 보관

- 확장성 

   - SNS는 페이스북, 인스타그램, 트위터 뿐만아니라 스냅챗, 핀터레스트, 유튜브, 왓챠 등등 수도없이 많고, 앞으로도 계속 나타날 것

   - API 제공을 하지 않는다면

      - 어떻게 타사 SNS 콘텐츠에 대해 데이터의 트렌딩을 분석할 것인가에 대한 전략을 가지는 것

      - 단지 크롤링을 한다면 해당 콘텐츠가 얼마나 사용자에게 impression과 Reach 되었는지 어떻게 판단할 것인가

[마케터가 좋아할만한 SNS 분석 툴 10선](https://www.ciokorea.com/news/37875?page=0,1)

- 완성도 vs 기술적 챌린지

   - 트렌드 분석이라는 주제로 갔을 때, 깊이 파느냐 넓게 가느냐에 대한 전략적인 차이가 있을 것 같다.

   - 완성도 측면

      - 특정 SNS의 특화된 측면에 대해 차별화된 트렌드 분석 도구 및 방법 제시

      - 프론트 : 시각화 방법, 인터랙션에 대한 고민, Real-Time 구현

      - 백엔드 : 다양한 소스의 데이터를 어떻게 처리, 관리할 것인지, 최적화, 성능 개선, 테스팅

      - 데이터 처리 : 데이터 소스를 어디서 어떻게 얻을 것인가? 처리 방법, 성능 최적화

   - 기술적

      - 다양한 SNS(+ 새롭게 생겨날 수 있는 서비스)에서 어떻게 데이터 소스를 얻을 것인가

      - 엄청나게 많은 데이터 소스의 데이터를 어떻게 관리할 것인지 (아키텍쳐 적인 측면이 강할 듯)

      - 쏟아지는 데이터 관리 도구 및 전략

[d3/d3](https://github.com/d3/d3)

- 사용자

데이터의 1차 결과물

