def superReducedString(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or  stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0 :
        return "Empty string"
    else:
      return  "".join(stack)

print(superReducedString("aaabccddd"))