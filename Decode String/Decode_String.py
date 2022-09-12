letter_map = {str(i): chr(i + 96) for i in range(1, 27)}

runs = int(input())
for _ in range(runs):
    size = int(input())
    encoded = input()
    decoded = ''
    i = 0
    while i < size:
        lt = int(encoded[i])
        if lt != 0:
            decoded += letter_map[encoded[i]]
            i += 1
        else:
            e = i + 1
            if e < size:
                if encoded[e] == '0':
                    # remove last char
                    decoded = decoded[:-1]
                    decoded += letter_map[encoded[i-1] + '0']
                    i += 2
                else:
                    decoded = decoded[:-2]
                    decoded += letter_map[encoded[i-2] + encoded[i-1]]
                    i += 1
            else:
                decoded = decoded[:-2]
                decoded += letter_map[encoded[i-2] + encoded[i-1]]
                i += 1
    print(decoded)
