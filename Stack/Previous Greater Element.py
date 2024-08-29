# Previous Greater Element
def prevGreater(arr, n): # (list, var)
    stack = list() # Creating stack

    #Add the first element from list to the stack
    stack.append(arr[0]) 

    print("-1", end = ", ") #First element inthe stack should return -1
    
    for i in range(1, n):
        while (len(stack) > 0 and stack[-1] < arr[i]):
            stack.pop()

        if len(stack) == 0:
            print("-1", end = ", ")
        else:
            print(stack[-1],  end = ", ")

        stack.append(arr[i])

arr = [10, 4, 2, 20, 40, 12, 30]
n = len(arr) # n = 7
prevGreater(arr, n) # (list, var)


