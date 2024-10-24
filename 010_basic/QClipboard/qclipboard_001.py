import sys

from PySide6.QtGui import (
    QClipboard, QPixmap
)

from PySide6.QtWidgets import QApplication # Qt対応のVFXツールでは省略可

#=====================================#
# Text
#=====================================#
# 文字データのコピー
def copy_text(text: str):
    cb = QClipboard()
    cb.setText(text)

# 文字データのペースト
def paste_text():
    cb = QClipboard()
    return cb.text()

#=====================================#
# Image
#=====================================#
def copy_image(image: str):
    # クリップボードにイメージデータを送る。画像編集ソフトなどでペースト出来る
    cb = QClipboard()
    cb.setPixmap(QPixmap(image))

def paste_image():
    # 画像ソフトのコピペやプリントスクリーンのデータを取得出来る
    cb = QClipboard()
    return cb.pixmap()


#=====================================#
# Main
#=====================================#
if __name__ == '__main__':
    app = QApplication(sys.argv) # Qt対応のVFXツールでは省略可
    
    # Clipboard to Text
    copy_text('Test')

    # Text form Clipboard
    print(paste_text())
    
    # Clipboard to Image
    copy_image(r'C:\Users\yamagishi\Pictures\pic001.png')
    
    # Image from Clipboard
    file= r'C:\Users\yamagishi\Pictures\pic001_new.png'
    image = paste_image()
    image.save(file)

    # この後画像をツールで読み込んだり
    # nuke.tcl('drop', file)