# mengimport library yang dibutuhkan
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

# membuat class untuk render pandas3d
class MyTropi(ShowBase):
    # Digunakan untuk membuat fungsi
    def __init__(self):
        # Digunakan untuk mengembalikan nilai super
        super().__init__()

        # digunakan untuk load atau mengambil nilai pada data file 3d
        tropi = self.loader.loadModel("punyaku.egg")
        # deklarasi nilai posisi
        tropi.setPos(0, 7, 0)
        # deklarasi ukuran
        tropi.setScale(0.3, 0.3, 0.3)
        # render 3d
        tropi.reparentTo(self.render)


# Digunakan untuk mendeklarasikan class
tropi = MyTropi()
# Digunakan untuk menjalankan tropi yang sudah dideklarasikan
tropi.run()