print("Kontrol Yapılıyor")


try:
    from colorama import init
    init()
    from colorama import Fore, Style
    print(Fore.GREEN + "Kurulum tamamlandı!" + Style.RESET_ALL)
except ImportError:
    print("Gerekli kütüphaneler bulunamadı. Kurulum yapılıyor...")
    import os
    os.system("pip install colorama")
    print("Gerekli kurulumlar başarıyla yapıldı program açılıyor!")
    print("")
print(Fore.LIGHTMAGENTA_EX)
print("---------------------------------------------------------------------------------------------------------------")
import time
from colorama import Fore, init
while True:
    print("Birinci Senaryoya Hoşgeldiniz")
    print(Fore.LIGHTRED_EX)
    print("Merhaba Bir E-posta Aldınız!")
    print(Fore.LIGHTGREEN_EX)
    print("Gönderici: support@example.com")
    print("Konu: Hesap Güvenliği ve Bilgilerin Güncellenmesi.")
    print("İçerik: Hesabınızda Şüpheli Giriş Bulunmuştur, Hesabınızı Güvence Altına Almak İçin Aşşağıdaki Linke Tıklayınız.")
    print(Fore.LIGHTBLUE_EX)
    cevap = input("Size Bu E-posta Güvenilir Geliyor mu? (evet/hayır): ").lower()
    if cevap == "hayır":
        print("Harika şüpheli e-postaları ayırt edebiliyorsunuz, Tebrikler!")
        print("Çıkış Yapılıyor...")
        time.sleep(1.5)
        exit()
    if cevap == "evet":
        print("Üzgünüm, Bu e-posta bir phishing saldırısı olabilir lütfen daha dikkatli olun!")
        print("Tekrar denemek için biraz bekleyiniz ")
        time.sleep(2)
