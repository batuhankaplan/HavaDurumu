import requests


def hava_durumu_getir(sehir):
    api_anahtari = "789ce68eeb2b7fa82de2597168070c77"  # Senin API anahtarın
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # İstek URL'sini oluştur
    tam_url = base_url + "appid=" + api_anahtari + "&q=" + sehir + ",TR&lang=tr&units=metric"


    # API'ye istek gönder
    response = requests.get(tam_url)

    # Yanıtı kontrol et
    if response.status_code == 200:
        veri = response.json()


        ana_bilgiler = veri['main']
        sicaklik = ana_bilgiler['temp']
        hissedilen = ana_bilgiler['feels_like']
        nem = ana_bilgiler['humidity']
        hava_bilgisi = veri['weather'][0]['description']

        print(f"{sehir} için hava durumu:")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Hissedilen sıcaklık: {hissedilen}°C")
        print(f"Nem oranı: {nem}%")
        print(f"Hava durumu: {hava_bilgisi}")

    else:
        # Hata kodu ve gelen yanıtı yazdır, böylece neden hata olduğunu görebilirsiniz
        print(f"Şehir bulunamadı veya başka bir hata oluştu. Hata kodu: {response.status_code}")


# Kullanıcıdan şehir ismi al ve hava durumunu getir
def ana_menu():
    while True:
        print("\nTürkiye'deki şehirlerin hava durumunu öğrenmek için şehir ismini girin.")
        print("Çıkmak için 'q' yazın.")

        sehir = input("Şehir ismi: ").capitalize()

        if sehir.lower() == 'q':
            print("Programdan çıkılıyor.")
            break
        else:
            hava_durumu_getir(sehir)


# Programı başlat
ana_menu()
