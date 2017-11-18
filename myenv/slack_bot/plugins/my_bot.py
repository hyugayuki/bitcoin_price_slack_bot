from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import requests #http通信用のモジュール
import json     #josnを扱うためにモジュール

BF_api_url = "https://api.bitflyer.jp/v1/"
CC_api_url = "https://coincheck.com/"
ZF_api_url = "https://api.zaif.jp/api/1/"
BB_api_url = "https://public.bitbank.cc/"

def BF_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        BF_api_url  + path
        ,headers = {
        })
    return request_data

def CC_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        CC_api_url  + path
        ,headers = {
        })
    return request_data

def ZF_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        ZF_api_url  + path
        ,headers = {
        })
    return request_data

def BB_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        BB_api_url  + path
        ,headers = {
        })
    return request_data

@respond_to('bitflyer', re.IGNORECASE)
def mention_func(message):
    message.reply('取引所bitFlyerの現在のビットコイン価格情報です。')
    data = BF_get_api_call('ticker').json()
    message.reply('最終取引額：' + str(data['ltp']) + ',　買い注文高値：' + str(data['best_bid']) + ',　売り注文安値：' + str(data['best_ask']))

@respond_to('coincheck', re.IGNORECASE)
def mention_func(message):
    message.reply('取引所coincheckの現在のビットコイン価格情報です。')
    data = CC_get_api_call('api/ticker').json()
    message.reply('最終取引額：' + str(data['last']) + ',　買い注文高値：' + str(data['bid']) + ',　売り注文安値：' + str(data['ask']))

@respond_to('zaif', re.IGNORECASE)
def mention_func(message):
    message.reply('取引所Zaifの現在のビットコイン価格情報です。')
    data = ZF_get_api_call('ticker/btc_jpy').json()
    message.reply('最終取引額：' + str(data['last']) + ',　買い注文高値：' + str(data['bid']) + ',　売り注文安値：' + str(data['ask']))

@respond_to('bitbank', re.IGNORECASE)
def mention_func(message):
    message.reply('取引所bitbankの現在のビットコイン価格情報です。')
    data = BB_get_api_call('btc_jpy/ticker').json()
    data = data['data']
    message.reply('最終取引額：' + str(data['last']) + ',　買い注文高値：' + str(data['buy']) + ',　売り注文安値：' + str(data['sell']))
