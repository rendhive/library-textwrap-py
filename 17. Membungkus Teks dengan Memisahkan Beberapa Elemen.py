import textwrap

text = "Ini adalah contoh kalimat panjang! " \
       "Kita akan membuatnya lebih pendek dengan membungkusnya."
wrapped_text = textwrap.fill(text, width=40)

print("Teks yang dibungkus:")
print(wrapped_text)
# Fungsi: Membungkus teks yang terdiri dari beberapa kalimat.
# Kondisi: Ketika Anda ingin menampilkan informasi padat dengan jelas.
