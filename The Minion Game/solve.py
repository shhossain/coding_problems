def minion_game(string):
    s,k = 0,0
    n = len(string)
    for i in range(n):
        if string[i] in "AEIOU":
            k+=n-i
        else:
            s+=n-i
    
    if s>k:
        print("Stuart",s)
    elif k>s:
        print("Kevin",k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)