scraper1.py - 1 söz və ya cümlə ilə google -da image search edib download edən skript

İstifadəsi: 
-source kodda 'searchterm' dəyişkəninin dəyərini axtarmaq istədiyiniz sözə uyğun dəyişin.Əgər söz birləşməsi və ya cümlə axtarmaq istəyirsizsə onda hər sözün arasında '+' işarəsi qoyun
-scrape olunan fayllar skriptlə eyni folderdə yaranacaq adı 'searchterm' dəyərinin qiyməti olan folderdə olacaq
    
------------------------------------------------------------------------------------------------------------------------------

uploader.py - download olunmuş faylları s3 ə upload edən fayl

İstifadəsi:
-[bucketname] aws s3 bucket adı
- 7. sətrdə os.chdir(['download olan şəkillərin folder ünvanı'])
