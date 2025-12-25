import sys

loai = input("Điền loại phép tính: ")
so1 = float(input("Số đầu tiên: "))
so2 = float(input("Số thứ hai: "))
if loai == "+":
    dapan = so1 + so2
elif loai == "-":
    dapan = so1 - so2
elif loai == "*" or loai == "x":
    dapan = so1 * so2
elif loai == ":" or loai == "/":
    dapan = so1 / so2
else:
    print("Phép tính không hợp lệ")
    sys.exit()

print("Đáp án là:",round(dapan, 2))