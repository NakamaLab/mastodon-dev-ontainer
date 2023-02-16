#!/usr/bin/python
# como correr como servicio https://www.raspberrypi.org/forums/viewtopic.php?t=197513

import os
import json
import datetime
from mastodon import Mastodon

file_dir = os.path.dirname(os.path.realpath('__file__'))
config_file_name = os.path.join(file_dir, 'config.json')

with open(config_file_name) as config_file:
    config = json.load(config_file)


access_token = config['mastodon']['access_token']
api_base_url = config['mastodon']['api_base_url']


api = Mastodon(access_token=access_token,api_base_url=api_base_url)


# If the authentication was successful, you should
# see the name of the account print out
print(api.account_verify_credentials())

api.toot('Tooting from Python using #mastodonpy !' +
         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
