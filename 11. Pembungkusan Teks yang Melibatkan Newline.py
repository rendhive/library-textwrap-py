import textwrap

sample_text = "Baris pertama\nBaris kedua\nBaris ketiga"
wrapped_text = textwrap.fill(sample_text, width=25)

print("Teks dengan newline yang dibungkus:")
print(wrapped_text)
# Fungsi: Membungkus teks yang memiliki newline di dalamnya.
# Kondisi: Ketika Anda ingin menampilkan teks format multiline dengan pembungkusan.
