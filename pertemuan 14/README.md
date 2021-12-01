<h1>Penjelasan Mengenai Program yang dibuat</h1>
<hr>
<h5>Kreshna Putra Adi Wicaksana</h5>
<h5>V3920032</h5>
<h5>TI-D</h5>
<h5>PRAKTIK GAME DEVELOPMENT PERTEMUAN 14</h5>
<hr>

<div style="text-align:justify">
  <h1><span>Alur Yang Dilakukan Untuk Membuat Media Player</span></h1>
  <hr>
  <ol>
    <li>Kita mengimportkan atau mengambil library yang diperlukan, yang saya perlukan ini pygame, tkinter, dan os</li>
    <li>kemudian kita membuat sebuah window dengan perintah tkr.Tk()</li>
    <li>selanjutnya kita membuat tempat edit window yang dimana hal ini digunakan untuk memberikan nama title dan juga ukuran frame yang dibuat</li>
    <li>selanjutnya kita membuat program untuk playlist dan kita deklarasikan dengan songlist</li>
    <li>selanjutnya kita deklarasi VolumeLevel dengan Scale yang digunakan untuk mengatur volumenya</li>
    <li>setelah itu kita membuat sebuah inputan playlist yang dimana kita deklarasikan playlist. disini saya menggunakan for yang didalamnya berisi songlist tadi</li>
    <li>kemudian kita inisialisasi dan inisialisasi mixer untuk sound</li>
    <li>Membuat Fungsi</li>
      <ul>
        <table style="width:100%">
          <tr>
            <td>
              <th>Play</th>
              <td>fungsi Play ini untuk menjalankan atau memutar musik yang telah dipilih. pada program yang dibuat ini saya menggunakan mixer load, play, set_volume, dan get_volume</td>
            </td>
          </tr>
          <tr>
            <td>
              <th>Stop</th>
              <td>fungsi ExitPlayer ini digunakan untuk mematikan musik yang sedang diputar</td>
            </td>
          </tr>
          <tr>
            <td>
              <th>Pause</th>
              <td>fungsi Pause ini digunakan untuk memberhentikan musik sementara</td>
            </td>
          </tr>
          <tr>
            <td>
              <th>UnPause</th>
              <td>fungsi UnPause ini digunakan untuk menjalankan musik setelah sebelumnya di berhentikan sementara atau Pause</td>
            </td>
          </tr>
        </table>
      </ul>
    <li>kemudian kita membuat button atau tombol sebanyak 4 buah yang digunakan untuk Play, Stop, Pause, dan UnPause</li>
    <li>kemudian kita membuat sting untuk lagu dengan labelnya ini dipilih dari songtitle</li>
    <li>selanjutnya kita membuat penempatan sebuah widgetnya yang sudah dibuat terlebih dahulu</li>
    <li>dan yang terakhir ini untuk mainloop</li>
  </ol>
</div>
<hr>
