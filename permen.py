permen = [("Permen Coklat", 30000), ("Permen Strawberry", 35000), ("Permen Vanilla", 42000), ("Permen Karet", 10000), ("Permen Melon", 34000)]

def list_permen():
  print("Tersedia Permen:")
  for i, p in enumerate(permen):
    print(f"{i+1}. {p[0]} - Rp{p[1]}")

def pembelian():
  list_permen()

  jenis_permen = int(input("Masukkan angka sesuai urutan permen yang diinginkan: "))
  banyak_permen = int(input("Masukkan jumlah permen yang diinginkan: "))

  cari_permen = permen[jenis_permen -1]

  total_harga = cari_permen[1] * banyak_permen

  print(f"Total harga: Rp{total_harga}")

pembelian()