
def divide(x,y):
    return x/y

def multiply(x, y):
    return x * y

def add(x,y):
    return x+y

<<<<<<< HEAD
def subtract(x, y):
    return x - y


#여기 위에다가 함수 추가하세요
=======

#여기 위에다가 함수 추가하세요


num1 = float(input("첫 번째 숫자를 입력하세요: "))

num2 = float(input("두 번째 숫자를 입력하세요: "))

result = num1 - num2
print("두 숫자의 차는:", result)
>>>>>>> bfaaf7165ef186453bc6c19952041c6500e6b966

def calculator():
    print("간단한 계산기")
    print("사칙연산을 선택하세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")

    choice = input("선택(1/2/3/4): ")

    num1 = float(input("첫 번째 숫자 입력: "))
    num2 = float(input("두 번째 숫자 입력: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("잘못된 입력입니다.")

calculator()

