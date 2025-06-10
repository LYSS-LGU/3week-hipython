import datetime
import re # 정규 표현식을 사용하기 위해 import

# 전역 변수 선언 (공통 사용)
store_name = '또!젤라또'

menu_list = [
    {'name':'또젤라또','count':'1가지맛', 'price':3000},
    {'name':'또또젤라또','count':'2가지맛', 'price':5000},
    {'name':'또또또젤라또','count':'3가지맛', 'price':7000}
]

flavor_list = [
    {'flavor':'달콤초코봄바람'},
    {'flavor':'새콤달콤딸기정원'},
    {'flavor':'요거트빛파도'},
    {'flavor':'말차소풍'},
    {'flavor':'체리팝송'},
    {'flavor':'포도에몽'},
    {'flavor':'바닐라하모니'},
    {'flavor':'쿠키크러쉬'},
    {'flavor':'소금바다우유'},
    {'flavor':'블루베리썸머'},
    {'flavor':'스윗피치'},
    {'flavor':'레몬샤워'},
]

point_list = []
all_orders = []

# ================= 함수 정의 =================

def select_menu():
    """
    메뉴를 선택하는 함수.
    선택된 메뉴 인덱스를 반환.
    사용자 입력의 유효성을 검증하여 올바른 메뉴 번호를 받을 때까지 반복.
    """
    print("="*45)
    print(f'{store_name:^40}')
    print("="*45)
    print("어서오세요 아이스크림을 또 주는 또젤라또입니다\n")

    for i, menu in enumerate(menu_list):
        print(f'{i + 1}. {menu["name"]:<6} {menu["count"]:>12} {menu["price"]:>10,}원')
    print("="*45)

    while True: # 유효한 입력이 들어올 때까지 반복
        order_input = input('주문할 메뉴 번호를 입력해주세요: ').strip() 
        
        # 입력값이 숫자인지 먼저 확인
        if not order_input.isdigit():
            print("앗! 메뉴 번호는 숫자로 입력해주셔야 해요. 다시 시도해볼까요? 😉\n")
            continue # 다시 입력받도록 반복문 처음으로 돌아감

        order_num = int(order_input)
        
        # 입력된 숫자가 메뉴 범위 내에 있는지 확인
        if 1 <= order_num <= len(menu_list):
            return order_num - 1 # 올바른 입력이면 인덱스 반환 (0부터 시작)
        else:
            print(f"죄송해요! {len(menu_list)}번까지의 메뉴 중에서 선택해주세요. 다시 한번 부탁드려요! ✨\n")

