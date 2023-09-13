# django-game-inventory
 
# Implementasi di *Local Machine*
## Setup Awal
### 1. Pastikan *virtual environment* (venv) sudah aktif
Sebelum membuat *project* Django, kita memerlukan venv untuk menampung semua *library* yang kita gunakan di dalam *project*. Cara untuk mengaktifkan venv adalah sebagai berikut:
- Windows
```
env\Scripts\activate.bat
```
- Mac
```
source env/bin/activate
```

### 2. Jalankan script instalasi *library*
Pada *project* ini, terdapat beberapa *library* yang digunakan demi mempercepat proses pengembangan. Untuk itu, jika ingin menjalankan di *local machine* sendiri, diperlukan untuk menjalankan beberapa *script* berikut:
- Instalasi *library*
```
pip install -r requirements.txt
```
- Instalasi *package*
```
npm i
```
Instalasi *package* tidak diharuskan untuk menggunakan Node Package Manager. *Package manager* lain seperti Yarn dan Bun juga bisa digunakan di *project* ini. Alasan perlu meng-*install* *package* juga padahal sudah ada *library* adalah karena *project* ini menggunakan TailwindCSS sebagai *framework* CSS-nya.

## Langkah Pembuatan *Project*
### 1. Membuat *project* Django baru
Untuk membuat *project* baru, sebelumnya harus dipastikan bahwa direktori terminal sudah sesuai. Jika sudah, perintah berikut dijalankan untuk membuat *project* Django:
```
py manage.py startapp game_inventory .
```
Sebuah aplikasi main juga diperlukan pada *project*. Oleh karena itu, perintah berikut perlu dijalankan juga:
```
py manage.py startapp main .
```

### 2. Konfigurasi *Project*
#### Aplikasi `game_inventory`
Ubah pengaturan `ALLOWED_HOST` agar membolehkan aplikasi untuk dijalankan oleh segala *host* dengan mengubah pengaturan berikut di `settings.py` milik `game_inventory`:
```py
...
ALLOWED_HOSTS = ['*']
...
```

Tambahkan aplikasi `main` sebagai `INSTALLED_APP` di `settings.py` dengan mengubah pengaturan berikut:
```py
INSTALLED_APPS = [
    ...,
    'main',
]
```

#### Direktori Utama


# Bagan
# Alasan menggunakan virtual environment
# MVC, MVT, MVVM, dan Perbedaannya
Pada pengembangan website, terdapat beberapa pola arsitektural yang dikembangkan oleh *developer* untuk membuat *project* lebih *scalable* dan mudah untuk di-*maintain*. Ketiga arsitektur yang akan dibahas kali ini adalah beberapa yang paling populer di antara arsitektur-arsitektur yang ada. Ketiganya memiliki dua komponen utama yang memiliki peran krusial dalam arsitektur:
- **Model** — komponen inti dari arsitektur, merupakan struktur data dinamik milik aplikasi yang independen dari *user interface*. Secara langsung mengatur data, logika, dan peraturan dari aplikasi.
- **View** — mengurus logika presentasi, yaitu bagaimana data yang dikelola oleh model akan dipresentasikan kepada pengguna.

Perbedaan pendekatan dari tiap arsitektur mulai terlihat pada komponen ketiga. Masing-masing komponen pembeda pada arsitektur sebenarnya memiliki tujuan sama, namun dengan pendekatan yang berbeda. Berikut adalah penjelasan mengenai perbedaan pendekatan yang digunakan oleh arsitektur-arsitektur di atas.

## Model View Controller (MVC)
Pola arsitektural ini adalah yang paling sering digunakan oleh *framework* pengembangan *website* untuk membuat *project* yang *scalable*. Perbedaan dengan dua arsitektur lainnya terdapat pada komponen ketiganya, *controller*, yaitu:
- **Controller** — bertindak sebagai jembatan antara *model* dan *view* untuk memproses semua *business logic* dan *request* yang datang.

## Model View Template (MVT)
Pola arsitektur yang sering digunakan pada aplikasi website Django, yaitu *framework* Python *high-level*. Memiliki banyak persamaan dengan arsitektur MVC namun terdapat beberapa perbedaan untuk menyesuaikan dengan kebutuhan pengembangan aplikasi website. Perbedaan signifikan yang dimiliki MVT dengan arsitektur lain adalah:
- **View** — pada Django, *view* berisi lebih banyak tentang pemrosesan data dan logika dibandingkan menampilkan suatu hal. Oleh karena itu, bisa dibilang pada arsitektur ini *view* merupakan perpaduan antara *controller* dan *view* pada arsitektur MVC.
- **Template** — berisi bagian statik dari *output* HTML dan juga berbagai sintaks khusus yang menjelaskan bagaimana konten dinamis akan ditampilkan. Perannya mirip seperti *view* pada arsitektur MVC.

## Model View View Model (MVVM)
Pola arsitektural yang sering digunakan pada aplikasi yang memerlukan banyak interaksi pengguna seperti aplikasi *desktop* dan *single page application* dengan *framework* seperti Angular dan Vue. Perbedaan signifikan yang dimiliki MVVM dengan arsitektur lain adalah:
- **View Model** — penengah antara *model* dan *view* yang mengandung logika presentasi dan mengubah data dari model menjadi format yang bisa ditampilkan oleh *view*. 
