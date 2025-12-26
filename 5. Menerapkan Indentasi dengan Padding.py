import textwrap

sample_text = "Menggunakan padding di setiap baris."
indented_text = textwrap.indent(sample_text, prefix='* ', indent_first=True)

print("Teks dengan padding pertama:")
print(indented_text)
# Fungsi: Menambahkan indentasi di baris pertama.
# Kondisi: Ketika Anda ingin menyoroti baris pertama dengan cara berbeda.
