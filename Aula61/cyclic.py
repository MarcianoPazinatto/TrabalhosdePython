#  A = [3, 8, 9, 7, 6]
#  K = 3

A = [3, 8, 9, 7, 6]

for i in range(3):
    A.insert(0, A[-1])
    A.pop()
print(A)

B = [1, 2, 3, 4]
# K = 4

for i in range(4):
    B.insert(0,B[-1])
    B.pop()
print(B)
