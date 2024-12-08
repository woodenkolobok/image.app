from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from back import blur_image, unmask_image

file_path = "Battlefield-2042.jpg"


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

save_open_buttons = QHBoxLayout()
open_button = QPushButton('Открыть')
save_open_buttons.addWidget(open_button)
layout.addLayout(save_open_buttons)

tools_layout = QHBoxLayout()
blur_button = QPushButton('Заблюрить')
unmask_button = QPushButton('Снять блюр')
tools_layout.addWidget(blur_button)
tools_layout.addWidget(unmask_button)
layout.addLayout(tools_layout)

picture = QLabel()
pixmap = QPixmap("Battlefield-2042.jpg").scaledToWidth(500)
picture.setPixmap(pixmap)
layout.addWidget(picture)


window.setLayout(layout)

window.show()

def update_pixmap(file_path):
    global pixmap
    pixmap = QPixmap(file_path).scaledToWidth(500)
    picture.setPixmap(pixmap)

def openFileButtonHandler():
    global file_path
    file_path = QFileDialog.getOpenFileName()[0]
    if file_path:
        update_pixmap(file_path)
        
def blurButton():
    blur_image(file_path)
    update_pixmap(file_path)

def unmaskButton():
    unmask_image(file_path)
    update_pixmap(file_path)


open_button.clicked.connect(openFileButtonHandler)
blur_button.clicked.connect(blurButton)
unmask_button.clicked.connect(unmaskButton)
app.exec()