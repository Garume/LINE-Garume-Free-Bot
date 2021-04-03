## ![logo](LINE-sm.png) LINE-Garume-Free-Bot

[![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/) 
----
LINEBot キッカー無しの多機能BOTと呼ばれるものです。  
送信取り消し、自動既読、自動追加、グループのURL発行などできます。  
2年前に書いたものなのでいくつかのAPIは使えないです。（天気確認とか）  
元のライブラリを改造し,QRコードによるログイン、FlexMessageの使用を簡単にしています.  

## 導入  
GarumeBot.pyを起動後QRコードを読み込むかURLからログインすることで使えます。
```python
>>>cl() → URLログイン
>>>cl(showQr=True) → QRログイン
>>>cl("token") → トークンログイン
>>>cl("ID","PASS") → メールログイン
```
メールログインの場合一度ログインすればcrt(セキュリティ証明書)が発行されるため次回以降すぐログインできます

## 使い方
Letter Sealingを必ずオフにしてください  
ヘルプとチャットに打つことでコマンド一覧が出るので参考にしてください  
ソースを見たほうが早いかもしれません  

## Flex Message
本来、非公式BOTなどで使えるメッセージをJSONに記述することで使えます
![](https://developers.line.biz/assets/img/flexMessageSimulator.6fa91ae3.png)
https://developers.line.biz/ja/docs/messaging-api/using-flex-messages/
***
#### ここからJSONを簡単に作成できます
https://developers.line.biz/flex-simulator/
***
#### 例
![](https://i.gyazo.com/5e1c0d547ad65de38385edb059b9cf37.png)  
サイトを用いることでコマンドを自動で打つなどができる*LIFF*という機能も存在しますがいつか別記します。


## 注意
作者はプログラミング超初心者なのでわけわからんエラー起きるかもしれませんが何とかしてください  
また一斉送信を連続で使用したり、全蹴りをするとトーク規制、垢BANになるので注意  
さらにこのBOTはサーバー上で動かすことを想定しているためローカルでの使用はお勧めしません。  
使う人は（多分いない）VPS上にpython環境を構築し起動してください。  


## 参考
- Linepy https://github.com/fadhiilrachman/line-py

## ライセンス

- [MIT](https://raw.githubusercontent.com/aocattleya/Ramen-Timer/master/LICENSE)  
　

## 作者

- [Github](https://github.com/desuboruto)
- Discord ガルム#8522 ←質問はここまで
