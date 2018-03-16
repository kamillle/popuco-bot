# -*- coding: utf-8 -*-
import os

# botアカウントのトークンを指定
API_TOKEN = os.environ.get("CSLACK_API_KEY")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "意味わかんねーよ死ね バーーーーーーーーーーーカ!!!"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
