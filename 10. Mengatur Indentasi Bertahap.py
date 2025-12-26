import textwrap

sample_text = "Mengatur indentasi bertahap menggunakan textwrap."
indented_text = textwrap.indent(sample_text, prefix='-- ', indent_first=False)

print("Teks dengan indentasi bertahap:")
print(indented_text)
# Fungsi: Menerapkan indentasi hanya untuk baris setelah baris pertama.
# Kondisi: Ketika Anda ingin membuat struktur teks yang bertahap.