def select_flavors(selected_menu):
    """
    맛 선택 함수
    선택한 메뉴에 따라 선택해야 하는 맛의 개수만큼 입력을 받음.
    입력 유효성을 검증하고, 중복 선택을 방지하며, 유효한 맛 리스트를 반환.

    Args:
        selected_menu (dict): 사용자가 선택한 메뉴 정보 (name, count, price 포함)

    Returns:
        list[str] | None: 선택된 맛 리스트 (정상 선택), 0 입력 시 None 반환
    """
    
    try:
        # 'count' 문자열에서 숫자만 추출 (예: '1가지맛' -> 1)
        # re.findall은 리스트를 반환하므로 첫 번째 요소를 가져옴
        flavor_count_str = re.findall(r'\d+', selected_menu['count'])[0]
        flavor_count = int(flavor_count_str)
    except (IndexError, ValueError): # re.findall이 빈 리스트를 반환하거나 int 변환 실패 시
        print("맛 수 정보를 확인할 수 없습니다. 개발자에게 문의해주세요! 🛠️")
        return []

    print(f"\n'{selected_menu['name']}' 선택 — {flavor_count}가지 맛을 골라주세요!")

    cols_per_row = 3 # 한 줄에 출력할 맛의 개수
    for i, fla in enumerate(flavor_list):
        print(f"{i+1}. {fla['flavor']:<10}", end='')
        if (i + 1) % cols_per_row == 0 or i == len(flavor_list) - 1:
            print() # 3개마다 줄바꿈, 마지막 맛 출력 후 줄바꿈

    while True: # 유효한 맛 개수가 선택될 때까지 반복
        flavor_input = input(f"\n원하는 맛 번호들을 쉼표(,)로 구분하여 {flavor_count}가지 입력하세요 (예: 1, 3, 5) / 0 입력시 메뉴 선택으로 돌아가기: ").strip()

        if flavor_input == '0':
            print("맛 선택을 취소하고 메뉴로 돌아갑니다. 다시 신중하게 골라볼까요? 😌\n")
            return None  # 맛 선택 취소

        # 쉼표로 분리하고 각 부분을 숫자로 변환 준비
        parts = flavor_input.split(',')
        flavor_nums_str = [p.strip() for p in parts] # 공백 제거된 문자열 리스트

        selected_flavor_indices = []
        is_valid_input = True # 입력 유효성 플래그

        for part in flavor_nums_str:
            if not part.isdigit(): # 각 부분이 숫자인지 확인
                print("맛 번호는 숫자로만 입력해주세요! 😅 다시 한번 확인해볼까요?\n")
                is_valid_input = False
                break # 유효하지 않은 입력 발견 시 반복 중단
            
            num = int(part) - 1 # 인덱스로 변환 (0부터 시작)
            if not (0 <= num < len(flavor_list)): # 유효한 맛 번호 범위인지 확인
                print(f"죄송해요! 1부터 {len(flavor_list)}까지의 맛 중에서 선택해주세요. 없는 맛 번호가 있어요! 🥺\n")
                is_valid_input = False
                break # 유효하지 않은 입력 발견 시 반복 중단
            selected_flavor_indices.append(num)
        
        if not is_valid_input: # 유효하지 않은 입력이 있었다면 다시 입력받기
            continue

        # 선택된 맛의 개수가 메뉴에서 요구하는 개수와 맞는지 확인
        if len(selected_flavor_indices) != flavor_count:
            print(f"딱! {flavor_count}가지 맛을 선택해주셔야 해요. 지금은 {len(selected_flavor_indices)}가지 맛이 선택되었네요. 다시 한번 부탁드려요! 🙏\n")
            continue
        
        # 중복된 맛 선택 방지 (선택 사항: set을 이용해 중복 제거 후 개수 비교)
        if len(set(selected_flavor_indices)) != flavor_count:
            print("똑같은 맛을 두 번 고르셨네요! 🍦 서로 다른 맛으로 골라주시면 감사하겠습니다! 😊\n")
            continue

        # 모든 유효성 검증을 통과했다면 선택된 맛 리스트 반환
        selected_flavors = [flavor_list[i]['flavor'] for i in selected_flavor_indices]
        return selected_flavors


def cart(orders, selected_menu, selected_flavors):
    """
    주문 확인 및 장바구니 추가 함수
    현재 선택한 메뉴와 맛을 출력하고 사용자에게 장바구니 추가 여부를 확인.
    올바른 'Y/N' 입력을 받을 때까지 반복.

    Args:
        orders (list): 현재 주문 목록 리스트 (dict 요소)
        selected_menu (dict): 선택된 메뉴 정보
        selected_flavors (list): 선택된 맛 리스트

    Returns:
        bool: 장바구니에 추가(True), 취소(False)
    """
    print("\n선택한 주문:")
    print(f"메뉴: {selected_menu['name']}") # 선택한 메뉴(사이즈) 
    for idx, name in enumerate(selected_flavors):
        print(f" - 맛 {idx+1}: {name}") #맛 순번과 맛이름
    print(f"가격: {selected_menu['price']:,}원") #총 가격

    while True: # 'Y' 또는 'N'이 입력될 때까지 반복
        confirm = input("\n이 주문을 장바구니에 추가할까요? (Y: 추가 / N: 취소): ").strip().lower()
        if confirm == 'y':               
            orders.append({
                'menu_name': selected_menu['name'],
                'flavor_names': selected_flavors,
                'price': selected_menu['price']
            })
            print("주문이 장바구니에 추가되었습니다! 장바구니가 든든해졌어요! 🎉\n")
            return True
        elif confirm == 'n':
            print("주문이 취소되었습니다. 다시 골라볼까요? 괜찮아요! 😄\n")
            return False
        else:
            print('앗! "Y" 또는 "N"으로만 입력해주셔야 해요. 다시 시도해볼까요? 😊')


def extra_order():
    """
    추가 주문 여부 확인 함수.
    올바른 'Y/N' 입력을 받을 때까지 반복.

    Returns:
        bool: 추가 주문할 경우 True, 아니면 False
    """    
    while True: # 'Y' 또는 'N'이 입력될 때까지 반복
        another = input("추가 주문하시겠습니까? (Y/N): ").strip().lower()
        if another == 'y':
            return True  # 다시 메뉴 선택으로
        elif another == 'n':
            return False  # 주문 확인 단계로
        else:
            print('앗! "Y" 또는 "N"으로만 입력해주셔야 해요. 다시 시도해볼까요? 😊')

