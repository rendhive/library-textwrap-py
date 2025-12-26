import textwrap

sample_text = "Ini adalah teks yang panjang namun akan dibungkus."
wrapped_text = textwrap.fill(sample_text, width=30)

print("Panjang teks setelah pembungkusan:")
print(len(wrapped_text))
# Fungsi: Menghitung panjang dari teks yang telah dibungkus.
# Kondisi: Ketika Anda perlu mengetahui ukuran setelah pembungkusan.
