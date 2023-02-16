# Introduction

Python program in a devcontainer that publish a tooth on Mastodon


# Prerequisites

- Python 3 (allready installed on raspbian lite)
- Pip 3 to install requirements
  - Mastodon.py
- A Mastodon account: don't use your personal account
  - Create a new account
  - In the new account `https://mastodon.social/settings/profile` set "Require follow request" to true.
  - In the new account `https://mastodon.social/settings/profile` set "Htis is a bot account" to true.
  - In the new account `https://mastodon.social/settings/preferences/other` set the posting privacy to "Only Show to followers"
  - Then follow this new account from your personal account.
- A secure MQTT server on internet (dont use a public one). Some free options io.adafruit.com / cloudamqp.com

```bash

$ git clone https://github.com/NakamaLab/mastodon-dev-ontainer.git ./mastodon
$ cd mastodon
$ pip3 install -r requirements.txt
```

# Configuration

Create a `config.json` file with the following data

```json
{
  "mastodon": {
    "access_token": "Application access token",
    "api_base_url": "https://mastodon.social')"
  }
}
```
