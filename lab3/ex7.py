import numpy as np

x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])
n = len(x)

a = np.max(x)
b = np.min(x)
c = np.median(x)
mean = np.mean(x)
d = np.sum(x[x < mean])

e = np.where(x>10)[0]
f = np.flip(x)
g = np.sort(x)
h = np.flip(g)

i = x + x[::-1]
k = x[x>=0]
l = np.abs(x)




count = 0
for i in range(n):
    for j in range(i+1, n-1):
        if x[i] + x[j] == 0:
            count = count + 1

m = len(x) - len(np.unique(x))


def amstrong(num):
    if num<=0:
        return False
    chuoi = str(num)
    k = len(chuoi)
    return sum(int(d) ** k for d in chuoi) == num
m = np.array([num for num in x if amstrong(num) == True])


print(a, b, c, d, e, f, g, h, i, k, l, count, m)
