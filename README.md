## 何をやるか

仮想通貨取引所のオープンAPIを用いて価格情報をリアルタイムで取得し、slackのbotが価格を返答します。
- coincheck (https://coincheck.com/ja/documents/exchange/api#about)
- bitFlyer (https://lightning.bitflyer.jp/docs/api)
- Zaif (http://techbureau-api-document.readthedocs.io/ja/latest/index.html)
- Bitbank(https://public.bitbank.cc/)


## どうやるのか

cryptopricebot.slack.com にて、
@crypto_bot とのダイレクトチャットか、ボットのいるチャンネルで@crypto_botメンションを付け、
coincheck , zaif , bitflyer, Bitbank が含まれるメッセージで、その文字列に反応し、それぞれの取引所から価格を取得し返答してくれます。
