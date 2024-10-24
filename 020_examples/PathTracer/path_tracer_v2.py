#=========================================================#
# Reference From:
# https://raytracing.xyz/
# https://www.pythonguis.com/tutorials/bitmap-graphics/
# 
# Python 3.7.9 & PySide6
# Coding by Tatsuya Yamagishi
# Updated : DEC 14 2021
# Created : DEC 10 2021
#=========================================================#

import dataclasses
import math
import os
import random
import sys
import time

from perlin_noise import PerlinNoise
from PySide6 import QtCore, QtGui, QtWidgets

@dataclasses.dataclass
class Info:
    name: str = 'Y-Ray'
    version: str = 'v2.1.0'
    width: int = 400
    height: int = 200
    viewColor: QtGui.QColor = QtGui.QColor('Blue')
    refresh: int = 200

    _NO_HIT: float = float('inf')
    _EPSILON: float = 0.001
    _DEPTH_MAX: int = 10
    _VACUUM_REFRACTIVE_INDEX: float = 1.0
    _SAMPLES: int = 4
    _DISPLAY_GAMMA: float = 2.2

    @classmethod
    def NO_HIT(cls):
        return cls._NO_HIT

    @classmethod
    def EPSILON(cls):
        return cls._EPSILON

    @classmethod
    def DEPTH_MAX(cls):
        return cls._DEPTH_MAX

    @classmethod
    def VACUUM_REFRACTIVE_INDEX(cls):
        return cls._VACUUM_REFRACTIVE_INDEX

    @classmethod
    def SAMPLES(cls):
        return cls._SAMPLES

    @classmethod
    def DISPLAY_GAMMA(cls):
        return cls._DISPLAY_GAMMA

