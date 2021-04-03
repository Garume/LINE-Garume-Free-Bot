# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, datetime, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, ssl, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
botTime = time.time()
cl = LINE(showQr=True)
cl.log("Auth Token :\n " + str(cl.authToken) +"\n正常なログインを確認")

oepoll = OEPoll(cl)
try:
    TOpen = codecs.open("template.json","r","utf-8")
    plate = json.load(TOpen)
    cl.log("テンプレートの読み込みに成功")
except:
    cl.log("テンプレートの読み込みに失敗")
try:
    SOpen = codecs.open("temp.json","r","utf-8")
    settings = json.load(SOpen)
    cl.log("設定ファイルの読み込みに成功")
except Exception as e:
    cl.log(e)
    cl.log("設定ファイルの読み込みに失敗しました\n設定ファイルを作成しますか？　Y/N")
    mod = str(input())
    if mod == "Y":
        with open("temp.json","w") as A:
            A.write("""

    {
    "alwayRead": true,
    "autoAdd": true,
    "autoRespon":false,
    "CHANGEDURL":false,
    "CHANGEDGNAME":false,
    "CHANGEDGPNG":false,
    "checkContact":false,
    "checkPost":false,
    "unsendMessage":false,
    "autoJoin": true,
    "autoJoinTicket": false,
    "autoLeave": false,
    "autoRead": false,
    "blacklist": {
        "u347a00a4e110f48bca14fddb06d378fc": true,
        "udce60e69b567ce75fd03ec98065340db": true,
        "ue90a191326f77f7b02314cc487a309bc": true
    },
    "canceljoin": false,
    "cancelprotect": false,
    "changeGroupPicture": {},
    "changePicture": {},
    "checkSticker": false,
    "contact": false,
    "dblack": false,
    "dblacklist": false,
    "detectMention": false,
    "inviteprotect": false,
    "keyCommand": "",
    "kickerjoin": false,
    "kickjoin": false,
    "kickmeber": true,
    "lang": "JP",
    "mimic": {
        "copy": false,
        "status": true,
        "target": {
            "ud4d2c8cbf1429842fc2f65e7f044647c": true
        }
    },
    "protect": false,
    "qrprotect": false,
    "reread": false,
    "sanka": false,
    "taikai": false,
    "timeline": false,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "wblack": false,
    "wblacklist": false 
    }
    """)

        SOpen = codecs.open("temp.json","r","utf-8")
        settings = json.load(SOpen)     #なぜこう書いた
    else:
        sys.exit(0)
msg_dict = {
    "IMG":{}
}
bl = [""]
apikey_param = "3ade5ea614a1d8f3b937"
urlss = "https://chatbot-api.userlocal.jp/api/chat?"
params = {
    "message": "",
    "key": apikey_param
}
clMID = cl.profile.mid
admin = ["",clMID]
# admin = 最高権限
# Right = 貴族権限
# Free = 誰でもオーケー
try:
    with open("admin.json","r") as AOpen:
        admins = json.load(AOpen)
    cl.log("最高権限リストの読み込みに成功しました")
except Exception as e:
    cl.log(e)
    cl.log("最高権限リストの読み込みに失敗しました")
    mod = str(input("リストを作成しますか？\nY/N\n"))
    if mod == "Y":
        admins = admin
        with open("admin.json","w") as A:
            A.write(str(admins))

    else:
        sys.exit(0)

try:
    POpen = codecs.open("right.json","r","utf-8")
    Right = json.load(POpen)
    cl.log("貴族権限リストの読み込みに成功しました")
except:
    cl.log("貴族権限リストの読み込みに失敗しました")
    mod = str(input("リストを作成しますか？\nY/N"))
    if mod == "Y":
        Right = []
        with open("right.json","w") as A:
            A.write(str(Right))

    else:
        sys.exit(0)
alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
def restartBot():
    print ("ログイン完了")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def isalnum(s):
    return alnumReg.match(s) is not None
WEATHER_URL="http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
TODAY=0
TOMMOROW=1
def unsei(num):
        i = int(num)
        day = datetime.datetime.today().strftime("%Y/%m/%d")
        res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ day)
        req = res.json()
        reqq = json.dumps(req["horoscope"][day][i], indent=4, ensure_ascii=False)
        return (reqq.translate(str.maketrans('','',str({})))).replace(' ','')
def seiza():
    Seiza = """
1 = 牡羊座
2 = 牡牛座
3 = ふたご座
4 = 蟹座
5 = 獅子座
6 = おとめ座
7 = 天秤座
8= 蠍座
9 = 射手座
10 = 山羊座
11 = 水瓶座
12 = 魚座
"""
    return Seiza
def get_weather_info(num2):
    try:
        url = WEATHER_URL % num2
        html = urllib.request.urlopen(url)
        html_json = json.loads(html.read().decode('utf-8'))
    except Exception as e:
        print (e)
    return html_json
def set_weather_info(weather_json, day):
    max_temperature = None
    min_temperature = None
    try:
        daytime = weather_json['forecasts'][day]['dateLabel']
        place = weather_json['title']   
        date = weather_json['forecasts'][day]['date']
        weather = weather_json['forecasts'][day]['telop']
        max_temperature = weather_json['forecasts'][day]['temperature']['max']['celsius']
        min_temperature = weather_json['forecasts'][day]['temperature']['min']['celsius']
    except Exception as e:
        print (e)
    msg = "%s%s\n%s\nweather: %s\nmin: %s\nmax: %s" % \
               (daytime, date, place, weather, min_temperature, max_temperature)
    return msg
