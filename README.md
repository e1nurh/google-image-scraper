Google-Image-Scraper Documentation

Haqqında:

Yazmış olduğum scraper google images -də daxil etdiyimiz söz və ya söz birləşməsini axtarır və uyğun şəkilləri daxil etdiyimiz sözə uyğun olaraq yaratdığı qovluğa download edir.

Project linki:
	https://github.com/mrelick/google-image-scraper

İstifadəsi: 
1.Projecti clone edək 
	- git clone https://github.com/mrelick/google-image-scraper.git
2.Projecti clone etdiyimiz qovluğa gedək 
	- cd datasetbuilder
3.virtual environment imizi yaradaq, aktiv edib və lazım olan modulları quraşdıraq
	- virtualenv datasetenv
	- datasetenv\Scripts\activate
	- pip install -r requirements.txt
4.Scriptimizi çalışdıraq
	- python scraper.py -s [axtarmaq_istədiyimiz_söz]

NOTE: [axtarmaq_istədiyimiz_söz] ifadəsinin yerinə axtarmaq istədiyiniz sözü yazmalısınız.Əgər axtarmaq istədiyimiz söz yox sözlər birləşməsidirsə o zaman hər sözün arasına + işarəsi qoyulmalıdır. Məsələn: python+proqramlaşdırma+dili

python scraper.py -s python+proqramlaşdırma+dili

NOTE: Əgər download prosesi bitdikdən sonra bütün şəkillərin S3 bucket ə upload olunmasını istəyiriksə əlavə olaraq -b və -d argumentlərini commanda əlavə etməliyik.Burada -b S3 Bucket Name -d isə download olunmuş şəkillərin qovuğunun adıdır.Məsələn:
python scraper.py -s [axtarmaq_istədiyimiz_söz] -b [bucket_adı] -d [directory]
	5.Bitdi

