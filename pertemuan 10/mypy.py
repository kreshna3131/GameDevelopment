# memasukkan library yang dibutuhkan
import sys
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

# membuat class
class MyApp(ShowBase):
    # menginisialisasi fungsi
    def __init__(self):
        # untuk menjalankan file
        ShowBase.__init__(self)
        # mematikan mouse
        self.disableMouse()
        # jika keluar dari program akan memberhentikan program
        self.accept('escape', sys.exit)
        # deklarasi nilai tampilan
        self.scene = self.loader.loadModel("models/environment")
        # merender gambar yang sudah dideklarasikan
        self.scene.reparentTo(self.render)
        # digunakan untuk deklarasi ukuran
        self.scene.setScale(0.25, 0.25, 0.25)
        # digunakan untuk deklarasi posisi
        self.scene.setPos(-8, 42, -2)
        # digunakan untuk kamera berputar
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        # digunakan untuk deklarasi 3d yang digunakan
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        # digunakan untuk deklarasi ukuran 3d yang digunakan
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        # untuk render ulang
        self.pandaActor.reparentTo(self.render)
        # deklarasi perulangan model walk
        self.pandaActor.loop("walk")
        # deklarasi musik
        self.Musik = self.loader.loadMusic("westlife.ogg")
        # mengatur besar volume
        self.Musik.setVolume(0.9)
        # looping musik
        self.Musik.setLoop(True)
        # memulai musik
        self.Musik.play()

        # deklarasi pergerakan aktor
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -15, 0),
                                                   startPos=Point3(0, 15, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 15, 0),
                                                   startPos=Point3(0, -15, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # utuk menjalankan aktor pada koordinat
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")

    # Digunakan untuk membuat fungsi perputaran kamera
    def spinCameraTask(self, task):
        # deklarasi waktu
        angleDegrees = task.time * 8
        # deklarasi sudut kamera
        angleRadians = angleDegrees * (pi / 180.0)
        # deklarasi posisi angle kamera
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        # setting angle yang sudah di deklarasi
        self.camera.setHpr(angleDegrees, 0, 0)
        # mengembalikan nilai untuk menjalankan ulang task
        return Task.cont


# deklarasi class untuk dijalankan
MyPy = MyApp()
# menjalankan class yang sudah dideklarasikan
MyPy.run()