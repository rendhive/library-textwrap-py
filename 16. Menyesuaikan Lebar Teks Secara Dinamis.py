import textwrap

def custom_wrap(text, width):
    return textwrap.fill(text, width=width)

sample_text = "Teks ini akan dibungkus dengan lebar yang dinamis."
print("Teks yang dibungkus dengan lebar 40:")
print(custom_wrap(sample_text, 40))
# Fungsi: Membungkus teks dengan width yang dapat dikustomisasi.
# Kondisi: Ketika Anda ingin mengubah lebar berdasarkan situasi yang berbeda.
