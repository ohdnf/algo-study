# algo-study
> 남겨진 자들의 외로운 사투...
> 박선환, ~~박유은~~, 신채린, ~~오지수~~, 장현준, 홍주표



## 스터디 규칙

### 언제

매주 목요일 오후 8시에 미팅을 합니다.

### 어디서

오프라인 또는 온라인 미팅을 합니다.

- [온라인 미팅 링크](https://ssafylive.webex.com/join/jupyohong7)

### 무엇을

- 책 <파이썬 알고리즘 인터뷰>을 **한 챕터씩** 풀고
- 프로그래머스의 카카오 블라인드 테스트 **한 문제씩** 도전해봅니다.

### 어떻게

- 해당 문제 폴더에 소스 코드를 저장하고 Github Repository에 푸시합니다!

### 누가

누구든 스터디에 참여하고 싶으신 분은 멤버들에게 연락해주세요:wink:



## 협업 룰

### 파일 형식

`한글로문제이름띄어쓰기없이_내이름.확장자명`

### 커밋 메시지

오답노트 등 문제 풀면서 느낀 점을 적어서 공유해주세요:kissing_heart:

> `git commit` 명령어로 vi 창에서 편집합니다.
>
> (예시)
>
> ```
> 왜 이 문제가 이분탐색인가?
> 걸린 시간: 1시간 30분
> 우선 구하고자 하는 값이 모든 사람이 심사를 받을 수 있는 시간의 최솟값이다.
> 심사에 걸리는 시간, 남은 사람(n)의 최대 범위가 1,000,000,000까지 된다.
> 시간이 주어지면 각 심사관마다 심사할 수 있는 사람의 수를 구할 수 있다.
> 해당 시간에 심사할 수 있는 사람의 합(passed)이 주어진 n값(심사 받아야하는 사람의 수)보다 크면 답이 될 수 있다.
> 시간을 0분(주어진 시간의 단위는 분이다)부터 1분씩 늘려나가면 언젠가 심사가능 한 사람의 수가 n값보다 커진다.
> 따라서 답은 0과 무한히 큰 수 사이에 있을 것이다. 
> 하지만 위와 같은 방법은 만약 답이 1,000,000,000분이라면 1,000,000,000번 계산해야하므로 효율적이지 못하다.
> 효율적인 방법 중 하나가 이분탐색이다.
> 최소 시간(0)과 최대 시간의 중간값을 구해 조건을 만족하면 더 작은 값(시간의 최솟값을 구하라고 하였으므로)을 찾고
> 조건을 만족하지 못한다면 더 큰 값을 찾는다.
> 이 문제에서 최대 시간은 주어진 인원을 심사관이 똑같이 나눠 심사했을 때라고 가정하고 풀었다.
> 최대 시간 = (남은 인원 수 // 심사관 수) * (각 심사관마다 소요 시간)
> 조건을 만족한다면 최솟값을 중간값으로 치환해 다시 중간값을 구하고
> 조건을 만족하지 못한다면 최댓값을 중간값으로 치환해 다시 중간값을 구한다.
> 최솟값이 최댓값보다 커질 때까지 반복한다.
> 0 ----------------------------- 25 ----------------------------------------------- 51
>                                 25 ------------------------ 38 ------------------- 51
>                                 25 ------------ 31 -------- 38
>                                 25 ---- 28 ---- 31
>                                         28 -29- 31
>                                         28
> ```



## 우리가 풀 문제들

### 파이썬 알고리즘 인터뷰

> 박상길 저, 책만
>
> - [구매 링크](https://book.naver.com/bookdb/book_detail.nhn?bid=16406247)
> - [Github 링크](https://github.com/onlybooks/algorithm-interview)
> - [정오표](https://www.onlybook.co.kr/entry/algorithm-interview-errata)

책에 나온 LeetCode 문제들을 열심히 풀어봅니다.



#### 비선형 자료구조

##### 그래프
- [x] [섬의 개수](https://leetcode.com/problems/number-of-islands/)
- [x] [전화 번호 문자 조합](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [x] [순열](https://leetcode.com/problems/permutations/)
- [x] [조합](https://leetcode.com/problems/combinations/)
- [x] [조합의 합](https://leetcode.com/problems/combination-sum/)
- [x] [부분 집합](https://leetcode.com/problems/subsets/)
- [x] [일정 재구성](https://leetcode.com/problems/reconstruct-itinerary/)
- [x] [코스 스케줄](https://leetcode.com/problems/course-schedule/)

##### 최단 경로 문제
- [x] [네트워크 딜레이 타임](https://leetcode.com/problems/network-delay-time/)
- [x] [K 경유지 내 가장 저렴한 항공권](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

##### 트리
- [x] [이진 트리의 최대 깊이](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] [이진 트리의 직경](https://leetcode.com/problems/diameter-of-binary-tree/)
- [x] [가장 긴 동일 값의 경로](https://leetcode.com/problems/longest-univalue-path/)
- [x] [이진 트리 반전](https://leetcode.com/problems/invert-binary-tree/)
- [x] [두 이진 트리 병합](https://leetcode.com/problems/merge-two-binary-trees/)
- [x] [이진 트리 직렬화 & 역직렬화](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [ ] [균형 이진 트리](https://leetcode.com/problems/balanced-binary-tree)
- [ ] [최소 높이 트리](https://leetcode.com/problems/minimum-height-trees)
- [ ] [정렬된 배열의 이진 탐색 트리 변환](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)
- [ ] [이진 탐색 트리(BST)를 더 큰 수 합계 트리로](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree)
- [ ] [이진 탐색 트리(BST) 합의 범위](https://leetcode.com/problems/range-sum-of-bst)
- [ ] [이진 탐색 트리(BST) 노드 간 최소 거리](https://leetcode.com/problems/minimum-distance-between-bst-nodes)
- [ ] [전위, 중위 순회 결과로 이진 트리 구축](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

##### 힙

- [ ] 배열의 K번째 큰 요소
- [ ] 트라이 구현
- [ ] 팰린드롬 페어



#### 알고리즘

##### 정렬

- [ ] 리스트 정렬
- [ ] 구간 병합
- [ ] 삽입 정렬 리스트
- [ ] 가장 큰 수
- [ ] 유효한 애너그램
- [ ] 색 정렬
- [ ] 원점에 K번째로 가까운 점

##### 이진 검색

- [ ] 이진 검색
- [ ] 회전 정렬된 배열 검색
- [ ] 두 배열의 교집합
- [ ] 두 수의 합 II
- [ ] 2D 행렬 검색 II

##### 비트 조작

- [ ] 싱글 넘버
- [ ] 해밍 거리
- [ ] 두 정수의 합
- [ ] UTF-8 검증
- [ ] 1비트의 개수

##### 슬라이딩 윈도우

- [ ] 최대 슬라이딩 윈도우
- [ ] 부분 문자열이 포함된 최소 윈도우
- [ ] 가장 긴 반복 문자 대체

##### 그리디 알고리즘

- [ ] 주식을 사고팔기 가장 좋은 시점 II
- [ ] 키에 따른 대기열 재구성
- [ ] 태스크 스케줄러
- [ ] 주유소
- [ ] 쿠키 부여

##### 분할 정복

- [ ] 과반수 엘리먼트
- [ ] 괄호를 삽입하는 여러 가지 방법

##### 다이나믹 프로그래밍

- [ ] 피보나치 수
- [ ] 최대 서브 배열
- [ ] 계단 오르기
- [ ] 집 도둑



#### 선형 자료구조

##### 해시 테이블

- [ ] 해시맵 디자인
- [ ] 보석과 돌
- [ ] 중복 문자 없는 가장 긴 부분 문자열
- [ ] 상위 K 빈도 요소

##### 배열

- [ ] 두 수의 합
- [ ] 빗물 트래핑
- [ ] 세 수의 합
- [ ] 배열 파티션 I
- [ ] 자신을 제외한 배열의 곱
- [ ] 주식을 사고팔기 가장 좋은 시점

##### 연결 리스트

- [ ] 팰린드롬 연결 리스트
- [ ] 두 정렬 리스트의 병합
- [ ] 역순 연결 리스트
- [ ] 두 수의 덧셈
- [ ] 페어의 노드 스왑
- [ ] 홀짝 연결 리스트
- [ ] 역순 연결 리스트 II

##### 스택, 큐

- [ ] 유효한 괄호
- [ ] 중복 문자 제거
- [ ] 일일 온도
- [ ] 큐를 이용한 스택 구현
- [ ] 스택을 이용한 큐 구현
- [ ] 원형 큐 디자인

##### 데크, 우선순위 큐

- [ ] 원형 데크 디자인
- [ ] k개 정렬 리스트 병합



#### 문자열 조작

- [ ] 유효한 팰린드롬
- [ ] 문자열 뒤집기
- [ ] 로그 파일 재정렬
- [ ] 가장 흔한 단어
- [ ] 그룹 애너그램
- [ ] 가장 긴 팰린드롬 부분 문자열



### 프로그래머스 문제 도전

매주 한 문제씩 격파해 나가자([링크](https://programmers.co.kr/learn/challenges?tab=all_challenges))

#### 2018 카카오 블라인드 리크루트

- [x] 비밀지도
- [x] [다트 게임](https://programmers.co.kr/learn/courses/30/lessons/17682)
- [x] [캐시](https://programmers.co.kr/learn/courses/30/lessons/17680)
- [ ] [셔틀버스](https://programmers.co.kr/learn/courses/30/lessons/17678)
- [ ] 뉴스 클러스터링
- [ ] 프렌즈4블록
- [ ] 추석 트래픽
- [ ] n진수 게임
- [ ] 압축
- [ ] 파일명 정렬
- [ ] 방금그곡
- [ ] 자동완성

#### 2019 카카오 개발자 겨울 인턴십

- [x] [징검다리 건너기](https://programmers.co.kr/learn/courses/30/lessons/64062)
- [x] [호텔 방 배정](https://programmers.co.kr/learn/courses/30/lessons/64063)
- [ ] [불량 사용자](https://programmers.co.kr/learn/courses/30/lessons/64064)

