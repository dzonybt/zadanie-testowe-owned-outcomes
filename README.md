# Crawler - zadanie testowe
autor: Rafał Rakowski (dzonybt@gmail.com)

Crawler oparty na docker-compose, django rest framework, Celery i BeatifullSoap4.
Dodatkowe biblioteki: Django Suit, Flower

## Działanie
Na podstawie zadanej frazy i ilości podstron program pobiera adresy z wyników wyszukiwania google. Pobieranie adresów realizowane jest przez worker Celery.

## Wersje
* v2 (2017-01-30) - workery przeszukują po 10 podstron  
* v1 (2017-01-24) - wprowadzanie frazy tylko przez django rest framework; podstrony wyszukiwania realizowane są przez taski (tylko jeden kontener)  

## Uruchamianie kontenerów
```shell
docker-compose up
```

## Dostęp do Flower
```shell
<host-IP>:5555
```

## Tworzenie dodatkowych workerów Celery
```shell
docker-compose scale worker=<+INT>
```
