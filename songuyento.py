a = int(input("Nhập số cần kiểm tra: "))

# Loại trừ hết số nhỏ hơn 2
if a < 2:
    snt = False
else:
    snt = True
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0: # Nếu chia hết cho i thì không phải SNT
            snt = False
            break

#Kết quả
if snt:
    print(f"{a} là số nguyên tố")
else:
    print(f"{a} không phải là số nguyên tố")