def set2_weather_info(weather_json):
    max_temperature = None
    min_temperature = None
    try:
        place = weather_json['title']   
        shousai = weather_json['description']['text']
    except Exception as e:
        print (e)
    msg = "【天気詳細】\n%s\n%s" % \
               (place, shousai)
    return msg 
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("ログイン完了")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    #cl.log("[エラー] " + str(text))
    time_ = datetime.datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def cmi(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if texX + command in string:
                return True
    return False
def HELP():
    Mhelp = """~FREE BOT~
~システム~
★help
☆メッセージで送るよ
★ヘルプ
☆ファイルで送ってみるよ
★コマンドリスト
☆タップ式のリストを送るよ
★test
☆動いてるか確認
★スピード
☆速度を計測します
★権限
☆権限を確認
★設定確認
☆設定を確認
★稼働時間
☆稼働時間を表示


~グループ~
★オールメンション
☆すべての人にメンションするよ！
★さようなら
☆退会するよ！
★スタンプ確認
☆スタンプのIDを表示するよ！
★グル名変更:[変えたい名前]
☆グループ名を変えるよ！
★アカウント情報+メンション
☆メンションしたひとの情報を表示するよ
★g情報
☆グループ情報を取得します
★メンバーリスト
☆メンバーリストを取得します


~どこでも~
★スタンプ確認
☆スタンプのIDを表示するよ！
★プロフィール
☆あなたのプロフィールを作成するよ！
★クイックセッティング
☆設定メニューを表示するよ！(設定不可)


~既読~
★既読確認
☆既読を確認するよ
★既読ポイントセット
☆既読ポイントをセットするよ
★既読ポイント消去
☆既読ポイントを消去するよ

~その他~
★おみくじ
☆おみくじを引く
▲運勢▲
★運勢
☆星座のリストを送るよ！
★運勢:[星座の番号]
☆あなたの今日の運勢を送るよ！
▲天気▲
★天気
☆あなたが設定した地域の天気を表示するよ！
★天気詳細
☆より詳しく表示するよ！
★天気登録:[地域コード]
☆天気を登録するよ！http://www.nankuma.com/etc/livedoor-weather-id.html ここから選んで6桁の数字を「天気登録:数字」と打ってね！
★天気確認
☆あなたの設定した天気コードを確認するよ！


~貴族権限持ち~
★権限リスト
☆権限を見れるよ
★クイックセッティング
☆設定メニューを表示するよ！(設定可)
★モード変更
☆自動で返信するようになるよ！！
★再起動
☆再起動します

~最高権限持ち~
権限追加　削除
最高権限追加　削除
Gi: グル一斉送信
ci: 全コチャ一斉送信
TL: タイムラインに投稿
オールミッド 友達をMIDにしてリスト化
通話マクロ 数 そのまま

"""
    with open("help.txt","w") as H:
        H.write(str(Mhelp))
    return Mhelp
def Setting(sender):
    ret_ = "現在の設定です"
    if settings["autoAdd"] == True: ret_ += "\n◯ 追加 「オン」"
    else: ret_ += "\n✖ 追加 「オフ」"
    if settings["autoJoin"] == True: ret_ += "\n◯ 参加 「オン」"
    else: ret_ += "\n✖ 参加 「オフ」"
    if settings["autoLeave"] == True: ret_ += "\n◯ 強制退出 「オン」"
    else: ret_ += "\n✖ 強制退出 「オフ」"
    if settings["autoJoinTicket"] == True: ret_ += "\n◯ URL参加 「オン」"
    else: ret_ += "\n✖ URL参加 「オフ」"
    if settings["autoRead"] == True: ret_ += "\n◯ 既読 「オン」"
    else: ret_ += "\n✖ 既読 「オフ」"
    if settings["sanka"] == True: ret_ += "\n◯ 参加挨拶 「オン」"
    else: ret_ += "\n✖ 参加挨拶 「オフ」"
    if settings["taikai"] == True: ret_ += "\n◯ 退会挨拶 「オン」"
    else: ret_ += "\n✖ 退会挨拶 「オフ」"
    if settings["CHANGEDURL"] == True: ret_ += "\n◯ URL変更通知 「オン」"
    else: ret_ += "\n✖ URL変更通知 「オフ」"
    if settings["CHANGEDGPNG"] == True: ret_ += "\n◯ 画像変更通知 「オン」"
    else: ret_ += "\n✖ 画像変更通知 「オフ」"
    if settings["CHANGEDGNAME"] == True: ret_ += "\n◯ 名前変更通知 「オン」"
    else: ret_ += "\n✖ 名前変更通知 「オフ」"
    if settings["autoRespon"] == True: ret_ += "\n◯ 自動返信 「オン」"
    else: ret_ += "\n✖ 自動返信 「オフ」"
    if settings["checkContact"] == True: ret_ += "\n◯ 連絡先 「オン」"
    else: ret_ += "\n✖ 連絡先 「オフ」"
    if settings["checkPost"] == True: ret_ += "\n[ ᴏɴ ] 投稿 「オン」"
    else: ret_ += "\n✖ 投稿 「オフ」"
    if wait["FriendAdd"] == True: ret_ += "\n[ ᴏɴ ] ランダム追加 「オン」"
    else: ret_ += "\n✖　ランダム追加 「オフ」"
    if settings["unsendMessage"] == True: ret_ += "\n[ ᴏɴ ] 送信取り消し 「オン」"
    else: ret_ += "\n✖ 送信取り消し 「オフ」"
    if wait["clock"] == True: ret_ += "\n◯ クロック 「オン」"
    else: ret_ += "\n✖ クロック 「オフ」"
    if sender in wait['tenki'].keys(): ret_ +="\n天気コード:"  + wait['tenki'][sender]
    else: ret_ += "\n天気コードは登録されていません"
    ret_ += "\n以上が今の設定だよ"
    return ret_
wait = {
    "makuro":"",
    'tenki':{},
    "cName":"パララークサイカ",
    "clock":False,
    "FriendAdd":False
}

wait2 = {
    'readPoints':{},
    'readMembers':{},
    'setTimes':{},
    'ROMs':{}
}
wait3 = {
    "Tstanp":{},
    "stanp":{}
}

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凶"]
area = {
    '稚内': "011000",'旭川': "012010",'留萌': "012020",'札幌': "016010",'岩見沢': "016020",'倶知安': "016030",'網走': "013010",'北見': "013020",
    '紋別': "013030",'根室': "014010",'釧路': "014020",'帯広': "014000",'室蘭': "015010",'浦河': "015020",'函館': "017010",'江差': "017020",'青森': "020010",
    'むつ': "020020",'八戸': "020030",'盛岡': "030010",'宮古': "030020",'大船渡': "030030",'仙台': "040010",'白石': "040020",'秋田': "050010",'横手': "050020",
    '山形': "060010",'米沢': "060020",'酒田': "060030",'新庄': "060040",'福島': "070010",'小名浜': "070020",'若松': "070030",'東京': "130010",'大島': "130020",
    '八丈島': "130030",'父島': "130040",'横浜': "140010",'小田原': "140020",'さいたま': "110010",'熊谷': "110020",'秩父': "110030",'千葉': "120010",'銚子': "120020",
    '館山': "120030",'水戸': "080010",'土浦': "080020",'宇都宮': "090010",'大田原': "090020",'前橋': "100010",'みなかみ': "100020",'甲府': "190010",'河口湖': "190020",
    '名古屋': "230010",'豊橋': "230020",'岐阜': "210010",'高山': "210020",'静岡': "220010",'網代': "220020",'三島': "220030" ,'浜松': "220040",'津': "240010",'尾鷲': "240020",
    '新潟': "150010",'長岡': "150020",'高田': "150030",'相川': "150040",'長野': "200010",'松本': "200020",'飯田': "200030",'富山': "160010",'伏木': "160020",'金沢': "170010",
    '輪島': "170020",'福井': "180010",'敦賀': "180020",'大阪': "270000",'神戸': "280010",'豊岡': "280020",'京都': "260010",'舞鶴': "260020",'大津': "250010",'彦根': "250020",
    '奈良': "290010",'風屋': "290020",'和歌山': "300010" ,'潮岬': "300020",'鳥取': "310010",'米子': "310020" ,'松江': "320010",'浜田': "320020",'西郷': "320030" ,'岡山': "330010",
    '津山': "330020",'広島': "340010",'庄原': "340020",'下関': "350010",'山口': "350020",'柳井': "350030",'萩': "350040",'徳島': "360010",'日和佐': "360020",'高松': "370000",
    '松山': "380010",'新居浜': "380020",'宇和島': "380030",'高知': "390010",'室戸岬': "390020",'清水': "390030",'福岡': "400010",'八幡': "400020",'飯塚': "400030",'久留米': "400040",
    '大分': "440010",'中津': "440020",'日田': "440030",'佐伯': "440040",'長崎': "420010",'佐世保': "420020",'厳原': "420030",'福江': "420040",'佐賀': "410010",'伊万里': "410020",
    '熊本': "430010",'阿蘇乙姫': "430020",'牛深': "430030",'人吉': "430040",'宮崎': "450010",'延岡': "450020",'都城': "450030",'高千穂': "450040",'鹿児島': "460010",'鹿屋': "460020",   
    '種子島': "460030",'名瀬': "460040",'那覇': "471010",'名護': "471020",'久米島': "471030",'南大東': "472000",'宮古島': "473000",'石垣島': "474010",'与那国島': "474020"
}
omikuzi = ["大吉","中吉","小吉","末吉","大凶","凶"]
hosi = ["☆☆☆☆☆"] * 10 + ["★☆☆☆☆"] * 10 + ["★★☆☆☆"] * 20 + ["★★★☆☆"] * 25 + ["★★★★☆"] * 20 + ["★★★★★"] * 10 + ["★UNLIMITED:STAR★"] * 5
os.makedirs("rereadImg", exist_ok=True)
cl.log("開始します")
def lineBot(op):
    try:
#########################################################################################################
        if op.type == 0:
            return
#########################################################################################################
        if op.type == 5:
            contact = cl.getContact(param2)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1,"追加ありがとうございます\nこのアカウントはグループに招待すると使えます")
