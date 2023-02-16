# Introduction

Python program that listens to a MQTT topic and publish a still image or an animated gif to twitter.

**WORK IN PROGRESS**

# Prerequisites

- A raspberry pi / zero with raspbian lite
- Python 3 (allready installed on raspbian lite)
- Pip 3 to install requirements
  - picamera
  - Mastodon.py
  - systemd
  - paho-mqtt
- A Mastodon account: don't use your personal account
  - Create a new account
  - In the new account `https://mastodon.social/settings/profile` set "Require follow request" to true.
  - In the new account `https://mastodon.social/settings/profile` set "Htis is a bot account" to true.
  - In the new account `https://mastodon.social/settings/preferences/other` set the posting privacy to "Only Show to followers"
  - Then follow this new account from your personal account.
- A secure MQTT server on internet (dont use a public one). Some free options io.adafruit.com / cloudamqp.com

```bash
$ sudo apt-get update
$ sudo apt-get -y install python3-pip python3-picamera git imagemagick
$ cd ~
$ git clone https://github.com/NakamaLab/nkm-pi-cam ./cam
$ cd cam
$ pip3 install -r requirements.txt
```

# Configuration

Create a `config.json` file with the following data

```json
{
  "mastodon": {
    "access_token": "Application access token",
    "api_base_url": "https://mastodon.social')"
  },
  "mqtt": {
    "server": "a.server.cloudamqp.com",
    "port": 1883,
    "user": "username",
    "pass": "a_passwrod",
    "topic": "home/nkm-pi-cam/command"
  }
}
```

# Running as a Service

```bash
$ sudo cp ~/cam/nkm-pi-cam.service /etc/systemd/system
$ systemctl enable nkm-pi-cam
$ systemctl start nkm-pi-cam
# view logs
$ journalctl -u nkm-pi-cam
```

Uninstall

```bash
$ systemctl stop nkm-pi-cam
$ systemctl disable nkm-pi-cam
```
