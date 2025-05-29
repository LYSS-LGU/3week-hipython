# 3week-함수 & 메서드

> 참고자료 (기본자료형, 복합자료형)

| 함수              | 설명                             | 예시                                  |
| ----------------- | -------------------------------- | ------------------------------------- |
| lower()           | 모두 소문자로 변환               | "Python".lower() → "python"           |
| upper()           | 모두 대문자로 변환               | "python".upper() → "PYTHON"           |
| capitalize()      | 첫 글자만 대문자                 | "hello".capitalize() → "Hello"        |
| title()           | 각 단어의 첫 글자 대문자         | "hello world".title() → "Hello World" |
| strip()           | 앞뒤 공백 제거                   | " hello ".strip() → "hello"           |
| lstrip()          | 왼쪽 공백 제거                   | " hello".lstrip()                     |
| rstrip()          | 오른쪽 공백 제거                 | "hello ".rstrip()                     |
| replace(old, new) | 문자열 바꾸기                    | "hello".replace("l", "x") → "hexxo"   |
| split()           | 문자열 나누기 (기본: 공백)       | "a b c".split() → ['a', 'b', 'c']     |
| join(list)        | 리스트를 문자열로 결합           | " ".join(['a', 'b']) → "a b"          |
| find(sub)         | 처음 등장하는 위치 (없으면 -1)   | "apple".find("p") → 1                 |
| index(sub)        | 처음 등장하는 위치 (없으면 오류) | "apple".index("p") → 1                |
| count(sub)        | 부분 문자열 개수                 | "banana".count("a") → 3               |
| startswith(sub)   | 해당 문자열로 시작?              | "python".startswith("py") → True      |
| endswith(sub)     | 해당 문자열로 끝남?              | "python".endswith("on") → True        |
| isalnum()         | 영문자+숫자인가?                 | "abc123".isalnum() → True             |
| isalpha()         | 영문자만인가?                    | "abc".isalpha() → True                |
| isdigit()         | 숫자만인가?                      | "123".isdigit() → True                |
| isspace()         | 공백문자만 있는가?               | " \t\n".isspace() → True              |

---

| 메서드             | 사용 예시              | 설명                      |
| ------------------ | ---------------------- | ------------------------- |
| append(x)          | lst.append(4)          | 맨 뒤에 x 추가            |
| insert(i, x)       | lst.insert(1, "a")     | i 위치에 x 삽입           |
| extend(iter)       | lst.extend([4, 5])     | 리스트에 여러 값 추가     |
| remove(x)          | lst.remove("a")        | x와 일치하는 첫 항목 삭제 |
| pop()              | lst.pop()              | 마지막 항목 제거하고 반환 |
| pop(i)             | lst.pop(0)             | i번째 항목 제거하고 반환  |
| clear()            | lst.clear()            | 리스트 전체 비우기        |
| index(x)           | lst.index("a")         | x의 위치(인덱스) 반환     |
| count(x)           | lst.count("a")         | x의 개수 세기             |
| sort()             | lst.sort()             | 오름차순 정렬 (원본 변경) |
| sort(reverse=True) | lst.sort(reverse=True) | 내림차순 정렬             |
| reverse()          | lst.reverse()          | 항목 순서 뒤집기          |
| copy()             | lst2 = lst.copy()      | 리스트 복사               |
