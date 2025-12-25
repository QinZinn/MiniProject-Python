print("0 là không, 1 là có")

a = int(input("Parabol hướng lên? "))
b = int(input("Đỉnh ở phần âm? "))
c = int(input("Tại x=0 thì y dương? "))

if a == 0:
    print("a < 0")
else:
    print("a > 0")

if c == 0:
    print("c < 0")
else:
    print("c > 0")

if b == 0 and a == 0:
    print("b > 0")
elif b == 0 and a == 1:
    print("b < 0")
elif b == 1 and a == 0:
    print("b < 0")
elif b == 1 and a == 1:
    print("b > 0")
else:
    print("?")