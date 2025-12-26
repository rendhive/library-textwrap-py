import textwrap

text = "Teks ini akan dibungkus dan diindikasikan."
wrapped_text = textwrap.fill(text, width=30)
indented_text = textwrap.indent(wrapped_text, '> ')

print("Teks yang dibungkus dan diindikasikan:")
print(indented_text)
# Fungsi: Menggabungkan pembungkusan dan indentasi untuk menghasilkan format yang lebih baik.
# Kondisi: Ketika Anda ingin menampilkan potongan teks yang dipresentasikan dengan rapi.
