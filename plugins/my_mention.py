# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import re                               # 正規表現

from libs import my_functions           # 外部関数の読み込み

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                              文字列中に':'はいらない
@respond_to('github')
def mention_func(message):
    message.reply('https://github.com/cotree/connect')

@respond_to('issue')
def mention_func(message):
    message.reply('https://github.com/cotree/connect/issue')

@respond_to('pr')
def mention_func(message):
    message.reply('https://github.com/cotree/connect/pulls')

#@respond_to('github sprint')
#def mention_func(message):
#    message.reply('https://github.com/cotree/connect')

@respond_to('さては')
def mention_func(message):
    message.reply('アンチだなオメー')

@respond_to('おはよう')
def mention_func(message):
    message.reply('今日も１日がんばるぞい！٩( ‘ω’ )و')

@respond_to('おそよう')
def mention_func(message):
    message.reply('俺はこういう人間だ！俺はこういう人間！')

@respond_to('かえる')
def mention_func(message):
    message.reply('エサヒィ～スープゥードゥラァ～イ！')

@respond_to('そそぐ？だれ？')
def mention_func(message):
    message.reply('私だよ!!!!!')

@respond_to('私のことどのくらい好きか教えて')
def mention_func(message):
    message.reply('いっぱいちゅき♡')

@respond_to('えいえい、怒った？')
def mention_func(message):
    message.reply('怒ってないよ')

@respond_to('生きてる？')
def mention_func(message):
    message.reply('もしもしポリスメン？')


@listen_to('おすおす')
def listen_func(message):
    message.send('誰かがおすおすと投稿したようだ')
    message.reply('君だね？')