import sys
from collections import OrderedDict
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QMessageBox, QWidget, QLabel, QListWidgetItem
from PyQt5.QtCore import QCoreApplication, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie, QFont, QColor


from dichngonngu import Ui_MainWindow as Ui_MainAppWindow
from lichsu import Ui_MainWindow as Ui_HistoryWindow
from googletrans import Translator

# --- CÁC BIẾN TÙY CHỈNH ---
LOADING_MARGIN_TOP = 20
LOADING_MARGIN_BOTTOM = 20
# Độ mờ của lớp phủ nền (0.0 = hoàn toàn trong suốt, 1.0 = hoàn toàn đen).
DIMMING_OPACITY = 0.7

LANG_MAP = {
    'Tự phát hiện': 'auto',
    'Tiếng Việt': 'vi',
    'Tiếng Anh': 'en',
    'Tiếng Nhật': 'ja',
    'Tiếng Trung': 'zh-cn',
    'Tiếng Hàn': 'ko',
    'Tiếng Đức': 'de',
    'Tiếng Pháp': 'fr',
    'Tiếng Nga': 'ru',
    'Tiếng Tây Ban Nha': 'es',
    'Tiếng Ả Rập': 'ar'

}

class HistoryWindow(QMainWindow, Ui_HistoryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lịch sử dịch")

        self.history_list_widget = QListWidget(self.centralwidget)
        self.history_list_widget.setGeometry(10, 60, 341, 431)
        self.history_list_widget.setStyleSheet("font-size: 14px; border: 1px solid #ccc;")

        self.thoat_2.clicked.connect(self.hide)

    def update_history_display(self, history_data):
        self.history_list_widget.clear()

        if not history_data:
            self.history_list_widget.addItem("Chưa có lịch sử dịch.")
            return

        for date, entries in history_data.items():
            date_item = QListWidgetItem(date)
            font = date_item.font();
            font.setBold(True);
            font.setPointSize(10)
            date_item.setFont(font);
            date_item.setForeground(QColor("#1d428a"))
            self.history_list_widget.addItem(date_item)

            for entry in entries:
                entry_str = f"  - [{entry['src_name']} → {entry['dest_name']}] \"{entry['orig']}\" → \"{entry['trans']}\""
                self.history_list_widget.addItem(entry_str)

            self.history_list_widget.addItem("")


class MainApp(QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Chương trình dịch ngôn ngữ")
        self.setFixedSize(self.size())

        self.translator = Translator()
        self.translation_history = OrderedDict()
        self.history_window = None

        # --- THÊM LẠI LỚP NỀN MỜ ---
        self.dimming_overlay = QWidget()
        self.dimming_overlay.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.dimming_overlay.setStyleSheet("background-color: black;")
        self.dimming_overlay.setWindowOpacity(DIMMING_OPACITY)
        self.dimming_overlay.hide()

        # Lớp chứa ảnh GIF
        self.gif_widget = QLabel()
        self.gif_widget.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.gif_widget.setAttribute(Qt.WA_TranslucentBackground)

        self.loading_movie = QMovie("load/loading.gif")
        if self.loading_movie.isValid():
            self.gif_widget.setMovie(self.loading_movie)
            self.gif_widget.setScaledContents(False)
            self.gif_widget.setAlignment(Qt.AlignCenter)
        else:
            self.gif_widget.setText("Lỗi: Không tìm thấy 'load/loading.gif'")
            self.gif_widget.setAlignment(Qt.AlignCenter)
            self.gif_widget.setStyleSheet("background-color: black; color: white;")

        self.gif_widget.hide()

        # Kết nối tín hiệu
        self.translation_timer = QTimer(self);
        self.translation_timer.setSingleShot(True);
        self.translation_timer.setInterval(2000);
        self.translation_timer.timeout.connect(self.translate_text)
        self.nhapvanban.textChanged.connect(self.start_translation_timer)
        self.pushButton.clicked.connect(self.show_history_with_loading)
        self.ngaythangnam.setDate(QDate.currentDate());
        self.ngaythangnam.setReadOnly(True)
        self.thoat.clicked.connect(self.close)

        if hasattr(self, 'chuyendoi'):
            self.chuyendoi.clicked.connect(self.swap_languages_and_text)

        self.ngonngudautien.clear();
        if 'Tiếng Việt' not in LANG_MAP: LANG_MAP['Tiếng Việt'] = 'vi'
        self.ngonngudautien.addItems(LANG_MAP.keys())
        self.ngonnguthu2.clear()
        dest_langs = list(LANG_MAP.keys());
        dest_langs.remove('Tự phát hiện')
        self.ngonnguthu2.addItem("Chọn ngôn ngữ");
        self.ngonnguthu2.addItems(dest_langs)
        self.ngonnguthu2.currentTextChanged.connect(self.retranslate_on_selection_change)

    def swap_languages_and_text(self):
        source_lang = self.ngonngudautien.currentText()
        target_lang = self.ngonnguthu2.currentText()
        if source_lang == "Tự phát hiện" or target_lang == "Chọn ngôn ngữ":
            QMessageBox.information(self, "Thông báo",
                                    "Không thể hoán đổi khi đang chọn 'Tự phát hiện' hoặc chưa chọn ngôn ngữ đích.")
            return
        self.ngonngudautien.blockSignals(True);
        self.ngonnguthu2.blockSignals(True)
        self.ngonngudautien.setCurrentText(target_lang);
        self.ngonnguthu2.setCurrentText(source_lang)
        self.ngonngudautien.blockSignals(False);
        self.ngonnguthu2.blockSignals(False)
        input_text = self.nhapvanban.text();
        output_text = self.bandich.text()
        self.nhapvanban.setText(output_text);
        self.bandich.setText(input_text)

    # --- NÂNG CẤP HÀM SHOW_LOADING ---
    def show_loading(self, parent_window=None, with_dimming=False):
        # with_dimming=False là giá trị mặc định, nghĩa là không có nền mờ

        if parent_window and parent_window.isVisible():
            target_geometry = parent_window.geometry()
        else:
            screen_geometry = QApplication.primaryScreen().geometry()
            main_window_geometry = self.geometry()
            main_window_geometry.moveCenter(screen_geometry.center())
            target_geometry = main_window_geometry

        margin_x = self.nhapvanban.x();
        gif_width = self.width() - (2 * margin_x)
        start_y = self.ngonngudautien.y() + self.ngonngudautien.height() + LOADING_MARGIN_TOP
        end_y = self.pushButton.y() - LOADING_MARGIN_BOTTOM
        gif_height = end_y - start_y

        # Chỉ hiển thị và cập nhật lớp nền mờ nếu được yêu cầu
        if with_dimming:
            self.dimming_overlay.setGeometry(target_geometry)
            self.dimming_overlay.raise_()
            self.dimming_overlay.show()

        # Lớp GIF thì luôn hiển thị
        gif_x = target_geometry.x() + margin_x;
        gif_y = target_geometry.y() + start_y
        self.gif_widget.setGeometry(gif_x, gif_y, gif_width, gif_height)
        self.gif_widget.raise_()  # Luôn đưa GIF lên trên cùng
        self.gif_widget.show()

        if self.loading_movie.isValid(): self.loading_movie.start()

    def hide_loading(self):
        # Luôn ẩn cả hai để đảm bảo sạch sẽ
        if self.loading_movie.isValid(): self.loading_movie.stop()
        self.gif_widget.hide()
        self.dimming_overlay.hide()

    def show_history_with_loading(self):
        # --- KHI QUA FORM LỊCH SỬ, BẬT NỀN MỜ ---
        # Gọi show_loading với tùy chọn with_dimming=True
        self.show_loading(parent_window=self, with_dimming=True)
        QTimer.singleShot(3000, self.open_history_window)

    def open_history_window(self):
        self.hide_loading()
        if self.history_window is None:
            self.history_window = HistoryWindow()
            if hasattr(self.history_window, 'thoat_3'):
                self.history_window.thoat_3.clicked.connect(self.clear_history_data)

        self.history_window.update_history_display(self.translation_history)
        self.history_window.show()
        self.history_window.raise_();
        self.history_window.activateWindow()

    def start_translation_timer(self):
        if self.nhapvanban.text().strip(): self.translation_timer.start()

    def retranslate_on_selection_change(self):
        if self.nhapvanban.text().strip() and self.ngonnguthu2.currentText() != "Chọn ngôn ngữ":
            self.translation_timer.stop();
            self.translate_text()

    def translate_text(self):
        source_lang_ui = self.ngonngudautien.currentText();
        dest_lang_ui = self.ngonnguthu2.currentText();
        text_to_translate = self.nhapvanban.text().strip()
        if not text_to_translate: self.bandich.clear(); return
        if dest_lang_ui == "Chọn ngôn ngữ": self.bandich.setText("Vui lòng chọn ngôn ngữ đích!"); return
        try:
            self.bandich.setText("Đang dịch...")
            QApplication.processEvents()
            translation = self.translator.translate(text_to_translate, src=LANG_MAP.get(source_lang_ui),
                                                    dest=LANG_MAP.get(dest_lang_ui))
            self.bandich.setText(translation.text)

            final_source_lang_name = self.ngonngudautien.currentText()
            if source_lang_ui == "Tự phát hiện":
                detected_lang_name = next((name for name, code in LANG_MAP.items() if code == translation.src), None)
                if detected_lang_name:
                    final_source_lang_name = detected_lang_name
                    self.ngonngudautien.blockSignals(True);
                    self.ngonngudautien.setCurrentText(detected_lang_name);
                    self.ngonngudautien.blockSignals(False)

            current_date_str = QDate.currentDate().toString("dd/MM/yyyy")
            entry_details = {'src_name': final_source_lang_name, 'dest_name': dest_lang_ui.strip(),
                             'orig': text_to_translate, 'trans': translation.text}
            if current_date_str not in self.translation_history: self.translation_history[current_date_str] = []
            self.translation_history[current_date_str].insert(0, entry_details)
            self.translation_history.move_to_end(current_date_str, last=False)
            if self.history_window: self.history_window.update_history_display(self.translation_history)
        except Exception as e:
            self.bandich.setText("Lỗi dịch!");
            QMessageBox.critical(self, "Lỗi", f"Đã có lỗi xảy ra:\n{e}")

    def clear_history_data(self):
        if self.history_window:
            reply = QMessageBox.question(self.history_window, 'Xác nhận',
                                         'Bạn có chắc chắn muốn xóa toàn bộ lịch sử không?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.translation_history.clear()
                self.history_window.update_history_display(self.translation_history)
                QMessageBox.information(self.history_window, "Thông báo", "Đã xóa lịch sử dịch.")


# --- KHỐI THỰC THI CHÍNH ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()


    def start_app():
        main_app.hide_loading()
        main_app.show()


    # Khi khởi động, gọi loading không có nền mờ (with_dimming=False là mặc định)
    main_app.show_loading()

    QTimer.singleShot(3000, start_app)
    sys.exit(app.exec_())