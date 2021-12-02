<h1>Penjelasan Mengenai Program yang dibuat</h1>
<hr>
<h5>Kreshna Putra Adi Wicaksana</h5>
<h5>V3920032</h5>
<h5>TI-D</h5>
<h5>PRAKTIK GAME DEVELOPMENT PERTEMUAN 14</h5>
<hr>

<div>
  <h1><span>Alur Yang Dilakukan Untuk Membuat Media Player</span></h1>
  <hr>
  <ol>
    <li>Pada line 1 hingga 6 Kita mengimportkan atau mengambil library yang diperlukan, yang saya perlukan ini pygame,
      tkinter, pickle, dan os
    </li>
    <li>Kemudian pada line 8 kita membuat sebuah class yang bernama player dan parameternya tk.Frame</li>
    <li>Membuat Fungsi</li>
    <ul>
      <table style="width:100%">
        <tr>
          <td>1
          <th>Fungsi __init__</th>
          <td>fungsi init ini digunakan untuk menginisialisasi semua yang dibutuhkan pada aplikasi yang ingin dibuat.
            pada hal ini kita membuat beberapa hal yang ingin dibuat seperti frame, tombol, dan membuka playlist</td>
          </td>
        </tr>

        <tr>
          <td>2
          <th>Fungsi create_frames</th>
          <td>fungsi ini digunakan untuk membuat frame atau tampilan yang ingin kita tampilkan saat dijalankan. pada hal
            ini berisi beberapa label dan style yang dibutuhkan</td>
          </td>
        </tr>
        <tr>
          <td>3
          <th>Fungsi track_widgets</th>
          <td>fungsi ini digunakan untuk menampilkan nama atau judul lagu yang sedang diputar. untuk membuat bagian ini,
            saya menggunakan beberapa label</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>4
          <th>Fungsi control_widgets</th>
          <td>fungsi ini digunakan untuk membuat dan menampilkan serta menjalankan sebuah program atau aplikasi yang
            dibuat. pada control_widgets ini kita menampilkan beberapa tampilan seperti tombol untuk mengambil folder
            playlist, tombol play, pause, next, dan previous, serta juga terdapat tombol volume yang dimana pada volume
            ini kita menggunakan tombol slider. pada slider ini kita set volume mixernya ini sebesar 0.8</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>5
          <th>Fungsi tracklist_widgets</th>
          <td>fungsi ini digunakan untuk menampilkan list lagu yang ada pada folder yang sudah dipilih sebelumnya. pada
            fungsi ini kita menggunakan Listbox agar muncul list lagu yang ada didalamnya</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>6
          <th>Fungsi retrieve_songs</th>
          <td>fungsi ini digunakan untuk mengambil lagunya</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>7
          <th>Fungsi enumerate_songs</th>
          <td>fungsi ini digunakan untuk menghitung jumlah lagu yang ada didalamnya</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>8
          <th>Fungsi play_pause_song</th>
          <td>fungsi ini digunakan untuk tombol pause dan play, pada hal ini saya menggabungkan fungsi pause dan play
            yang dimana jika musik sedang berhenti maka jalankan musik saat tombol ditekan dan sebaliknya.</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>9
          <th>Fungsi play_song</th>
          <td>fungsi ini digunakan untuk menyalakan atau memutar musik yang sudah dipilih dari folder yang sudah kita
            pilih juga sebelumnya</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>10
          <th>Fungsi pause_song</th>
          <td>fungsi ini digunakan untuk memberhentikan sebuah musik yang dimana didalamnya ini terdapat mixer music
            pause dan unpause atau stop sementara dan menjalankannya lagi</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>11
          <th>Fungsi prev_song</th>
          <td>fungsi ini digunakan untuk kembali ke musik sebelumnya atau dengan kata lain balik ke lagu yang sebelumnya
            di putar. hal ini saya menggunakan -1 untuk mundur ke lagu sebelumnya</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>12
          <th>Fungsi next_song</th>
          <td>fungsi ini digunakan untuk melanjutkan atau berpindah ke lagu selanjutnya, hal ini berkebalikan dengan
            fungsi prev_song</td>
          </td>
        </tr>
        </tr>
        <tr>
          <td>13
          <th>Fungsi change_volume</th>
          <td>fungsi ini digunakan untuk mengubah volume yang dimana kita menggunakan set_volume untuk mengatur pelan
            dan kencangnya suatu lagu</td>
          </td>
        </tr>
      </table>
    </ul>
    <li>kemudian pada line 187 ini kita membuat sebuah if __name__ sama dengan __main__ maka jalankan line 188 hingga
      190</li>
    <li>selanjutnya line 192 ini deklarasi img dan diisi dengan foto yang bernama wallpaper</li>
    <li>selanjutnya line 193 ini deklarasi img dan diisi dengan foto yang bernama next</li>
    <li>selanjutnya line 194 ini deklarasi img dan diisi dengan foto yang bernama previous</li>
    <li>selanjutnya line 195 ini deklarasi img dan diisi dengan foto yang bernama play</li>
    <li>selanjutnya line 196 ini deklarasi img dan diisi dengan foto yang bernama pause</li>
  </ol>
</div>
<hr>
