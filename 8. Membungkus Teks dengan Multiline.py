import textwrap

sample_text = """Ini adalah kalimat pertama.
Ini adalah kalimat kedua.
Ini adalah kalimat ketiga."""
wrapped_text = textwrap.fill(sample_text, width=50)

print("Teks multiline yang dibungkus:")
print(wrapped_text)
# Fungsi: Membungkus teks multiline dengan lebar tertentu.
# Kondisi: Ketika Anda ingin menampilkan teks yang terbagi dalam beberapa baris.
