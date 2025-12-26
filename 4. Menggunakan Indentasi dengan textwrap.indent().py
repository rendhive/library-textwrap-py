import textwrap

sample_text = "Teks ini akan diindikasikan setiap barisnya."
indented_text = textwrap.indent(sample_text, prefix='> ')

print("Teks yang diindikasikan:")
print(indented_text)
# Fungsi: Menambahkan prefiks ke setiap baris dari teks.
# Kondisi: Ketika Anda ingin membuat teks lebih terstruktur dengan penanda khusus.
