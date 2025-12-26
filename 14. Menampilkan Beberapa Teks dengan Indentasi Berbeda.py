import textwrap

text1 = "Ini adalah teks pertama."
text2 = "Ini adalah teks kedua."
indented_text1 = textwrap.indent(text1, prefix='> ')
indented_text2 = textwrap.indent(text2, prefix='* ')

print("Teks dengan indentasi berbeda:")
print(indented_text1)
print(indented_text2)
# Fungsi: Mengubah indentasi dari dua teks berbeda dan menampilkannya.
# Kondisi: Ketika Anda ingin menekankan perbedaan antara dua teks.
