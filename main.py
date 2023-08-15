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

def first_scenario():
    while True:
        print("Birinci Senaryoya Hoşgeldiniz")
        print(Fore.LIGHTRED_EX)
        print("Merhaba Bir E-posta Aldınız!")
        print(Fore.LIGHTGREEN_EX)
        print("Gönderici: support@example.com")
        print("Konu: Hesap Güvenliği ve Bilgilerin Güncellenmesi.")
        print("İçerik: Hesabınızda Şüpheli Giriş Bulunmuştur, Hesabınızı Güvence Altına Almak İçin Aşşağıdaki Linke Tıklayınız.")
        print("Link: www.sifredegistirme123.com")
        print(Fore.LIGHTBLUE_EX)
        cevap = input("Size Bu E-posta Güvenilir Geliyor mu? (evet/hayır): ").lower()
        if cevap == "hayır":
            print("Harika şüpheli e-postaları ayırt edebiliyorsunuz, Tebrikler!")
            print("İkinci senaryoya geçiş yapılıyor...")
            time.sleep(1.5)
            second_scenario()  # İkinci senaryoya geçiş yapılıyor
            break
        if cevap == "evet":
            print("Üzgünüm, Bu e-posta bir phishing saldırısı olabilir lütfen daha dikkatli olun!")
            print("Tekrar denemek için biraz bekleyiniz ")
            time.sleep(2)
print("-----------------------------------------------------------------------------------------------------------------")



def second_scenario():
    while True:
        print("İkinci Senaryoya Hoşgeldiniz")
        print(Fore.LIGHTCYAN_EX)
        print("Güvenli bağlantıyı seçmelisiniz!")
        print(Fore.LIGHTGREEN_EX)
        print("www.google.com")
        print("www.securebank.xyz")
        print("www.notsecurebank.net")
        cevap1 = input("Hangi bağlantı güvenli geliyor? (1/2/3): ")
        if cevap1 == "1":
            print("Doğru cevap!, bu konuda cidden iyisiniz")
            print("Üçüncü senaryoya geçiş yapılıyor! (3. senaryo daha gelmedi :))")
            break
        if cevap1 == "2":
            print("Yanlış seçim yaptınız lütfen tekrar deneyiniz!")
            print("Tekrar denemek için biraz bekleyin")
            time.sleep(1.5)
        if cevap1 == "3":
            print("Yanlış seçim yaptınız lütfen tekrar deneyiniz!")
            print("Tekrar denemek için biraz bekleyin")
            time.sleep(1.5)
def third_scenario():
    print("Üçüncü Senaryoya Hoşgeldiniz!")
    print(Fore.LIGHTCYAN_EX)
    print("Geliştirilme Aşamasında...")




if __name__ == "__main__":
    first_scenario()
