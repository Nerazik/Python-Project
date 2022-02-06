from math import *
def ctg(k):
    return cos(k) / sin(k)
a = float(input("Введите значения параметра a:\n"))
k = -1
while True:
    if round(k * 2 - a, 2) == 0:
     k += 0.3
    continue
    z = (math.log(fabs(ctg(a**2))- k*1)) / (k*2) - a
    print("{0} {1:.2f} {2} {3:.4f}" .format("k =", k, "z(a) = ", z))
    k += 0.3
    if k > 6:
     break
