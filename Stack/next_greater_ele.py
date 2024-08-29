def next_greater(arr, n):
    result = []
    stack = []
    
    stack.append(arr[n-1])
    result.append(-1)

    for i in range(n-2, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()

        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(arr[i])
    result.reverse()
    return result



arr = [5, 15, 10, 8, 6, 12, 9, 18]
n = len(arr)

result = next_greater(arr, n)
print(" ".join(map(str, result)))