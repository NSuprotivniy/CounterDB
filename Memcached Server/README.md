# Memcached Server

Django сервер, реализующий систему хранения счётчика лайков. В качестве хранилища используется key-value база данных Memcached.

Используются JSON ответы на сохранение и получение счётчика по идентификатору поста, получаемого из URL.

```
GET http:\\example.com\1\save
GET http:\\example.com\1\get
```
``` json
{
	"post_id":2,
    "counter":34
}
```


## Пакеты

* django [https://www.djangoproject.com/](https://www.djangoproject.com/)

Установка [https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)

```
sudo apt-get install python3-pip
sudo pip3 install django
```

* memcached [https://memcached.org/](https://memcached.org/)

Установка [https://www.liquidweb.com/kb/how-to-install-memcached-on-ubuntu-14-04-lts/](https://www.liquidweb.com/kb/how-to-install-memcached-on-ubuntu-14-04-lts/)

```
sudo apt-get install memcached
memcached -h
```

* libmemcached
```
sudo apt-get install libmemcached-dev zlib1g-dev
```

* pylibmc [https://github.com/django-pylibmc/django-pylibmc](https://github.com/django-pylibmc/django-pylibmc)
```
pip3 install django-pylibmc
```

* python-memcached [https://github.com/pinterest/pymemcache](https://github.com/pinterest/pymemcache)

Не обязательно для работы приложения.

```
pip3 install python3-memcached
```

## Запуск

```
python manage.py createcachetable
python manage.py runserver
```