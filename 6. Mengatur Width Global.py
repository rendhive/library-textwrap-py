import textwrap

textwrap_width = 40
sample_text = "Teks ini terlalu panjang untuk tampil tanpa dibungkus."
wrapped_text = textwrap.fill(sample_text, width=textwrap_width)

print("Teks yang dibungkus dengan width global:")
print(wrapped_text)
# Fungsi: Mengatur lebar global dan membungkus teks sesuai dengan itu.
# Kondisi: Ketika Anda ingin menggunakan `width` yang konsisten di beberapa tempat.
