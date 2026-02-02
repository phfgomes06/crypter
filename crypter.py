import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QTextEdit, QPushButton)

from cryptographies import abbacrypt

class CrypterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypter")
        self.resize(400,500)

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(15)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Sentence to crypt or decrypt...")
        layout.addWidget(self.input_text)

        self.btn_convert = QPushButton("convert")
        self.btn_convert.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
                color: gray;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)

        self.btn_convert.clicked.connect(self.convert)
        layout.addWidget(self.btn_convert)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)
    
    def convert(self):
        text = self.input_text.toPlainText()
        encrypted = abbacrypt(text)
        self.output.setPlainText(encrypted)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrypterApp()
    window.show()
    sys.exit(app.exec())