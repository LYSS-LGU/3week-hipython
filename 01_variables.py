# %% [markdown]
# # 들어가기 : 주석

# %%


# %%
# 이코드는 실행되지 않습니다.
# age = input()
#age

# %%
# 이코드는 실행되지 않습니다.
# age = input()
#age

# %%
def calculate_sum(a, b) :
    result = a + b
    
    return result

print( calculate_sum(3, 4) )

# %%

# %% [markdown]
# # 표준 입력과 표준 출력

# %%
12345
10
# ipython 라이브러리의 기본 기능
# print(12345) 표준출력 기능을 내장하고 있다.

# %%
print(12345)
10

# %%
'12345'  # 문자열 str

# %%
type('12345')

# %%
type(12345)

# %%
12345+10

# %%
#'12345'+10  #typeerror

# %%
"12345"*3

# %%
name = input('당신의 이름을 입력하세요')

# %%
age = input('당신의 나이를 입력하세요')
age

# %%

# %%
age

# %%
#입력받은 name을 출력
name

# %%
print(age, name)

# %%
print( '나는 '+name+'이고 나이는 '+age+'입니다.')

# %%
age = int(age)

# %%
age + 10

# %% [markdown]
# # 연습

# %%
# 자기 이름으로 삼행시 짓기

print('바: 바밤바는 ')
print('밤: 밤이 들어 있는 ')
print('바: 바이다')

# %%
line1 = input('바: ')
line2 = input('밤: ')
line3 = input('바: ')

# %%
print(line1, line2, line3, sep='\n ')  #줄바꿈 기호

# %% [markdown]
# 문자열의 시작이 \ 역슬래시 -> 이스케이스 문자, 특수 문자
# \n
# \t
# \\

# %%
삼행시 = line1 +'\n'+ line2 +'\n'+ line3
print(삼행시)
삼행시

# %% [markdown]
# # 변수

# %% [markdown]
# 변수는 type safe : 변수를 선언할 때 타입(유형)을 지정하지 않아도 되는 특성  
# 변수명 = 값
# 

# %% [markdown]
# ## 변수의 명명규칙
# 1. 문자, 숫자, 밑줄(_ 언더바)을 가지고 만든다
# 2. 숫자로 시작하면 X
# 3. 대소문자를 구분
# 4. 예약어, 특수기호, 공백 X
#    

# %%
false dd = 10

# %%
x = 10
y = 'hello'
z = 3.141592
x,y,z

# %%
print(type(x), type(y), type(z))

# %%
a,b,c = 10,20,30
a,b,c

# %%
a=10; b=20; c=30

# %%
a = b = c = 40
a,b,c

# %%
d = True #bool형
e = None #type이 없음 NoneType 
d,e

# %%
a = 10
b = a
print(a,b)
id(a), id(b)

# %%
# 의미 부여 하기 어려운 변수명 > 수식이 아닌 경우는 사용하지 않음
x = 100
y = 100

# 의미 있는 변수명
age = 20
name = '김영리'
user_name = 'Alic'
admin_name = 'Bob'

#대문자 Upper-case 상수에 사용
PI = 3.141592
MAX_CONNECTIONS = 10 #최대 연결 수
MIN_VALUE = 0 #최소값



# %% [markdown]
# ## NAME_SPACE
# 
# 변수가 최초로 정의된 영역에 따라 유효범위가 결정됩니다.   
# 
# - 지역변수 : 함수 영역 내에서 선언한 변수
# - 전역변수 : 함수 영역 밖에서 선언한 변수, global 키워드
# - 정적변수 : 클래스에서 사용하는 변수

# %%
# 지역변수 local variable
def local_example():
    local_var = 100
    print('여기는 함수의 영역입니다. ', local_var)

#local_var #NameError: name 'local_var' is not defined
local_example()

# %%
# 전역 변수 global variable
global_var = '나는 전역이다'
print(global_var)

def global_example():
    local_var = 100
    print('여기는 함수의 영역입니다. ', local_var, global_var)

global_example()


# %%
# 전역 변수 global variable
var_test = '나는 전역이다'
print(var_test)

def global_example():
    global var_test
    var_test = 100
    print('여기는 함수의 영역입니다. ', var_test)

global_example()
print(var_test)

# %%
# 변수 영역 연습

counter = 0 #global

def increment_counter():
    #counter = counter + 1
    global counter 
    counter += 1
    print('카운터 : ', counter)

increment_counter()
increment_counter()
increment_counter()

# %% [markdown]
# # 교재 변수 연습 

# %%
a=123
a=-178
a=0
a

# %%


# %% [markdown]
# # 자료형 
# 
# - 기본 자료형 : 숫자형, 문자열형 str, 부울형
# - 복합 자료형 : 리스트, 셋, 튜플, 딕셔너리
#   

# %% [markdown]
# | type | 설명 | 예 |
# |--------|--------|--------| 
# | 정수형 (int) | 정수를 저장하는 자료형 | 1, -5, 100 |
# |실수형 (float)|소수점이 있는 숫자를 저장하는 자료형 | 3.14, -0.001, 2.0|
# |문자열 (str)|텍스트를 저장하는 자료형|"Hello", '파이썬'|
# |논리형 (bool)|참/거짓 값을 저장하는 자료형|True, False|

# %% [markdown]
# - 수정 불가능한 데이터 타입 : 수치형, 부울형, 문자열, 튜플
# - 수정 가능한 데이터 타입 : 리스트, 딕셔너리, 셋

