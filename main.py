# ************************** man hinh loai 2 *************************
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.obj_pos_2 = None
        self.obj_pos = None
        self.first_mouse_pos = None

    def mousePressEvent(self, event):
        self.first_mouse_pos = event.pos()
        self.obj_pos = self.uic.label.pos()
        self.obj_pos_2 = self.uic.label_2.pos()

    def mouseMoveEvent(self, event):
        # label
        with_oj = self.uic.label.width()
        height_oj = self.uic.label.height()
        # label 2
        with_oj_2 = self.uic.label_2.width()
        height_oj_2 = self.uic.label_2.height()

        if self.obj_pos.x() < self.first_mouse_pos.x() < self.obj_pos.x() + with_oj and \
                self.obj_pos.y() < self.first_mouse_pos.y() < self.obj_pos.y() + height_oj:
            updated_cursor_position = event.pos()
            updated_cursor_x = updated_cursor_position.x() - self.first_mouse_pos.x() + self.obj_pos.x()
            updated_cursor_y = updated_cursor_position.y() - self.first_mouse_pos.y() + self.obj_pos.y()
            self.uic.label.move(updated_cursor_x, updated_cursor_y)

        elif self.obj_pos_2.x() < self.first_mouse_pos.x() < self.obj_pos_2.x() + with_oj_2 and \
                self.obj_pos_2.y() < self.first_mouse_pos.y() < self.obj_pos_2.y() + height_oj_2:
            updated_cursor_position = event.pos()
            updated_cursor_x = updated_cursor_position.x() - self.first_mouse_pos.x() + self.obj_pos_2.x()
            updated_cursor_y = updated_cursor_position.y() - self.first_mouse_pos.y() + self.obj_pos_2.y()
            self.uic.label_2.move(updated_cursor_x, updated_cursor_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())