def show_orders(orders):
    """
    현재 주문 내역 출력 함수.
    주문이 없을 경우 메시지를 출력.

    Args:
        orders (list): 주문 내역 리스트 (dict 요소)
    """
    
    if not orders:
        print("현재 주문이 없습니다. 텅 비어 있네요! 😥")
    else:
        print("\n✨ 현재 주문 내역:")
        for i, order in enumerate(orders):
            print(f"{i+1}. {order['menu_name']} — {order['price']:,}원")
            for idx, name in enumerate(order['flavor_names']):
                print(f"    - 맛 {idx+1}: {name}")


def canceled(orders):
    """
    주문 취소 처리 함수
    주문 내역을 출력하고 사용자가 취소를 원하는 주문을 삭제할 수 있게 함.
    유효한 취소 입력 (번호, 0, Y/N)을 받을 때까지 반복.

    Args:
        orders (list): 현재 주문 내역 리스트

    Returns:
        bool: 남은 주문이 있으면 False (결제 진행) 없으면 True (처음으로 돌아감)
    """
    while True:
        if not orders:
            print("현재 주문이 없습니다. 텅 비어 있네요! �")
            return True # 주문이 없으면 처음으로 돌아감
            
        cancel_q = input("\n주문 내역 중 취소할 주문이 있습니까? (Y/N): ").strip().lower()
        if cancel_q == 'n':
            print("주문 취소를 마치고 결제를 진행합니다! 💸\n")
            return False # 취소 안 하고 결제 진행
        elif cancel_q == 'y':
            while True: # 유효한 취소 번호가 들어올 때까지 반복
                show_orders(orders) # 현재 주문 내역을 다시 보여줌
                if not orders: # 주문이 모두 취소되어 더 이상 취소할 주문이 없을 경우
                    print("더 이상 취소할 주문이 없습니다. 결제를 진행합니다.\n")
                    return False # 결제 진행
                    
                del_input = input("취소할 주문 번호를 입력하세요 (0 입력시 결제창으로): ").strip()
                if del_input == '0':
                    print("주문 취소를 마치고 결제를 진행합니다! 💸\n")
                    return False # 결제 진행
                
                if not del_input.isdigit():
                    print("주문 번호는 숫자로만 입력해주세요! 다시 한번 확인해볼까요? 🤔\n")
                    continue # 다시 입력받도록 반복문 처음으로 돌아감

                del_index = int(del_input) - 1
                if 0 <= del_index < len(orders):
                    removed = orders.pop(del_index)
                    print(f"'{removed['menu_name']}' 주문이 시원하게 삭제되었습니다! 💨")
                    # 취소 후 다시 취소할지 물어보기 위해 바깥 while True로 돌아감 (cancel_q 질문)
                    break # 내부 루프 탈출, 바깥 루프 (cancel_q)로 돌아가 다시 Y/N 질문
                else:
                    print(f"죄송해요! 1부터 {len(orders)}까지의 주문 번호 중에서 선택해주세요. 잘못된 번호예요! 🧐\n")
        else:
            print('앗! "Y" 또는 "N"으로만 입력해주셔야 해요. 다시 시도해볼까요? 😊')


def check_out(orders):
    """
    최종 결제 금액 계산 함수.
    주문 내역과 총 결제 금액을 출력.

    Args:
        orders (list): 현재 주문 내역 리스트

    Returns:
        int: 총 결제 금액
    """
    print("\n💳 최종 주문 내역:")
    if not orders: # 결제 단계에서 주문이 비어있을 경우
        print("결제할 주문이 없습니다. 😥")
        return 0

    for i, order in enumerate(orders):
        print(f"{i+1}. {order['menu_name']} — {order['price']:,}원")
        for idx, name in enumerate(order['flavor_names']):
            print(f"    - 맛 {idx+1}: {name}")
    
    total_price = sum(order['price'] for order in orders)
    print('\n' + '='*45)
    print(f"💰 총 결제 금액: {total_price:,}원")
    return total_price


