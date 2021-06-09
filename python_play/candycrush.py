def candy_crush(input_str,target):
    if target > len(input_str):
        return input_str
    stack = []
    for char in input_str:
        if (stack and stack[-1][0] == char and stack[-1][1] == target -1):
            for _ in range(target-1):
                stack.pop()
        else:
            count = 1 if not stack or stack[-1][0] != char else stack[-1][1]+1
            stack.append((char,count))
    return ''.join(letter for letter,num in stack)

print(candy_crush("pbbcggttciiippooaais",2))
        
