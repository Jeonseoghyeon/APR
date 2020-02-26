import sys
sys.stdin = open("UN_input.txt","r")

numbers = int(input())
for number in range(numbers):
    n = int(input())
    n_n = [list(map(int, input().split())) for i in range(n)]
    row = []
    count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if n_n[j][i] != 0:
                count += 1
                if j == n-1:
                    row.append(count)
            else:
                if count != 0:
                    row.append(count)
                    count = 0
    row_dict = {}
    for i in row:
        if i not in row_dict:
            row_dict[i] = 1
        else:
            row_dict[i] = row_dict[i] + 1
    result = []
    result_size = []
    for row, column in row_dict.items():
        size = int(row) * column
        result.append([size, row, column])
        result_size.append(size)
    for j in range(len(set(row_dict))):
        nth = min(result_size)
        result_size.remove(nth)
        stack = []
        minNum = 1000
        Num = 0
        for i in range(len(set(row_dict))):
            if result[i][0] == nth:
                stack.append([i, result[i][1]])
        if len(stack) == 1:
            result[j], result[stack[0][0]] = result[stack[0][0]], result[j]
        else:
            for iii in range(len(stack)):
                if stack[iii][1] < minNum:
                    # print(iii)
                    minNum, Num = stack[iii][1], stack[iii][0]
            result[j], result[Num] = result[Num], result[j]
    answer = ''
    result.sort()
    # print(result)
    print("#{}".format(number+1),end=' ')
    print(len(result),end=' ')
    for reees in range(len(result)):
        print(result[reees][1],result[reees][2],end= ' ')
    print()
    