import sys
from cx_Freeze import setup, Executable

# Các file và thư mục cần sao chép vào thư mục build
# Bao gồm cả thư mục chứa ảnh và các file .py giao diện
include_files = ['load/', 'dichngonngu.py', 'lichsu.py']

# Các gói thư viện mà chương trình của bạn sử dụng
# cx_Freeze đôi khi không tự phát hiện được hết, nên chúng ta khai báo rõ ràng
packages = ['sys', 'os', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'collections', 'googletrans']

build_exe_options = {
    'packages': packages,
    'include_files': include_files,
    # 'include_msvcr': True, # Bỏ comment dòng này nếu bạn build trên Windows và gặp lỗi thiếu MSVCR...dll
}

# Cấu hình cho file thực thi .exe
# base="Win32GUI" là bắt buộc cho các ứng dụng giao diện trên Windows để không hiện cửa sổ dòng lệnh màu đen
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Trình Dịch Thuật",
    version="1.0",
    description="Chương trình dịch ngôn ngữ của Hoàng Anh",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="load/app_icon.ico")]
)