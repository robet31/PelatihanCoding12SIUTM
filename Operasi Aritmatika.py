# Input dari pengguna
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

# Exponen/pangkat
exponen = a ** b

# Perkalian
kali = a * b

# Pembagian
bagi = a / b

# Modulus
modulus = a % b

# Floor Division
floor = a // b

# Penjumlahan
jumlah = a + b

# Pengurangan
kurang = a - b

# Menampilkan hasil
print(f'{a} ** {b} = {exponen}')
print(f'{a} * {b} = {kali}')
print(f'{a} / {b} = {bagi}')
print(f'{a} % {b} = {modulus}')
print(f'{a} // {b} = {floor}')
print(f'{a} + {b} = {jumlah}')
print(f'{a} - {b} = {kurang}')
