#nhap so tu nguoi dung
so = int(input("Nhap mot so nguyen: "))
#kiem tra xem so do co phai sso chan hay khong
if so % 2 == 0:
    print(so, "la so chan.")
else:
    print(so, "khong phai la so chan.")