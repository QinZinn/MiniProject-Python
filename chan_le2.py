a=[]
#Số lượng số chẵn/lẻ ban đầu
chan = 0
le = 0
#Số lượng phần tử trong list
n = int(input("Bạn muốn nhập bao nhiêu số? "))
#Nhập các số vào list
for _ in range(n):
    a.append(int(input("Nhập số: ")))
#Thêm số vào danh sách
for i in a:
    if i % 2 == 0:
        chan += 1
    else:
        le += 1
#Output
print("Số chẵn:", chan)
print("Số lẻ:", le)