# module tính toán hai số
import math
def tong(x,y):
    return x+y
def hieu(x,y):
    return x-y

# Ví dụ từ module tinh_toan_hai_so đưa vào hai hàm tổng,hiệu
from tinh_toan_hai_so import tong,hieu
x,y = 3,5
print("Tổng ",x,"+",y,"=",tong(x,y))
print("Hiệu ",x,"-",y,"=",hieu(x,y))

#Ví dụ: import tất cả  các hàm thuộc tính vào namespace hiện tại
# Từ module tinh_toan_hai_so
from tinh_toan_hai_so import*
a,b=3,5
print("Tổng ",x,"+",y,"=",tong(x,y))
print("Hiệu ",x,"+",y,"=",hieu(x,y))

