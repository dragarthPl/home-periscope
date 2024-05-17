# Home Periscope

![image](img/home-periscope.png)

## Motivation

The project was initiated because I had a significant problem with the accessibility of the internet module (ecoNET 300) for the VITECO furnace (EG PELLET MINI COMPACT 16 HYBRID) with the PELLAS HYBRID burner. The project is planned to be expanded to automate other household devices (e.g., blinds, lighting, etc.).

## Project Assumptions

- [ ] Reading data from the furnace
  - [x] Reading room temperature
  - [x] Reading water temperature in the furnace
  - [x] Reading domestic hot water (DHW) temperature
  - [x] Reading the furnace operating mode
  - [ ] Reading the flame status
  - [ ] Reading the temperature change schedule
  - [ ] Reading the fan speed
- [ ] Modifying furnace settings
  - [ ] Changing the room temperature
  - [ ] Changing the maximum DHW temperature
  - [ ] Changing the maximum water temperature in the furnace
  - [ ] Changing the furnace operating mode
- [ ] Reading data from the air conditioning
  - [ ] Reading indoor temperature
  - [ ] Reading outdoor temperature
- [ ] Displaying data on a website
- [ ] Automatic furnace control
- [ ] "Placeholder"/demo mode - running the application without communication with the furnace
- [ ] Automatic application testing

## Communication with the Furnace Controller

We communicate with the furnace controller using the RS485 protocol. For this purpose, we use a USB to RS485 converter connected to a Raspberry Pi Zero. We assume two variants of communication with the application:
- [ ] Communication with the application via USB, in which case the application code resides on the Raspberry Pi Zero.
- [ ] Communication with the application via the network, in which case the application code resides on another server.

Additionally, we assume a variant where the application runs with a "placeholder," meaning without communication with the furnace.

- [ ] Placeholder variant

## Materials/Inspiration:

- [Thread on Elektroda](https://www.elektroda.pl/rtvforum/topic3346727.html)
- [Furnace manual](https://www.viteco.pl/pliki/produkty/eg-pellet-mini-compact-16-hybrid/instrukcja-obsugi-eg-pellet-mini-compact-16-hybrid.pdf)
- [Raspberry Pi Zero pinout](https://pinout.xyz/pinout/serial_pi_zero)
- [Econet analyzer](https://github.com/twkrol/econetanalyze)
- [PyPlumIO - native library for communication with the ecoMAX controller](https://github.com/denpamusic/PyPlumIO)
- [PyPlumIO documentation](https://pyplumio.denpa.pro/)
- [ecoNet300 manual](https://thermostahl.ro/wp-content/uploads/2020/08/ecoNET300_DTR_1.0_ENG.pdf)
- [UART configuration on Raspberry Pi](https://www.abelectronics.co.uk/kb/article/1035/serial-port-setup-in-raspberry-pi-os)
- [S.Control 892 manual](https://galmet.com.pl/uploads/productfiles/instrukcja-pellasx-scontrol-892-20042017.pdf)

## Devices Used:

- Raspberry Pi Zero
- USB to RS485 Converter (e.g., [Waveshare USB to RS485](https://www.waveshare.com/usb-to-rs485-b.htm))

## Installing Python on Raspberry Pi in a Different Version Than the Standard

- [Step-by-step guide](https://www.enablegeek.com/tutorial/install-python-on-a-raspberry-pi-step-by-step-guide/)

## Installation and Setup - Raspberry Pi

### Requirements

- Python 3.11
- Redis 7.2.4
- Poetry 1.8.1
- Node.js v20.11.0
- PNPM 8.14.3

### Environment Setup

### Option 1: Raspberry Pi Zero

#### Installing Python 3.11

1. Update the system
```bash
sudo apt-get update
```

2. Install dependencies
```bash
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

3. Download Python 3.11
```bash
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tar.xz
```

4. Install Python 3.11
```bash
tar -xvf Python-3.11.9.tar.xz
cd Python-3.11.9
./configure --enable-optimizations
make -j 2
sudo make altinstall
```

5. Verify the installation
```bash
python3.11 --version
```

#### Installing Redis 7.2.4

1. Download Redis 7.2.4
```bash
wget https://download.redis.io/redis-stable.tar.gz
```

2. Compile and install
```bash
tar -xzvf redis-stable.tar.gz
cd redis-stable
make
sudo make install
```

3. Start Redis
```bash
redis-server
```

#### Installing Poetry 1.8.2

1. Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3.11 -
```

2. Add to PATH
```bash
export PATH="/home/maurycy/.local/bin:$PATH"
```