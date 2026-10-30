#!/usr/bin/env python3
# Sonsuz Boş Döngü Simülatörü v1.0
# Bu kod gerçekten çalışır ama hiçbir işe yaramaz. Mükemmel.

import time
import random

print("=" * 50)
print("SONSUZ BOŞ DÖNGÜ SİMÜLATÖRÜ")
print("Dünyanın en ciddi anlamsızlık üreticisi")
print("=" * 50)

# İç gizli mesaj (saklı)
_gizli_politik = "secimler onemlidir ama bazen sandiklar yorulur"

print("\nBaşlatılıyor... Lütfen sabırla bekleyin, sonsuzluk yakın.")
time.sleep(1)

for i in range(1, 16):
    anlamsiz = random.choice([
        "Hiçbir şey olmuyor ama oluyor gibi",
        "Boşluk doldu, şimdi daha boş",
        "Zaman geçiyor, döngü dönüyor",
        "Anlam aranıyor... bulunamadı",
        "Vay be, bu kadar boş olabilir mi?"
    ])
    print(f"Döngü #{i}: {anlamsiz}")
    time.sleep(random.uniform(0.3, 0.8))

print("\n" + "=" * 50)
print("SİMÜLASYON TAMAMLANDI")
print("Sonuç: Anlam yok. Ama çok ciddi bir yok.")
print("Hayatın anlamı denemesi:", 42 + random.randint(-5, 5))
print("=" * 50)
print("\nBu programı çalıştırdığın için teşekkürler. Şimdi git çay iç.")
