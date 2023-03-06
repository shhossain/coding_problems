# Chef has an array AA of length NN.

# He can modify this array by applying a special operation any number of times. In one operation, he can:

# Select two indices ii and jj (1\le i \lt j \le |A|)(1≤i<j≤∣A∣).
# Append A_i \oplus A_jA 
# i
# ​
#  ⊕A 
# j
# ​
#   to the end of the array, where \oplus⊕ denotes the bitwise XOR operation
# Remove A_iA 
# i
# ​
#   and A_jA 
# j
# ​
#   from the array.
# Chef wants to maximize the product of all the elements of the array after applying these operations.

# Help Chef determine the maximum product he can achieve by applying this operation any (possibly zero) number of times. As this number can be large, print it modulo 998244353998244353.

# Input Format
# The first line of input will contain a single integer TT, denoting the number of test cases.
# Each test case consists of two lines of input.
# The first line of each test case contains one integer NN — the number of elements in the array.
# The second line consists of NN space-separated integers A_1, A_2, \ldots, A_NA 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#   denoting the elements of the array initially.
# Output Format
# For each test case, output the maximum product he can achieve modulo 998244353998244353.

# Constraints
# 1 \leq T \leq 5\cdot 10^41≤T≤5⋅10 
# 4
 
# 2 \leq N \leq 10^52≤N≤10 
# 5
 
# 1 \leq A_i \leq 10^91≤A 
# i
# ​
#  ≤10 
# 9
 
# The sum of NN over all test cases won't exceed 3\cdot 10^53⋅10 
# 5
#  .
# Sample 1:
# Input
# Output
# 3
# 4
# 1 2 1 2
# 2
# 3 3
# 2
# 2 1
# 9
# 9
# 3
# Explanation:
# Test case 11: Chef can make the following operations:

# Operation 11: Choose i = 1i=1 and j = 2j=2, append A_1\oplus A_2 = 1\oplus 2 = 3A 
# 1
# ​
#  ⊕A 
# 2
# ​
#  =1⊕2=3 to the end of the array and remove elements A_1A 
# 1
# ​
#   and A_2A 
# 2
# ​
#  . Thus, the array becomes [1, 2, 3][1,2,3].
# Operation 22: Choose i = 1i=1 and j = 2j=2, append A_1\oplus A_2 = 1\oplus 2 = 3A 
# 1
# ​
#  ⊕A 
# 2
# ​
#  =1⊕2=3 to the end of the array and remove elements A_1A 
# 1
# ​
#   and A_2A 
# 2
# ​
#  . Thus, the array becomes [3, 3][3,3].
# The product of all elements of the array is 3\times 3 = 93×3=9. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.

# Test case 22: The product of all elements of the array is 3\times 3 = 93×3=9. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.
# Thus, Chef does not need to perform any operations.

# Test case 33: Chef can make the following operation:

# Operation 11: Choose i = 1i=1 and j = 2j=2, append A_1\oplus A_2 = 1\oplus 2 = 3A 
# 1
# ​
#  ⊕A 
# 2
# ​
#  =1⊕2=3 to the end of the array and remove elements A_1A 
# 1
# ​
#   and A_2A 
# 2
# ​
#  . Thus, the array becomes [3][3].
# The product of all elements is 33. It can be shown that this is the maximum product that can be obtained by applying any number of operations on the array.


for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    
    