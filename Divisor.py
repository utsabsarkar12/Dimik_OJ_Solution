testCase = int(input())

for i in range(1, testCase + 1):
    number = int(input())
    print(f'Case {i}:', end=' ')

    for j in range(1, number + 1):
        if number % j == 0:
            print(j, end=' ')

    print()