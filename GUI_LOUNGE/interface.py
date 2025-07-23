import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize


class WaguriWindow(QWidget):
    def __init__(self):
        super().__init__()

        print("🚀 Initializing WaguriWindow...")

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool  # No taskbar icon
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        gif_path = os.path.join(base_dir, "assets", "waguri_san.gif")
        print(f"📂 Looking for GIF at: {gif_path}")

        if not os.path.exists(gif_path):
            print("❌ ERROR: GIF not found!")
            self.setFixedSize(200, 200)
            self.setStyleSheet("background-color: magenta;")
        else:
            self.label = QLabel(self)
            self.movie = QMovie(gif_path)
            self.movie.setScaledSize(QSize(145, 200))  # ✅ Corrected here
            self.label.setMovie(self.movie)
            self.label.setFixedSize(145, 200)
            self.setFixedSize(145, 200)
            self.movie.start()
            print("🎞️ GIF loaded and playing!")

        self.move(20, 20)
        print("✅ WaguriWindow setup complete.")

    def enterEvent(self, event):
        print("Waguri: T-Tsuki...? You hovered on me again...")
        return super().enterEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaguriWindow()
    window.show()
    sys.exit(app.exec())
