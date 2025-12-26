import textwrap

items = ["Item 1", "Item 2", "Item 3"]
formatted_list = textwrap.fill('\n'.join(f'- {item}' for item in items), width=30)

print("Daftar bulleted:")
print(formatted_list)
# Fungsi: Membungkus daftar item dengan format bulleted.
# Kondisi: Ketika Anda ingin menampilkan item dengan format yang rapi.
