a = int(input("Nhập số cần kiểm tra: "))
if a<2:
    print(f"{a} là số nguyên tố")
else:
    snt = True

    for i in range(2,a):
        for k in range(2,a):
            if i*k == a:
                snt = False
                break
        if not snt:
            break
if snt:
    print(f"{a} là số nguyên tố")
else:
    print(f"{a} không phải là số nguyên tố")