# coinbot
Coinbot is a simple bot that returns basic information from <br />
Coinbase.com about digital currencies, in USD format. <br />

## Requirments
* python >= 3.6
* pip
    * coinbase
    * -U discord.py
    
> **Note:**
> It is recommended to install this application in a python virtual environment.<br /> 

## Installation
Sign up with [Coinbase](https://coinbase.com "Coinbase") <br />
Enable an API key at https://coinbase.com/settings/api <br />
Record your API KEY + SECRET

Head over to [Discord](https://discordapp.com/developers/applications/me "Discord") and create a new app. <br />
Record your *Client_ID*. On the left, click *Bot*, and then *Add Bot*. <br />
Once you are done setting up your bot, record the *Token* and *Client Secret*. <br />

In coinbase.py replace all <...> with appropriate information. <br />

To start bot, run:
```
python coinbot.py
```

To add bot to server add your *Client_ID* to this URL and visit in browser:  <br />
https://discordapp.com/oauth2/authorize?client_id= *Client_ID* &scope=bot <br />

## Usage
When bot is active in server type: <br />

<b>%list</b> to return a list of Coinbase supported digital currencies that can be used as arguments for other functions. <br />
<b>%prices BTC</b> to return a list of current BTC trading prices. <br />
<b>%exchange ETH LTC</b> to return exchange rate between two currencies. <br />
<b>%history BCH period</b> to return a percentage of gain or loss from specified period. <br />
Valid period argurments are <b>hour</b>, <b>day</b>, <b>week</b>, <b>month</b>, and <b>year</b>.
