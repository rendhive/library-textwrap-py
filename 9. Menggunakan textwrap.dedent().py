import textwrap

sample_text = """
    Ini adalah contoh teks dengan indentasi.
    Kami akan menghapus indentasi ini.
"""
dedented_text = textwrap.dedent(sample_text)

print("Teks setelah menghapus indentasi:")
print(dedented_text)
# Fungsi: Menghapus indentasi dari teks yang memiliki indentasi yang tidak diinginkan.
# Kondisi: Ketika Anda ingin membersihkan teks yang memiliki indentasi berlebih.
