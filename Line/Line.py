#  LRRLL, where L stands for a person looking left and R stands for a person looking right, the counts for each person are [0,3,2,3,4], and the value is 0+3+2+3+4=12.

def get_val(string):
    val = 0
    str_len = len(string)
    for n, i in enumerate(string):
        if i == 'L':
            val += n
        elif i == 'R':
            val += str_len - n - 1
    return val


# create permutations of the string except itself
def permutations(string):
    # get permutations  

st = "LRRRLLLRLLRL"
vals = permutations(st)
print(vals)

