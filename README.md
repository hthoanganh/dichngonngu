# Ứng dụng Dịch thuật Đa ngôn ngữ của Hoàng Anh / Hoang Anh's language translation app
![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![PyQt5](https://img.shields.io/badge/Qt-PyQt5-green.svg) ![API](https://img.shields.io/badge/API-Google_Translate-red.svg)

Một ứng dụng dịch thuật desktop được xây dựng bằng Python và thư viện PyQt5. Chương trình cho phép người dùng dịch văn bản giữa nhiều ngôn ngữ khác nhau một cách nhanh chóng và trực quan, sử dụng Google Translate API làm backend. Ứng dụng cũng đi kèm các tính năng tiện ích như tự động phát hiện ngôn ngữ, hoán đổi ngôn ngữ và lưu trữ lịch sử dịch.

## 📸 Hình ảnh Demo

**Giao diện dịch chính:**
*Một ảnh GIF thể hiện chức năng dịch tự động sẽ rất ấn tượng ở đây!*
**Cửa sổ Lịch sử dịch:**
## ✨ Các tính năng chính

* **Dịch thuật đa ngôn ngữ:** Hỗ trợ dịch giữa hơn 10 ngôn ngữ phổ biến:
    * Tiếng Việt, Anh, Nhật, Trung, Hàn, Đức, Pháp, Nga, Tây Ban Nha, Ả Rập.
* **Tự động phát hiện ngôn ngữ:** Tự động xác định ngôn ngữ nguồn khi người dùng nhập văn bản.
* **Dịch gần thời gian thực:** Chương trình tự động dịch sau một khoảng nghỉ ngắn khi người dùng gõ văn bản, không cần nhấn nút.
* **Hoán đổi ngôn ngữ:** Dễ dàng hoán đổi ngôn ngữ nguồn và đích cùng với nội dung văn bản chỉ bằng một cú nhấp chuột.
* **Lịch sử dịch:**
    * Tự động lưu lại tất cả các bản dịch.
    * Hiển thị lịch sử được nhóm theo ngày một cách rõ ràng.
    * Cho phép xóa toàn bộ lịch sử.
* **Giao diện người dùng hiện đại:**
    * Hiển thị ngày tháng hiện tại.
    * Sử dụng hiệu ứng loading (ảnh GIF) mượt mà khi khởi động và khi thực hiện các tác vụ tốn thời gian, mang lại trải nghiệm người dùng tốt hơn.

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python 3
* **Giao diện người dùng (GUI):** PyQt5
* **Thư viện dịch thuật:** `googletrans` (một thư viện không chính thức cho Google Translate API)
* **Công cụ:** Qt Designer, PyCharm/VS Code

## 🚀 Cài đặt và Chạy dự án

Để chạy dự án này trên máy của bạn, hãy làm theo các bước sau:

**1. Clone repository về máy:**
```bash
git clone [ĐƯỜNG-DẪN-REPO-GITHUB-CỦA-BẠN]
cd [TÊN-THƯ-MỤC-DỰ-ÁN]
```

**2. Tạo và kích hoạt môi trường ảo:**
*Khuyên dùng để không ảnh hưởng đến các thư viện Python trên máy của bạn.*
```bash
# Tạo môi trường ảo (trên Windows)
python -m venv .venv

# Kích hoạt môi trường ảo (trên Windows)
.\.venv\Scripts\activate
```

**3. Cài đặt các thư viện cần thiết:**
*Tất cả các thư viện cần thiết đã được liệt kê trong file `requirements.txt`.*
```bash
pip install -r requirements.txt
```

**4. Cấu trúc thư mục:**
*Hãy chắc chắn rằng bạn có một thư mục tên là `load` và bên trong có chứa file `loading.gif` để hiệu ứng hoạt động.*
```
your-project-folder/
│
├── main.py
├── dichngonngu.py
├── lichsu.py
├── requirements.txt
└── load/
    └── loading.gif
```

**5. Chạy chương trình:**
```bash
python main.py
```

---
Cảm ơn bạn đã ghé thăm dự án!