#########################################################################################################
        if op.type == 13:
            if settings["autoJoin"] == True:
                cl.acceptGroupInvitation(op.param1)
                cl.sendMessage(op.param1, "フリーBOTです。\nhelpでどうぞ")
#########################################################################################################
        if op.type == 17:
            if settings["sanka"] == True:
                if op.param2 in clMID:
                    return
                ginfo = cl.getGroup(op.param1)
                cl.sendMessage(op.param1, "誰かが参加したよ")
#########################################################################################################
        if op.type == 15:
            if settings["taikai"] == True:
                if op.param2 in clMID:
                    return
                cl.sendMessage(op.param1, "誰かが退会したよ")
#########################################################################################################
        if op.type == 24 or op.type == 22:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1) #トークルーム招待時
#########################################################################################################
        if op.type == 1:
            print ("[1]設定ファイルを更新する")
#########################################################################################################
        if op.type == 11:
            if op.param3 ==  "1":
                if settings["CHANGEDGNAME"] == True:
                    G = cl.getGroup(op.param1)
                    cl.sendMessage(op.param1,"%sがグループの名前を%sに変更しました。"%op.param2 %G.name)
            if op.param3 ==  "2":
                if settings["CHANGEDGPNG"] == True:
                    cl.sendMessage(op.param1,"%sがグループ画像を変更しました。"%op.param2)
            if op.param3 ==  "4":
                if settings["CHANGEDURL"] == True:
                    cl.sendMessage(op.param1,"%sが招待URLを変更しました。"%op.param2)
