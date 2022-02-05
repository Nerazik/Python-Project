from math import *
while True:
 try:
  x = float(input("Введите x:\n"))
  y = float(input("Введите y:\n"))
  if x > 0 and y < 2:
    f = (5 + x - y)
  elif x < 0 or 2 <= y < 12:
    f = (4 - x * y)
  else:
    f = (x + y)
  print ("x =", x, "y =", y, "f =", f,)
  break
 except:
    print("Некорретный ввод данных!")