def member_ship(point_list, total_price):
    """
    포인트 적립 처리 함수
    전화번호로 적립 또는 신규 등록.
    올바른 전화번호 (숫자, 길이)와 'Y/N' 입력을 받을 때까지 반복.

    Args:
        point_list (list): 포인트 정보 저장 리스트
        total_price (int): 총 결제 금액

    Returns:
        str: 전화번호 (회원), 또는 "고객"
    """
    while True: # 포인트 적립 여부 'Y/N' 입력 루프
        point_q = input('포인트 적립하시겠습니까? (Y/N): ').strip().lower()
        if point_q == 'y':
            while True: # 전화번호 입력 및 유효성 검증 루프
                # 사용자에게 전화번호 입력 형식 안내
                membership = input("전화번호 11자리를 입력해주세요 (예: 01012345678): ").strip()
                
                if not membership.isdigit(): # 전화번호가 숫자로만 구성되었는지 확인
                    print("전화번호는 숫자로만 입력해주셔야 해요! 🔢 다시 한번 확인해볼까요?\n")
                    continue
                
                if len(membership) != 11: # 전화번호 자릿수 검증 (예: 11자리)
                    print("전화번호 11자리를 정확히 입력해주세요! 📱 다시 시도해볼까요?\n")
                    continue
                
                break # 유효한 전화번호 입력 시 내부 루프 탈출

            saved_point = total_price // 100 # 총 결제 금액의 1%를 포인트로 적립
            idx = -1 # 기존 회원 인덱스 초기화
            
            # point_list에서 기존 회원 찾기
            for i, user in enumerate(point_list):
                if user['membership_nb'] == membership:
                    idx = i
                    break
                    
            if idx != -1: # 기존 회원일 경우
                point_list[idx]['membership_point'] += saved_point # 기존 포인트에 합산
                total_point = point_list[idx]['membership_point']
                print(f"기존 회원({membership})님! {saved_point}포인트 적립 완료! 현재 총 {total_point}포인트가 있어요! 🌟")
            else: # 신규 회원일 경우
                point_list.append({'membership_nb': membership, 'membership_point': saved_point}) # 새 회원 정보 추가
                total_point = saved_point
                print(f"새로운 회원({membership})님, 환영합니다! 🎉 {saved_point}포인트가 적립되었어요! 총 {total_point}포인트!")
                
            return membership  # 적립된 전화번호 반환
            
        elif point_q == 'n': # 포인트 적립을 원하지 않을 경우
            print("포인트 적립 없이 진행됩니다. 다음에 또 이용해주세요! 😊")
            return "고객" # "고객" 문자열 반환
        else: # 'Y' 또는 'N' 외의 입력일 경우
            print('앗! "Y" 또는 "N"으로만 입력해주셔야 해요. 다시 시도해볼까요? 😊')

# ================= 메인 루프 =================
while True: # 전체 주문 시스템 반복 (새로운 손님 또는 초기화)
    orders = [] # 각 손님의 주문 목록 초기화

    while True: # 개별 손님의 메뉴 선택 및 장바구니 담기 루프
        order_num = select_menu() # 메뉴 선택 함수 호출
        if order_num is None: # 잘못된 메뉴 입력 시 다시 메뉴 선택으로
            continue
        selected_menu = menu_list[order_num] # 선택된 메뉴 정보 가져오기

        selected_flavors = select_flavors(selected_menu) # 맛 선택 함수 호출
        if selected_flavors is None: # 맛 선택을 취소했을 경우 다시 메뉴 선택으로
            continue
        elif not selected_flavors: # 맛 선택 시 유효성 검증 실패했을 경우 다시 메뉴 선택으로
            continue

        # 선택된 메뉴와 맛을 장바구니에 추가할지 확인
        if not cart(orders, selected_menu, selected_flavors):
            continue # 장바구니 추가 취소 시 다시 메뉴 선택으로

        # 추가 주문 여부 확인
        if not extra_order():
            break  # 추가 주문을 원하지 않으면 메뉴 선택 루프 종료

    # 결제 전 주문 취소 여부 확인
    if canceled(orders):
        continue  # 모든 주문이 취소된 경우, 처음부터 다시 시작 (새로운 손님)

    total_price = check_out(orders) # 최종 결제 금액 계산
    if total_price == 0: # 모든 주문이 취소되어 결제 금액이 0인 경우
        print("남은 주문이 없습니다. 처음으로 돌아갑니다.\n")
        continue # 처음부터 다시 시작

    name = member_ship(point_list, total_price) # 멤버십 포인트 적립

    # 주문 시간 기록 및 전체 주문 내역에 추가
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    all_orders.append({
        'timestamp': now,
        'orders': orders.copy(), # 현재 주문 목록을 복사하여 저장 (orders가 나중에 초기화되므로)
        'total_price': total_price
    })

    print(f"\n{name}님, 주문 감사합니다! 또 오세요.🍦")
    print("=" * 45)

