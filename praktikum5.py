#mengimpor library Tkinter untuk membuat GUI
import tkinter as tk
from tkinter import messagebox  #untuk menampilkan pesan

#fungsi untuk memproses prediksi berdasarkan input nilai
def hasil_prediksi():
    try:
        #loop untuk setiap entry pada list 'entries'
        for entry in entries:
            nilai = int(entry.get())  #menginput dan mengubahnya menjadi int
            #memeriksa apakah nilai antara 0 dan 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")  #menampilkan error jika nilai tidak benar
            #jika input benar, maka akan menampilkan hasil prediksi
            hasil_label.config(text="Prediksi Prodi : Teknologi Informasi")
    except ValueError as ve:
        #menampilkan pesan error jika input tidak benar 
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

#membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  #menentukan judul jendela aplikasi
root.geometry("500x600")  #mengatur ukuran jendela aplikasi
root.configure(bg="#f0f0f0")  #mengatur warna latar belakang jendela aplikasi

#membuat label untuk judul aplikasi
judul_label = tk.Label(root, text= "Aplikasi Prediksi Prodi Pilihan", font=("Arial", 12)) 
judul_label.pack(pady=20)  #menampilkan label dengan jarak 20

#membuat frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)  #menampilkan frame dengan jarak 10

#membuat list untuk menyimpan entry nilai
entries = []
#membuat 10 input nilai
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12))  #label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  #menampilkan label dalam grid
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  #entry untuk input nilai
    entry.grid(row=i, column=1, padx=10, pady=5)  #menampilkan entry dalam grid
    entries.append(entry)  #menambahkan entry ke dalam list 'entries'

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=30)  #menampilkan tombol dengan jarak 30

hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue")  
hasil_label.pack(pady=20)  #menampilkan label hasil prediksi dengan jarak 20

root.mainloop()  #menjalankan loop aplikasi untuk menunggu interaksi pengguna
