# mengimport library yang akan digunakan
from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import TextNode, NodePath, LightAttrib
from panda3d.core import LVector3
from direct.actor.Actor import Actor
from direct.task.Task import Task
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
import sys

# membuat fungsi untuk melihat nilai min dan max
def clamp(i, mn=-1, mx=1):
    return min(max(i, mn), mx)

# membuat fungsi untuk menampilkan tulisan
def genLabelText(text, i):
    return OnscreenText(text=text, parent=base.a2dTopLeft, scale=.06,
                        pos=(0.06, -.08 * i), fg=(1, 1, 1, 1),
                        shadow=(0, 0, 0, .5), align=TextNode.ALeft)

# membuat sebuah kelas untuk karakter
class LookingGrippingDemo(ShowBase):
    # inisialisasi untuk membuat fungsi
    def __init__(self):
        # mengembalikan ke library
        ShowBase.__init__(self)

        # membuat teks penjelasan di pojok kiri
        self.onekeyText = genLabelText("ESC: Keluar", 1)
        self.onekeyText = genLabelText("[1]: Pemanas Air", 2)
        self.twokeyText = genLabelText("[2]: Permen", 3)
        self.threekeyText = genLabelText("[3]: Pisang", 4)
        self.fourkeyText = genLabelText("[4]: Samurai", 5)

        # Set keyboard input
        self.accept('escape', sys.exit)
        self.accept('1', self.switchObject, [0])
        self.accept('2', self.switchObject, [1])
        self.accept('3', self.switchObject, [2])
        self.accept('4', self.switchObject, [3])

        # mematikan mouse kontrol kamera
        base.disableMouse()
        # mengatur posisi kamera
        camera.setPos(0, -15, 2)

        # memanggil karakter yang akan digunakan
        self.eve = Actor("models/eve",
                         {'walk': "models/eve_walk"})
        # render karakter pada screen
        self.eve.reparentTo(render)

        # membuat kontrol join untuk mengatur leher
        self.eveNeck = self.eve.controlJoint(None, 'modelRoot', 'Neck')

        # mengatur interval berjalannya
        self.eve.actorInterval("walk", playRate=2).loop()

        # membuat tugas untuk mengatur kepala
        taskMgr.add(self.turnHead, "turnHead")

        # membuat kontrol untuk mengatur pergerakan tangan
        self.rightHand = self.eve.exposeJoint(None, 'modelRoot', 'RightHand')

        # deklrasi posisi impor desain yang digunakan
        positions = [("teapot", (0, -.66, -.95), (90, 0, 90), .4),
                     ("models/candycane", (.15, -.99, -.22), (90, 0, 90), 1),
                     ("models/banana", (.08, -.1, .09), (0, -90, 0), 1.75),
                     ("models/sword", (.11, .19, .06), (0, 0, 90), 1)]

        # membuat daftar array kosong
        self.models = []
        for row in positions:
            # load model yang digunakan
            np = loader.loadModel(row[0])
            # mengatur posisi, rotasi, dan mengatur ukuran
            np.setPos(row[1][0], row[1][1], row[1][2])
            np.setHpr(row[2][0], row[2][1], row[2][2])
            np.setScale(row[3])
            
            # mengulangi pergerakan tangan kanan
            np.reparentTo(self.rightHand)
            # menambahkan ke dalam daftar model
            self.models.append(np)

        # deklarasi objek pertama yang diambil
        self.switchObject(0)
        # mengatur light
        self.setupLights()

    # membuat fungsi untuk mengganti objek
    def switchObject(self, i):
        for np in self.models:
            np.hide()
        self.models[i].show()

    # membuat fungsi menggerakkan kepala
    def turnHead(self, task):
        # membuat percabangan nilai input
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            # membuat nilai x dan y
            self.eveNeck.setP(clamp(mpos.getX()) * 50)
            self.eveNeck.setH(clamp(mpos.getY()) * 20)

        # perluangan task tanpa batas
        return Task.cont

    # mengatur cahaya
    def setupLights(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.4, .4, .35, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 8, -2.5))
        directionalLight.setColor((0.9, 0.8, 0.9, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))

# membuat instance dari kelas yang dibuat
tugasku = LookingGrippingDemo()
# menjalankan program
tugasku.run()
