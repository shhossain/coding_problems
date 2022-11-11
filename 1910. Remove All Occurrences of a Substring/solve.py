s = "daabcbaabcbc"
part = "abc"



while True:
    idx = s.find(part)
    if idx == -1:
        break
    s = s[:idx] + s[idx+len(part):]
print(s)
