# Home Periscope

![image](img/home-periscope.png)

## Motywacja

Projekt powstał dlatego że miałem duży problem z osiągalnością modulu internetowego (ecoNET 300)
do pieca VITECO (EG PELLET MINI COMPACT 16 HYBRID) z palnikiem PELLAS HYBRID.
Zakładana jest rozudowa projektu o automatyzacje innych urządzeń w domu (np. rolety, oświetlenie, itp.)

## Założenia projektu

- [ ] Odczyt danych z pieca
  - [ ] Odcztanie temperatury mieszcza
  - [ ] Odczytanie temperatury wody w piecu
  - [ ] Odczytanie temperatury C.W.U.
  - [ ] Odczytanie trybu pracy pieca
  - [ ] Odczytanie stanu płomienia
  - [ ] Odczytanie harmonogramu zmiany temperatury
  - [ ] Odczytanie szybkości obrotów wentylatora
- [ ] Modyfikacja ustawień pieca
  - [ ] Zmiana temperatury mieszczą
  - [ ] Zmiana temperatury max temperatury C.W.U.
  - [ ] Zmiana temperatury max wody w piecu
  - [ ] Zmiana trybu pracy pieca
- [ ] Wyświetlanie danych na na stronie internetowej
- [ ] Automatyczne sterowanie piecem
- [ ] Tryb "zaślepki"/demo - uruchomienie aplikacji bez komunikacji z piecem
- [ ] Automatyczne testoanie aplikacji

## Komunikacja z sterownikiem pieca

Ze sterownikiem pieca komunikujemy się za pomocą protokołu RS485. W tym celu wykorzystujemy konwerter USB - RS485, podłączony do Raspberry Pi Zero.
Zakładamy dwa warianty komunikacji z aplikacją: 
- [ ] Komunikacja z aplikacją za pomocą USB, w tym wariancie kod aplikacji znajduje się na Raspberry Pi Zero
- [ ] Komunikacja z aplikacją za pomocą sieci, w tym wariancie kod aplikacji znajduje się na inny serwerze

Dodatko zakładamy warian uruchomienia aplikaji z "zaślepką", czyli bez komunikacji z piecem.

- [ ] Wariant z "zaślepką"

## Materiały/Inspiracje:

 - [Wątek na elektordzie] (https://www.elektroda.pl/rtvforum/topic3346727.html)
 - [Instrukcja pieca] (https://www.viteco.pl/pliki/produkty/eg-pellet-mini-compact-16-hybrid/instrukcja-obsugi-eg-pellet-mini-compact-16-hybrid.pdf)
 - [Rozkład pinów Raspberry Pi Zero] (https://pinout.xyz/pinout/serial_pi_zero)
 - [Analizator Econet] (https://github.com/twkrol/econetanalyze)
 - [PyPlumIO - natywna biblioteka do komunikacji z kontolerem ecoMAX ] (https://github.com/denpamusic/PyPlumIO)
 - [Dokumentacja PyPlumIO] (https://pyplumio.denpa.pro/)
 - [ecoNet300 - instrukcja] (https://thermostahl.ro/wp-content/uploads/2020/08/ecoNET300_DTR_1.0_ENG.pdf)
 - [Konfiguracja UART na malince] (https://www.abelectronics.co.uk/kb/article/1035/serial-port-setup-in-raspberry-pi-os)
 - [Instrukcja S.Control 892] (https://galmet.com.pl/uploads/productfiles/instrukcja-pellasx-scontrol-892-20042017.pdf)

## Wykorzystane urządzenia:

 - Raspberry Pi Zero
 - Konwerter USB - RS485 (np. https://www.waveshare.com/usb-to-rs485-b.htm)

## Instalacja python na raspbery pi w innej wersji niż standardowa 

 - https://www.enablegeek.com/tutorial/install-python-on-a-raspberry-pi-step-by-step-guide/

## Instalaja i uruchomienie - raspbery pi

### Wymagania

- Python 3.11
- Redis 7.2.4
- poetry 1.8.1
- nodejs v20.11.0
- pnpm 8.14.3

### Przygotowanie środowiska

### Opcja 1. Raspberry Pi Zero

#### Instalcja Python 3.11

1. Aktualzacja systemu
```bash
sudo apt-get update
```

2. Instalacja zależności
```bash
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

3. Pobranie Python 3.11
```bash
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tar.xz
```

4. Instalacja Python 3.11
```bash
tar -xvf Python-3.11.9.tar.xz
cd Python-3.11.9
./configure --enable-optimizations
make -j 2
sudo make altinstall
```

5. Veryfikacja instalacji
```bash
python3.11 --version
```

#### Instalacja Redis 7.2.4

1. Pobrać Redis 7.2.4
```bash
wget https://download.redis.io/redis-stable.tar.gz
```

2. Kompliacja i instalacja
```bash
tar -xzvf redis-stable.tar.gz
cd redis-stable
make
sudo make install
```

3. Uruchomienie Redis
```bash
redis-server
```

#### Instalacja poetry 1.8.2

1. Instalacja poetry
```bash
curl -sSL https://install.python-poetry.org | python3.11 -
```

2. Dodanie do PATH
```bash
export PATH="/home/maurycy/.local/bin:$PATH"
```
