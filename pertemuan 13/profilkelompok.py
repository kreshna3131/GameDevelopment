import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame


# Add some text
bk_text = "Nama Kelompok"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.70), scale=0.20,
                          fg=(255, 255, 255, 6), align=TextNode.ACenter,
                          mayChange=1)


# Callback function to set text
v = [0]


def setText(status=None):

    bk_text = "CurrentValue : %s" % v
    textObject.setText(bk_text)


def itemSel(arg):
    if arg == "List Nama Anggota":
        l1 = DirectLabel(text="Kelompok 3", text_scale=0.07)
        l2 = DirectLabel(text="TI D", text_scale=0.08)
        l3 = DirectLabel(text="UNS", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(

            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.6, 0.6, -0.50, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in []:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='a.jpg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Bagas":

        l1 = DirectLabel(text="Bagas Aditya Pramudana", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920012", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(

            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='Bagas.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Dion":
        l1 = DirectLabel(text="Dion Aji cahyono", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920018", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(


            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Nonton,', 'Desain']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='Dion.jpg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Isnan":
        l1 = DirectLabel(text="Isnan Wijaya", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920029", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(


            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='Isnan.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Kreshna":
        l1 = DirectLabel(text="Kreshna Putra Adi Wicaksana", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920032", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(


            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='kreshna.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Ivan":
        l1 = DirectLabel(text="Ivan Fausta Dinata", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920030", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(


            frameColor=(1, 90, 10, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='ivan.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)


# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=1,
                        items=["List Nama Anggota", "Bagas",
                               "Dion", "Isnan", "Kreshna", "Ivan"],
                        highlightColor=(0.65, 0.1, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu


# Procedurally select a item
menu.set(0)

# Run the program
base.run()
