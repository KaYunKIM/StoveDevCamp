# Code Convention

### Git commit 

- Branch 관리

   - Master → Develop → Frontend/Backend/Data → Feature/기능명 브랜치 따기

- Commit message

   - "feat/기능이름: Create/Modify/Refactor/Delete 등 작업 파일 이름, jira 이슈 번호

   - ex) git commit -m "feat/login: Create login.vue, S03P22A305-2"

   ## Github Repogitory naming convention

Naming a GitHub repo seems so simple - you'd just want something that is:

- Descriptive

- Readable

- Consistent

- Contextual

- Future-friendly

- Extensible

- Reusable

- Brief (short / succinct)

Although there is no wrong way to name a repo, some names are better than others. Here are some considerations for picking an awesome name for your GitHub repo.

#### __Follow Conventions__

Following the naming conventions that are established for a particular project, code language or community is good place to start. But often Git projects are for websites where many languages are in play. For simplicity sake, modeling website repos after the domain makes sense.

```plain text
http://domain.com ➔ domain.com.git
http://sub.domain.com ➔ sub.domain.com.git

```

For other projects, let's keep the lowercase and dashes pattern:

```plain text
star-wars.git
the-empire-strikes-back.git
return-of-the-jedi.git

```

## __Semantic Commit Messages__

See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

feat/login/2

chore(deps): Install dependencies

feat(login): implement login form

main ← feat/login/2

`squash and merge` / `merge`

chore(deps): Install dependencies

feat(login): implement login form

feat(login): add login form

feat: Implement login feature, S03P22A305-2

요약

~~

관련 자료

~~

git commit

feat: add hat wobble

### __Example__

```plain text
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.

```

More Examples:

- `feat`: (new feature for the user, not a new feature for build script)

- `fix`: (bug fix for the user, not a fix to a build script)

- `docs`: (changes to the documentation)

- `style`: (formatting, missing semi colons, etc; no production code change)

- `refactor`: (refactoring production code, eg. renaming a variable)

- `test`: (adding missing tests, refactoring tests; no production code change)

- `chore`: (updating grunt tasks etc; no production code change)

References:

- [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)

