import textwrap

sample_text = "Teks ini sangat panjang dan harus dipotong."
shortened_text = textwrap.shorten(sample_text, width=30, placeholder="...")

print("Teks yang dipotong:")
print(shortened_text)
# Fungsi: Memotong teks dan menambahkan placeholder.
# Kondisi: Ketika Anda perlu membatasi panjang tampilan teks tanpa kehilangan makna.
