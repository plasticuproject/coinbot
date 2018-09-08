# coinbot
Coinbot is a simple bot that returns basic information from <br />
Coinbase.com about digital currencies, in USD format. <br />

## Requirments
Python 3.x and PIP
```
pip install coinbase
pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
```

## Installation
Sign up with Coinbase at https://coinbase.com <br />
Enable an API key at https://coinbase.com/settings/api <br />
Record your API KEY + SECRET

Head over to https://discordapp.com/developers/applications/me and create a new Discord app. <br />
Click on "Create Bot User". <br />
Once done, you can get the secret bot token. <br />

In coinbase.py replace all <...> with appropriate information. <br />

To start bot, run:
```
python coinbot.py
```

To add bot to server add your CLIENT_ID to this URL and visit in browser: <br />
"https://discordapp.com/oauth2/authorize?client_id=<YOUR_BOT_CLIENT_ID_GOES_HERE>&scope=bot" <br />

## Usage Examples
When bot is active in server type: <br />

<b>%list</b> to return a list of Coinbase supported digital currencies that can be used as arguments for other functions. <br />

<b>%prices BTC</b> to return a list of current BTC trading prices. <br />

<b>%exchange ETH LTC</b> to return exchange rate between two currencies<br />

<b>%history BCH month</b> to return a percentage of gain or loss from specified period. <br />
Valid period argurments are <b>hour</b>, <b>day</b>, <b>week</b>, <b>month</b>, and <b>year</b>.
