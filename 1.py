user_input = int(input("정수 입력:"))
for i in range(1, user_input + 1):
    print("*" * i)
for i in range(user_input - 1, 0, -1):
    print("*" * i, "\t")