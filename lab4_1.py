a = float(input("Введите a:\n"))
b = float(input("Введите b:\n"))
c = float(input("Введите c:\n"))
d = float(input("Введите d:\n"))
LV = abs(a) >= abs(b) and abs(b) >= abs(c) and abs(c) >= abs(d)
print("Числа по модулю не возрастают:", LV)
