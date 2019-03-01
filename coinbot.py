'''
Coinbot is a simple bot that returns basic information from
Coinbase.com about digital currencies, in USD format.

# by plasticuproject
# MIT LICENSE
'''

import discord
from discord.ext import commands
import requests
from requests.exceptions import RequestException
from coinbase.wallet.client import Client


# discord bot prefix
bot = commands.Bot(command_prefix='%')

# coinbase account login for api acces
client = Client('<API KEY>', '<API SECRET>')

# build list of coinbase supported digital currencies
coins = ['BTC', 'LTC', 'BCH', 'ETH', 'ETC', 'BAT', 'ZRX', 'USDC', 'XRP']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def list(ctx):

    # return list of coinbase supported digital currencies
    value = ', '.join(coins)
    embed = discord.Embed(title=value)
    
    await ctx.send(embed=embed)


@bot.command()
async def prices(ctx, coin):
    # return coin prices

    try:
        coin = coin.upper()
        buy = client.get_buy_price(currency_pair = '{}-USD'.format(coin))
        sell = client.get_sell_price(currency_pair = '{}-USD'.format(coin))
        spot = client.get_spot_price(currency_pair = '{}-USD'.format(coin))
        buyAmount = buy.get('amount')
        sellAmount = sell.get('amount')
        spotAmount = spot.get('amount')
        value = 'Buy: ${0}, Sell: ${1}, Spot: ${2}'.format(buyAmount, 
                                                      sellAmount, spotAmount)
        embed = discord.Embed(title=value)

    except:
        embed = discord.Embed(title='ERROR: Please check your syntax and' +
                                    ' try again', color=0xff0000)

    await ctx.send(embed=embed)


@bot.command()
async def exchange(ctx, coin_one, coin_two):
    # return exchange rate from one coin to another

    try:
        coin_one = coin_one.upper()
        coin_two = coin_two.upper()
        getRates = client.get_exchange_rates(currency=coin_one)
        rate = getRates.get('rates').get(coin_two)
        try:
            float(rate)
            value = '1 {0} is worth {1} {2}'.format(coin_one, rate, coin_two)
            embed = discord.Embed(title=value)
        except ValueError:
            embed = discord.Embed(title='This exchange would not make sense')
    except:
        embed = discord.Embed(title='ERROR: Exchange data not available' + 
                              ' try again',color=0xff0000)

    await ctx.send(embed=embed)


@bot.command()
async def history(ctx, coin, period):
    #return percentage of change in coin value

    try:
        coin = coin.upper()
        period = period.lower()
        his = client.get_historic_prices(currency_pair = coin + 
                                         '-USD', period = period)
        previous = his.get('prices')[-1].get('price')
        current = client.get_spot_price(currency_pair = 
                                        '{}-USD'.format(coin)).get('amount')
        previous = float(previous)
        current = float(current)
        if previous == current:
            embed = discord.Embed(title=coin + ': 0% change')
        else:
            if current - previous < 0:
                sign = 0
            elif current - previous > 0:
                sign = 1
            value = abs(current - previous) / previous * 100
        if sign == 1:
            embed = discord.Embed(title=coin + 
                                  ': UP {0:.2f}%'.format(value),color=0x008000)
        elif sign == 0:
            embed = discord.Embed(title=coin + 
                            ': DOWN {0:.2f}%'.format(value), color=0xff0000)
    except:
        embed = discord.Embed(title='ERROR: Please check your syntax and' +
                              ' try again',color=0xff0000)

    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title='coinbot', 
                          description='Coinbase query bot.', color=0xeee657)
    
    # give info about you here
    embed.add_field(name='Author', value='<YOUR NAME>')
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name='Server count', value=f'{len(bot.guilds)}')

    # give users a link to invite this bot to their server
    embed.add_field(name='Invite', value='https://discordapp.com/oauth2/' + 
                    'authorize?client_id=<YOUR_BOT_CLIENT_ID>&scope=bot')

    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='coinbot', description='Coinbase query bot.' +
                          ' List of commands are:', color=0xeee657)
    embed.add_field(name='%list', value='Return list of coinbase supported' + 
                    ' digital currencies', inline=False)
    embed.add_field(name='%prices', value='Example: "%prices BTC"',
                    inline=False)
    embed.add_field(name='%exchange', value='Example: "%exchange BTC ETH"',
                    inline=False)
    embed.add_field(name='%history', value='Example: "%history BTC week."' + 
                    ' Peirod usage limited to hour, day, week, month and year',
                     inline=False)
    embed.add_field(name='%info', value='Gives a little info about the bot', 
                    inline=False)
    embed.add_field(name='%help', value='Gives this message', inline=False)

    await ctx.send(embed=embed)


bot.run('<YOUR_TOKEN_GOES_HERE>')
