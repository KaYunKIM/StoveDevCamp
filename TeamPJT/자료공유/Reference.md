# Reference

## Twitter API

[Use Cases, Tutorials, & Documentation](https://developer.twitter.com/en)

[트위터 API 소개](https://help.twitter.com/ko/rules-and-policies/twitter-api)

## RESTful API

[Best practices for REST API design - Stack Overflow Blog](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

## MSA(Micro Service Architecture)

[대용량 웹서비스를 위한 마이크로 서비스 아키텍쳐의 이해](https://bcho.tistory.com/948)

[MSA 아키텍쳐 구현을 위한 API 게이트웨이의 이해 (API GATEWAY)](https://bcho.tistory.com/1005)

## Python 가상환경 & 패키지 관리

### 가상 환경 설치하기

- 로컬에 `venv`로 파이썬 가상 실행환경을 설정합니다.

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
which python
```

### 의존성 설치하기

- `requirements.txt` 에 명시된 의존성을 설치합니다.

```bash
pip install -r requirements.txt
```

### 의존성 관리하기

- 현재 pip에 설치된 모듈들을 `requirements.txt`에 명시합니다.

```bash
pip freeze > requirements.txt
```

### 참고자료

[파이썬에서 venv로 가상 환경 사용하기](https://www.daleseo.com/python-venv/)

[Python 패키지 의존성 관리](https://xn--lg3bu39b.xn--mk1bu44c/85)

