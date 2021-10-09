# mengambil atau memasukkan library
import pygame
import random
from enum import Enum
from collections import namedtuple

# inisialisasi
pygame.init()
# deklarasi font dan ukuran
font = pygame.font.Font('arial.ttf', 25)

# membuat class arah
class ARAH(Enum):
    KANAN = 1
    KIRI = 2
    ATAS = 3
    BAWAH = 4

# deklarasi poin diisi dengan subclass Tuple
Point = namedtuple('Point', 'x, y')

# deklarasi warna
HITAM = (0, 0, 0)
HIJAU = (0,255,128)
UNGU = (255, 51, 255)
PINK = (102, 255, 255)
ABU = (234,234,234)

# ukuran block
BLOCK_SIZE = 20
# kecepatan ular
SPEED = 10

# membuat class game
class Ular:
    # digunakan untuk perintah kode yang dibuat, dan terdapat ukuran tinggi dan lebar
    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h
        # inisialisasi display yang diisi dengan ukuran height dan width
        self.display = pygame.display.set_mode((self.w, self.h))
        # membuat nama pada display saat dijalankan
        pygame.display.set_caption('ULAR | TI-D_V3920032_KRESHNA PUTRA_UTS GAMEDEV')
        # mengatur waktu
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = ARAH.KANAN
        # untuk menambahkan point
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                    Point(self.head.x-BLOCK_SIZE, self.head.y),
                    Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        # untuk score
        self.score = 0
        # untuk makanan
        self.makanan = None
        self._place_food()
        
    # membuat fungsi makanan
    def _place_food(self):
        # deklarasi x dan y dengan random randint untuk makanan
        x = random.randint(0, (self.w - BLOCK_SIZE ) // BLOCK_SIZE ) * BLOCK_SIZE 
        y = random.randint(0, (self.h - BLOCK_SIZE ) // BLOCK_SIZE ) * BLOCK_SIZE
        # untuk point saat memakan
        self.makanan = Point(x, y)
        if self.makanan in self.snake:
            self._place_food()
        
    # membuat fungsi step
    def play_step(self):
        # mengambil inputan user
        for event in pygame.event.get():
            # jika event.type ini sama dengan QUIT
            if event.type == pygame.QUIT:
                # maka akan menjalankan pygame.quit atau keluar
                pygame.quit()
                quit()
            # event.type sama dengan tombol
            if event.type == pygame.KEYDOWN:
            # jika event.type ini sama dengan tombol kiri
                if event.key == pygame.K_LEFT:
                    # maka jalankan self.direction = ARAH.KIRI
                    self.direction = ARAH.KIRI
            # jika event.type ini sama dengan tombol kanan
                elif event.key == pygame.K_RIGHT:
                    # maka jalankan self.direction = ARAH.KANAN
                    self.direction = ARAH.KANAN
            # jika event.type ini sama dengan tombol atas
                elif event.key == pygame.K_UP:
                    # maka jalankan self.direction = ARAH.ATAS
                    self.direction = ARAH.ATAS
            # jika event.type ini sama dengan tombol bawah
                elif event.key == pygame.K_DOWN:
                    # maka jalankan self.direction = ARAH.BAWAH
                    self.direction = ARAH.BAWAH

        # untuk move atau berpindah, dan update head
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # mengecek jika game over False
        game_over = False
        # dan jika collision berjalan
        if self._is_collision():
            # maka game over true dan mengembalikan nilai score
            game_over = True
            return game_over, self.score
            
        # memindahkan atau menambahkan makanan pada tampilan layar.
        # jika self.head sama dengan makanan maka score akan bertambah 1
        if self.head == self.makanan:
            self.score += 1
            self._place_food()
        # jika else maka menghapus item pada indeks
        else:
            self.snake.pop()
        
        # mengupdate ui dan waktu
        self._update_ui()
        # tick di isi dengan kecepatan
        self.clock.tick(SPEED)
        # mengembalikan saat game over dan menampilkan score
        return game_over, self.score
    
    # fungsi collision
    def _is_collision(self):
        # jika telah mencapai batas maka mengembalikan nilai True
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # atau jika terkena badannya sendiri maka nilai True
        if self.head in self.snake[1:]:
            return True
        # maka mengembalikan nilai false
        return False
        
    # update ui
    def _update_ui(self):
        # berfungsi untuk memberikan warna pada latar
        self.display.fill(ABU)
        
        # mengatur si ular yang dibuat dengan ukuran dan warna yang diberikan seperti dibawah ini
        for pt in self.snake:
            pygame.draw.rect(self.display, UNGU, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, PINK, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        # mengatur warna dan ukuran untuk makanan yang dimakan ular
        pygame.draw.rect(self.display, HIJAU, pygame.Rect(self.makanan.x, self.makanan.y, BLOCK_SIZE, BLOCK_SIZE))
        
        # untuk menampilkan teks skor yang diisi dengan string score
        text = font.render("Skor yang diperoleh: " + str(self.score), True, HITAM)
        # mengatur posisi untuk menampilkan skor
        self.display.blit(text, [190, 5])
        # untuk memperbarui sebagian layar
        pygame.display.flip()
        
    # fungsi untuk berjalan atau mengarahkan ular
    def _move(self, direction):
        # deklarasi x dan y
        x = self.head.x
        y = self.head.y
        # jika direction sama dengan ARAH.KANAN
        if direction == ARAH.KANAN:
            # jika x ditambah sama dengan block size
            x += BLOCK_SIZE
        # jika direction sama dengan ARAH.KIRI
        elif direction == ARAH.KIRI:
            # jika x dikurang sama dengan block size
            x -= BLOCK_SIZE
        # jika direction sama dengan ARAH.BAWAH
        elif direction == ARAH.BAWAH:
            # jika y ditambah sama dengan block size
            y += BLOCK_SIZE
        # jika direction sama dengan ARAH.ATAS
        elif direction == ARAH.ATAS:
            # jika y dikurang sama dengan block size
            y -= BLOCK_SIZE
        # maka self head ini berisi point x dan y
        self.head = Point(x, y)
            

# jika __name__ sama dengan __main__ yang dibmana game = ular
if __name__ == '__main__':
    game = Ular()

    # maka akan melakukan perulangan game
    while True:
        game_over, score = game.play_step()
        # jika game berakhir maka true
        if game_over == True:
            break
    # dan mencetak hasil scorenya
    print('Final Score', score)
        
    # keluar dari pygame
    pygame.quit()