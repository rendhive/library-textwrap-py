import textwrap

sample_text = "Ini adalah contoh teks yang sangat panjang dan perlu dibungkus."
wrapped_text = textwrap.wrap(sample_text, width=30)

print("Teks yang dibungkus:")
for line in wrapped_text:
    print(line)
# Fungsi: Membungkus teks menjadi baris-baris dengan panjang maksimum tertentu.
# Kondisi: Ketika Anda ingin menampilkan teks dengan format yang lebih rapi di konsol.
