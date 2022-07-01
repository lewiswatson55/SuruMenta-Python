# Suru-Menta
 A simple bot using discord.py to directly message a predetermined user for logging, debugging, and monitoring of remote systems.

## Dependencies - see requirements.txt
  [Discord.py](https://discordpy.readthedocs.io/)

# Usage
Basic CLI Usage

```
$ python SuruMenta.py "Message Here"
```

Usage within a python script

``` python
 import SuruMenta as sm
 sm.run_bot("Alert!")
```

# Configuration and Set Up
  Note 0: Please remember that even though discord sends messages over HTTPS, your messages are not necessarily secure so please only use this code for status alerts and non-sensitive information.

  Note 1: Please ensure you have discord.py

  Note 2: You will need to add your bot to a discord server that your user is in so it is able to DM you (steps below) - this server can be blank with just your user and bot.

  Note 3: Discord developer bot setup changes often so please check the discord developer documentation for the latest changes.

## Setting Up Discord Bot Account:
  1. Log into Discord's developer portal.

  2. Click on New Application and select a username.

  3. Under settings select Bot > Add Bot > Yes, Do it!

  4. Copy your bots token and keep it for later.

  5. Navigate to OAuth2 in settings tab and under scopes select 'bot'.

  6. Select Administrator under permissions tab.

  7. Press 'Copy' and paste into browser in another tab, then add bot to your server.

  That's your bot account set up.

## Configuring Code:
  1. Get your Discord UserID by right-clicking your username and selecting 'Copy ID'.

  2. Paste your UserId in place of "1234567890" in the botconfig.json files.

  3. Using the token saved from Step 4 of 'Setting Up Discord Bot Account' replace "changemeToken" in botconfig.json to your bot accounts token.

  4. Test the code is working - see 'Usage' section.


# Author and Acknowledgements

  See [original DiscordJS implementation here.](https://github.com/lewiswatson55/Suru-Menta/)

  Created by: [Lewis N Watson](https://github.com/lewiswatson55/)