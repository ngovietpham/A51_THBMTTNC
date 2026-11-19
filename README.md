# A51_THBMTTNC

## Giới thiệu
Repo lưu trữ bài thực hành Python của môn Thực hành Bảo mật Thông tin Nâng cao, Bài 1: Lập trình cơ bản với Python. Các nội dung được sắp xếp theo mục 1.6.2, 1.6.3 và 1.6.4 của giáo trình.

## Nội dung bài tập
- **ex01:** chương trình `hello.py`.
- **ex02 – Python cơ bản:** 10 bài về nhập/xuất dữ liệu, điều kiện, vòng lặp, danh sách, chuỗi và hàm.
- **ex03 – List, Tuple, Dictionary:** 6 bài gồm tính tổng số chẵn, đảo ngược danh sách, chuyển list thành tuple, lấy phần tử đầu/cuối của tuple, đếm số lần xuất hiện và xóa key khỏi dictionary.
- **ex04 – OOP:** chương trình quản lý sinh viên; thêm, cập nhật, xóa, tìm kiếm, sắp xếp và hiển thị danh sách. Điểm học lực được xếp theo các mức trong giáo trình.

## Cấu trúc thư mục
```text
A51_THBMTTNC-git/
├── .gitignore
├── README.md
└── lab-01/
    ├── ex01/
    │   └── hello.py
    ├── ex02/
    │   ├── ex02_01.py ... ex02_10.py
    ├── ex03/
    │   ├── ex03_01.py ... ex03_06.py
    └── ex04/
        ├── SinhVien.py
        ├── QuanLySinhVien.py
        └── Main.py
```

## Yêu cầu
- Python 3.12 hoặc Python 3 tương thích.
- Không cần cài thư viện ngoài cho các bài tập này.

## Cách chạy
Mở thư mục repo trong VS Code. Có thể mở từng file `.py` và chọn **Run Python File**, hoặc chạy tại PowerShell ở thư mục gốc repo:

```powershell
python .\lab-01\ex02\ex02_01.py
python .\lab-01\ex03\ex03_01.py
python .\lab-01\ex04\Main.py
```

Thay tên file để chạy bài khác trong `ex02` hoặc `ex03`. Với ex04, chạy `Main.py`; giữ ba file Python của ex04 cùng một thư mục để các lệnh import hoạt động.

## Git
File `.gitignore` ở thư mục gốc bỏ qua các file Python đã biên dịch (`*.pyc`) và thư mục cache (`__pycache__/`).