#=========================================================#
# Class
#=========================================================#
@dataclasses.dataclass
class Vec:
    x: float
    y: float
    z: float

    def add(self, v):
        return Vec(self.x + v.x, self.y + v.y, self.z + v.z)

    def add(self, v):
        return Vec(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def sub(self, v):
        return Vec(self.x - v.x, self.y - v.y, self.z - v.z)
    
    def scale(self, s):
        return Vec(self.x * s, self.y * s, self.z * s)
    
    def neg(self):
        return Vec(-self.x, -self.y, -self.z)
    
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def normalize(self):
        return self.scale(1.0 / self.len())
    
    def dot(self, v):
        return (self.x * v.x + self.y * v.y + self.z * v.z)
    
    def cross(self, v):
        return Vec( self.y * v.z - v.y * self.z,
                    self.z * v.x - v.z * self.x,
                    self.x * v.y - v.x * self.y)

    def reflect(self, n):
        return self.sub(n.scale(2 * self.dot(n)))

    def refract(self, n, eta: float):
        dot = self.dot(n)
        d = 1.0 - (eta**2) * (1.0 - (dot**2))
        
        if (0 < d):
            a = self.sub(n.scale(dot)).scale(eta)
            b = n.scale(math.sqrt(d))
            
            return a.sub(b)
        
        return self.reflect(n)

    def randomHemisphere(self):
        dir = Vec(0.0, 0.0, 0.0)

        for i in range(100):
            dir = Vec(
                random.uniform(-1.0, 1.0),
                random.uniform(-1.0, 1.0),
                random.uniform(-1.0, 1.0)
            )

            if (dir.len() < 1.0):
                break

        dir = dir.normalize()

        if dir.dot(self) < 0:
            dir = dir.neg()

        return dir

    def toString(self):
        return f'Vec({self.x}, {self.y}, {self.z})'

@dataclasses.dataclass
class Spectrum:
    r: float
    g: float
    b: float
  
    def add(self, v):
        return Spectrum(self.r + v.r, self.g + v.g, self.b + v.b)

    def mul(self, v):
        return Spectrum(self.r * v.r, self.g * v.g, self.b * v.b)
    
    def scale(self, s: float):
        return Spectrum(self.r * s, self.g * s, self.b * s)

    def toColor(self):
        GAMMA = Info.DISPLAY_GAMMA()
        
        ig = int(min(pow(self.g, 1.0 / GAMMA) * 255, 255))
        ib = int(min(pow(self.b, 1.0 / GAMMA) * 255, 255))
        ir = int(min(pow(self.r, 1.0 / GAMMA) * 255, 255))
        
        return (ir, ig, ib)

    @staticmethod
    def BLACK():
        return Spectrum(0, 0, 0)

    @staticmethod
    def COLOR_SKY():
        return Spectrum(0.7, 0.7, 0.7)

@dataclasses.dataclass
class Ray:
    origin: Vec
    dir: Vec

    def __init__(self, origin: Vec, dir: Vec):
        self.origin = origin.add(dir.scale(Info.EPSILON()))
        self.dir = dir.normalize()

@dataclasses.dataclass
class Material:
    diffuse: Spectrum = None
    reflective: float = 0.0
    refractive = 0 # 屈折割合
    refractiveIndex = 1 # 屈折率
    emissive = Spectrum.BLACK() # 発光色

@dataclasses.dataclass
class Light:
    pos: Vec
    power: Spectrum

@dataclasses.dataclass
class Intersection:
    t: float = Info.NO_HIT()    # 交差点までの距離
    p: Vec = None               # 交差点
    n: Vec = None               # 法線
    material: Material = None   # マテリアル

    def hit(self):
        return self.t != Info.NO_HIT()

# カメラ
@dataclasses.dataclass
class Camera:
    eye: Vec = None
    origin: Vec = None
    xaxis: Vec = None
    yaxis: Vec = None

    def lookAt(
        self, eye: Vec, target: Vec, up: Vec,
        fov: float, width:  int, height: int ):
        
        self.eye = eye
        imagePlane = (height / 2) / math.tan(fov / 2)
        v = target.sub(eye).normalize()
        self.xaxis = v.cross(up).normalize()
        self.yaxis = v.cross(self.xaxis)
        center = v.scale(imagePlane)
        self.origin = center.sub(
            self.xaxis.scale(0.5 * width)).sub(self.yaxis.scale(0.5 * height)
        )

    def ray(self, x: float, y: float):
        p = self.origin.add(self.xaxis.scale(x)).add(self.yaxis.scale(y))
        dir = p.normalize()
        return Ray(self.eye, dir)

class Intersectable:
    def intersect(self, ray: Ray):
        pass

class Sphere(Intersectable):
    def __init__(self, center: Vec, radius: float, material: Material):
        self.center   = center
        self.radius   = radius
        self.material = material

    def intersect(self, ray: Ray) -> Intersection:
        isect = Intersection()
        v = ray.origin.sub(self.center)
        b = ray.dir.dot(v)
        c = v.dot(v) - self.radius**2
        d = b * b - c
        
        if (d >= 0):
            s = math.sqrt(d)
            t = -b - s
        
            if (t <= 0):
                t = -b + s
            
            if (0 < t):
                isect.t = t
                isect.p = ray.origin.add(ray.dir.scale(t))
                isect.n = isect.p.sub(self.center).normalize()
                isect.material = self.material

        return isect

class Plane(Intersectable):
    def __init__(self, p: Vec, n: Vec, material: Material):
        self.n = n.normalize()
        self.d = -p.dot(self.n)
        self.material = material

    def intersect(self, ray):
        isect = Intersection()
        v = self.n.dot(ray.dir)
        t = -(self.n.dot(ray.origin) + self.d) / v
        
        if (0 < t):
            isect.t = t
            isect.p = ray.origin.add(ray.dir.scale(t))
            isect.n = self.n
            isect.material = self.material

        return isect

class CheckedObj(Intersectable):
    def __init__(
        self, obj: Intersectable, 
        gridWidth: float, material2: Material
    ):
        self.obj = obj
        self.gridWidth = gridWidth
        self.material2 = material2

    def intersect(self, ray: Ray):
        isect = self.obj.intersect(ray)

        if isect.hit():
            i = (   round(isect.p.x/self.gridWidth) +
                    round(isect.p.y/self.gridWidth) +
                    round(isect.p.z/self.gridWidth)
            )
            
            if (i % 2 == 0):
                isect.material = self.material2

        return isect

class TexturedObj(Intersectable):
    def __init__(self, obj: Intersectable, image: QtGui.QImage,
         size: float, origin: Vec, uDir: Vec, vDir:  Vec
    ):
        self.obj = obj
        self.image = image
        self.size = size
        self.origin = origin
        self.uDir = uDir
        self.vDir = vDir

    def intersect(self, ray: Ray):
        isect = self.obj.intersect(ray)

        if isect.hit():
            u = isect.p.sub(self.origin).dot(self.uDir) / self.size
            u = math.floor((u - math.floor(u)) * self.image.width())
            
            v = -isect.p.sub(self.origin).dot(self.vDir) / self.size
            v = math.floor((v - math.floor(v)) * self.image.height())

            c_obj = QtGui.QColor(self.image.pixel(int(u), int(v)))
            c = c_obj.getRgb()

            mtl = Material(Spectrum(c[0] / 255.0, c[1] / 255.0, c[2] / 255.0).mul(isect.material.diffuse))
            mtl.reflective = isect.material.reflective
            mtl.refractive = isect.material.refractive
            mtl.refractiveIndex = isect.material.refractiveIndex
            isect.material = mtl

        return isect

class Scene:
    def __init__(self) -> None:
        self.objList = []
        self.lightList = []

        self.skyColor = None
    #===========================================#
    # Set / Get
    #===========================================#
    def setSkyColor(self, c):
        self.skyColor = c
    
    def getSkyColor(self):
        return self.skyColor
    #===========================================#
    # Trace
    #===========================================#
    def trace(self, ray: Ray, depth: int):
        VACUUM_REFRACTIVE_INDEX = Info.VACUUM_REFRACTIVE_INDEX()

        if Info.DEPTH_MAX() < depth:
            return Spectrum.BLACK()

        isect = self.findNearestIntersection(ray)

        if not isect.hit():
            return self.getSkyColor()

        m = isect.material

        dot = isect.n.dot(ray.dir)

        if (dot < 0): # 外部から進入する場合
            col = self.interactSurface(
                ray.dir, isect.p, isect.n, m,
                VACUUM_REFRACTIVE_INDEX / m.refractiveIndex, depth)

            return col.add(m.emissive.scale(-dot))

        else: # 内部から出ていく場合
            return self.interactSurface(
                ray.dir, isect.p, isect.n.neg(), m,
                m.refractiveIndex / VACUUM_REFRACTIVE_INDEX, depth)

    #===========================================#
    # Method
    #===========================================#
    def addIntersectable(self, obj: Intersectable):
        self.objList.append(obj)
    
    def addLight(self, light: Light):
        self.lightList.append(light)

    def findNearestIntersection(self, ray: Ray):
        isect = Intersection()
        for obj in self.objList:
            tisect = obj.intersect(ray)
            
            if ( tisect.t < isect.t ):
                isect = tisect
            
        return isect

    def lighting(self, p: Vec, n: Vec, m: Material):
        L = Spectrum.BLACK()

        for light in self.lightList:
            c = self.diffuseLighting(p, n, m.diffuse, light.pos, light.power)
            L = L.add(c)

        return L

    def diffuseLighting(
            self, p: Vec,
            n: Vec,
            diffuseColor: Spectrum,
            lightPos: Vec,
            lightPower: Spectrum
        ):

        v = lightPos.sub(p)
        l = v.normalize()
        dot = n.dot(l)

        if (dot > 0):
            if (self.visible(p, lightPos)):
                r = v.len()
                factor = dot / (4 * math.pi * r * r)
                return lightPower.scale(factor).mul(diffuseColor)

        return Spectrum.BLACK()

    def visible(self, org: Vec , target: Vec ):
        v = target.sub(org).normalize()
        shadowRay = Ray(org, v)
        for obj in self.objList:
            if (obj.intersect(shadowRay).t < v.len()):
                return False

        return True

    # 交点からのレイの方向を求め追跡する
    def interactSurface(
            self, rayDir:  Vec, p: Vec ,
            n: Vec, m: Material, eta: float, depth: int):
        
        ks = m.reflective
        kt = m.refractive

        t = random.random()
        if (t < ks):                    # 鏡面反射
            r = rayDir.reflect(n);      # 反射レイを導出
            c = self.trace(Ray(p, r), depth + 1)

            return c.mul(m.diffuse)
        elif (t < ks + kt):             # 屈折
            r = rayDir.refract(n, eta)  # 屈折レイを導出
            c = self.trace(Ray(p, r), depth + 1)
            
            return c.mul(m.diffuse)
        else:                           # 拡散反射
            r = n.randomHemisphere()
            li = self.trace(Ray(p, r), depth + 1)

            fr = m.diffuse.scale(1.0 / math.pi)
            factor = 2.0 * math.pi * n.dot(r)
            l = li.mul(fr).scale(factor)

            return l
#=========================================================#
# Core
#=========================================================#
class Core:
    def __init__(self):
        self.info = Info()

        self.scene = Scene()
        self.camera = Camera()
        self.initScene()
        self.initCamera()

        self.imageTest = QtGui.QImage(r'C:\Users\ta_yamagishi\Pictures\shibuya.png')

        self.initScene()

    #===========================================#
    # InitScene
    #===========================================#
    def initCamera(self):
        self.camera.lookAt(
            Vec(3.0, 1.5, 5.0), # 視点
            Vec(0.0, 0.0, 0.0), # 注視点
            Vec(0.0, 1.0, 0.0), # 上方向
            math.radians(40.0), # 視野角
            self.width(),
            self.height()
        )

    def initScene(self):
        scene = self.scene

        # 空の色
        scene.setSkyColor(
            Spectrum(0.7, 0.75, 0.8)
        )

        # 球
        mtl1 = Material(Spectrum(0.7, 0.3, 0.9))
        scene.addIntersectable(
            Sphere(Vec(-2.2, 0, 0), 1, mtl1)
        )

        mtl2 = Material(Spectrum(0.9, 0.7, 0.3))
        mtl2.reflective = 0.8
        scene.addIntersectable(
            Sphere(Vec(0, 0, 0), 1, mtl2)
        )

        mtl3 = Material(Spectrum(0.3, 0.9, 0.7))
        mtl3.refractive = 0.8
        mtl3.refractiveIndex = 1.5
        scene.addIntersectable(
            Sphere(Vec(2.2, 0, 0), 1, mtl3)
        )

        # 光源
        mtlLight = Material(Spectrum(0.0, 0.0, 0.0))
        mtlLight.emissive = Spectrum(30.0, 20.0, 10.0)
        scene.addIntersectable(
            Sphere(Vec(0, 4.0, 0), 1, mtlLight)
        )

        # チェック柄の床
        mtlFloor1 =  Material( Spectrum(0.9, 0.9, 0.9))
        mtlFloor2 =  Material( Spectrum(0.4, 0.4, 0.4))
        scene.addIntersectable(
            CheckedObj(
                Plane(Vec(0, -1, 0), Vec(0, 1, 0), mtlFloor1),
                1,
                mtlFloor2
            )
        )
    #===========================================#
    # Set / Get
    #===========================================#
    def setWidth(self, w: int):
        self.info.width = w

    def width(self):
        return self.info.width

    def setHeight(self, h: int):
        self.info.height = h

    def height(self):
        return self.info.height

    def setSize(self, w: int, h: int):
        self.setWidth(w)
        self.setHeight(h)

    def size(self):
        return (self.width(), self.height())

    def name(self):
        return self.info.name

    def version(self):
        return self.info.version

    def viewColor(self):
        return self.info.viewColor

    def refresh(self):
        return self.info.refresh

    #=====================================#
    # Method
    #=====================================#
    def calcPixelColor(self, x, y):
        SAMPLES = Info.SAMPLES()
        sum = Spectrum.BLACK()

        for i in range(SAMPLES):
            ray = self.calcPrimaryRay(x, y)
            sum = sum.add(self.scene.trace(ray, 0))

        return sum.scale(1.0 / SAMPLES).toColor()
        
    def calcPrimaryRay(self, x, y):
        return self.camera.ray(
            x + random.uniform(-0.5, 0.5),
            y + random.uniform(-0.5, 0.5)
        )

    def intersectRaySphere(self, rayDir):
        v = self.eye.sub(self.sphereCenter)
        b = rayDir.dot(v)
        c = v.dot(v) - self.sphereRadius**2
        d = b*b-c

        if (0<=d): # 交差した場合、交点までの距離を計算
            s = math.sqrt(d)
            t = -b-s
            
            if t <= 0:
                t = -b+s
            if 0<t:
                return t

        return Info.NO_HIT()

    def diffuseLighting(self, p: Vec, n: Vec,):
        v = self.lightPos.sub(p)
        l = v.normalize()
        
        dot = n.dot(l)

        if (dot > 0):
            r = v.len()
            factor = dot / (4 * math.pi * r * r)
            return self.lightPower.scale(factor).mult(self.diffuseColor)
        else:
            return self.BLACK

#=========================================================#
# GUI
#=========================================================#
# レンダー用Widget
class RenderWidget(QtWidgets.QWidget):
    def __init__(self, core, parent=None):
        super().__init__(parent)
        self.core = core

        self.init()
        self.initSignals()

        # Update Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(self.core.refresh())

    def init(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Rendering Button
        self.button_render = QtWidgets.QPushButton('Rendering')
        self.button_render.setMinimumHeight(30)
        font = QtGui.QFont()
        font.setFamily('Arial Black')
        font.setPointSize(11)
        self.button_render.setFont(font)

        layout.addWidget(self.button_render)

        # View
        w, h = self.core.size()
        self.image = QtGui.QImage(w, h, QtGui.QImage.Format_RGB888)
        self.image.fill(self.core.viewColor())
        self.pixmap = QtGui.QPixmap(self.image)
        self.view = QtWidgets.QLabel()
        self.view.setPixmap(self.pixmap)
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.view)

        # Log
        self.log = QtWidgets.QTextEdit()
        layout.addWidget(self.log)

    def initSignals(self):
        self.button_render.pressed.connect(self.draw)

    #=====================================#
    # Set / Get
    #=====================================#
    def setLog(self, text):
        self.log.moveCursor(QtGui.QTextCursor.End)
        self.log.insertPlainText(str(text)+'\n')
        self.log.ensureCursorVisible()
        print(text)

    def setImage(self, file):
        self.image = QtGui.QImage(file)
        
        self.updateByImage()

    #=====================================#
    # Method
    #=====================================#
    def updateByImage(self):
        size = self.image.size()
        w = size.width()
        h = size.height()

        self.core.setSize(w, h)
        self.pixmap = QtGui.QPixmap(self.image)
        self.view.setPixmap(self.pixmap)

        self.core.initCamera()

        self.parent().setup()
        
    #=====================================#
    # Draw
    #=====================================#
    def draw(self):
        start = time.time()
        self.setLog('> Start Render.')
        self.setLog(f'Sample:{Info.SAMPLES()}')

        w, h = self.core.size() 
        self.pixmap = self.view.pixmap()
        self.pixmap.fill(self.core.viewColor())
        painter = QtGui.QPainter(self.pixmap)
        pen = QtGui.QPen()
        pen.setWidth(1)

        for y in range(h):
            for x in range(w):
                r, g, b = self.core.calcPixelColor(x, y)

                color = QtGui.QColor(r, g, b)
                pen.setColor(color)
                painter.setPen(pen)
                painter.drawPoint(x, y)
                
                QtWidgets.QApplication.processEvents()

        painter.end()
        self.setLog('Render Finished.')
        
        elapsed = time.time() - start
        m, s = divmod(elapsed, 60)
        log = f'Time = {int(m)}m{s:.3f}s'
        self.setLog(log)
        self.setLog('')
        self.parent().status_bar.showMessage(log)

        self.update()

# メインウィンドウ
class MainWinodw(QtWidgets.QMainWindow):
    def __init__(self, core, parent=None):
        super().__init__(parent)

        self.core = core

        self.init()
        self.setup()

    def setup(self):
        w, h = self.core.size()
        self.resize(w+100, h)

        title = f'{self.core.name()} {self.core.version()} : [{w} x {h}]'
        self.setWindowTitle(title)

    def init(self):
        #=====================================#
        # Central Widget
        #=====================================#
        self.render_widget = RenderWidget(self.core)
        self.setCentralWidget(self.render_widget)

        #=====================================#
        # Menubar
        #=====================================#
        self.menu_bar = self.menuBar()

        # File Menu
        self.menu_file = self.menu_bar.addMenu('File')
        
        # Save Menu
        action = QtWidgets.QAction('Save', self)
        action.triggered.connect(self.saveImage)
        action.setShortcut(QtGui.QKeySequence('Ctrl+S'))
        self.menu_file.addAction(action)

        action = QtWidgets.QAction('Open', self)
        action.triggered.connect(self.openImage)
        action.setShortcut(QtGui.QKeySequence('Ctrl+O'))
        self.menu_file.addAction(action)

        self.menu_file.addSeparator()

        action = QtWidgets.QAction('Exit', self)
        action.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        action.triggered.connect(self.exit)
        self.menu_file.addAction(action)

        # Edit Menu
        self.menu_edit = self.menu_bar.addMenu('Edit')

        # Copy Menu
        action = QtWidgets.QAction('Copy', self)
        action.triggered.connect(self.copyImage)
        action.setShortcut(QtGui.QKeySequence('Ctrl+C'))
        self.menu_edit.addAction(action)

        action = QtWidgets.QAction('Paste', self)
        action.triggered.connect(self.pasteImage)
        action.setShortcut(QtGui.QKeySequence('Ctrl+V'))
        self.menu_edit.addAction(action)

        #=====================================#
        # Statsubar
        #=====================================#
        self.status_bar = self.statusBar()

    def saveImage(self):
        self.render_widget.setLog('> Save Image')

        path = os.path.dirname(os.path.abspath(__file__))
        file, ext = QtWidgets.QFileDialog.getSaveFileName(
            self,
            dir = path,
            filter = '*.png'
        )
        
        if file:
            pixmap = self.render_widget.view.pixmap()
            pixmap.save(file)
            self.render_widget.setLog(f'File = {file}\n')

    def openImage(self):
        path = os.path.dirname(os.path.abspath(__file__))
        file, ext = QtWidgets.QFileDialog.getOpenFileName(
            self,
            dir = path,
            filter = '*.png *.jpg'
        )

        if file:
            self.render_widget.setLog('> Open Image')
            self.render_widget.setLog(f'File = {file}\n')

            image = QtGui.QImage(file)
            self.render_widget.setImage(image)
    
    def copyImage(self):
        self.render_widget.setLog('> Copy Image')

        cb = QtGui.QClipboard()
        pixmap = self.render_widget.pixmap

        cb.setPixmap(pixmap)

    def pasteImage(self):
        self.render_widget.setLog('> Paste Image')

        cb = QtGui.QClipboard()
        image = cb.image()

        self.render_widget.setImage(image)

    def exit(self):
        self.close() 

def main():
    app = QtWidgets.QApplication(sys.argv)
    core = Core()
    view = MainWinodw(core)
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()