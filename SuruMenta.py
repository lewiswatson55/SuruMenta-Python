# SuruMenta Python
## Description: A simple bot using discord.py to directly message a predetermined user for logging, debugging, and monitoring of remote systems.
## Author: Lewis Watson (https://lnwatson.co.uk)

import sys
import discord
import json
import asyncio

# Load bot config
with open('botconfig.json') as json_file:
    bot_config = json.load(json_file)
    bot_token = bot_config['bot_token']
    admin_id = int(bot_config['admin_id'])  # Ensure it's an integer

# Set intents
intents = discord.Intents.default()

class Bot(discord.Client):
    def __init__(self, message, *args, **kwargs):
        super().__init__(intents=intents, *args, **kwargs)
        self.alert_message = message

    async def on_ready(self):
        print(f'Logged in as {self.user}!')
        try:
            admin = await self.fetch_user(admin_id)
            await admin.send(self.alert_message)
            print(f"Sent alert to {admin.name} ({admin_id}): {self.alert_message}")
        except Exception as e:
            print(f"Failed to send message: {e}")

        await self.close()  # Shut down after sending

# If program is run directly, run the bot
if __name__ == "__main__":
    try:
        alert = sys.argv[1]  # Get message from CLI argument
    except IndexError:
        alert = "[IndexError] No Alert Passed In..."
    except Exception as e:
        alert = f"[Unexpected Error] {e}"

    # Run the bot
    client = Bot(alert)
    client.run(bot_token)
