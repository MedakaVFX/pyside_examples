# PySide Examples <!-- omit in toc -->
PySide in VFX.


# Contents: <!-- omit in toc -->

- [System Environment:](#system-environment)
- [Release Note:](#release-note)
- [Installation:](#installation)
- [Getting Started](./000_Geting_Started/Getting_Started.md)
- [Darkstyle:](#darkstyle)
- [Import PySide6:](#import-PySide6)
  - [Example1:](#example1)
  - [Example2:](#example2)
  - [Example3:](#example3)
- [Qt.py](#qtpy)
  - [Example:](#example)

# System Environment:
* Window11
* Python 3.12.4
* PySide6 (Qt 6.8.0.1)


# Installation:
**PySide6:** https://pypi.org/project/PySide6/
```
python -m pip install --upgrade pip
pip install PySide6
```

**Check PySide6**
```
pip list -o
pip show PySide6
```

**Updrade Package**
```
pip install -U PySide6
```

# Import PySide6:
## Example1:
```Python
from PySide6 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QWidget()
    view.show()
    app.exec()
```

## Example2:
```Python
from PySide6.QtCore import (
    Qt
)
from PySide6.QtGui import (
    QColor
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget
)
```

## Example3:
```Python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
```

# QtPy
PyQt5, PySide6, PyQt6, PySide6 互換モジュール
https://pypi.org/project/QtPy/

VFXツールはツールによってQtのPythonモジュールやバージョンが異なるのでqtpyを使ってコードを書いておくと互換性が高まる。

### Example:
```Python
try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from Qt import QtCore, QtGui, QtWidgets
```

# Darkstyle:
Qt用ダークテーマスタイルシート
  
**QDarkstyle:** https://pypi.org/project/QDarkStyle/
```
pip install QDarkStyle
```

**PyQtDarkTheme:** https://pypi.org/project/pyqtdarktheme/
```
pip install pyqtdarktheme
```