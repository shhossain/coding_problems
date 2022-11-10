# Recently, Chef visited his doctor. The doctor advised Chef to drink at least 20002000 ml of water each day.

# Chef drank XX ml of water today. Determine if Chef followed the doctor's advice or not.

for _ in range(int(input())):
    x = int(input())
    if x >= 2000:
        print("YES")
    else:
        print("NO")
