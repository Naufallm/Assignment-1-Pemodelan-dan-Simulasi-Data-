# Struktur Kode #

* Class 
Merepresentasikan platform transportasi online dengan sumber daya terbatas (pengemudi) dan mengelola antrean pelanggan dan pelayanan transportasi.

* Function Customer 
Mensimulasikan pelanggan yang tiba dan meminta layanan transportasi. Jika pengemudi tersedia, layanan dimulai segera; jika tidak, pelanggan menunggu.

* Function Customer_arrival
Mensimulasikan kedatangan pelanggan dalam sistem dengan pola kedatangan acak. Memanggil fungsi customer untuk setiap pelanggan yang tiba.

* Simulation Execution
Menjalankan simulasi dalam periode tertentu dan mencatat statistik seperti waktu tunggu rata-rata dan utilisasi sistem.

# Cara Menjalankan
1. Menggunakan python, pastikan sudah terinstall
2. Menginstall library simPy
   `` pip install simpy
   ``
3. Menjalankan simulasi dari code tersebut
4. Hasil simulasi akan ditampilkan dalam bentuk log kedatangan pelanggan, waktu layanan, dan statistik performa sistem.

# Contoh Output #

Customer 1 arrived at 0.12 minutes.

Customer 1 started service after waiting 0.00 minutes.

Customer 2 arrived at 0.34 minutes.

Customer 2 started service after waiting 0.00 minutes.

...

=== Simulation Summary ===

Average Wait Time: 0.00 minutes

Max Wait Time: 0.00 minutes

Min Wait Time: 0.00 minutes

