## Django’da Küreselleştirme (Internationalization)

[Django’da Küreselleştirme Medium Blog Post](https://medium.com/@umit.ozturk.9716/djangoda-yerelle%C5%9Ftirme-localization-ve-k%C3%BCreselle%C5%9Ftirme-internationalization-32b2adddb1b6)'u için


```
mkdir ~/translate && cd ~/translate 
virtualenv -p python3 env 
source env/bin/activate
pip install -r requirements.txt

python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver
```


dil seçeneği oluşturmak için
```
django-admin.py makemessages -l tr 
django-admin.py makemessages -l en
```

.po dosyalarını değiştirdikten sonra
```
django-admin.py compilemessages 
```
![](https://cdn-images-1.medium.com/max/800/1*3Ubc1tzzjEaU5KxgspvRJw.jpeg)


![](https://cdn-images-1.medium.com/max/800/1*NUjtZgry6R-_5ltoP4bE5Q.jpeg)



![](https://cdn-images-1.medium.com/max/800/1*isQbl1un9FfrfFugHD8xhw.jpeg)


![](https://cdn-images-1.medium.com/max/800/1*ZAS2c-M5RLf08slhCYjA1Q.jpeg)


## License

MIT © [Ümit Öztürk](https://twitter.com/__umitozturk__)