{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ce1dde1b",
   "metadata": {},
   "source": [
    "# 파일 입출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c80550e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 텍스트 파일 쓰기\n",
    "with open(\"abc/파일이름.txt\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(\"저장할 내용\")\n",
    "\n",
    "# 텍스트 파일 읽기\n",
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as f:\n",
    "    content = f.read()\n",
    "    print(\"읽은 내용:\", content)\n",
    "\n",
    "# 바이너리 파일 쓰기 (예: 이미지, 오디오 저장할 때)\n",
    "bytes_data = b'\\x48\\x69'  # 예시: 'Hi'\n",
    "with open(\"abc/파일이름.txt\", \"wb\") as f:\n",
    "    f.write(bytes_data)\n",
    "\n",
    "# 읽기 + 쓰기 모드\n",
    "with open(\"abc/파일이름.txt\", \"r+\", encoding=\"utf-8\") as f:\n",
    "    content = f.read()\n",
    "    f.write(\"\\n새로운 내용 추가됨\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "847592c8",
   "metadata": {},
   "source": [
    "# 파일 쓰기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29085a6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#쓰기 모드: \"a\" (append)\n",
    "\n",
    "with open(\"abc/파일이름.txt\", \"a\", encoding=\"utf-8\") as file:\n",
    "    file.write(\"추가된 내용입니다.\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c90cb000",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    text = input(\"파일에 저장할 내용을 입력하세요 (종료: exit): \")\n",
    "    if text == \"exit\":\n",
    "        break\n",
    "    with open(\"abc/파일이름.txt\", \"a\", encoding=\"utf-8\") as f:\n",
    "        f.write(text + \"\\n\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d534e18",
   "metadata": {},
   "source": [
    "# write()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e2b241d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# write()\n",
    "\n",
    "\n",
    "with open(\"abc/파일이름.txt\", \"w\", encoding=\"utf-8\") as file:\n",
    "    file.write(\"반복문을 사용하여 파일에 데이터를 저장합니다.\")\n",
    "\n",
    "# - 파일을 열고 내용을 저장한 후 자동으로 닫힌다\n",
    "# - open 함수에 with 문을 사용하면 파일 열고 닫기가 자동으로 처리 됨\n",
    "# - 반복문을 활용하면 여러 줄도 효율적으로 저장 가능"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa42774d",
   "metadata": {},
   "source": [
    "### 반복문을 활용한 파일 쓰기\n",
    "\n",
    "반복문을 활용하면 리스트나 다른 시퀀스 자료형의 데이터를 **한 줄씩 자동으로 파일에 저장**할 수 있다.\n",
    "\n",
    "이는 대량의 데이터를 다룰 때 매우 효율적이다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d883263",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 예제: 리스트의 데이터를 파일에 저장하기\n",
    "\n",
    "lines = [\n",
    "    \"Python 파일 입출력\\n\",\n",
    "    \"반복문을 사용하여 데이터를 저장합니다.\\n\",\n",
    "    \"데이터 처리가 편리합니다.\\n\"\n",
    "]\n",
    "\n",
    "with open(\"abc/파일이름.txt\", \"w\", encoding=\"utf-8\") as file:\n",
    "    for line in lines:\n",
    "        file.write(line)\n",
    "\n",
    "\n",
    "# - `lines`: 파일에 저장할 문자열이 담긴 리스트\n",
    "# - `for line in lines`: 각 줄을 반복하면서\n",
    "# - `file.write(line)`: 한 줄씩 파일에 저장함\n",
    "# - `\\n`: 줄바꿈 문자로, 줄 단위 저장을 가능하게 한다\n",
    "\n",
    "# 이 방식은 파일을 한 번만 열고 여러 줄을 순차적으로 저장하므로 **성능과 안정성 면에서 효율적**이다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afb43e0e",
   "metadata": {},
   "source": [
    "# writelines()\n",
    "\n",
    "writelines() 함수는 리스트나 반복 가능한 객체의 모든 요소를 파일에 한 번에 기록하는 메서드이다. \n",
    "\n",
    "각 요소는 자동으로 줄바꿈되지 않으므로, 필요한 경우 줄바꿈 문자를 직접 포함해야 한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90c05a1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "lines = [\"첫 번째 줄입니다.\\n\", \"두 번째 줄입니다.\\n\", \"세 번째 줄입니다.\\n\"]\n",
    "\n",
    "with open('abc/파일이름.txt', 'w') as f:\n",
    "    f.writelines(lines)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "366dcf9e",
   "metadata": {},
   "source": [
    "# 파일 읽기 \n",
    "### read vs readline vs readlines 비교\n",
    "\n",
    "| 함수명 | 설명 | 반환 형식 |\n",
    "| --- | --- | --- |\n",
    "| `read()` | 전체 내용을 한 문자열로 읽음 | 문자열(str) |\n",
    "| `readline()` | 한 줄만 읽음 | 문자열(str) |\n",
    "| `readlines()` | 전체 줄을 리스트로 반환 | 리스트(list) |"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a771a8e",
   "metadata": {},
   "source": [
    "## read()\n",
    "\n",
    "파일에 저장된 내용을 프로그램으로 불러오려면 `read()` 함수를 사용한다.\n",
    "\n",
    "전체 내용을 **문자열 형태로 한 번에 읽는다.**\n",
    "\n",
    "- `\"r\"` 모드는 읽기(read) 전용 모드이다\n",
    "- `read()`는 전체 파일 내용을 한 번에 가져온다\n",
    "- `with` 블록을 벗어나면 파일은 자동으로 닫힌다\n",
    "\n",
    "- 파일이 존재하지 않으면 오류가 발생한다 (`FileNotFoundError`)\n",
    "- 파일을 여러 번 읽으려면 포인터를 다시 처음으로 돌리거나 파일을 다시 열어야 한다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1028a7e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    content = file.read()\n",
    "    print(content)\n",
    "\n",
    "# 예제 실행 결과 (abc/파일이름.txt에 다음과 같은 내용이 있을 경우)\n",
    "\n",
    "#  Python 파일 입출력\n",
    "#  반복문을 사용하여 데이터를 저장합니다.\n",
    "# 데이터 처리가 편리합니다.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "358cf5ea",
   "metadata": {},
   "source": [
    "# readline()\n",
    "\n",
    "`readline()` 함수는 파일에서 **한 줄씩 순차적으로 읽을 수 있는 함수**이다.\n",
    "\n",
    "한 줄만 읽기 때문에 **반복문과 함께 사용**하면 매우 유용하다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e94893f7",
   "metadata": {},
   "source": [
    "- 첫 번째 줄만 읽어서 출력한다\n",
    "- 반복해서 `readline()`을 호출하면 다음 줄을 차례로 읽는다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2632772b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    line = file.readline()\n",
    "    print(line)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3beb6d6",
   "metadata": {},
   "source": [
    "- 반복문을 사용한 전체 줄 읽기\n",
    "\n",
    "```python\n",
    "with open(\"example.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    while True:\n",
    "        line = file.readline()\n",
    "        if not line:\n",
    "            break\n",
    "        print(line.strip())\n",
    "```\n",
    "  \n",
    "    - `while True`: 무한 반복 시작\n",
    "    - `readline()`: 한 줄씩 읽는다\n",
    "    - `if not line`: 읽은 내용이 없으면 반복 종료\n",
    "    - `strip()`: 줄바꿈 문자 제거\n",
    "    \n",
    "    ```\n",
    "    Python 파일 입출력\n",
    "    반복문을 사용하여 데이터를 저장합니다.\n",
    "    데이터 처리가 편리합니다.\n",
    "    ```\n",
    "    \n",
    "\n",
    "- 이 방식은 **줄 수가 정해지지 않은 텍스트 파일**을 처리할 때 유용하다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4761ef69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python 파일 입출력\n",
      "반복문을 사용하여 데이터를 저장합니다.\n",
      "데이터 처리가 편리합니다.\n"
     ]
    }
   ],
   "source": [
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    while True:\n",
    "        line = file.readline()\n",
    "        if not line:\n",
    "            break\n",
    "        print(line.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f917f039",
   "metadata": {},
   "source": [
    "## readlines()\n",
    "\n",
    "`readlines()` 함수는 파일 전체 내용을 **줄 단위로 나누어 리스트 형태로 읽는다.**\n",
    "\n",
    "각 줄이 문자열 원소가 되어 리스트에 저장된다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09dd4a3f",
   "metadata": {},
   "source": [
    "```python\n",
    "with open(\"example.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    lines = file.readlines()\n",
    "\n",
    "for line in lines:\n",
    "    print(line.strip())\n",
    "```\n",
    "\n",
    "- `readlines()`: 파일 전체 내용을 한 줄씩 리스트로 반환한다\n",
    "- `for line in lines`: 리스트의 각 줄을 반복해서 출력\n",
    "- `strip()`: 줄바꿈 문자 제거"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2fe45a1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python 파일 입출력\n",
      "반복문을 사용하여 데이터를 저장합니다.\n",
      "데이터 처리가 편리합니다.\n"
     ]
    }
   ],
   "source": [
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as file:\n",
    "    lines = file.readlines()\n",
    "\n",
    "for line in lines:\n",
    "    print(line.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ab2b64e",
   "metadata": {},
   "source": [
    "```python\n",
    "with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:\n",
    "    for line in f.readlines():\n",
    "        print(line.upper().strip())\n",
    "\n",
    "```\n",
    "\n",
    "- 전체 파일을 읽고, 각 줄을 대문자로 변환한 후 출력한다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b7857657",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PYTHON 파일 입출력\n",
      "반복문을 사용하여 데이터를 저장합니다.\n",
      "데이터 처리가 편리합니다.\n"
     ]
    }
   ],
   "source": [
    "with open(\"abc/파일이름.txt\", \"r\", encoding=\"utf-8\") as f:\n",
    "    for line in f.readlines():\n",
    "        print(line.upper().strip())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b21f8b2",
   "metadata": {},
   "source": [
    "# 피클, 직렬화 / 역직렬화\n",
    "\n",
    "직렬화(Serialization)는 파이썬의 객체나 데이터 구조를 파일이나 네트워크로 전송할 수 있는 형식으로 변환하는 과정이다.\n",
    "반대로 역직렬화(Deserialization)는 파일이나 네트워크에서 받은 데이터를 다시 파이썬 객체로 변환하는 과정을 말한다.\n",
    "\n",
    "Python에서는 주로 `pickle` 모듈을 사용하여 직렬화와 역직렬화를 수행한다.\n",
    "\n",
    "직렬화와 역직렬화의 주요 사용 사례는 다음과 같다:\n",
    "\n",
    "- 객체의 영속성(persistence) 유지\n",
    "- 네트워크를 통한 데이터 전송\n",
    "- 복잡한 데이터 구조의 저장과 복원"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7dca79a9",
   "metadata": {},
   "source": [
    "### 다음은 pickle 모듈을 사용한 직렬화/역직렬화의 기본 예제"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "319a1429",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': '홍길동', 'age': 30, 'scores': [90, 85, 88]}\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "\n",
    "# 직렬화할 데이터 딕셔너리\n",
    "data = {\n",
    "    'name': '홍길동',\n",
    "    'age': 30,\n",
    "    'scores': [90, 85, 88]\n",
    "}\n",
    "\n",
    "# 직렬화하여 파일에 저장\n",
    "with open('abc\\파일이름.pickle', 'wb') as f:\n",
    "    pickle.dump(data, f)\n",
    "\n",
    "# 파일에서 역직렬화하여 읽기\n",
    "with open('abc\\파일이름.pickle', 'rb') as f:\n",
    "    loaded_data = pickle.load(f)\n",
    "\n",
    "print(loaded_data)  # 원본 데이터가 그대로 복원됨"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42c7a32f",
   "metadata": {},
   "source": [
    "위 예제에서 dictionary 객체를 pickle을 사용하여 파일에 저장하고, 다시 읽어오는 과정을 보여준다. 직렬화된 데이터는 바이너리 형태로 저장되므로, 파일을 열 때 'wb'(쓰기-바이너리) 또는 'rb'(읽기-바이너리) 모드를 사용해야 한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "efe33c69",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "cbda7f8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 직렬화하여 파일에 저장\n",
    "with open('abc\\파일이름.json', 'w') as f:\n",
    "    json.dump(data, f, ensure_ascii=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b10f24a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': '홍길동', 'age': 30, 'scores': [90, 85, 88]}\n"
     ]
    }
   ],
   "source": [
    "with open('abc\\파일이름.json', 'r') as f:\n",
    "    loaded_txt = json.load(f)\n",
    "\n",
    "print(loaded_txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "3e97e093",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['name', 'age'], ['bob', 20], ['alice', 15]]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import csv\n",
    "data = [['name','age'], ['bob', 20], ['alice', 15]]\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "632ff157",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 직렬화하여 파일에 저장\n",
    "with open('abc/파일이름.csv', 'w') as f:\n",
    "    wrt = csv.writer(f)\n",
    "    wrt.writerows(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "ccf098a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "df.to_csv('abc/파일이름_df.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "541ec1da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>name</td>\n",
       "      <td>age</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>bob</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>alice</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0      0    1\n",
       "0           0   name  age\n",
       "1           1    bob   20\n",
       "2           2  alice   15"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_csv('abc/파일이름_df.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b777551",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
