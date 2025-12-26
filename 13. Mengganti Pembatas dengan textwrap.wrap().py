import textwrap

sample_text = "Bunga, Matahari, Lautan, Bulan"
wrapped_text = textwrap.wrap(sample_text, width=20)

print("Teks yang dibungkus dengan pembatas baru:")
for line in wrapped_text:
    print('- ' + line)
# Fungsi: Mengganti pembatas sebelum menampilkan hasilnya.
# Kondisi: Ketika Anda ingin memperindah tampilan output.
