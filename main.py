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
            print("Üçüncü senaryoya geçiş yapılıyor!")
            third_scenario()
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
    puan = 0
    
    
    
    print(Fore.LIGHTYELLOW_EX)
    print("Üçüncü Senaryoya Hoşgeldiniz!(Sınav)")
    print("10 Soruda 80 Puan veya Üstü Almanız Gerekmektedir")
    print(Fore.LIGHTCYAN_EX)
    print("Siber Güvenlik İçin En Yaygın Olarak Kullanılan İşletim Sistemi Nedir?")
    print("""
    1)KaliLinux
    2)Windows
    3)Linux
    4)MacOS
    """)
    cevapla1 = input("Cevabınız nedir? 1/2/3/4: ")
    if cevapla1 == "1":
        print("Doğru Cevap!")
        puan += 20
    if cevapla1 == "2":
        print("Yanlış Cevap!")
    if cevapla1 == "3":
        print("Yanlış Cevap!")
    if cevapla1 == "4":
        print("Yanlış Cevap")
    print("Hangisi Siber Güvenlikte Kullanılan Bir Tool Değildir?")
    print("""
    1)CMD
    2)Nmap
    3)Gobuster
    4)BruteSploit
    """)
    cevapla2 = input("Cevabınız nedir? 1/2/3/4: ")
    if cevapla2 == "1":
        print("Doğru Cevap!")
        puan += 20
    if cevapla2 == "2":
        print("Yanlış Cevap!")
    if cevapla2 == "3":
        print("Yanlış Cevap!")
    if cevapla2 == "4":
        print("Yanlış Cevap!")
    print("Aşşağıdakilerden Hangisi Daha Güçlü Bir Paroladır")
    print("""
    1) kaan1232002
    2) AsqDx6.1!
    3) 123456
    4) alı1907A
    """)
    cevapla3 = input("Cevabınız nedir? 1/2/3/4: ")
    if cevapla3 == "1":
        print("Yanlış Cevap!")
    if cevapla3 == "2":
        print("Doğru Cevap!")
        puan += 20
    if cevapla3 == "3":
        print("Yanlış Cevap!")
    if cevapla3 == "4":
        print("Yanlış Cevap!")
    print("Aşşağıdakilerden Hangisi Zararlı Yazılım Değildir?")
    print(""""
    1)Trojan
    2)Malware
    3)Router
    4)Worm
    """)
    cevapla4 = input("Cevabınız Nedir? 1/2/3/4: ")
    if cevapla4 == "1":
        print("Yanlış Cevap!")
    if cevapla4 == "2":
        print("Yanlış Cevap!")
    if cevapla4 == "3":
        print("Doğru Cevap!")
        puan += 20
    if cevapla4 == "4":
        print("Yanlış Cevap!")
    print("Aşşağıdakilerden Hangisi Bir Ağ Topolojisi Değildir?")
    print("""
    1)Bus
    2)Star
    3)Ring
    4)Modem
    """)
    cevapla5 = input("Cevabınız Nedir? 1/2/3/4: ")
    if cevapla5 == "1":
        print("Yanlış Cevap!")
    if cevapla5 == "2":
        print("Yanlış Cevap!")
    if cevapla5 == "3":
        print("Yanlış Cevap!")
    if cevapla5 == "4":
        print("Doğru Cevap!")
        puan += 20
    print("Toplam Puan: "+ str(puan))
    if int(puan) > 79:
        print("Test Bitmiştir, Kazandınız!")
        print("Çıkış Yapılıyor...")
        time.sleep(1.5)
        exit()
    else:
        print("Testi Geçemediniz, Kaybettiniz")
        print("Çıkış Yapılıyor...")
        time.sleep(1.5)
        exit()
if __name__ == "__main__":
    first_scenario()
