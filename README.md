# django-game-inventory
 
# Bagaimana aku melakukan checklist
# Bagan
# Alasan menggunakan virtual environment
# MVC, MVT, MVVM, dan Perbedaannya
Pada pengembangan website, terdapat beberapa pola arsitektural yang dikembangkan oleh *developer* untuk membuat *project* lebih *scalable* dan mudah untuk di-*maintain*. Ketiga arsitektur yang akan dibahas kali ini adalah beberapa yang paling populer di antara arsitektur-arsitektur yang ada. Ketiganya memiliki dua komponen utama yang memiliki peran krusial dalam arsitektur, yaitu **model** dan **view** yang akan dijelaskan di bawah.

- **Model** — komponen inti dari arsitektur, merupakan struktur data dinamik milik aplikasi yang independen dari *user interface*. Secara langsung mengatur data, logika, dan peraturan dari aplikasi. Pada konteks Django, model biasanya merepresentasikan sebuah tabel di basis data sebuah aplikasi.
- **View** — mengurus segala logika *user interface* dari aplikasi

Perbedaan pendekatan dari tiap arsitektur mulai terlihat pada komponen ketiga. Masing-masing komponen pembeda pada arsitektur sebenarnya memiliki tujuan sama, namun dengan pendekatan yang berbeda. Berikut adalah penjelasan mengenai perbedaan pendekatan yang digunakan oleh arsitektur-arsitektur di atas.

## Model View Controller (MVC)
Pola arsitektural ini adalah yang paling sering digunakan oleh *framework* pengembangan *website* untuk membuat *project* yang *scalable*. Perbedaan dengan dua arsitektur lainnya terdapat pada komponen ketiganya, yaitu *controller*.
- **Controller** — bertindak sebagai jembatan antara *model* dan *view* untuk memproses semua *business logic* dan *request* yang datang.

## Model View Template (MVT)
Pola arsitektur yang sering digunakan pada aplikasi website Django, yaitu *framework* Python *high-level*. Memiliki banyak persamaan dengan arsitektur MVC namun terdapat beberapa perbedaan untuk menyesuaikan dengan kebutuhan pengembangan aplikasi website.
- **View** — pada Django, *view* berisi lebih banyak tentang pemrosesan data dan logika dibandingkan menampilkan suatu hal. Oleh karena itu, bisa dibilang pada arsitektur ini *view* merupakan perpaduan antara *controller* dan *view* pada arsitektur MVC.
- **Template** — berisi bagian statik dari *output* HTML dan juga berbagai sintaks khusus yang menjelaskan bagaimana konten dinamis akan ditampilkan. Perannya mirip seperti *view* pada arsitektur MVC.

## Model View View Model (MVVM)
Pola arsitektural yang sering digunakan pada aplikasi yang memerlukan banyak interaksi pengguna seperti aplikasi *desktop* dan *single page application* dengan *framework* seperti Angular dan Vue. 
- **View Model** — penengah antara *model* dan *view* yang mengandung logika presentasi dan mengubah data dari model menjadi format yang bisa ditampilkan oleh *view*. 

## Lantas apa perbedaannya?
Yo ndak tahu kok tanya saya
