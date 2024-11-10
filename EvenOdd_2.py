test_case = int(input())

for i in range(test_case):
    number = input()
    str_input = int(number[-1])

    if str_input % 2 == 0:
        print('even')
    else:
        print('odd')
