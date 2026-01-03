a=[]
#Số lượng phần tử trong list
n = int(input("Bạn muốn nhập bao nhiêu số? "))
#Nhập các số vào list
for _ in range(n):
    a.append(int(input("Nhập số: ")))
#Xác định loại số
for i in a:
    if i%2 == 0:
        print(f"{i} là số chẵn")
    else:
        print(f"{i} là số lẻ")
