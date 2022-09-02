def swap(a, b):
    return b, a

def max_so_far(a):
    # kadane's algorithm
    max_so_far = 0
    max_ending_here = 0
    max_ending_here2 = 0
    for i in range(len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

        j = i - 1
        if j >= 0:
            max_ending_here2 += a[j]
            if max_ending_here2 < 0:
                max_ending_here2 = 0
            elif max_so_far < max_ending_here2:
                max_so_far = max_ending_here2
                a[i], a[j] = swap(a[i], a[j])
                max_ending_here = max_ending_here2
            elif max_so_far > max_ending_here2:
                max_ending_here2 = max_ending_here
    # return max_so_far
    print(max_so_far)


# def calculate_max(a):
#     max_so_fars = []
#     for i in range(len(a)):
#         j = i + 1
#         if j < len(a):
#             a[i], a[j] = swap(a[i], a[j])
#             max_so_fars.append(max_so_far(a))
#             a[i], a[j] = swap(a[i], a[j])
    
#     return max(max_so_fars)
        
        
        

# a = [-1,5,7,-5,11,2,-11]
a = [1,-10,2,2]
# a = [1] * 1000
print(max_so_far(a))

# runs = int(input())
# for i in range(runs):
#     n = int(input())
#     a = list(map(int, input().split()))
#     max_o = max_op(a)
#     print("Case {}: {} {}".format(i+1, max_o[0], max_o[1]))
