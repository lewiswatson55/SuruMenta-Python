import sys, discord, json

global admin, alert

# Get bot_token and admin_id from botconfig.json
with open('botconfig.json') as json_file:
    bot_config = json.load(json_file)
    bot_token = bot_config['bot_token']
    admin_id = bot_config['admin_id']


class Bot(discord.Client):

    async def on_ready(self):
        global admin, alert
        print('Logged on as {0}!'.format(self.user))
        admin = await self.fetch_user(admin_id)
        await admin.send(alert)
        await self.close()

    async def on_message(self, message):
        if message.author == self.user:
            return
        print('Message from {0.author}: {0.content}'.format(message))
        await message.reply("Sus...")


# If program is run directly, run the bot
if __name__ == "__main__":

    # Try to get alert from cli args, catch errors
    try:
        alert = sys.argv[1]
    except IndexError:
        alert = "[IndexError] No Alert Passed In..."
    except:
        alert = "[Unexpected Error] " + str(sys.exc_info()[0]) + "..."

    # Create bot client and send alert
    client = Bot()
    client.run(bot_token)


# Function for running the bot in another python file
def run_bot(_alert):
    # Set alert to _alert
    global alert
    if _alert:
        alert = _alert
    else:
        alert = "No Alert Passed In..."

    # Create bot client and send alert
    client = Bot()
    client.run(bot_token)
    return client
