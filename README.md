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

