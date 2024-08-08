import os
import math
import random
import shutil
from tqdm import tqdm


def kopyala_jpg_dosyalari(kaynak_klasor, hedef_klasor, kopyalanama_oranı = 0.7):
    """
    Belirtilen klasördeki ve alt klasörlerdeki tüm JPG dosyalarını rastgele seçerek
    hedef klasöre kopyalar.

    Args:
        kaynak_klasor: JPG dosyalarının bulunduğu ana klasörün mutlak yolu.
        hedef_klasor: Kopyalanacak dosyaların hedef klasörünün mutlak yolu.
        kopyalanama_oranı: Kopyalanacak dosya oranı (0-1 arasında).
    """

    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)

    toplam_jpg_sayisi = 0
    for root, dirs, files in os.walk(kaynak_klasor):
        for file in files:
            if file.endswith(".jpg"):
                toplam_jpg_sayisi += 1

    kopyalanacak_sayi = math.ceil(toplam_jpg_sayisi*kopyalanama_oranı)

    print(f"\nToplam {toplam_jpg_sayisi} adet JPG dosyası bulundu. "
          f"\nBulunan JPG dosyalarının yaklaşık olarak {kopyalanacak_sayi} kadarı kopyalanacaktır.")
    print(" ")

    # Kullanıcıdan onay alma
    onay = input("Kopyalama işlemine devam etmek istiyor musunuz? (e/h): ")
    if onay.lower() != "e":
        print("İşlem iptal edildi.")
        return

    # tqdm ile ilerleme çubuğu oluştur
    with tqdm(total=toplam_jpg_sayisi, desc="JPG dosyaları kopyalanıyor...", colour='green', unit='MB',
              unit_scale=True) as pbar:
        for root, dirs, files in os.walk(kaynak_klasor):
            for file in files:
                if file.endswith(".jpg"):
                    kaynak_dosya_yolu = os.path.join(root, file)
                    hedef_dosya_yolu = os.path.join(hedef_klasor, file)

                    if random.random() <= kopyalanama_oranı:
                        shutil.copy2(kaynak_dosya_yolu, hedef_dosya_yolu)
                        pbar.update(1)

    print(f"\nToplam {toplam_jpg_sayisi} adet JPG dosyası bulundu.")
    print(f"{pbar.n} adet JPG dosyası kopyalandı.")

# Kodun bulunduğu dizinin iki üst dizini
ana_dizin = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mutlak yolları belirle (Yeni klasör adları ile)
kaynak_klasor = os.path.join(ana_dizin, 'KAYNAK_KLASOR_ADI')
hedef_klasor = os.path.join(ana_dizin, 'HEDEF_KLASOR_ADI')

# Fonksiyonu çalıştıralım
kopyala_jpg_dosyalari(kaynak_klasor, hedef_klasor)