- [https://seesparkbox.com/foundry/semantic_commit_messages](https://seesparkbox.com/foundry/semantic_commit_messages)

- [http://karma-runner.github.io/1.0/dev/git-commit-msg.html](http://karma-runner.github.io/1.0/dev/git-commit-msg.html)

[Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

## __Git branch names__

Categorize by a slash(`/`) then concatenate with a dash(`-`).

For example,

```plain text
feat/fire-alarm

feat/swimming-pool

refactor/rename-variables

fix/wrong-type-declarations

test/swimming-pool

...
```

## Database Naming Convention

### 복수형 vs 단수형

- 테이블은 엔티티의 인스턴스들을 표현하기 때문에 의미적으로 복수형이 더 맞다.

- 테이블을 단수형을 사용했을 때 SQL 문에서 `SELECT activity.name` 으로 표현할 수 있는 장점이 있다.

   - 하지만 복수형을 사용하더라도 SQL alias를 사용하는 것으로 극복 가능하다.

   - `SELECT id, name, description FROM products product WHERE product.name = ‘foo’ AND product.description = ‘bar’`

- REST API에서 자원에 대한 요청 역시 테이블에 따라 복수형으로 하는 것이 좋다. ex) `GET /users/1`

[The table naming dilemma: singular vs. plural](https://medium.com/@fbnlsr/the-table-naming-dilemma-singular-vs-plural-dc260d90aaff#:~:text=Since%20the%20table%20is%20storing,when%20writing%20an%20SQL%20statement)

### camelCase vs snake_case in database

- MySQL 에서 데이터베이스는 데이터 디렉토리 내의 디렉토리에 해당하고, 테이블은 파일에 해당한다. 따라서, 운영체제의 대소문자 구분이 데이터베이스, 테이블 및 트리거 이름의 대소문자 구분에 영향을 준다.

- Windows는 대소문자를 구분하지 않지만 Unix는 구분, macOS는 구분하지 않는 파일 시스템을 사용하지만 대소문자를 구분하는 볼륨도 지원함.

- 따라서 `snake_case` 가 이식성과 사용 편의성 측면에서 가장 권장된다.

- 하지만 `camelCase` 를 사용하는 경우도 있고, JS가 `camelCase`를 사용하기 때문에 얻을 수 있는 편의성이 있다.

- 무엇보다 일관된 규칙을 채택하는 것이 가장 좋다.

[MySQL :: MySQL 8.0 Reference Manual :: 9.2.3 Identifier Case Sensitivity](https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html)

## RESTful API

### 서버 응답에 HTTP 상태 코드를 사용해라

오류 발생시 API 사용자의 혼동을 없애기 위해 오류를 정상적으로 처리하고 발생한 오류의 종류를 나타내는 HTTP 응답 코드를 반환해야합니다. 이를 통해 API 관리자는 발생한 문제를 이해할 수있는 충분한 정보를 얻을 수 있습니다. 오류로 인해 시스템이 중단되는 것을 원하지 않으므로 오류를 처리하지 않은 채로 둘 수 있습니다. 즉, API 소비자가 오류를 처리해야합니다.

일반적인 오류 HTTP 상태 코드는 다음과 같습니다.

- 400 잘못된 요청 – 이는 클라이언트 측 입력이 유효성 검사에 실패 함을 의미합니다.

- 401 Unauthorized – 사용자가 리소스에 액세스 할 수있는 권한이 없음을 의미합니다. 일반적으로 사용자가 인증되지 않은 경우 반환됩니다.

- 403 금지됨 – 사용자가 인증되었지만 리소스에 액세스 할 수 없음을 의미합니다.

- 404 Not Found – 리소스를 찾을 수 없음을 나타냅니다.

- 500 내부 서버 오류 – 일반적인 서버 오류입니다. 아마도 명시 적으로 던져서는 안됩니다.

- 502 Bad Gateway – 업스트림 서버의 잘못된 응답을 나타냅니다.

- 503 서비스를 사용할 수 없음 – 서버 측에서 예기치 않은 일이 발생했음을 나타냅니다 (서버 과부하, 시스템의 일부 오류 등이 될 수 있음).

[Best practices for REST API design - Stack Overflow Blog](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

[Best Practices for your REST API](https://solidgeargroup.com/en/best-practices-rest-api/)

## Python Code Convention

- 전체적인 스타일은 black 으로 관리

- commit 전 검사 자동화를 위해 pre-commit 사용

[Black으로 파이썬 코드 스타일 통일하기](https://www.daleseo.com/python-black/)

- 이 외의 고려사항

   1. 모듈화. 각 프로그램을 공통적인 부분에서 함수 단위까지 점차 세분화  

   ( 하나의 .py 에는 여러 개의 class 가 있어도 되지만 기능적으로 공통적인 요소가 있어야 하고,  class - method  관계도 마찬가지)

    2.  class 이름은 명사

    3.  method 이름은 동사_명사(대상)

       - 데이터베이스 관련 기능의 method 명은 해당 쿼리의 명령어로 표현

      (select, insert, delete, update 등)

       - Database 내의 method 는 최대한 간결히 표현

       - ORM 사용하시면 조금 다를 수 있는 부분이라 참고만 해주세요

    4. application 파일에서는 Database 내의 method 를 직접 사용하지 않을 것

       - wrapper method 만들어 필요에 따라 변형(에러 및 파라미터 처리) 하여 사용

       - wrapper method 함수의 이름은 DB method 이름을 응용하여 사용

      (select → get / insert → save 등)

     5. method 별로 기능과 설명 및 파라미터 설명 주석 꼭 달기

        -  함수 내부 첫 줄에서 """ """ 처리로 쉽게 작성할 수 있음(파이참만 제공될 수도 있어요..)

        -  파라미터, 리턴 값의 타입도 명시 [str], [int] 등

        -  이 외에도 우리 모두를 위해 # 를 사용한 주석을 코드 곳곳에 넣어주면 좋아요:)

        -  단 코드만 봐도 알 만한 코드에 대해서는 구구절절 주석 달 필요는 없음

     6. 변수 명은 최대한 줄여 쓰지 않기

        - 의미가 명확하거나 너무 길어지는 경우를 제외하고는 단어 전체 사용

        - 의미를 알 수 없는 단순한 변수 이름 사용 x (a, b, num 등)

   ```python
   # Example DB
   class Database:
   	def select_registered_users(user_id):
   		"""
   		회원가입한 유저의 정보를 조회
   
   		:parm user_id: [str] 유저의 ID
   		
   		:return: [dict] 유저의 데이터(ID, name, register_date)
   		"""
   		## fill the function
   
   
   # Example application
   class Website:
   	def get_registered_users(user_id, date):
   		"""
   		특정 날짜에 회원가입한 유저의 정보를 조회
   
   		:parm user_id: [str] 유저의 ID
   		:parm user_id: [str] 특정 날짜('YYYY-MM-DD)'
   		
   		:return: [dict] 유저의 데이터(ID, name, register_date)
   		"""
   		## call 'select_registered_users' here
   		## and implement remained function
   ```

   