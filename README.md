# Bilinmesi gerekenler:
* Program çalışıtırldığında kendisiyle **aynı konumda olan her şeyi** farklı bir konuma taşıyacaktır o yüzden denerken mutlaka yeni bir klasör açın onun içindeyken deneyin.
* Programın amacı bilgisayara zarar vermek değil sadece kullanıcıyı sinir etmektir.
>DOOM.exe, DOOM.py'nin exeye dönüştürülmüş halidir. Dolayısıyla Exe'ye basıldığında ne olduğunu merak ediyorsanız DOOM.py'yi inceleyebilirsiniz.
>Projenin son halini (yemlemeye hazır halini) Releases kısmından indirebilirsinz.

# Gerekli olanlar neler?
* DOOM klasörü
* DOOM.exe

 **Fakat bunların aynı konumda olması gerekiyor !**
 
 >NOT: Dosyalardaki DOOM.py bir değişiklik lazım olursa kodu düzenlemek için orada yani artık işlevi yok.
 
 # Nasıl Çalışıyor?
 * DOOM.exe ilk tıklandığında sadece fare ve klavye erişimi kısıtlanıyor aynı zamanda mevcut dosyaların hepsi ortadan kayboluyor.
 * Bilgisayar her açıldığında virüs tekrar başlayarak önce bilgilendirme yazısı ardından da oyun açılıyor.
 Oyun bitirildiği takdirde virüs bütün erişim kısıtlarını kaldırıyor ve kullanıcı artık özgürce bilgisayarını kullanabiliyor.
 
 >Virüs silinmediği takdirde her bilgisayar açılışında tekrar başlatılacaktır.
 
 # Hangi dosya nereye gidiyor?
 * DOOM.exe'ye tıklandığında mevcut klasörde ne kadar dosya varsa DOOM.exe hariç hepsini "C:/Users/\<kullanici adi>/Doomed" yoluna taşıyor.
 * DOOM.exe ise win+r yapıp "shell:startup" yazdığında çıkan yere kendini taşıyor.
 
 # Kurtulma Yolları:
 * Dosyaların yerini bulup silerek. Tabii bunun için oyunu bitirmeniz gerekecek.
 * "hesoyam" yazdıktan sonra "Space" ya da "Enter" tuşuna basarsanız klavye ve fare kısıtlamaları ortadan kalkacaktır.

<html>

<head></head>
<body>
<img src="data:image/png;base64,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">
</body>
</html>
