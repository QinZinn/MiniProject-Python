quang_duong = float(input("Số km đã đi: "))
tien = 0
if quang_duong > 0 and quang_duong < 0.4:
    tien = 20000
if quang_duong > 0.4 and quang_duong <= 10:
        tien = 20000 + (quang_duong - 0.4)*15000
if quang_duong > 10 and quang_duong < 50:
        tien = 20000 + 9.6*16000 + (quang_duong - 10)*12000
if quang_duong > 50:
        tien = 20000 + 9.6*15000 + 40*12000 + (quang_duong - 50)*8000
if quang_duong <0:
    print("Quãng đường không thể âm!")

print(f"Số tiền cần trả là: {tien}")