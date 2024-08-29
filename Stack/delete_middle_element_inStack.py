def deletemiddle(stack):
    sizeofStack = len(stack)
    mid = sizeofStack//2
    if mid%2 == 0:
        mid = int[mid -1]
    stack.pop(mid)


list = input().split()

stack = [int(x) for x in list]
deletemiddle(stack)
print(stack)