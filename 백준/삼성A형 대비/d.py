arr = [3,4,1,2,3,5,1]
N = len(arr)
subset_list = []
for i in range(1<<N):
    subset = []
    for j in range(N):
        if i&(1<<j):  # j번째 요소가 1인지 아닌지 판별
            subset.append(arr[j])
    if len(subset)==3:
        subset_list.append(subset)
    print()
print()

print(subset_list)