# PySide6 : Getting Started
`Pythonなどプログラムがちょっと分かる人` が新たにPySide6を始めようとした際に参考になりそうな感じでまとめてみた。


Updated: 2024/10/24 Tatsuya YAMAGISHI(CG Sup. )
- PySide6対応

Created: 2022/06/21 Tatsuya YAMAGISHI(CG Sup. )

# 関連 & 参考：
- [Qt公式](https://www.qt.io/)
- [Qt公式(JP)](https://www.qt.io/ja-jp/)
- [Qt fro Python](https://doc.qt.io/qtforpython-6/)
- [PySide6公式 : Getting started](https://doc.qt.io/qtforpython-6/gettingstarted.html)
- [Create professional user-interfaces for your Python apps](https://www.pythonguis.com/)


## 概要：
0. [始めに](#intro)
1. [Python3のインストール:](#install_python)
2. [PySide6インストール:](#install_PySide6)
3. [開発環境:](#develop)
4. [Import PySide6:](#import)
5. [Qアプリケーションの作成:](#qapplication)
6. [GUIの作成:QtDesigner](#qtdesigner)
7. [Windowの作成:](#window)
   1. [QDialog](#qdialog)
   2. [QMainWindow](#qmainwindow)
   3. [QWidet](#qwidget)
   4. [Widgetの種類](#widgets)
8. [PySideのクラスカスタマイズ基本:](#customize_basic)
9. [Widgetのカスタマイズ:](#customize)
10. [QLayout:](#qlayout)
11. [シグナルの設定:](#signal)
12. [作成したWidgetをDialogやMainWindowに配置:](#gui)
13. [Examples:](#examples)



<a id="intro"></a>

# 0. はじめに
- PySideはQt(C++のライブラリ)をPythonで使えるようにしたGUI作成用ライブラリ。
- PySideのプログラムは `クラス` を使うため、クラスの基本的な知識があると良い。
  - 参考：[VFXのためのPySideまとめ　PySideのためのクラス](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html)
- 駆け足で記事を書いたため、おかしな所はつど修正していく予定。
- **記事の内容に一切の責任を持ちません。**



<a id="install_python"></a>

# 1. Python3のインストール
Pythonのインストールに関してはネットに沢山の情報があると思うのでここでは割愛。

### 参考：
- [Pythonのバージョンを確認、表示（sys.versionなど）](https://note.nkmk.me/python-sys-platform-version-info/)
  
### VFX用途のPythonのバージョンについて
2024/10/24現在
- [VFX Reference Platform](https://vfxplatform.com/) などを参考に環境に合ったバージョンを選択。良く分からない場合は、最新のバージョンをインストールして問題ない。


### VFXツールのPythonについて
- Maya、Nuke、Houdini、3dsMaxは標準でPython、PySideが組み込まれているため**インストールは不要**。
- Python3が使えるクライアントバージョンを選択。Nukeだと13.0以降など。
  - OSで実行したい際は別途OSにPython3、PySide6をインストールする必要がある。


### Pythonには対応しているがPySideに対応していないツール
- Pythonに対応していればPySideを動かせる場合がある。
  - 関連： [BlenderでPySide6のツールを動かすまで](https://www.notion.so/yamagishi-vfx/Blender-PySide6-e724122a5db848d9b7964db76fe479c5)
- Cinema4dでPySideのツールを動かすのはとても困難な印象。
  - ShotGridの [tk-cinema](https://github.com/mikedatsik/tk-cinema) で実現しているようだが、WindowsだとCinema4d用のPySide6のビルドを準備する必要があったり、とても敷居が高く感じた。Cinema4dのPythonが c++ APIのラッパーでスクリプトの難易度がとても高いという背景などもある。


### PySide2(Qt5)との違いについて ###
- [Qt5（PySide2）との違い](https://www.notion.so/yamagishi-vfx/Qt5-PySide6-f1721b13068f4dd98fc199469a78f7ad)



<a id="install_PySide6"></a>
# 2. PySide6 インストール：

### 参考：
- [pipでアップデートするときのコマンド pip update](https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8)
- [pipでいれたパッケージを一括アップデート](https://dragstar.hatenablog.com/entry/2016/09/02/113243)
- 関連：[PySide6 インストール ](https://yamagishi-2bit.blogspot.com/2021/11/vfx-vfxPySide6-PySide6.html)



### PySide6のインストール

Pipを最新にしておく。環境によっては`pip`コマンドは`pip3`。
```
pip install --upgrade pip
```
PySide6のインストール
```
pip install PySide6
```

**情報確認**
```
pip show PySide6
```

**PySide6を最新に**
```
pip install -U PySide6
```

**一覧**
```
pip list
```

**アップデート可能なパッケージリスト**
```
pip list -o
```




<a id="develop"></a>

# 3. 開発環境
### VSCodeのインストール
- コードエディタとして `VSCode` をインストール
- MayaなどのVFXツールは `簡易コードエディタ` が搭載されているためインストールは必須ではないが・・・。
  - VSCodeなどの高機能エディタは `スペルミス` や `補完機能` など便利な機能が沢山あるため `VSCode` などの高機能エディタの使用を推奨。これに慣れてしまうと普通のドキュメント作成もVSCodeが手放せない。
  - `VSCode` 以外のエディタでは `PyCharm` の名前をよく耳にする。
  
   ![image](https://i.gyazo.com/a70de37f8f1609d7a447dfdbcb494af1.png)
  


### Python拡張をインストール
- 言語は `日本語` に設定して問題ないと思う。日本語使うと挙動がおかしくなる貧弱なVFXツールとは出来が違う。
- 左のツールバーのエクステンションなどから **Python拡張をインストール**

![](https://i.gyazo.com/a12b8c984f90b87ef7421532434f1109.png)


### 大事な設定：TABはスペース4つを確認
画面右下を確認

![](https://i.gyazo.com/34de041a17d1adf071e27f8df55dd94e.png)

関連：[全ツール共通のスクリプトエディタの設定：インデントはスペース4つ](https://yamagishi-2bit.blogspot.com/2021/05/vfxpython.html)


### Pythonスクリプトの実行
- プログラムを書いて `test.py` などで保存
- CTRL+F5 の `Run Without Debugging` で プログラムを評価
- 僕の環境では、F5の `Start Debugging` だと PySide6が上手く動作しない事がある。

![](https://i.gyazo.com/47e4c22b22258078972e2d57dd49afaf.jpg)


### ターミナル（コマンドプロンプト）などでコマンドで実行（本来のスクリプト実行方法）
Windowsはファイルをダブルクリックしても実行可
```
python test.py
```

### VSCode上のターミナルからでも実行可
![image](https://gyazo.com/9a5e19c19d1f190bb438830f800f02f2.png)



### VSCode便利な操作
- [参考：VS Code の便利なショートカットキー](https://qiita.com/12345/items/64f4372fbca041e949d0)
- 記事を書いている環境が `英語キーボード` 環境であるため、日本語キーボードとショートカットが異なる可能性あり。
  
| ショートカット | 説明 |
| ---- | ---- |
| Ctrl + \ | ページを水平分割 |
| Ctrl + / | コメントアウト |
| Alt + Shift + ↑↓ | 選択行（複数可）を複製 |
| Alt + Shift + ALT + ↑↓ | カーソルを複製（複数行同時編集） |
| Shift + Delete | 1行丸ごと削除 | 
| Ctrl + D | 選択している単語と同じ文字を選択。押すたびに追加選択 | 
| Alt + PgUp/PgDn | カーソル位置を変えずにスクロール | 
| Ctrl + k → v | Markdown `.md` 形式のプレビュー | 




<a id="import"></a>

# 4. Import PySide6
**関連：**[import PySide](https://yamagishi-2bit.blogspot.com/2021/11/PySide6-import-pyside-vfx.html)
- いくつかimportの方式があり、それぞれメリットデミリットがあるように思える。僕個人は `最適` を提案出来るほど知識を有していない。
- `PySide6.QtWidgets` に様々な種類のウィジェットが入っている。

Example:
```Python
from PySide6.QtCore import (
    QPoint, QRect, QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QKeySequence
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)
```

### 動作確認：バージョンの表示
```Python
"""
 Reference From : 
    https://doc.qt.io/qtforpython-5/quickstart.html
"""

import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)

>>> Result：# 表示はCoreとなっているQtのバージョンのようだ。
>>> '6.8.0'
```

<a id="qtdesigner"></a>



<a id="qapplication"></a>

# 5. Qアプリケーション作成

アプリケーション作成最小コード

![](https://i.gyazo.com/9fe7fe6fe3f9385c9dffc2d03c15038a.png)
```Python
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
window = QWidget()

# ウィジェットの表示
window.show()

# アプリケーションメインループ開始
app.exec()
```

### 注1：QApplicationは一番最初に必ず作らないとならない
![image](https://i.gyazo.com/9d87fbcd0015771c9c0061dcbb0cb981.png)

**Widgetオブジェクトが作れない。**
```
> QWidget: Must construct a QApplication before a QWidget
```

### 注2：QtでGUIが作成されているVFXツールの場合
`QApplication` は**１つだけ作成**

一般の環境ではあまりないかもしれないが、MayaなどのVFXツールはQtでアプリケーションが作られており、Python、PySideがツールにガッツリ組み込まれている。ツール起動時に `QApplication` が作成されるらしく、`QApplication` を作ろうとするとエラーを返す。

**先ほどのコードをMayaで実行した結果：**
- Mayaが落ちる事もある。
```
# Result
# Error: RuntimeError: file <maya console> line 8: A QApplication instance already exists. 
```

Qtベースのツール上でのPySideはQアプリケーションの処理を省略する。
```Python
app = QApplication(sys.argv)
app.exec()
```
を省略

### PySide6が使えるVFXツールにおけるウィジェットの表示
- Maya
- Nuke
- Houdini
- 3dsMax

などが同じコードでウィンドウを作成出来る。

![image](https://i.gyazo.com/12c9f68e67d9fd7c5800d7c776f4be0d.png)

```Python
import sys

from PySide6.QtWidgets import QWidget

# ウィジェットオブジェクト作成
window = QWidget()

# ウィジェットの表示
window.show()
```

### Tips：OSとVFXツールで同じプログラムを使い回したい場合
`QApplication.instance()` で `QApplication` を取得し条件分岐させるなど
```Python
app = QApplication.instance()

if app is None:
    # OS用
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()
else:
    # VFXツール用
    window = QWidget()
    window.show()
```    


# 6.GUIのデザイン：QtDesigner
ここではプログラムコード主体で進めていくが、GUIのデザインは `QtDesigner` を使うと楽。

- 関連：[QtDesignerで学ぶQtの基本概念](https://yamagishi-2bit.blogspot.com/2021/11/PySide6-qtdesignerqt-vfx.html)
- 関連：[QtDesignerの.uiファイルの読み込み](https://yamagishi-2bit.blogspot.com/2021/11/PySide6-qtdesigner-vfx.html)

- Linuxは `QtDesigner` を別途インストールする必要があるらしい。




<a id="window"></a>

# 7. Windowの作成
PySide6で準備されているWindow用のウィジェットは

- `QDialog`
- `QMainWindow`

の２つ

- `QWidget` は `parent` の有無でWindowとしてもパーツとしても振舞う。
- `QWidget` から派生する多くのWidget群も同様の振る舞いをする。
- `QDialog`, `QMainWindow` は `parent` を 設定すると、親画面の手前に常にWindowが表示されるようになる。
  - 「VFXツールのメイン画面の手前に常に表示させる方法」はこの辺の仕様によるものらしい。
  - 関連：[VFXツールの各PySideGUI導入調べた](https://yamagishi-2bit.blogspot.com/2021/07/pyside-pysidegui-python.html)

---

<a id="qdialog"></a>
### 7.1 QDialog：ウィンドウとして表示
- 公式[PySide6 QDialog](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QDialog.html)

最も簡単にWindowの作成、運用が可能。

![](https://i.gyazo.com/17d20a4102d4ace5183b77798b2be89e.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ダイアログオブジェクト作成
dialog = QDialog()

# ウィンドウタイトルを変更
dialog.setWindowTitle('My Dialog')

# ウィンドウサイズの変更
dialog.resize(300, 200)

# ウィンドウの表示位置
dialog.move(100, 200)

# ダイアログの表示
dialog.show()

# アプリケーションメインループ開始
app.exec()
```

### モーダルウィンドウ：QDialog.exec()
`QDialog` は独自で `exec_()` 関数を持っており、単体でもアプリケーションの起動が出来る。この方法で起動する事で `モーダルウィンドウ` として振舞うようだ。将来的に自分でダイアログとして表示させる際に知っておいた方がいい機能。

**参考：**

- [PySide6.QtWidgets.QDialog.exec()](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QDialog.html#PySide6.QtWidgets.PySide6.QtWidgets.QDialog.exec_)
- [モーダルウィンドウ](https://wa3.i-3-i.info/word11432.html)

Example : `show()` と `app.exec()` を省略

![](https://i.gyazo.com/dc9fb8cb5da7204a2eb20c726b46c895.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ダイアログオブジェクト作成
dialog = QDialog()

# ウィンドウタイトルを変更
dialog.setWindowTitle('My Dialog')

# ウィンドウサイズの変更
dialog.resize(300, 200)

# ダイアログでメインループ開始
dialog.exec()
```

戻り値を受け取れる。ダイアログから値を取得する際などに大事な仕様。

```Python
# ダイアログでメインループ開始
result = dialog.exec()
print(result)

# Result:
# 0
```

### モーダルウィンドウの重要性
ユーザーに必ず何かしらの情報を入力して欲しい際は、モーダルウィンドウとしてダイアログを表示する必要がある。

![](https://i.gyazo.com/201f19745395042f09ea399c5ee7f48f.png)

### QDailogからの派生ダイアログ
QDialogから派生する様々な種類のダイアログがあるようだ。

**引用：** [PySide6 QDialog](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QDialog.html)
![](https://i.gyazo.com/492c8f0bac409df65e9fbf8967bdede7.jpg)




<a id="qmainwindow"></a>

### 7.2 QMainWindow
先ほどの `QDialog` と表示は全く同じだが、`QMainWindow` は `メニューバー` や `ステータスバー` を使えるようだ。

![](https://i.gyazo.com/0aae8bd03f9657f2734c4e8fb4d067e2.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
window = QMainWindow()

# ウィンドウタイトルを変更
window.setWindowTitle('Main Window')

# ウィンドウサイズの変更
window.resize(300, 200)

# ウィジェットの表示
window.show()

# アプリケーションメインループ開始
app.exec()
```

### QMainWindowにメニューやステータスバーを追加
- [関連：QMainWindow](https://yamagishi-2bit.blogspot.com/2021/11/PySide6-qmainwindow-vfx.html)


`QtDesigner` で `QMainWindow` を選択するとデフォルトでメニューやステータスバーが追加されているが、コードでフルスクラッチする場合は少し定義が多くなる。

![](https://i.gyazo.com/1da326108a048cd96121a7922a3bf43c.png)

Example1 : 説明用にメニューやステータスバーを実装
```Python
import sys

from PySide6.QtGui import (
    QKeySequence
)

from PySide6.QtWidgets import (
    QApplication, QAction, QMainWindow,
    QMenu, QMenuBar, QStatusBar,
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィンドウオブジェクト作成
window = QMainWindow()


#--------------------------#
# メニューバーの作成
#--------------------------#
"""
 * QMainWindow.menuBar()でもメニューバーを作成出来る。

menubar = window.menuBar()
"""
menubar = QMenuBar()
window.setMenuBar(menubar)

# ファイルメニューの作成
menu_file = QMenu('File')
menubar.addAction(menu_file.menuAction())

# # ファイルメニュー内にアクションを追加
action = QAction('Exit')
action.setShortcut(QKeySequence('Ctrl+Q'))
action.triggered.connect(window.close)
menu_file.addAction(action)


#--------------------------#
# ステータスバーの作成
#--------------------------#
"""
 * QMainWindow.statuBar()でもステータスバーを作成出来る。

statusbar = window.statusBar()
"""
statusbar = QStatusBar(window)
window.setStatusBar(statusbar)
statusbar.showMessage('Status Bar') 
# メッセージの表示時間。timeout: int=0 (ms)
# statusbar.showMessage('Status Bar', 5000) 


#--------------------------#
# ウィンドウ作成
#--------------------------#
# ウィンドウタイトルを変更
window.setWindowTitle('Main Window')

# ウィンドウサイズの変更
window.resize(300, 200)

# ウィンドウの表示
window.show()

# アプリケーションメインループ開始
app.exec()
```

----

Example2: QMainWindow.menuBar()、QMainWindow.statsuBar()を用いた場合。

- Example1と結果は同じ
- `window.setMenuBar(menubar)`、`window.setStatusBar(statusbar)` などが省略可

```Python
import sys

from PySide6.QtGui import (
    QKeySequence
)

from PySide6.QtWidgets import (
    QApplication, QAction, QMainWindow,
    QMenu, QMenuBar, QStatusBar,
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィンドウオブジェクト作成
window = QMainWindow()


#--------------------------#
# メニューバーの作成
#--------------------------#
# menubar = QMenuBar()
# window.setMenuBar(menubar)

# QMainWindow.menuBar()でメニューバー作成
menubar = window.menuBar()

# ファイルメニューの作成
menu_file = QMenu('File')
# メニューバーにファイルメニュー追加
menubar.addAction(menu_file.menuAction())

# # ファイルメニュー内にアクションを追加
action = QAction('Exit')
action.setShortcut(QKeySequence('Ctrl+Q'))
action.triggered.connect(window.close)
menu_file.addAction(action)


#--------------------------#
# ステータスバーの作成
#--------------------------#
# statusbar = QStatusBar(window)
# window.setStatusBar(statusbar)

# QMainWindow.statsuBar()でステータスバー作成
statusbar = window.statusBar()


statusbar.showMessage('Status Bar') 
# statusbar.showMessage('Status Bar', 5000) # timeout: int=0 (ms)

# ウィンドウタイトルを変更
window.setWindowTitle('Main Window')

# ウィンドウサイズの変更
window.resize(300, 200)

# ウィンドウの表示
window.show()

# アプリケーションメインループ開始
app.exec()
```

---


<a id="qwidget"></a>

### QWidget
- 全てのWidgetのベース。これをベースに様々なWidgetに派生している。
- 後述する **parentの指定によって挙動が変わる。**
  - parentを指定しないと `Window` として起動
  - parentを指定すると `パーツ(Widget)` として配置
- **PySideでは `parent` を意識する事はとても大事**
- Mayaなどで `QDialog` や `QMainWindow` 以外の `Window用ではないWidget` にMayaのメイン画面を parent すると Mayaのメイン画面に配置されてしまう場合がある。

引用元：[PySide6 QWidget](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QWidget.html)
- `QMainWindow` や `QDialog` も `QWidget`　の派生クラスである事が分かる。

![](https://i.gyazo.com/5933fec47f762bf1ed072e628cf320b9.png)

**Example1: QWidgetをWindowで表示**

![image](https://i.gyazo.com/c75f1fe1b0a38f4f5444fd3236542086.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = QWidget()

# ウィンドウタイトルを変更
view.setWindowTitle('Main Window')

# ウィンドウサイズの変更
view.resize(300, 200)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()
```

**Example2 : QPushButtonをWindowとして表示**

![image](https://i.gyazo.com/a2c06c60df8eff1ebe16ce53e64b7aaa.png)


```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = QPushButton('Push')

# ウィンドウタイトルを変更
view.setWindowTitle('Main Window')

# ウィンドウサイズの変更
view.resize(300, 200)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()
```

**Example3 : 一般的なWidgetにMayaのメイン画面をparentした場合**

Mayaのメイン画面にボタンが配置され合体する。

![iamge](https://i.gyazo.com/85ea333f015ab2a69948d20d0aa41ebd.jpg)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget
)

from maya import OpenMayaUI as omui 
from shiboken2 import wrapInstance

# QPushButtonを作成
view = QPushButton('Push')

# ウィンドウサイズの変更
view.resize(300, 200)

# Mayaのメインウィンドウ取得
maya_main_window_ptr = omui.MQtUtil.mainWindow()
maya_main_window = wrapInstance(int(maya_main_window_ptr), QWidget) 

# Mayaのメインウィンドウをボタンのparentにセット
view.setParent(maya_main_window)

# ウィジェットの表示
view.show()
```

<a id="qwidget"></a>

### 7.4 その他Widgetの種類
- `PySide6.QtWidgets` のリファレンスを確認
  - めちゃくちゃある 公式：[PySide6.QtWidgets](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/index.html)
- QtDesignerで確認
  - 代表的なWidgetが左の `ウィジェットボックス` に配置さえてるので分かりやすい。
  - クラス名は配置した後、右側のプロパティなどで確認。

    ![](https://i.gyazo.com/db0d64af9c8085722dc674130f3b066d.png)



<a id="customize_basic"></a>

# 8. PySideのクラスカスタマイズ基本

### 基本形
- 特定の `Widgetのクラス` を継承し拡張するやり方が基本

Example: QWidgetクラスのカスタマイズ

![image](https://i.gyazo.com/416864341facd0c3b376ae18aa2be73f.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    # __init__関数。parent=Noneはテンプレート
    def __init__(self, parent=None):

        # parentを継承元に渡すようにする。
        super().__init__(parent)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = MyWidget()

# ウィンドウタイトルを変更
view.setWindowTitle('MyWidget')

# ウィンドウサイズの変更
view.resize(300, 200)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()
```

### Widgetの設定をクラス内に移動
- 処理する場所をクラス内に移動した。結果は同じ。運用方法によってどこで設定するのが適切か？は変わってくると思う。
- Widgetで使える関数は「[公式リファレンス:QWidget](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QWidget.html)」などを参照
- 派生したクラスでさらに関数が拡張され、使える関数は滅茶苦茶沢山ある。

![image](https://i.gyazo.com/416864341facd0c3b376ae18aa2be73f.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ウィンドウタイトルの設定
        self.setWindowTitle('MyWidget')
        
        # ウィンドウサイズの変更
        self.resize(300, 200)

        # ウィンドウの表示位置
        self.move(100, 200)

        # ウィジェット表示も内包可能
        self.show()


app = QApplication(sys.argv)
view = MyWidget()
app.exec()
```

### 基本的にはどのクラスを継承しても構文は同じ
Example : QDialogの場合

![image](https://i.gyazo.com/416864341facd0c3b376ae18aa2be73f.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ウィンドウタイトルの設定
        self.setWindowTitle('MyWidget')

        # ウィンドウの表示位置
        self.move(100, 200)
        
        # ウィンドウサイズの変更
        self.resize(300, 200)


app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()
```

基底クラスを `QDialog` に変更しただけ

![](https://i.gyazo.com/f616bf0c73fe38bdee852b91d05337d2.png)


### QPushButtonの場合

![](https://i.gyazo.com/a2160eacc08b7d8e6184756e94c2d363.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton
)

# QPushButtonクラスを継承してカスタムクラスを作成
class MyWidget(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ウィンドウタイトルの設定
        self.setWindowTitle('MyWidget')
        
        # ウィンドウサイズの変更
        self.resize(300, 200)


app = QApplication(sys.argv)
# QPushButtonの第一引数はボタンラベル名
view = MyWidget('Push')
view.show()
app.exec()
```



<a id="customize"></a>

# 9. Widgetのカスタマイズ
- `QWidget`をベースにすると **用途が明確では無い** ので汎用性が高い。
- 例えば `QDialog` や `QMainWindow` をベースにした場合は `ウィンドウ用` が確定する。

### QWidgetを拡張してボタンを配置してみる。
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget,
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ボタンを作成作成
        self.button = QPushButton('Push')
        
        self.setWindowTitle('MyWidget')
        self.resize(300, 200)


app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()
```
ボタンオブジェクトを作成してみたが何も表示されない。

![image](https://i.gyazo.com/2799dfec90067f4eaaaa9246ede405bd.png)


### Widgetはparentを設定しないとWindow。parentを指定するとパーツ。
- `QPushButton.show()` をするとButtonも別Windowとして表示される。
- `QPushButton` などの 多くのWidgetは `QWidgetの派生クラス` なので、基本的に **`QWidget`の特徴を継承** しているようだ。

![image](https://i.gyazo.com/2d74dacf2e7ca185eeb54bbaa903e27c.png)


### parentを指定してみる
[PySide6 : QPushButtonのリファレンス](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QPushButton.html) を見てみると最後の引数が `parent` のようだ。
![image](https://i.gyazo.com/9afdd20d353519ab543dc59d9acc438e.png)

`parent` としてベースのQWidgetを指定してみる。今度はWidget内にパーツとして配置された。殆どの**Widgetはオブジェクト作成の際の最後の引数が `parent` となっている**ようだ。

![image](https://i.gyazo.com/89fc50a452127d7c963d206cd7179110.png)

`デフォルト引数` なので明示的に書くことも。

```Python
QPushButton('Push', parent=self)
```


### Widgetの配置：setGeometry(x, y, width, height)
Widgetのレイアウトは `QWidget.setGeometry(x: int, y:int, w: int, h: int)` で出来る。

![image](https://i.gyazo.com/f83efdfa4716789da7c1f5f17a516077.png)

QtDesignerなら、レイアウトを簡単に出来るが・・・
![image](https://i.gyazo.com/5a6bb2436206eb0c867ecf07dc1a25a1.png)




<a id="qlayout"></a>

# 10.QLayout
数値でレイアウトするのは大変なので、レイアウトは基本的に `QLayout` を使う。

QLayoutは

- **水平レイアウト：** QHBoxLayout
- **垂直レイアウト：** QVBoxLayout
- **グリッドレイアウト：** QGridLayout

などがある。

### Widgetのメインレイアウトを設定：QWidget.setLayout
- **特徴：** Widgetはメインのレイアウトを持っている。


QtDesignerだと図の部分

![](https://i.gyazo.com/64ea713fd81b1a829056ea52327fcd3f.png)


**Example: QLayout**

![image](https://i.gyazo.com/2e89fe2e0f0e42ee1208215b5f44d42b.png)

- `QWidget.layout()` というWidgetのメインレイアウト取得用の関数があるため、アトリビュート名の重複に注意。
- `self.layout` という名前を使うと元の関数をオーバーライドしてしまう。(VSCodeなどでは既存の関数は `黄色` 等で表示)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        setLayoutでparentの定義もされるので引数のselfを省略しても問題ない。
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        """

        # 縦レイアウトを作成
        self.main_layout = QVBoxLayout(self)
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)

        """
        Qlayout.addWidget()の際に自動でparentがセットされるので
        self.button_1 = QPushButton('Button1')
        のように、layoutに配置する場合はparentの記述を省略可。
        """
        # ボタンを作成
        self.button_1 = QPushButton('Button1', self)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button_1)


        # ボタン2を作成
        self.button_2 = QPushButton('Button2', self)
        self.main_layout.addWidget(self.button_2)

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)


app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()
```

### QHBoxLayoutの場合
![image](https://i.gyazo.com/ab1df78b7604329b374b9940330f8f1e.png)


### ボタンのサイズの変更
![image](https://i.gyazo.com/86a18e4d62e7a4b28a26597dc3a3e977.png)


`QLayout` を使った場合、Widgetの配置やサイズは自動で調整されるため、大きさを変更したい場合は

- QtWidget.setMinimumSize(w: int, h: int)
  - QtWidget.setMinimumWidth(w: int)
  - QtWidget.setMinimumheight(h: int)
- QtWidget.setMaximumSize(w: int, h: int)
  - QtWidget.setMaximumWidth(w: int)
  - QtWidget.setMaximumHeight(h: int)
- QtWidget.setFixedSize(w: int, h: int)
  - QtWidget.setFixedWidth(w: int)
  - QtWidget.setFixedHeight(h: int)

など使うと楽。

![](https://i.gyazo.com/ec312cd5b2af45c69ec8189d8030da6e.png)


```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        setLayoutでparentの定義もされるので引数のselfを省略しても問題ない。
        self.main_layout = QVBoxLayout()
        """
        # 縦レイアウトを作成
        self.main_layout = QVBoxLayout(self)
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        self.button_1 = QPushButton('Button1', self)
        # 固定サイズを設定
        self.button_1.setFixedSize(200, 50)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button_1)


        # ボタン2を作成
        self.button_2 = QPushButton('Button2', self)
        # 最大幅設定
        self.button_2.setMaximumWidth(100)
        self.main_layout.addWidget(self.button_2)

        self.setWindowTitle('MyWidget')

        # ウィンドウサイズを固定したい場合。
        self.setFixedSize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()
```


### setLayoutの省略
`QLayout` の引数 `parent` に `MyWidgetクラス(self)` を指定すれば、setLayout()の処理を省略出来たりも。


![image](https://i.gyazo.com/47ae662277a07fdfe3fb2106259b571f.png)


### 位置合わせ
レイアウトの`setAlignment` を使う。

- `QLayout.setAlignment( <Qt.AlignmentFlag> )`

![image](https://i.gyazo.com/602af1f14406d266fbe2f40de1784d1f.png)


参考：[QtCore.Qt.AlignmentFlag](https://doc.qt.io/qtforpython-5/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag)

- `QtCore.Qt.AlignCenter`
- `QtCore.Qt.AlignTop`
- `QtCore.Qt.AlignLeft`
- `QtCore.Qt.AlignRight`

など。



### Layoutを組み合わせる
Layoutは `QLayout.addLayout( <QLayout> )` でレイアウトも追加出来る。これを使う事でレイアウトの自由度が高くなる。

![](https://i.gyazo.com/48f6a097a56e1d0877f11640d7da24ad.png)

Example:
```Python
import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # --- メインレイアウト -----------------------------#
        # メインレイアウトを作成
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        self.button = QPushButton('Button1', self)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button)


        # --- 追加レイアウト_1 -----------------------------#
        # レイアウト1を作成
        self.layout_1 = QHBoxLayout()

        # ラベルを作成しレイアウト１に登録
        self.label = QLabel('Name:')
        self.layout_1.addWidget(self.label)

        # ラインエディットを作成しレイアウト１に登録
        self.lineedit = QLineEdit(self)
        self.lineedit.setMinimumWidth(100)
        self.layout_1.addWidget(self.lineedit)

        # ボタンsetを作成しレイアウト１に登録
        self.button_set = QPushButton('Set', self)
        self.layout_1.addWidget(self.button_set)

        # レイアウト１をメインレイアウトにセット
        self.main_layout.addLayout(self.layout_1)


        # --- Windowの設定 --------------------------------#
        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()
```




<a id="signal"></a>

# 11. シグナルの設定
PySideでUIを操作した際の処理を定義するためには `signal` を使うのが基本のようだ。

### テスト用スクリプト
![image](https://i.gyazo.com/dc774050a6a1be7a7f5993b3e149819e.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        self.button = QPushButton('Push', self)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### QLineEditのシグナルを調べる
リファレンスを見てQLineEditの持つシグナルを調べる

参考：[PySide6 QLineEdit Signals](https://doc.qt.io/qtforpython-5/PySide6/QtWidgets/QLineEdit.html#signals)

![](https://i.gyazo.com/096f47ccbf6a79905480a14da6aed36a.png)

`textChanged`、`textEdited` など文字情報が変わった際に処理されるシグナルを使ってみようと思う。が、意味が同じに感じる。

リファレンスを見る。説明が何もない。

![](https://i.gyazo.com/d2a9a07cd194b82b5b35543682943b3c.png)

こういう時は本家のQtのリファレンスを見る。

**参考:** [Qt5 LineEdit](https://doc.qt.io/qt-6/qlineedit.html#textChanged)

![](https://i.gyazo.com/cf0768026f345d6ec86f22a6dc094ed7.png)

- **textChanged**
  - `文字` が変更した際に呼び出される。`setText()` などプログラム的に変更がされても実行される。
- **textEdit**
  - ユーザーが編集した際のみに呼び出される。

とても大きな違いがあるようだ。ここでは `textEdit` を使ってみる。

### シグナルの接続と接続先の関数（スロット）を準備する。

文字を入力する度にコンソールに関数の実行結果が表示される。

![image](https://i.gyazo.com/776f246594093ff14da3796e4efda5d0.png)

Example:
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラインエディットを作成
        self.line_edit = QLineEdit(self)
        # ラインエディットの文字を編集した際のシグナルを定義
        self.line_edit.textEdited.connect(self.line_edit_edited)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        self.button = QPushButton('Push', self)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')

    # ラインエディットの文字を編集した際に呼び出される関数
    def line_edit_edited(self):
        print('Test')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### シグナルのconnect先は関数を指定する
PySideの用語で `Signal（シグナル）` の接続先は `Slot（スロット）` と呼ばれるようだ。

![image](https://i.gyazo.com/48ec67c13608cd0bd6f873a7c0c3e651.png)


### 関数の実行結果ではなく、関数そのものを引数にする。
最初少し困惑したがPythonは変数などに関数そのものを設定出来る。
- `関数名()` ：関数の実行結果
- `関数名`  : 関数そのもの

Example:
```Python
test = print
print(test) 
test('Test')
```
Result:
```
<built-in function print>
Test
```


### シグナルに引数が設定されている場合がある
- Signalに必要な引数ではなく、スロット側で受け取る事が出来る引数。
- 詳しくはリファレンス参照。

![image](https://i.gyazo.com/6a041ff728f88c2329f4de85b42c89f3.png)

面倒なので、とりあえずスロット用関数を作って中身を見てみた。入力した文字列を受け取れるようだ。

![](https://i.gyazo.com/28124dc9aa533c60caaa71a06d998711.png)


```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        # シグナルをスロットに接続
        self.line_edit.textEdited.connect(self.line_edit_edited)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        self.button = QPushButton('Push', self)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')

    # シグナルの接続先関数
    def line_edit_edited(self, arg):
        """ line_edit.textEdited

         * ここにLineEditが編集された際の処理を定義
        
        """
        
        print(type(arg))
        print(arg)

        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```



### ボタンが押されたらLineEditをクリアするようにしてみた
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        # シグナルをスロットに接続
        self.line_edit.textEdited.connect(self.line_edit_edited)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        """
        QPushButtonもLineEditと同じように
            * QPushButton.clicked: ショートカットキーの入力などを含むクリック
            * QPushButton.pressed: ボタンが押されたとき。
        という似たようなシグナルがある。

        """
        self.button = QPushButton('Push', self)
        self.button.clicked.connect(self.button_clicked)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')

    
    def line_edit_edited(self, arg):
        """ line_edit.textEdited
        ラインエディットを編集した際のスロット

         * ここにLineEditが編集された際の処理を記述
        
        """

        print(type(arg))
        print(arg)

    
    def button_clicked(self):
        """ 
        ボタンを押した時のスロット

         * ここにボタンが押された際の処理を記述
        
        """

        self.line_edit.setText('')

        
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### Tips:Lambdaでもスロットを定義出来る
無記名関数をスロットとして定義出来る。知っておくと何かの時に役立つテクニック。
- 繰り返しになるが、signalの接続は関数の実行結果ではなく関数そのもの。
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        # シグナルに無記名関数を渡す
        self.line_edit.textEdited.connect(lambda: print('Test'))
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        self.button = QPushButton('Push', self)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### Lambdaで引数を変えて関数をラップ - 失敗例
- 変数 `name` が最後の評価になってしまい、全部の出力が　`C`。
- Python3で `lambda` の仕様の変更があった影響か？以前動いていたコードが上手く動作しなくなっている。

以前の対応例：現在は上手く動作しない
```Python
self.button_b.clicked.connect(lambda x=name: self.button_pressed(x))
```

Examples:
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        name = 'A'
        self.button_a = QPushButton(name, self)
        self.button_a.clicked.connect(lambda: self.button_pressed(name))
        self.main_layout.addWidget(self.button_a)

        name = 'B'
        self.button_b = QPushButton(name, self)
        self.button_b.clicked.connect(lambda: self.button_pressed(name))
        self.main_layout.addWidget(self.button_b)

        name = 'C'
        self.button_c = QPushButton(name, self)
        self.button_c.clicked.connect(lambda: self.button_pressed(name))
        self.main_layout.addWidget(self.button_c)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### 望んだ動作をするLambda式の書き方
```Python
lambda func=self.button_pressed, value=name: func(value)
```
Example:
```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        name = 'A'
        self.button_a = QPushButton(name, self)
        self.button_a.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value)
            )
        self.main_layout.addWidget(self.button_a)

        name = 'B'
        self.button_b = QPushButton(name, self)
        self.button_b.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value)
            )
        self.main_layout.addWidget(self.button_b)

        name = 'C'
        self.button_c = QPushButton(name, self)
        self.button_c.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value)
            )
        self.main_layout.addWidget(self.button_c)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### Tips : functools.partial を使う方法もあるらしい
参考 : [Lambda or partial as slot](https://forum.qt.io/topic/121647/lambda-or-partial-as-slot)

- 推奨される方法かどうか？は不明

```Python
import functools
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        name = 'A'
        self.button_a = QPushButton(name, self)
        self.button_a.clicked.connect(
                functools.partial(self.button_pressed, name)
            )
        self.main_layout.addWidget(self.button_a)

        name = 'B'
        self.button_b = QPushButton(name, self)
        self.button_b.clicked.connect(
                functools.partial(self.button_pressed, name)
            )
        self.main_layout.addWidget(self.button_b)

        name = 'C'
        self.button_c = QPushButton(name, self)
        self.button_c.clicked.connect(
                functools.partial(self.button_pressed, name)
            )
        self.main_layout.addWidget(self.button_c)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```

### forループなどでボタンを作ってみたり
- Lambda式でも問題なし

![image](https://i.gyazo.com/db285f2fe9ff3e0ffe507a4a7557b294.png)

```Python
import functools
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        """ ボタンを作成
        Qtではローカル変数などでWidgetがどこにも保持されない場合、Widgetは表示されない。
        * main_layout内にbuttonオブジェクトが配置される。
        * この場合は、self.button = QPushButton() など変数に格納しなくても問題ない。
        """

        button_name_list = ['A', 'B', 'C',]

        for button_name in sorted(button_name_list):
            button = QPushButton(button_name, self)
            button.clicked.connect(
                functools.partial(self.button_pressed, button_name)
            )

            self.main_layout.addWidget(button)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()
```


### Tips：PySide6ではスロット用のデコレータのワークフローがある。
慣れてきたら。

  - [参考：Qt for Python Signals and Slots](https://wiki.qt.io/Qt_for_Python_Signals_and_Slots)



<a id="gui"></a>

# 11. 作成したWidgetをDialogやMainWindowに配置
- **用途を限定したくない** 場合はGUIのデザインは `QWidget` を基本にしておくと便利。
- `QDialog` や `QMainWindow` は用途が明確。
  - **QDialog :** 常にWindow。ダイアログとしての機能を拡張できる。
  - **QMainWindow :** 常にWindow。メニューバーやステータスバーを使える。

----

### 11.1 基底クラスを変更する
- 先ほどのコードの基底クラスを `QDialog` や `QMainWinodw` に書き換えても全く同じWindowを表示出来る。

![image](https://gyazo.com/c9db1b240a5a0d8a97f0daf1651bd06b.png)

Example: 基底クラスを`QDialog`に変更した場合

赤線の部分のみ変更した。

![image](https://i.gyazo.com/4e71cd71766ea709f5d9cdbafab05873.png)


----

### 11.2 ダイアログに配置して表示
![iamge](https://i.gyazo.com/38ef3aeaa7aa4d43eb683db33e64ea5c.png)

- MyWidget部分は先ほどのコードを使うので、ここではQDialog部分のコードのみ掲載。

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QDialog,
    QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        ・・・
        ＜略＞
        ・・・


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.widget = MyWidget(self)
        self.main_layout.addWidget(self.widget)

        self.setWindowTitle(self.__class__.__name__)
        self.resize(300, 200)


app = QApplication(sys.argv)
dialog = MyDialog()
result = dialog.exec()

"""
ダイアログだが普通のWindowとして表示したい場合

app = QApplication(sys.argv)
dialog = MyDialog()
dialog.show()
app.exec()
"""
```


#### MyWidegtをパーツとして好きな所にどんどん追加出来る。
![image](https://gyazo.com/6430e478906db44da0080ab01afa5e3a.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QDialog,
    QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    ・・・・
    <省略>
    ・・・・

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # MyWdiget_1
        self.widget_1 = MyWidget(self)
        self.main_layout.addWidget(self.widget_1)

        # MyWdiget_2
        self.widget_2 = MyWidget(self)
        self.main_layout.addWidget(self.widget_2)

        self.setWindowTitle(self.__class__.__name__)
        self.resize(300, 200)

app = QApplication(sys.argv)
dialog = MyDialog()
result = dialog.exec()
```

#### ダイアログの使い方など
- 今回のコードではQDialogである意味は全くないが、「ダイアログとして使いたい」「入力した情報を取得したい」等の場合に意味が出てくる。
- 「OK」などのボタンを実装したり。

参考：

- 参考：DF TALK [祝PySide6デビュー！ ～ただひたすらウィジェットを紹介するページ～](https://dftalk.jp/?p=20768)
- 関連：[QDialog](https://yamagishi-2bit.blogspot.com/2021/11/updated20211126-yamagishi.html)

----

### 11.3 メインウィンドウとして表示
QMainWindowのメインとなるエリアは `CentralWidget` と呼ばれる。何かエヴァっぽくてかっこいいすね。

![image](https://i.gyazo.com/df9290b8388021fefe257c502ea5ca38.png)

Example:

![image](https://i.gyazo.com/38ef3aeaa7aa4d43eb683db33e64ea5c.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    ・・・・
    <省略>
    ・・・・    

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        
        self.widget = MyWidget(self)
        self.setCentralWidget(self.widget)

        self.setWindowTitle(self.__class__.__name__)
        self.resize(300, 200)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
```

<a id="examples"></a>

# PySide6 Examples：


### 有効/無効
`QWidget.setDisabled(<Bool>)`

```Python
text_edit = QTextEdit(self)
text_edit.setPlainText('Test')
text_edit.setDisabled(True)
```

![image](https://i.gyazo.com/2191dea64f2f0fd59912bebfd1be32b2.png)


### 非表示
```Python
line_edit.setHidden(True)
```

![image](https://gyazo.com/08451df39ced122de611a34bdf4f0b70.png)


### フォントの変更：QtGui.QFont
- `QWidget.setFont(GtGui.QFont)`

![image](https://i.gyazo.com/e3dec6fcee8a42bd02ce2b30d5c0523e.png)

```Python
from PySide6.QtGui import QFont

font = QFont('Arial Black')
# font.setFamily('Arial Black')
font.setPointSize(15)
font.setBold(True)
font.setItalic(True)


label = QLabel('Test')
label.setFont(font)
```

### フォント一覧：QFontComboBox
![image](https://i.gyazo.com/0b4521b8a8c1bff56a1efb9be9211fe6.png)

```Python
font_combobox =  QFontComboBox(self)

# QFont取得
font = font_combobox.currentFont()
```

### 文字の色の変更
![image](https://i.gyazo.com/94c7962f0e37be2746e083c97229c78d.png)

- `StyleSheet` というものがあり、その指定で色などデザインを定義する。CoreのQtに依存するためか？文字列で定義する事が多く、地味に面倒・・・。
- Widgetの種類などによって色の設定の手法がいくつか存在しており、調べるのが地味に大変・・・。
  - setBackGroundだったり、setStyleだったり、setStyleSheetだったり・・・。


```Python
""" スタイルシートの色指定方法色々
# 色名
# style_sheet = 'QLabel { color : red;}'

# 16進数
# style_sheet = 'QLabel { color : #ff0000;}'

# 8bit RGB
style_sheet = 'QLabel { color : rgb(255, 0, 0)}'
"""

style_sheet = 'QLabel { color : red;}'

# QLabel作成
label = QLabel('Test')
label.setStyleSheet(style_sheet)
```

### 背景色
![image](https://i.gyazo.com/58819857afafa92c16f0688719d8ad9c.png)

```Python
line_edit = QLineEdit('Test')
style = 'background-color: rgb(200, 50, 50);'
line_edit.setStyleSheet(style)
```


関連：[ウィジェットの背景色を変えてみる](https://yamagishi-2bit.blogspot.com/2021/09/PySide6-stylesheet.html)

### Widgetの背景を透明に

![](https://i.gyazo.com/491a787cb0318afbd972f1a2a735fd0c.png)

```Python
self.status = QtWidgets.QLabel('Status : -')
self.status.setAttribute(QtCore.Qt.WA_TranslucentBackground)
```

### QPushButtonの文字の位置合わせ
`setStyleSheet` を使うらしい。

![](https://i.gyazo.com/e552d98b36d55bd39cdf1701aa154fbf.png)

```Python
self.button = QtWidgets.QPushButton(self.path.name)
self.button.setFixedSize(200, 25)
self.button.setStyleSheet("QPushButton { text-align: left; }")
```

### QListWidget
![image](https://i.gyazo.com/0b880e6a3f84e59f12dcbd57e72be14b.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidget,
    QPushButton, QVBoxLayout,
)

ITEMS = ['CharaA', 'CharaB', 'CharaC', 'CharaD',]

class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)


        # ボタン作成
        self.button = QPushButton('Clear')


        # ListWidget作成
        self.list = QListWidget()
        # Item追加
        self.list.addItems(ITEMS)
        # ソート機能
        self.list.setSortingEnabled(True)
        # 隔行で色変更
        self.list.setAlternatingRowColors(True)


        # シグナル設定
        self.list.itemClicked.connect(self.list_activated)
        self.button.clicked.connect(self.button_clicked)


        # レイアウト
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.list)


    def list_activated(self, item):
        if item:
            print(item.text())


    def button_clicked(self):
        self.list.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyWidget()
    view.resize(150, 200)
    view.show()
    app.exec()
```

### QSplitter
![image](https://i.gyazo.com/9c8fbdfa9dbd7abd2f36f348bb4dfe34.png)
```Python
import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidget,
    QPushButton, QSplitter, QWidget, QVBoxLayout,
)

class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout(self)
        # レイアウトの周囲の余白を無しに
        self.main_layout.setContentsMargins(0, 0, 0, 0)


        # スプリッター作成/水平分割
        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)


        # 左側用ウィジェット
        self.widget_1 = QListWidget()


        # 右側用ウィジェット
        self.widget_2 = QWidget()
        self.layout_2 = QVBoxLayout(self.widget_2)

        self.button_1 = QPushButton('Button 1')
        self.button_2 = QPushButton('Button 2')
        self.button_3 = QPushButton('Button 3')

        # ウィジェットセット
        self.layout_2.addWidget(self.button_1)
        self.layout_2.addWidget(self.button_2)
        self.layout_2.addWidget(self.button_3)

        # スプリッターセット
        self.splitter.addWidget(self.widget_1)
        self.splitter.addWidget(self.widget_2)
        self.splitter.setSizes([244, 151])
        self.main_layout.addWidget(self.splitter)


        # シグナル
        self.splitter.splitterMoved.connect(
            lambda: self.splitter_moved(self.splitter)
        )


    def splitter_moved(self, splitter):
        print(splitter.sizes())


    """ 
    lambda使わない場合
        # シグナル
        self.splitter.splitterMoved.connect(self.splitter_moved)

    def splitter_moved(self):
        print(self.splitter.sizes())
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyWidget()
    view.resize(400, 200)
    view.show()
    app.exec()
```

### 手っ取り早くダークスタイルに
- PyPi: [QDarkStyle](https://pypi.org/project/QDarkStyle/)
  - Python3.10、PySide6には未対応のようだ（2022/06/25）

![image](https://i.gyazo.com/e2956a9c1377612caa2ea5a24510d942.png)

```Python
import sys

from PySide6.QtWidgets import (
    QApplication, QTextEdit, QVBoxLayout, QWidget
)

import qdarkstyle

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText('Test')
        self.main_layout.addWidget(self.text_edit)

        self.setWindowTitle('MyWidget')
        self.resize(300, 120)

app = QApplication(sys.argv)

# Set DarkStyel StyelSheet
dark_stylesheet = qdarkstyle.load_stylesheet_PySide6()
app.setStyleSheet(dark_stylesheet)

view = MyWidget()
view.show()

app.exec()
```

## Tips
- Python2用のPySide6の公式ビルドは存在しないと思うのでPython2にPySide6はインストール出来ないと思う。
- 一部VFXツールではツールのPython2用のPySide6ビルドが内包されていて、`Python2+PySide6` という特殊な環境が存在している。
- VSCodeで`jpynb`
    - なんと、JupyterNoteやJupyterLabのファイルはVSCode対応していて、普通に実行や編集が出来る。
    ![](https://i.gyazo.com/bf46de0ea8c982e7642c9c771e0a4358.png)

## 関連：
- [VFXのためのPySideまとめ](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html)