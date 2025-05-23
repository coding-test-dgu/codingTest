# codingTest
네카라쿠배당토를 가고 싶은 자들의 치열한 코딩테스트 준비 흔적을 남긴 곳 입니다

## 목차
1. [스터디 진행 방식과 규칙](#-스터디-진행-방식과-규칙)  
   - [진행 방식](#진행-방식)  
   - [회차별 진행 사항](#회차별-진행-사항)
2. [소스코드 업로드 규칙](#-소스코드-업로드-규칙)  
   - [파일명 업로드](#-파일명-업로드)  
   - [Commit Message 컨벤션](#-commit-message-컨벤션)  
   - [Pull request](#-pull-request)
3. [스터디원 규칙](#-스터디원-규칙)  
   - [브랜치 전략](#-브랜치-전략)  
   - [PR code review](#-pr-code-review)
4. [디렉토리 구조](#-디렉토리-구조)

## :large_orange_diamond: 스터디 진행 방식과 규칙
### 진행 방식
- 매주 라이브코딩 세션과 코드리뷰 세션 진행
- `라이브코딩 세션`은 문제 선정 후 풀이 + 각자의 풀이 방법 공유
- `코드리뷰 세션`은 각자 푼 문제 개념+알고리즘+풀이방식 설명
- 매주 일요일에 Main으로 Merge 진행

|월|화|수|목|금|토|일|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|`문제공지`||`라이브코딩`||`과제제출 PR`|`code review`|`코드리뷰 및 merge`|

### 회차별 진행 사항
|회차|문제 이름|문제 이름|문제 이름|문제 이름|문제 이름|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1주차 04.07~04.13|42748. K번째수|42840. 모의고사|43165. 타겟 넘버|||
<br>

## :large_orange_diamond: 소스코드 업로드 규칙
### :exclamation: 파일명 업로드
for 라이브코딩 : `날짜_이니셜_문제출처_문제이름.py`<br>
Ex.) 0406_KSH_Programmers[Level2]_도넛과 빙글빙글.py <br>

for 코드리뷰 : `주차_문제출처_문제이름.py` <br>
Ex.) 1주차_KSH_BOJ[Diamond1]_좌표압축.py
### :exclamation: Commit Message 컨벤션
```
이모티콘[Tag]: subject
```
:heavy_check_mark: `이모티콘` : 제출과 해결 유무를 구별
|Imoge|Description|
|:---:|---|
|:joy:|라이브코딩 문제 미해결시|
|:fire:|코드리뷰 과제 제출 및 라이브코딩 문제 해결시|
|:shit:|죽어도 모르겠을 때|

:heavy_check_mark: `Tag` : 어떤 종류의 `commit`인지 작성
|Tag|Description|
|:---:|---|
|Summit|주차별 코드리뷰 과제 제출|
|Unsol/Sol|라이브코딩 문제 미해결 / 해결|
|Refactor|소스 코드 수정 및 알고리즘 수정|
|Docs|문서 작업|

:heavy_check_mark: `subject` : 커밋 내용을 작성
```
예시)
🔥[Summit]: 1주차_KSH_과제제출
😂[Unsol]: KSH_문제 해결 중
🔥[Sol]: KSH_문제 해결 완료
💩[Unsol]: KSH_죽어도모르겠음
```

### :exclamation: Pull request
- PR 제목
    - 커밋메세지와 통일
- PR 내용<br>
    - `라이브코딩`<br>
    문제 접근 방식(어떤 아이디어->알고리즘->풀이방식)<br>
    어떤 어려움을 마주쳤는지(어디서 막혔는지 pain point)<br>
    리뷰과정에서 배운점과 확장 가능성
    - `코드리뷰`<br>
    문제 접근 방식(어떤 아이디어->알고리즘->풀이방식)<br>
    자유로운 내용 작성
- PR review : 모든 팀원들을 reviewer로 등록
    - 모든 팀원들 리뷰 마치면, merge
<br>

## :large_orange_diamond:스터디원 규칙
### :exclamation: 브랜치 전략
- 각자 이니셜로 된 브랜치에 커밋
- 커밋 후 PR을 열어, code review를 요청

### :exclamation: PR code review
- `라이브코딩`<br>
    내용 정리를 잘했는지 checking만 하고 댓글 달기

- `코드리뷰`<br>
    궁금한점 댓글 달기

- 리뷰 방식
    - 잘한 것은 과감하게 칭찬하기 Ex.) 종혁님 파싱 아이디어 너무 좋은데요??
    - 다른 풀이 방법이 있으면 간단히 소개 Ex.) 입력을 open(0)으로 받으면 수행시간 단축 가능합니다
    - 개선 필요한 부분 구체적으로 설명 Ex.) 2중 반복문이 수행시간 초과할 것 같아요
<br>

## :large_orange_diamond: 디렉토리 구조
```
└── 📂스터디원1 ( for 개인 문제 제출 )
       ├── 📂BOJ
       │      ├── 📂1주차
       |      |       ├── 💾문제1.py
       |      |       ├── 💾문제2.py
       |      |       └── 💾문제3.py
       │      ├── 📂2주차
       │      └── 📂...
       ├── 📂Programmers
       └── 📂기타플랫폼
. . .
 
└── 📂Study ( for 라이브 코딩 )
       ├── 💾KSH~~~.py
       ├── 💾LJH~~~.py
       ├── 💾LEE~~~.py

💾README.md
```
