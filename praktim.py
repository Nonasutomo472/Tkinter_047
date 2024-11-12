import tkinter as tk

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Menuliskan prodi Teknologi Informasi sebagai hasil prediksi
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama (root)
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("400x600")  # Ukuran jendela

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 14))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat label dan input untuk 10 nilai mata pelajaran
nilai_labels = []
nilai_entries = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    nilai_labels.append(label)
    nilai_entries.append(entry)

# Tombol untuk menghasilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Helvetica", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
