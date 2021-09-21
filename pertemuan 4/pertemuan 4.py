# untuk mengimport atau memasukkan atau mengambil library pygame dan sys
import pygame
import sys
from pygame import display

# deklrasi tinggi dan lebarnya saat dijalankan
WIDTH, HEIGHT = 600, 400
# membuat judul saat dijalankan
TITLE = "Smooth Movement Pertemuan 4"
# untuk warna font
font_color = (255, 0, 255)

# background
background = pygame.image.load('f.jpg')

# untuk inisialisasi semua modul pygame
pygame.init()
# untuk menampilkan display saat dijalankan dengan 2 parameter yaitu height dan width
win = pygame.display.set_mode((WIDTH, HEIGHT))
# untuk menampilkan gambar ikan
ikan = pygame.image.load("ikan.png")
# untuk setting yang berisi title
pygame.display.set_caption(TITLE)
# untuk jenis font dan ukurannya
font = pygame.font.SysFont("Times New Roman", 27)
# untuk memberikan tulisan pada display yang dijalankan dengan 3 parameter
text1 = font.render("KRESHNA PUTRA ADI WICAKSANA", True, font_color)
text2 = font.render("V3920032", True, font_color)
# untuk waktu yang telah berlalu
clock = pygame.time.Clock()

# class player
class Player:
    # berfungsi untuk menginisialisasi kelas
    def __init__(self, x, y):
        # deklarasi x dan y
        self.x = int(x)
        self.y = int(y)
        # untuk membuat sebuah persegi
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        # untuk warna
        self.color = (250, 120, 60)
        # untuk titik awal x dan y
        self.velX = 0
        self.velY = 0
        # untuk tombol kanan kiri atas bawah false
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        # untuk mengatur speed saat dijalankan
        self.speed = 4

    # digunakan untuk menggambar ulang gambar saat ini
    def draw(self, win):
        # berfungsi untuk menggambar pada window yang berbentuk persegi
        win.blit(ikan, self.rect)

    # berfungsi untuk mengupdate jendela window
    def update(self):
        # mengatur titik awal
        self.velX = 0
        self.velY = 0
        # untuk emngatur arahnya
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        # untuk membentuk dan mengeluarkan gambar ikan
        self.rect = pygame.Rect(int(self.x), int(self.y), 10, 10)

# menginisialisasi player
player = Player(WIDTH/2, HEIGHT/2)

# Looping atau perulangan while
while True:

    # jika event ini mendaftarkan semua ke dalam antrian
    for event in pygame.event.get():
        # jika event type sama dengan pygame.QUIT
        if event.type == pygame.QUIT:
            # maka jalankan sistem quit pygame dan sys
            pygame.quit()
            sys.exit()
        # jika event type sama dengan keydown
        if event.type == pygame.KEYDOWN:
            # maka jalankan LEFT, RIGHT, UP, DOWN dengan True atau benar
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
                # jika event type sama dengan keyup
        if event.type == pygame.KEYUP:
            # maka LEFT, RIGHT, UP, DOWN dengan False
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

        # untuk pembatas X agar tidak lewat dari batasnya
        if player.x > 560:
            player.x = 560
        if player.x < 30:
            player.x = 10
        # untuk pembatas Y agar tidak lewat dari batasnya
        if player.y > 360:
            player.y = 360
        if player.y < 30:
            player.y = 10

    # untuk mengisi object surface
    win.fill((12, 24, 36))
    win.blit(background,(0,0))
    # untuk menyalin konten dari surface ke surface lainnya
    win.blit(text1, (70, 0))
    win.blit(text2, (245, 370))
    # untuk menggambar ulang gambar saat ini
    player.draw(win)

    # untuk update
    player.update()
    pygame.display.flip()

    # untuk menunda game berjalan lebih lambat
    clock.tick(120)