#########################################################################################################
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoints']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMembers'][op.param1]:
                        pass
                    else:
                        wait2['ROMs'][op.param1][op.param2] = []
                        wait2['readMembers'][op.param1] += "\n[※]" + Name
                        wait2['ROMs'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
##############################################################################################
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if settings["autoRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(to,msg_id)
                else:
                    cl.sendChatChecked(to,msg_id)
            if msg.contentType == 13:
                if settings["checkContact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[表示名]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステータスメッセージ]:\n" + contact.statusMessage + "\n[アイコン画像url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホーム画像]:\n" + str(cu)) + ""
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        try:    
                            cl.sendMessage(msg.to,"[表示名]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステータスメッセージ]:\n" + contact.statusMessage + "\n[アイコン画像url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホーム画像]:\n" + str(cu)) + ""
                        except Exception as e:
                            cl.sendMessage(to,"ユーザー情報の取得に失敗しました\n" + str(e))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "URL\n" + msg.contentMetadata["postEndUrl"] + ""
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 7:
                if sender in wait3["Tstanp"]:
                    try:
                        stk_id = msg.contentMetadata['STKID']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "╔══[ スタンプ情報 ]"
                        ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                        ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                        ret_ += "\n╚══[ 以上 ]"
                        cl.sendMessage(to, str(ret_))
                        del wait3["Tstanp"][sender]
                        print(wait3["stanp"]["STKID"])
                        print(wait3["stanp"]["STKPKGID"])
                    except Exception as e:
                        print (e)           
            if msg.contentType == 0:
                if text is None:
                    return
                elif settings["autoRespon"] == True:
                    if msg.text == "通常モード" or text.lower() == "MODECHANGE":
                        settings["autoRespon"] = False
                        cl.sendMessage(to,"モードを変更しました")
                    elif "分身:" in msg.text or sender is clMID:
                        pass
                    elif msg.text == "設定確認":
                        cl.sendMessage(to,str(Setting(sender)))
                    else:
                        try:
                            params["message"] = msg.text
                            print(params)
                            urls = urllib.parse.urlencode(params)
                            print(urls)
                            dates = urlss + urls
                            with urllib.request.urlopen(dates) as res:
                                root = json.loads(res.read().decode("utf-8"))
                                cl.sendMessage(to,"分身: {0}".format(root["result"]))
                        except Exception as e:
                            cl.sendMessage(msg.to, str(e))
                elif "/ti/g/" in msg.text:
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.sendMessage(group.id, "フリーBOTです。\nhelpでどうぞ")
#############################################################################################
                elif text.lower() == 'おみくじ':
                    c = random.choice(omikuzi)
                    cl.sendMessage(to,c)
                elif text.lower() == 'オールメンション':
                    try:
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        if len(nama)<20:
                            cl.sendMessageWithMention(to,nama)  
                        else:
                            chunks = zip(*[iter(nama)]*20)
                            for i in chunks:
                                cl.sendMessageWithMention(to,list(i))             
                        cl.sendMessage(msg.to, "Total {} Mention".format(str(len(nama))))
                    except Exception as e:
                        cl.sendMessage(msg.to,str(e))
                elif text.lower() == '運勢':
                    Seiza = seiza()
                    cl.sendMessage(to, str(Seiza))
                elif "運勢:" in msg.text:
                    try:
                        unseinum = int(text.replace("運勢:","")) - 1
                        Un = unsei(unseinum)
                        your = cl.getContact(sender)
                        cl.sendMessage(to,your.displayName + "\nの今日の運勢は\n" + Un)
                    except Exception as e:
                        print(e)
                elif "天気登録:" in msg.text:
                    if "天気登録:数字" in msg.text:
                        pass
                    else:
                        i = text.replace("天気登録:","")
                        if not isalnum(i):
                            cl.sendMessage(to,"半角英数字でお願いします。")
                        else:
                            if len(i) != 6:
                                cl.sendMessage(to,"6つの数字でお願いします。")
                            else:
                                if i not in area.values():
                                    cl.sendMessage(to,"正しい地域コードでお願いします")
                                else:
                                    try:
                                        wait['tenki'][sender] = i
                                        cl.sendMessage(to,"登録完了しました")
                                    except Exception as e:
                                        cl.sendMessage(to,"登録失敗しました\n" + "エラー内容\n" + str(e))
                elif text.lower() =="天気確認":
                    try:
                        for key,value in area.items():
                            if value == wait['tenki'][sender]:
                                areavl = key
                        cl.sendMessage(to,str(wait['tenki'].keys()) + "\n" + str(wait['tenki'][sender]) + "\n" + str(areavl))
                    except Exception as e:
                        cl.sendMessage(to,"地域コードが設定されていません\n" + "エラー内容\n" + str(e))
                elif text.lower() == "天気":
                    try:
                        if sender in wait['tenki'].keys():
                            try:
                                wheather = get_weather_info(str(wait['tenki'][sender]))
                                for day in range(2):
                                    try:
                                        Wmsg = set_weather_info(wheather, day)
                                        cl.sendMessage(to,Wmsg)
                                    except Exception as e:
                                        cl.sendMessage(to,"取得に失敗しました\n" + "エラー内容\n" + str(e))
                            except Exception as e:
                                print(e)    
                        else:
                            cl.sendMessage(to,"あなたの地域の天気コードを教えてください\nhttp://www.nankuma.com/etc/livedoor-weather-id.html\nここから選んで6桁の数字を「天気登録:数字」と打ってね！")
                            cl.sendMessage(to,area)
                    except Exception as e:
                        print(e)
                elif text.lower() == "天気詳細":
                    try:
                        if sender in wait['tenki'].keys():
                            try:
                                wheather = get_weather_info(str(wait['tenki'][sender]))
                                try:
                                    Wmsg = set2_weather_info(wheather)
                                    cl.sendMessage(to,Wmsg)
                                except Exception as e:
                                    cl.sendMessage(to,"取得に失敗しました\n" + "エラー内容\n" + str(e))
                            except Exception as e:
                                print(e)    
                        else:
                            cl.sendMessage(to,"あなたの地域の天気コードを教えてください\nhttp://www.nankuma.com/etc/livedoor-weather-id.html\nここから選んで6桁の数字を「天気登録:数字」と打ってね！")
                    except Exception as e:
                        print(e)
                elif text.lower() == "スピード":
                    start = time.time()
                    cl.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "%s" % (elapsed_time))
                elif text.lower() == '既読ポイントセット':
                    cl.sendMessage(msg.to, "既読ポイントを設置しました！")
                    try:
                        del wait2['readPoints'][msg.to]
                        del wait2['readMembers'][msg.to]
                    except:
                        pass
                    now2 = datetime.datetime.now()
                    wait2['readPoints'][msg.to] = msg.id
                    wait2['readMembers'][msg.to] = ""
                    wait2['setTimes'][msg.to] = datetime.datetime.strftime(now2,"%H:%M")
                    wait2['ROMs'][msg.to] = {}
                elif text.lower() == "設定確認":
                    try:
                        cl.sendMessage(to, str(Setting(sender)))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == "既読ポイント消去":
                    cl.sendMessage(to, "既読ポイントを消去しました！")
                    try:
                        del wait2['readPoints'][msg.to]
                        del wait2['readMembers'][msg.to]
                        del wait2['setTimes'][msg.to]
                    except:
                        pass
                elif msg.text in ["既読確認","Checkread"]:
                    if msg.to in wait2['readPoints']:
                        try:
                            if wait2["ROMs"][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2["ROMs"][msg.to].items():
                                    chiya += rom[1] + "\n"
                            cl.sendMessage(msg.to, "[既読]%s\n\n設置時間:\n[%s]" % (wait2['readMembers'][msg.to],wait2['setTimes'][msg.to]))
                        except Exception as e:
                            print(e)                    
                    else:
                        cl.sendMessage(msg.to, "既読ポイントを設置してください！")
                elif text.lower() == "おみくじ":
                    cl.sendMessage(to,secrets.choice(omikuzi))
                elif "MURL:" in msg.text:
                    try:
                        LINE_id = str(cl.getUserTicket().id)
                        cl.sendMessage(to,LINE_id)
                        Htext = urllib.parse.quote(str(text.replace("MURL:","")))
                        cl.sendMessage(to,Htext)
                        BURL = "line://oaMessage/@%s/%s" % (LINE_id,Htext)
                        cl.sendMessage(to,BURL)
                    except Exception as e:
                        cl.sendMessage(to,str(e))
                elif text.lower() == "test":
                    cl.sendMessage(to,"動いてるよ！！")
                elif text.lower() == "権限":
                    if sender in admins:
                        cl.sendReplyMessage(msg_id,to,"あなたは最高権限者です")
                    elif sender in Right:
                        cl.sendReplyMessage(msg_id,to,"あなたは貴族権限者です")
                    else:
                        cl.sendReplyMessage(msg_id,to,"あなたはフリー権限者です")
                elif text.lower() == "さようなら":
                    cl.leaveGroup(to)
                elif text.lower() == "help":
                    cl.sendMessage(to,str(HELP()))
                elif text.lower() == "ヘルプ":
                    cl.sendFile(to,"help.txt")
                elif text.lower() == "スタンプ確認":
                    cl.sendMessage(to,"確認したいスタンプを送信してください\nスタンプを送らないとコマンドに反応しなくなります()。")
                    wait3["Tstanp"][sender] = True
                    cl.log(wait3["Tstanp"][sender])
                elif "NM:" in msg.text: #ネームメンション
                    _name = text.replace("NT:","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif "招待 " in msg.text:
                    midd = msg.text.replace("招待 ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    #midで招待
                elif text.lower() == 'uid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                    #自分のmid送信
                elif text.lower() == 'アイコン画像':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    #自分のアイコン送信
                elif text.lower() == 'ホーム画像':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                    #自分のホーム画像送信
                elif "グル名変更:" in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("グル名変更:","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(to, "グループ以外では使用できません")
                elif text.lower() == 'グル作者':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                    cl.sendMessage(to, "グループの作成者はこの人です")
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[グループID:]\n" + gid.id)
                elif text.lower() == 'url発行':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[以前発行したURLは無効になりました\nグループ参加URLを発行しました]\nline://ti/g/{}".format(str(ticket))) + ""
                        else:
                            cl.sendMessage(to, "urlが拒否されています、urlを許可してください".format(str(settings["keyCommand"]))) + ""
                elif text.lower() == 'url許可':
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "既にURLが許可されているよ")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "URLを許可しました")
                elif text.lower() == 'url拒否':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "既にURL拒否が拒否されているよ")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "URL拒否しました")
                elif "アカウント情報" in msg.text:#メンションでアカウント情報
                    if msg.toType == 2:
                        u = json.loads(msg.contentMetadata['MENTION'])['MENTIONEES'][0]['M']
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"表示名:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nステータスメッセージ:\n" + contact.statusMessage + "\n\nアイコン画像:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nホーム画像:\n" + str(cu)) + ""
                        except:
                            cl.sendMessage(msg.to,"表示名:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nステータスメッセージ:\n" + contact.statusMessage + "\n\nホーム画像:\n" + str(cu)) + ""
                elif text.lower() == '稼働時間':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "稼働時間は現在 {}".format(str(runtime)))
                elif text.lower() == "クイックリプライ":
                    AAA = {
                            "type": "text",
                            "text": "Select your favorite food category or send me your location!",
                            "quickReply": { 
                                "items": [
                                    {
                                    "type": "action",
                                    "action": {
                                        "type": "message",
                                        "label": "Sushi",
                                        "text": "Sushi"
                                        }
                                    }
                                ]
                            }
                        }
                    cl.sendFlex(to,AAA)
                elif text.lower() == "プロフィール":
                    contact = cl.getContact(msg._from)
                    cover = cl.getProfileCoverURL(msg._from)
                    cl.reissueUserTicket()
                    res = "╭━━━━profile info━━━\n"
                    res += "Display Name :{}\n".format(contact.displayName)
                    res += "Mid: {}\n".format(contact.mid)
                    res += "Status Message\n"+"{}\n".format(contact.statusMessage)
                    cl.sendMessage(to, res)
                    try:
                        poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                    except:
                        poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                    dax = {
                        "type": "template",
                        "altText": "berak di celana",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                    "imageUrl": poto,
                                    "layout": "horizontal",
                                    "action": {
                                        "type": "uri",
                                        "label": "PROFILE",
                                        "uri": poto,
                                        "area": {
                                            "x": 447,
                                            "y": 356,
                                            "width": 1040,
                                            "height": 1040
                                        }
                                    }
                                },
                                {
                                    "imageUrl": cover,
                                    "layout": "horizontal",
                                    "action": {
                                        "type": "uri",
                                        "label": "COVER",
                                        "uri": cover,
                                        "area": {
                                            "x": 447,
                                            "y": 356,
                                            "width": 1040,
                                            "height": 1040
                                        }
                                    }
                                },
                                {
                                    "imageUrl": "https://qr-official.line.me/L/"+cl.getUserTicket().id+".png",
                                    "layout": "horizontal",
                                    "action": {
                                        "type": "uri",
                                        "label": "CONTACT",
                                        "uri": "https://line.me/ti/p/"+cl.getUserTicket().id,
                                        "area": {
                                            "x": 447,
                                            "y": 356,
                                            "width": 1040,
                                            "height": 1040
                                        }
                                    }
                                }
                            ]
                        }
                    }
                    cl.sendFlex(to, dax)
                elif text.lower() == "確認":
                    cl.log(str("a"))
                    cate = {
                        "type":"flex",
                        "altText":"test",
                        "contents":{
                            "type": "carousel",
                            "contents": [
                                {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "自動追加 ON",
                                                    "uri": "line://app/1595484825-w4PmmQKv"
                                                },
                                                "height": "sm",
                                                "style": "primary",
                                                "color": "#00FF73"
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Second bubble"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                    cl.log(cate)
                    cl.sendFlex(to,cate)
                elif text.lower() == "クイックセッティング":
                    yes = "https://www.shoppingdeprecos.com.br/assets/home/home/img/package/yes.png"
                    no = "https://findicons.com/files/icons/719/crystal_clear_actions/64/messagebox_critical.png"
                    if settings["autoAdd"] == True: S1= ["追加 「オフ」",yes,"ADDOFF"]
                    else: S1 = ["追加 「オン」",no,"ADDON"]
                    if settings["autoJoin"] == True: S2= ["参加 「オフ」",yes, "JOINOFF"]
                    else: S2 = ["参加 「オン」",no, "JOINON"]
                    if settings["autoLeave"] == True: S3 = ["強制退出 「オフ」",yes, "AUTOLEAVEOFF"]
                    else: S3 = ["強制退出 「オン」",no,"AUTOLEAVEON"]
                    if settings["autoJoinTicket"] == True: S4 = ["URL参加 「オフ」",yes, "TICKETURLOFF"]
                    else: S4 = ["URL参加 「オン」",no,"TICKETURLON"]
                    if settings["autoRead"] == True: S5 = ["既読 「オフ」",yes, "AUTOREADOFF"]
                    else: S5 = ["既読 「オン」",no, "AUTOREADON"]
                    if settings["sanka"] == True: S6 = ["参加挨拶 「オフ」",yes,"SANKAOFF"]
                    else: S6 = ["参加挨拶 「オン」",no,"SANKAON"]
                    if settings["taikai"] == True: S7 = ["退会挨拶 「オフ」",yes,"TAIKAIOFF"]
                    else: S7 = ["退会挨拶 「オン」",no,"TAIKAION"]
                    if settings["CHANGEDURL"] == True: S8 = ["URL変更通知 「オフ」",yes,"CHANGEURLOFF"]
                    else: S8 = ["URL変更通知 「オン」",no,"CHANGEURLON"]
                    if settings["CHANGEDGPNG"] == True: S9 = ["画像変更通知 「オフ」",yes,"GPNGOFF"]
                    else: S9 = ["画像変更通知 「オン」",no,"GPNGON"]
                    if settings["CHANGEDGNAME"] == True: S10 = ["名前変更通知 「オフ」",yes,"GNAMEOFF"]
                    else: S10 =["名前変更通知 「オン」",no,"GNAMEON"]
                    if settings["autoRespon"] == True: S11 = ["自動返信 「オフ」",yes,"MODECHANGE"]
                    else: S11 = ["自動返信 「オン」",no,"MODECHANGE"]
                    if settings["checkContact"] == True: S12 = ["連絡先 「オフ」",yes,"CONTACTOFF"]
                    else: S12 = ["連絡先 「オン」",no,"CONTACTON"]
                    if settings["checkPost"] == True: S13 = ["投稿 「オフ」",yes,"POSTOFF"]
                    else: S13 = ["投稿 「オン」",no,"POSTON"]
                    if settings["unsendMessage"] == True: S14 = ["送信取り消し 「オフ」",yes,"UNSENDOFF"]
                    else: S14 = ["送信取り消し 「オン」",no,"UNSENDON"]
                    if wait["clock"] == True: S15 = ["クロック 「オフ」",yes,"CLOCKOFF"]
                    else: S15 = ["クロック 「オン」",no,"CLOCKON"]
                    cl.log(S15)
                    Squick = {
                        "type":"flex",
                        "altText":"設定確認",
                        "contents":{
                            "type": "carousel",
                            "contents": [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "body": {
                                            "backgroundColor": "#FF9500"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "flex": 3,
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "⚙Setting⚙",
                                                        "size": "3xl",
                                                        "align": "center",
                                                        "weight": "bold",
                                                        "color": "#00FFF2"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "box",
                                                "flex": 3,
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://pbs.twimg.com/media/ChQIAnxVEAAmazD.jpg",
                                                        "size": "lg",
                                                        "aspectMode": "cover",
                                                        "aspectRatio": "9:5"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "flex": 2,
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "希望と涙を添えて",
                                                                "gravity": "center",
                                                                "size": "lg",
                                                                "align": "center",
                                                                "weight": "bold",
                                                                "flex": 1
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "~FREE BOT~",
                                                                "gravity": "center",
                                                                "size": "lg",
                                                                "align": "center",
                                                                "weight": "bold",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "none",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "spacer",
                                                        "size": "xl"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "コマンド",
                                                        "margin": "xl",
                                                        "size": "xxs",
                                                        "align": "center",
                                                        "flex": 14
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "状態",
                                                        "margin": "xxl",
                                                        "size": "xxs",
                                                        "align": "start",
                                                        "flex": 3
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S1[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S1[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S1[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S2[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S2[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S2[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S3[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S3[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S3[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S4[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S4[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S4[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label":S5[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S5[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url":S5[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S6[0],
                                                            "uri":"line://app/1595484825-w4PmmQKv?" + S6[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S6[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "body": {
                                            "backgroundColor": "#FF9500"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "コマンド",
                                                        "margin": "xl",
                                                        "size": "xxs",
                                                        "align": "center",
                                                        "flex": 14
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "状態",
                                                        "margin": "xxl",
                                                        "size": "xxs",
                                                        "align": "start",
                                                        "flex": 3
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S7[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S7[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S7[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label":S8[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S8[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S8[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S9[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S9[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S9[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S10[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S10[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S10[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S11[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S11[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S11[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S12[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S12[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S12[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S13[0],
                                                            "uri":"line://app/1595484825-w4PmmQKv?" + S13[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S13[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S14[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S14[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S14[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": S15[0],
                                                            "uri": "line://app/1595484825-w4PmmQKv?" + S15[2]
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": S15[1],
                                                        "flex": 19
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "body": {
                                            "backgroundColor": "#FF9500"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "コマンド",
                                                        "margin": "xl",
                                                        "size": "xxs",
                                                        "align": "center",
                                                        "flex": 14
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "状態",
                                                        "margin": "xxl",
                                                        "size": "xxs",
                                                        "align": "start",
                                                        "flex": 3
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "オール オン",
                                                            "uri": "line://app/1595484825-w4PmmQKv?ALLON"
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "button",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "オール オフ",
                                                            "uri": "line://app/1595484825-w4PmmQKv?ALLOFF"
                                                        },
                                                        "height": "sm",
                                                        "style": "primary",
                                                        "color": "#00FF73",
                                                        "flex": 96
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                    cl.log(Squick)
                    cl.sendFlex(to,Squick)
                elif text.lower() == 'g情報':
                    Ginfo_ = "[グループ情報]"
                    try:
                        group = cl.getGroup(to)
                        try:
                            gCreator = group.creator.displayName
                            contact = cl.getContact(group.creator.mid)
                            Cpath = "https://os.line.naver.jp/os/p/{}".format(group.creator.mid)
                        except:
                            gCreator = ""
                            Cpath = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                        if group.invitee == [] or group.invitee is None or group.invitee == {}:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "リンクは閉じられています"
                            gTicket = "URL発行されていません"
                        else:
                            gQr = "許可されています"
                            gTicket = "line://ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        cl.log(gTicket)
                        path = "https://os.line.naver.jp/os/g/" + str(group.id)
                        Ginfo_ += "\nグループ名: {}".format(str(group.name))
                        Ginfo_ += "\nグループid: {}".format(group.id)
                        Ginfo_ += "\nグループ作成者: {}".format(str(gCreator))
                        Ginfo_ += "\nグループ人数: {}".format(str(len(group.members)))
                        Ginfo_ += "\n招待中: {}".format(gPending)
                        Ginfo_ += "\nURL: {}".format(gQr)
                        Ginfo_ += "\nURL: {}".format(gTicket)
                        Ginfo_ += "\nです。"
                        daxs = {
                            "type": "flex",
                            "altText": "グループ情報",
                            "contents":  {
                                "type": "bubble",
                                "body": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(Ginfo_),
                                            "wrap": True,
                                            "color": "#1AE501",
                                            "align": "center"
                                        }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "style": "link",
                                            "height": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "~FREE BOT~",
                                                "uri": "https://line.me/ti/p/"
                                            }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm"
                                        }
                                    ],
                                    "flex": 0
                                }
                            }
                        }
                        cl.sendFlex(to,daxs)
                        datas ={
                            "type": "template",
                            "altText": "グル画像&グル作成者",
                            "template": {
                                "type": "image_carousel",
                                "columns": [
                                    {
                                        "imageUrl": str(path),
                                        "layout": "horizontal",
                                        "action": {
                                            "type":"uri",
                                            "label":"グル画像",
                                            "uri": str(path)
                                        }
                                    },
                                    {
                                        "imageUrl":str(Cpath),
                                        "layout": "horizontal",
                                        "action": {
                                            "type":"uri",
                                            "label":"グル作成者",
                                            "uri":str(Cpath)
                                        }
                                    }
                                ]
                            }
                        }
                        cl.sendFlex(to,datas)
                    except Exception as e:
                        cl.log(e)
                elif text.lower() == "メンバーリスト":
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        cl.reissueUserTicket()
                        ret_ = "╭━━━══[ Member List ]"
                        no = 0 + 1
                        for mid in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mid.displayName))
                            no += 1
                        ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                        cl.sendMessage(to,ret_)
                        try:
                            warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            data = {
                                "type": "flex",
                                "altText": "{} MEMBER LIST".format(str(cl.getProfile().displayName)),
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": str(ret_),
                                                "wrap": True,
                                                "color": warnanya1,
                                                "align": "center"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [{
                                            "type": "button",
                                            "style": "link",
                                            "height": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "~FREE BOT~",
                                                "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                                                }                                                      
                                            },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }],
                                        "flex": 0
                                    }
                                }
                            }
                            cl.sendFlex(to, data)
                        except Exception as e:
                            cl.sendMessage(to,str(e))
            if sender in admins or Right:
#####################################################################################################################
                if text.lower() == "権限リスト":
                    Head = "【権限リスト】\n♚最高権限\n"
                    Head2 = "★貴族権限\n"
                    Head3 = "フリー権限\nみんな！！"
                    cl.log(admins)
                    cl.log(Right)
                    for A in admins:
                        try:
                            Head += "・" + cl.getContact(A).displayName + "\n"
                        except Exception as error:
                            #client.sendMessage(msg.to,str(error))
                            Head += "・Removed Contact\n"+str(error)+"\n"
                    Head += Head2
                    if Right == []:
                        Head += "権限者はいません\n"
                    else:
                        for B in Right:
                            try:
                                Head += "・" + cl.getContact(B).displayName + "\n"
                            except Exception as error:
                                #client.sendMessage(msg.to,str(error))
                                Head += "・Removed Contact\n"+error+"\n"
                    Head += Head3        
                    cl.sendMessage(to,Head)
                elif text.lower() == "再起動":
                    restartBot()
                    cl.sendMessage(to, "botを再起動しました")
                elif text.lower() == "モード変更" or text == "MODECHANGE":
                    if settings["autoRespon"] == False:
                        settings["autoRespon"] = True
                        cl.sendMessage(to,"モード癒に移行します")
                    elif settings["autoRespon"] == True:
                        settings["autoRespon"] = False
                        cl.sendMessage(to,"モード正常に移行します")
                ##############################################################################################
                elif text.lower() == "追加オン" or text == "ADDON":
                    if settings["autoAdd"] == True:
                        cl.sendMessage(to,"既にオンです。")
                    else:
                        settings["autoAdd"] = True
                        cl.sendMessage(to,"オンにしました。")
                elif text.lower() == "追加オフ" or text == "ADDOFF":
                    if settings["autoAdd"] == False:
                        cl.sendMessage(to,"既にオフです。")
                    else:
                        settings["autoAdd"] = False
                        cl.sendMessage(to,"オフにしました。")
##############################################################################################
                elif text.lower() == '参加オン' or text ==  "JOINON":
                    settings['autoJoin'] = True
                    cl.sendMessage(to,"オンにしました")
                elif text.lower() == '参加オフ' or text ==  "JOINOFF":
                    settings['autoJoin'] = False
                    cl.sendMessage(to,"オフにしました")
##############################################################################################
                elif text.lower() == 'URL探知オン' or text ==  "TICKETURLON":
                    settings['autoJoinTicket'] = True
                    cl.sendMessage(to,"オンにしました")
                elif text.lower() == 'URL探知オフ' or text ==  "TICKETURLOFF":
                    settings['autoJoinTicket'] = False
                    cl.sendMessage(to,"オフにしました")
##############################################################################################
                elif text.lower() == '自動既読オン' or text ==  "AUTOREADON":
                    settings['autoRead'] = True
                    cl.sendMessage(to,"自動既読をオンにしました")
                elif text.lower() == '自動既読オフ' or text ==  "AUTOREADOFF":
                    settings['autoRead'] = False
                    cl.sendMessage(to,"自動既読をオフにしました")
##############################################################################################
                elif text.lower() == '参加挨拶オン' or text ==  "SANKAON":
                    settings["sanka"] = True
                    cl.sendMessage(to, "参加挨拶をオンにしました")
                elif text.lower() == '参加挨拶オフ' or text ==  "SANKAOFF":
                    settings["sanka"] = False
                    cl.sendMessage(to, "参加挨拶をオフにしました")
##############################################################################################
                elif text.lower() == '退会挨拶オン' or text ==  "TAIKAION":
                    settings["taikai"] = True
                    cl.sendMessage(to, "退会挨拶をオンにしました")
                elif text.lower() == '退会挨拶オフ' or text ==  "TAIKAIOFF":
                    settings["taikai"] = False
                    cl.sendMessage(to, "グループ自動参加をオフにしました")
##############################################################################################
                elif text.lower() == 'URL変更通知オン' or text ==  "CHANGEURLON":
                    settings["CHANGEDURL"] = True
                    cl.sendMessage(to, "URL変更通知をオンにしました")
                elif text.lower() == "URL変更通知オフ" or text ==  "CHANGEURLOFF":
                    settings["CHANGEDURL"] = False
                    cl.sendMessage(to, "URL変更通知をオフにしました")
##############################################################################################
                elif text.lower() == '画像変更通知オン' or text ==  "GPNGON":
                    settings["CHANGEDGPNG"] = True
                    cl.sendMessage(to, "画像変更通知をオンにしました")
                elif text.lower() == '画像変更通知オフ' or text ==  "GPNGOFF":
                    settings["CHANGEDGPNG"] = False
                    cl.sendMessage(to, "画像変更通知をオフにしました")
##############################################################################################
                elif text.lower() == '名前変更通知オン' or text ==  "GNAMEON":
                    settings["CHANGEDGNAME"] = True
                    cl.sendMessage(to, "名前変更通知をオンにしました")
                elif text.lower() == '名前変更通知オフ' or text ==  "GNAMEOFF":
                    settings["CHANGEDGNAME"] = False
                    cl.sendMessage(to, "名前変更通知をオフにしました")
##############################################################################################    
                elif text.lower() == '連絡先オン' or text ==  "CONTACTON":
                    settings["checkContact"] = True
                    cl.sendMessage(to, "連絡先をオンにしました")
                elif text.lower() == '連絡先オフ' or text ==  "CONTACTOFF":
                    settings["checkContact"] = False
                    cl.sendMessage(to, "連絡先をオフにしました")
##############################################################################################
                elif text.lower() == '投稿オン' or text ==  "POSTON":
                    settings["checkPost"] = True
                    cl.sendMessage(to, "投稿オンにしました")
                elif text.lower() == '投稿オフ' or text ==  "POSTOFF":
                    settings["checkPost"] = False
                    cl.sendMessage(to, "投稿オフにしました")
##############################################################################################  
                elif text.lower() == '強制退出オン' or text ==  "AUTOLEAVEON":
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "強制退出オンにしました")
                elif text.lower() == '強制退出オフ' or text ==  "AUTOLEAVEOFF":
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "強制退出オフにしました")
##############################################################################################  
                elif text.lower() == '送信取り消しオン' or text ==  "UNSENDON":
                    settings["unsendMessage"] = True
                    cl.sendMessage(to, "送信取り消しオンにしました")
                elif text.lower() == '送信取り消しオフ' or text ==  "UNSENDOFF":
                    settings["unsendMessage"] = False
                    cl.sendMessage(to, "送信取り消しオフにしました")
##############################################################################################
                elif text.lower() == 'クロックオン' or text ==  "CLOCKON":
                    wait["clock"] = True
                    cl.sendMessage(to, "クロックオンにしました")
                elif text.lower() == 'クロックオフ' or text ==  "CLOCKOFF":
                    wait["clock"] = False
                    cl.sendMessage(to, "クロックオフにしました")
##############################################################################################
                elif text.lower() == 'ランダム追加オン' or text ==  "randomON":
                    wait["FriendAdd"] = True
                    cl.sendMessage(to, "ランダム追加オンにしました")
                elif text.lower() == 'ランダム追加オフ' or text ==  "randomOFF":
                    wait["FriendAdd"] = False
                    cl.sendMessage(to, "ランダム追加オフにしました")
##############################################################################################
                elif text ==  "ALLON":
                    settings["autoAdd"] = True
                    wait["clock"] = True
                    settings['autoJoin'] = True
                    settings['autoJoinTicket'] = True
                    settings['autoRead'] = True
                    settings["sanka"] = True
                    settings["taikai"] = True
                    settings["CHANGEDURL"] = True
                    settings["CHANGEDGPNG"] = True
                    settings["CHANGEDGNAME"] = True
                    settings["checkContact"] = True
                    settings["checkPost"] = True
                    settings["autoLeave"] = True
                    settings["unsendMessage"] = True
                    cl.sendMessage(to, "すべてオンにしました")
                elif text ==  "CLOCKOFF":
                    settings["autoAdd"] = False
                    wait["clock"] = False
                    settings['autoJoin'] = False
                    settings['autoJoinTicket'] = False
                    settings['autoRead'] = False
                    settings["sanka"] = False
                    settings["taikai"] = False
                    settings["CHANGEDURL"] = False
                    settings["CHANGEDGPNG"] = False
                    settings["CHANGEDGNAME"] = False
                    settings["checkContact"] = False
                    settings["checkPost"] = False
                    settings["autoLeave"] = False
                    settings["unsendMessage"] = False
                    cl.sendMessage(to, "すべてオフにしました")
##############################################################################################
            if sender in admins:
                if "権限追加" in text:
                    rightMid = json.loads(msg.contentMetadata['MENTION'])['MENTIONEES'][0]['M']
                    if str(rightMid) in Right:
                        cl.sendMessage(to,"すでに{}".format(cl.getContact(rightMid).displayName)+"は貴族権限リストに追加されているよ")
                    else:
                        Right.append(str(rightMid))
                        with open('Right.json','w') as f:
                            json.dump(Right, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName) + "さんを権限リストに追加したよ")
                elif "権限削除" in text:
                    rightMid = json.loads(msg.contentMetadata['MENTION'])['MENTIONEES'][0]['M']
                    if str(rightMid) not in Right:
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName)+"は貴族権限リストにいないよ")
                    else:
                        Right.remove(str(rightMid)) #場合によりここでエラー起きる可能性大
                        with open('Right.json','w') as f:
                            json.dump(Right, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName) + "さんを権限リストから削除したよ")
##############################################################################################################################
                elif "最高追加" in text:
                    rightMid = json.loads(msg.contentMetadata['MENTION'])['MENTIONEES'][0]['M']
                    if str(rightMid) in admins:
                        cl.sendMessage(to,"すでに{}".format(cl.getContact(rightMid).displayName)+"は貴族権限リストに追加されているよ")
                    else:
                        admins.append(str(rightMid))
                        with open('admin.json','w') as f:
                            json.dump(admins, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName) + "さんを権限リストに追加したよ")
                elif "最高削除" in text:
                    rightMid = json.loads(msg.contentMetadata['MENTION'])['MENTIONEES'][0]['M']
                    if str(rightMid) not in admins:
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName)+"は貴族権限リストにいないよ")
                    else:
                        admins.remove(str(rightMid))
                        with open('admins.json','w') as f:
                            json.dump(admins, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"{}".format(cl.getContact(rightMid).displayName) + "さんを権限リストから削除したよ")
                elif "Gi:" in msg.text:
                    bctxt = text.replace("Gi:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                        time.sleep(0.5)
                        #全グル一斉送信
                elif "ci:" in msg.text:
                    bctxt = text.replace("ci:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                        time.sleep(0.3)
                        #全個チャ一斉送信
                elif "TL:" in msg.text:
                    try:
                        timetext = text.replace("TL:","")
                        cl.createPost(text=str(timetext))
                        cl.sendMessage(to,"完了")
                    except Exception as e:
                        print(e)
                elif text.lower() ==  'オールミッド':
                    try:
                        t = cl.getAllContactIds()
                        if t == []:
                            cl.sendMessage(to,"友達はいません..")
                        else:
                            mc = "╔══[ All Mid List ]"
                            for singleid in t:
                                try:
                                    mc += "\n╠ "+cl.getContact(singleid).displayName + "mid:" + str(singleid)
                                    cl.log("╠ "+cl.getContact(singleid).displayName + "mid:" + str(singleid))
                                except:
                                    pass
                            with open('midlists.txt',mode='w',encoding='UTF-8') as f:
                                f.write(mc)
                            cl.sendFile(to,"midlists.txt")
                    except:
                        pass        
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "再起動します")
                    restartBot()
                elif "通話マクロ " in msg.text:
                    if msg.toType == 2:
                        try:
                            strnum = text.replace("通話マクロ ","")
                            num = int(strnum)
                            cl.sendMessage(to, "通話招待完了")
                            for var in range(0,num):
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.acquireGroupCallRoute(to)
                                cl.inviteIntoGroupCall(to, contactIds=members)
                        except Exception as e:
                            cl.sendMessage(to,str(e))
                elif "makuro:" in msg.text:
                    m = msg.text.replace("makuro:","")
                    if m in [""," ","　","\n",None]:
                        cl.sendMessage(to,"変更できない文字列です。")
                        time.sleep(5)
                    else:
                        wait["makuro"] = msg.text.replace("makuro:","")
                        cl.sendMessage(to,"変更しました.\n\n" + m)
                        time.sleep(5)
                elif "Cmakuro" == msg.text:
                    try:
                        cl.sendMessage(to,"現在マクロは以下のように設定されています。\n\n" + str(wait["makuro"]))
                        time.sleep(5)
                    except:                        
                        cl.sendMessage(to,"マクロを設定してください。")
                        time.sleep(5)
                elif "tm:" in text:
                    try:
                        s = text.replace("tm:","")
                        num = int(s)
                        cl.sendMessage(to, s + "回マクロするぜ！")
                        for var in range(0,num):
                            cl.sendMessage(to,wait["makuro"])
                        time.sleep(5)
                    except:
                        cl.sendMessage(to,"error")
                elif "forget" in text:
                        wait['makuro'] = ''
                        cl.sendMessage(to, 'reset learn message successfull!')
                        time.sleep(5)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.contentType == 0:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+msg.text)
                        else:
                            cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 1:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+"文字以外のメッセージが送られました")
                        else:
                            cl.log("[%s]"%(msg.to)+"文字以外のメッセージが送られました")
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    elif msg.contentType == 1:
                        cl.downloadObjectMsg(messageId = msg.id,saveAs ="rereadImg/" + str(msg.id)+".png")
                        msg_dict["IMG"][msg.id] = {"from":msg._from,"createdTime":msg.createdTime}
            except:
                pass
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["unsendMessage"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[メッセージを取り消した人は]\n%s\n[内容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["メッセージ回復"]
                        del msg_dict[msg_id]
                    elif msg_id in msg_dict["IMG"]:
                        if msg_dict["IMG"][msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[画像を取り消した人は]\n%s"%(cl.getContact(msg_dict["IMG"][msg_id]["from"]).displayName))    
                            cl.sendImage(at,"rereadImg/" + str(msg_id)+".png")
                            print ("メッセージ回復")
                            try:
                                os.remove('rereadImg/'+str(msg_id)+'.png')
                            except:
                                pass
                        del msg_dict["IMG"][msg_id]
                else:
                    pass
            except Exception as e:
                print(e)  
    except Exception as error:
        cl.log(error)

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                times = ["10","20","30","40","50","60","00"]
                if datetime.datetime.now().strftime("%M") in times:
                    if datetime.datetime.now().strftime("%S") == "00":
                        nowT = datetime.datetime.now().strftime("[%H:%M]")
                        profile = cl.getProfile()
                        profile.displayName = "希望と涙" + str(nowT)
                        cl.updateProfile(profile)
                        time.sleep(5)
        except Exception as e:
            cl.log(e)
            
#----------------------------------------

#-------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def friendAdd():
    while True:
        if wait["FriendAdd"] == True:
            if datetime.datetime.now().strftime("%S") == "00":
                try:
                    RGID = random.choice(cl.getGroupIdsJoined())
                    group = cl.getGroup(RGID)
                    gMembMids = [contact.mid for contact in group.members]
                    RMID = random.choice(gMembMids)
                    cl.log(RMID)
                    try:
                        cl.findAndAddContactsByMid(RMID)
                        cl.sendMessage(RMID,"フリーbotです。\n自動で追加しました\nhelpでどうぞ\n邪魔な場合ブロックしてください")
                    except:
                        cl.log("追加に失敗しました")
                except:
                    cl.log("追加に失敗しました")
                time.sleep(2)
#----------------------------------------

#-------------------------------
thread3 = threading.Thread(target=friendAdd)
thread3.daemon = True
thread3.start()
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)