# %%
# 수치형 - int
20, type(20)

# %%
age = 20
type(age)

# %% [markdown]
# 1. 진법 : 10진수, 2진수, 8진수, 16진수
# 2. 입력하는 방법은 다르지만, print() 결과는 동일하다.

# %%
a = 10
b = 0b0101 #2진수 - 0/1 로 표현하는 방법 -> 0101 = 2^3 + 2^2 + 2^1 + 2^0 = 
a,b

# %%
c = 0o10 # 0o 8진수 , 10 -> 8^1 + 8^0 = 8*1 + 0*0 = 8
c

# %%
d = 0b1000
d

# %%
e = 0x16d #> 1*16^2 + 6 * 16^1 + d(13)*16^0(1) = 256 + 96 + 16
16**2, 16*6, e

# %%
# float
b = 3.14
b, type(b)

# %% [markdown]
# 지수의 표기
# 
# 숫자 e2 -> 10^2의 곱 = 10**2
# 숫자 e-2 -> 10^-2의 곱 = 10**-2

# %%
fa = 10e2
fa, 10* 10**2

# %%
fb = 10e-2
fb, 10* 10**-2

# %%
fc = 3.1415e9
fc, 3.1415 * 10**9

# %% [markdown]
# BOOLEAN값 - True, False   
# 논리연산, 비교연산

# %%
ba = True
bb = true
type(ba), type(bb)

# %%
ba == 0

# %%
ba == 'True'

# %%
#논리 연산자 - and or not

bc = 1
ba and bc

# %%
# 사칙연산 + - * / // %
a=2
b=3

# %%
a+b
a-b
a*b
a/b, a//b , a%b #몫, 나머지

# %%
#비교 연산자
1+2 == 3
1+2 != 3
1+3 > 3
1+3 <= 4

# %%
# 비교연산자와 논리연산자의 결합
10%2 == 0 and 12%3 == 0

# %%
a = '1234'
b = '5678'
a,b, id(a), id(b)

# %%
id(a) == id(b)

# %%
# 대입연산자
a = 10
b = a+2
a,b

# %%
a = 20
a += 1  # a = a + 1
a

# %%
a -= 1 # a = a - 1  , 21 - 1 = 20
a

# %%
a = 3
b=2
a += 2 + b
a

# %% [markdown]
# # 문자열 str
# ' ' , " " , """ """, ''' '''  docstring
# 
# 인코딩 > 코드 > 숫자값 정해져 있어요. "코드표"

# %%
유니코드 문자 표준
영어는 ascii -> 유니코드
한국어도 유니코드

유니코드가 글자의 크기에 따라 utf-8 (디폴트값), [ utf-16 utf-32 ] 지정 필요
파이썬의 문자열 str -> unicode 기반이다.

euc-Kr  : 예전에 우리나라에서 쓰던 한글 코드
cp949   : MS 윈도우즈의 한글코드 


# %%
#인코딩
enc_text = text.encode('utf-8')
enc_text


# %%
#디코딩
dec_text = enc_text.decode('utf-8')
dec_text

# %%
#인코딩
enc_text = text.encode('euc-Kr')
enc_text

# %%
#디코딩
dec_text = enc_text.decode('euc-Kr')
dec_text

# %%
#인코딩
enc_text = text.encode('cp949')
enc_text

# %%
#디코딩
dec_text = enc_text.decode('cp949')
dec_text

# %%
파이썬의 인덱스는 0부터시작
음수의 인덱스 : 뒤에서부터 -1

# %%
text = '파이썬'
print(text)
print( ord('파'))

# %%
a = 'hello'
b = 'python'
a + b  #+ 는 문자열끼리 연산

# %%
c = '*'
c*10 #*는 숫자와 연산

# %%
d = "Kim's family"
d

# %%
e = '1'
e == '1'

# %%
# 문자열은 리스트, 열거형
a = '20010331Rabcd' #13개의 글자의 목록
a[0] #숫자 자리수 > 인덱스

# %%
a[3]  #인덱싱

# %%
a[0:4] #영역을 지정할 때 : (콜론), 슬라이싱 slice
a[:4]

# %%
#Rab  a = '20010331Rabcd'
a[8:11]


# %%
a[9:] #index = 0에서 시작한다

# %%
s = 'abc'
a = s
a is s

# %%
b = s[:]
a is b

# %%
s1 = '1'*1000
b = s1[:]
s1 == b


# %%
#구성원 연산자
'a' in s

# %%
```docstring
start
end
```


# %%
doc_string = '''docstring \n
start \n
end \n
'''
print(doc_string)
doc_string

# %%
# str의 함수
dir()

# %%
dir(text)

# %%
text._add_("4")

# %%
text.count('t')

# %%
letters = 'python'
print(letters[0], letters[2])

# %%
license_plate = "24가 2210"
print(license_plate[-4:])

# %%
string = "홀짝홀짝홀짝"
print(string[::2])

# %%
string = "PYTHON"
print(string[::-1])

# %%
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

# %%
raw-string : 모두 다 문자열이다 r`str?\`
f-string : 형식코드가 내포된 문자열 f'str{text}'

# %%
str_1 = '12\\4'
str_1

# %%
raw_str = r'12\4'
raw_str

# %%
raw_str_1 = r'Hello\nWorld'
print(raw_str_1)

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %% [markdown]
# 


