#Table Daftar Buku
daftarBuku = [
        {
            'judul' : 'BUKU ABC',
            'tahunTerbit' : 2005,
            'status' : 'tersedia',
            'peminjam' : "-"

        },
        {
            'judul' : 'BUKU DEF',
            'tahunTerbit' : 2013,
            'status' : 'dipinjam',
            'peminjam' : "Sulis"
        },
        {
            'judul' : 'BUKU GHI',
            'tahunTerbit' : 2010,
            'status' : 'tersedia',
            'peminjam' : "-"
        },
        {
            'judul' : 'BUKU JKL',
            'tahunTerbit' : 2011,
            'status' : 'dipinjam',
            'peminjam' : "David"
        }
]

#tampilkan tabel
def show() :
    print('\nList Daftar Buku Perpustakaan \n')
    print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format('Index', 'Judul Buku', 'Tahun Terbitan', 'Status Pinjaman', 'Nama Peminjam'))
    for i in range(len(daftarBuku)) :
        print('{}\t| {}\t| {:<15}\t| {:<10}\t\t| {}\t\t|'.format(i, daftarBuku[i]['judul'], daftarBuku[i]['tahunTerbit'], daftarBuku[i]['status'], daftarBuku[i]['peminjam']))


# Function Read
def read () :
    command = True
    while command != 3:
        print('''
            Daftar Informasi Buku

        1. Tampilkan list informasi buku perpustakaan
        2. Cari info buku
        3. Kembali ke menu utama
        ''')
        command = int(input("Masukkan nomor pilihan menu : "))

        # liat list buku
        if command == 1 :
            if len(daftarBuku) > 0 :
                show()
            else :
                print ('\n===DATA BUKU TIDAK TERSEDIA===')
        # mencari buku        
        elif command == 2 :
            namaBuku = input("Masukkan nama buku : ").upper()
            crossChecker = 0
            for i in range(len(daftarBuku)) :
                if namaBuku in daftarBuku[i].values():
                    print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format('Index', 'Judul Buku', 'Tahun Terbitan', 'Status Pinjaman', 'Nama Peminjam'))
                    print('{}\t| {}\t| {:<15}\t| {:<10}\t\t| {}\t\t|'.format(i, daftarBuku[i]['judul'], daftarBuku[i]['tahunTerbit'], daftarBuku[i]['status'], daftarBuku[i]['peminjam']))
                    crossChecker += 1
            if crossChecker == 0 :
                print("\n===BUKU TIDAK DITEMUKAN===")

#Function create
def create () :
    command = True
    while command != 2 :
        print('''
            Menu menambah Buku
        1. Masukkan Buku baru
        2. Kembali ke Beranda
        ''')
        command = int(input("Masukkan nomor pilihan menu : "))
        if command == 1 :
            namaBuku = input('Masukkan Nama Buku : ').upper()
            crossChecker = 0
            for i in range(len(daftarBuku)):
                if namaBuku in daftarBuku[i].values() :
                    print("\n====BUKU SUDAH TERCATAT===")
                    crossChecker += 1
                    break

            if crossChecker == 0:    
                tahunTerbit = int(input('Masukkan tahun terbitan : '))
                print(f"Nama Buku : {namaBuku}\nTahun terbit: {tahunTerbit}")
                konfirmasi = input('simpan data (y/n): ')
                if konfirmasi == 'y' :
                    daftarBuku.append({
                        'judul' : namaBuku,
                        'tahunTerbit' : tahunTerbit,
                        'status' : 'tersedia',
                        'peminjam' : "-"
                    })
                    show()
                    print('\n===DATA BERHASIL DITAMBAHKAN===')
                    break
                # else :
                #     break

#Function Update
def update():
    command = True
    while command != 2 :
        print('''
            Menu Status Peminjaman Buku
        1. Ubah informasi Buku
        2. Kembali ke Beranda
        ''')
        command = int(input("Masukkan nomor pilihan menu : "))
        if command == 1 :
            namaBuku = input('Masukkan judul buku : ').upper()
            crossChecker = 0
            for i in range(len(daftarBuku)):
                if namaBuku in daftarBuku[i].values():
                    print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format('Index', 'Judul Buku', 'Tahun Terbitan', 'Status Pinjaman', 'Nama Peminjam'))
                    print('{}\t| {}\t| {:<15}\t| {:<10}\t\t| {}\t\t|'.format(i, daftarBuku[i]['judul'], daftarBuku[i]['tahunTerbit'], daftarBuku[i]['status'], daftarBuku[i]['peminjam']))
                    updateStatus = input('Silahkan masukkan status terbaru\n (tersedia/dipinjam) : ').lower()
                    if updateStatus == 'tersedia' or updateStatus == 'dipinjam' :
                        if updateStatus == 'dipinjam' :
                            namaPeminjam = input('Masukkan Nama Peminjam : ').capitalize()
                            daftarBuku[i].update(
                            {   'status' : updateStatus,
                                'peminjam' : namaPeminjam})
                            show()
                            print("\n\t===DATA BERHASIL DIRUBAH===\t\n")
                        else :
                            daftarBuku[i].update(
                            {   'status' : updateStatus,
                                'peminjam' : '-'})
                            show()
                            print("\n\t===DATA BERHASIL DIRUBAH===\t\n")
                    else :
                        print('\n===STATUS TIDAK VALID===')
                    crossChecker += 1
                    break
            if crossChecker == 0:
                print('\n===BUKU TIDAK DITEMUKAN===')
                

#Function Delete
def delete():
    command = True
    while command != 2 :
        print('''
            Menu menghapus Buku
        1. Hapus Stock Buku
        2. Kembali ke Beranda
        ''')
        command = int(input('Masukkan nomor pilihan menu : '))
        if command == 1 :
            if command == 1 :
                namaBuku = input('Masukkan judul buku : ').upper()
                crossChecker = 0
                for i in range(len(daftarBuku)):
                    if namaBuku in daftarBuku[i].values():
                        print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format('Index', 'Judul Buku', 'Tahun Terbitan', 'Status Pinjaman', 'Nama Peminjam'))
                        print('{}\t| {}\t| {:<15}\t| {:<10}\t\t| {}\t\t|'.format(i, daftarBuku[i]['judul'], daftarBuku[i]['tahunTerbit'], daftarBuku[i]['status'], daftarBuku[i]['peminjam']))
                        crossChecker += 1
                        konfirmasi = input('Apakah yakin ingin menghapus data buku diatas? (y/n) : ')
                        if konfirmasi == 'y':
                            del daftarBuku[i]
                            show()
                            print("\n===DATA BERHASIL TERHAPUS===")
                            break
                if crossChecker == 0:
                    print('\n===BUKU TIDAK DITEMUKAN===')
                    

while True :
    pilihanMenu = int(input('''
        Selamat Datang di Perpustakaan Tarakan
        
        List Menu :
        1. Menampilkan Daftar Buku
        2. Menambah Buku
        3. Update status Buku
        4. Hapus Data Buku
        5. Exit Program
    
        Masukkan angka menu yang ingin dijalankan : '''))
    
    if pilihanMenu == 1 :
        read()
    elif pilihanMenu == 2 :
        create()
    elif pilihanMenu == 3 :
        update()
    elif pilihanMenu == 4 :
        delete()
    elif pilihanMenu == 5 :
        break
    else :
        print('Pilihan yang Anda Masukkan SALAH\n')
