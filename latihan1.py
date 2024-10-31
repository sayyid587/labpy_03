from random import random

n = int(input("Masukkan nilai N: "))

for i in range(1, n + 1):
  angka_acak = random()
  print(f"data ke: {i} => {angka_acak}")

print("Selesai")