# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
#cl = LINE()
#普通のURLログイン
cl = LINE("EykBkWqrBYw1Oup4trdb.fqar0GLtqQ22RYHxgVX86W.UgL2EzX0a0eKk11uyHdZYMmulVTlU/RjMv2T/uarg5U=")
#cl = LINE("メアド","パスワード")
#メアドログイン
#cl = LINE()
#cl = LINE("suisui@kpost.be","suisui912")
#↑サブ
#cl = LINE("suikun11@via.tokyo.jp","suisui11")
#↑メイン

cl.log("Auth Token :\n " + str(cl.authToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
admin=['',clMID]
msg_dict = {}
bl = [""]
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
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """
この半botは、むっくんの提供です

botについては下記アカウントまで

line://ti/p/@ipq1266y

★ヘルプ,help
↪︎コマンド送信
★gメンバー ,Gメンバー
↪︎グループメンバーの名前と人数を送信
★gリスト , Gリスト 
↪︎現在参加中のグループ名とグループ数を送信
★g情報 ,G情報
↪︎グループ情報を送信します
★url許可 ,URL許可
↪︎グループ参加URLを許可
★url拒否 ,URL拒否
↪︎グループ参加URLを拒否
★url発行 ,URL発行
↪︎グループ参加URLを発行
★gid ,GID
↪︎グループIDを送信
★グル作者 ,グル作者
↪︎グループ作成者のアカウントを送信
★アイコン (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーのアイコンを送信
★ホーム (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーのホーム画像を送信
★mid (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーのユーザー識別番号を送信
★連絡先 (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーのアカウントを送信
★ホーム画像
↪︎自分のホーム画像を送信
★アイコン画像
↪︎自分のアイコン画像を送信
★uid ,UID
↪︎自分のユーザー識別番号を送信
★me
↪︎自分のアカウントを送信
★test ,TEST,テスト
↪︎半botの動作確認
★リンクオン
↪︎タイムライン共有、ノートの投稿時にリンクを送信します
★リンクオフ
↪︎タイムライン共有、ノートの投稿時にリンク送信しません
★連絡先オン
↪︎送られてきたアカウントの情報送信をします
★連絡先オフ
↪︎送られてきたアカウントの情報送信をしません
★自動参加オン
↪︎グループに招待された時に自動参加します
★自動参加オフ
↪︎グループに招待された時に自動参加しません
★自動追加オン
↪︎追加された時に自動追加してメッセージを送信します
★自動追加オフ
↪︎追加された時に自動追加せず、メッセージも送信しません
★設定確認
↪︎現在の半bot設定を送信
★speed ,SPEED
↪︎処理速度を計測し送信
★ブラックリスト排除
↪︎ブラックリストユーザーをグループから退会させます
★ブラック登録 (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーをブラックリストに登録
★ブラック削除 (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザをブラックリストから削除
★招待 (mid)
↪︎ユーザー識別番号の方をグループに招待
★アカウント情報 (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーのアカウント情報を送信
★グル名変更:(変更したい名前)
↪︎グループ名を変更します
★Nk:(蹴りたい人の文字)
↪︎文字が含まれているユーザーを全て退会させます
★Tk (ﾒﾝｼｮﾝ)
↪︎メンションしたユーザーをグループから退会させます
"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "追加ありがとう、よろしくね\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
        if op.type == 13:
            if settings["autoJoin"] == True:
                if clMID in op.param3:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "自動参加だぜฟฟฟฟฟฟฟฟฟฟ\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
            #group = cl.getGroup(op.param1)
            #contact = cl.getContact(op.param2)
            #if settings["qrprotect"] == True:
                #if op.param2 in admin:
                    #pass
                #else:
                    #gs = cl.getGroup(op.param1)
                    #cl.kickoutFromGroup(op.param1,[op.param2])
                    #gs.preventJoinByTicket = True
                    #cl.updateGroup(gs)
        if op.type == 17:
            if settings["sanka"] == True:
                if op.param2 in clMID:
                    return
                ginfo = cl.getGroup(op.param1)
                cl.sendMessage(op.param1, "よォ腰抜けฟฟฟฟฟฟฟฟฟฟฟฟ\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
        if op.type == 15:
            if settings["taikai"] == True:
                if op.param2 in clMID:
                    return
                cl.sendMessage(op.param1, "お？ビビってにげちまったか？！ฟฟฟฟฟฟฟฟฟฟฟฟ\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
        if op.type == 24:
            print ("[ 24 ]　コピーを残すよう注意してください")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]設定ファイルを更新する")
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
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[表示名]:\n" + msg.contentMetadata["表示名"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステータスメッセージ]:\n" + contact.statusMessage + "\n[アイコン画像url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホーム画像]:\n" + str(cu)) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[表示名]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステータスメッセージ]:\n" + contact.statusMessage + "\n[アイコン画像url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホーム画像]:\n" + str(cu)) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "URL\n" + msg.contentMetadata["postEndUrl"] + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    #helpの後に送信するアカウント
                elif text.lower() == 'ヘルプ':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif "ci:" in msg.text:
                    bctxt = text.replace("ci:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                        #全個チャ一斉送信
                elif "Gi:" in msg.text:
                    bctxt = text.replace("Gi:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                        #全グル一斉送信
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                                    #メンションキックして招待して招待キャンセル
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                    #midキック
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                                #メンションキック
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                                    #メンションキック
                                    #Mk @ のみで使うと全蹴り
                elif "破壊しまぁぁぁすฟฟฟฟฟฟฟฟ " in msg.text:
                    X = cl.getGroup(msg.to)
                    X.name = "破壊しまぁぁぁすฟฟฟฟฟฟฟฟ"
                    cl.updateGroup(X)
                    Mk0 = text.replace("破壊しまぁぁぁすฟฟฟฟฟฟฟฟ ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    time.sleep(0.4)
                                except:
                                    pass
                                    #むっくんkick @ でグル名変更して全蹴り
                elif "Nk:" in msg.text:
                    _name = text.replace("Nk:","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                                    #ネームキック
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                    #midキックして招待してキャンセル
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                                    #メンションキック
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
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
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                            #midでメンションするぞ
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = ""
                        for mi_d in targets:
                            mc += "->" + mi_d + "\n"
                        cl.sendMessage(to,mc)
                elif "グル名変更:" in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("グル名変更:","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(to, "グループ以外では使用できません\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif "アカウント情報" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"表示名:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nステータスメッセージ:\n" + contact.statusMessage + "\n\nアイコン画像:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nホーム画像:\n" + str(cu)) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                        except:
                            cl.sendMessage(msg.to,"表示名:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nステータスメッセージ:\n" + contact.statusMessage + "\n\nホーム画像:\n" + str(cu)) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                elif "招待 " in msg.text:
                    midd = msg.text.replace("招待 ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    #midで招待
                elif "ブラック登録" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "ブラックリストに登録しました\n \n半bot提供者はσ(ﾟ∀ﾟ)です。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                                except:
                                    pass
                elif "ブラック削除" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "ブラックリストから削除しました\n \n半bot提供者はσむっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                                except:
                                    pass
                elif text.lower() == 'ブラックリスト排除':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "ブラックリストに登録されているユーザーはいません\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "ブラックリストユーザーを退会させました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(msg.to,"測定中です...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'只今の速度は\n' + format(str(elapsed_time)) + '秒です\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "再起動します")
                    restartBot()
                elif text.lower() == '稼働時間':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "稼働時間は現在 {}".format(str(runtime)))
                elif text.lower() == '設定確認':
                    try:
                        ret_ = "[設定]"
                        if settings["autoAdd"] == True: ret_ += "\n自動追加:有効"
                        else: ret_ += "\n自動追加:無効"
                        if settings["autoJoin"] == True: ret_ += "\n自動参加:有効"
                        else: ret_ += "\n自動参加:無効"
                        if settings["contact"] == True: ret_ += "\n連絡先情報:有効"
                        else: ret_ += "\n連絡先情報:無効"
                        if settings["timeline"] == True: ret_ += "\nリンク:有効"
                        else: ret_ += "\nリンク:無効"
                        if settings["sanka"] == True: ret_ += "\n参加通知:有効"
                        else: ret_ += "\n参加通知:無効"
                        if settings["taikai"] == True: ret_ += "\n退会通知:有効"
                        else: ret_ += "\n退会通知:無効"
                        if settings["detectMention"] == True: ret_ += "\nメンション返し:有効"
                        else: ret_ += "\nメンション返し:無効"
                        if settings["reread"] == True: ret_ += "\n送信取り消し:有効"
                        else: ret_ += "\n送信取り消し:無効"
                        ret_ += "\n現在はこのように設定されています\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == '自動追加オン':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動追加をオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '自動追加オフ':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動追加をオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ ipq1266y")
                elif text.lower() == '自動参加オン':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "グループ自動参加をオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '自動参加オフ':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "グループ自動参加をオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '連絡先オン':
                    settings["contact"] = True
                    cl.sendMessage(to, "連絡先情報をオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '連絡先オフ':
                    settings["contact"] = False
                    cl.sendMessage(to, "連絡先情報をオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '送信取り消しオン':
                    settings["reread"] = True
                    cl.sendMessage(to, "送信取り消しをオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '送信取り消しオフ':
                    settings["reread"] = False
                    cl.sendMessage(to, "送信取り消しをオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'リンクオン':
                    settings["timeline"] = True
                    cl.sendMessage(to, "タイムラインやノートのリンクをオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'リンクオフ':
                    settings["timeline"] = False
                    cl.sendMessage(to, "タイムラインやノートのリンクをオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")    
                elif text.lower() == 'メンション返しオン':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "メンション返しをオンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'メンション返しオフ':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "メンション返しをオフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '参加通知オン':
                    settings["sanka"] = True
                    cl.sendMessage(to, "参加通知オンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '参加通知オフ':
                    settings["sanka"] = False
                    cl.sendMessage(to, "参加通知オフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")  
                elif text.lower() == '退会通知オン':
                    settings["taikai"] = True
                    cl.sendMessage(to, "退会通知オンにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == '退会通知オフ':
                    settings["taikai"] = False
                    cl.sendMessage(to, "退会通知オフにしました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                    #自分をメンション。自分のアカウント送信。アカウント情報送信
                elif text.lower() == 'uid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                    #自分のmid送信
                elif text.lower() == 'アイコン画像':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    #自分のアイコン送信
                elif text.lower() == 'test':
                    cl.sendMessage(to, "稼働中です\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'ホーム画像':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                    #自分のホーム画像送信
                elif msg.text.lower().startswith("連絡先 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                            #メンション相手のアカウント送信。アカウント情報送信
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = [""]
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                        #   メンション相手のmid送信
                elif msg.text.lower().startswith("アイコン "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ホーム "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
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
                            cl.sendMessage(to, "[以前発行したURLは無効になりました\nグループ参加URLを発行しました]\nline://ti/g/{}".format(str(ticket))) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                        else:
                            cl.sendMessage(to, "urlが拒否されています、urlを許可してください".format(str(settings["keyCommand"]))) + "\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                elif text.lower() == 'url許可':
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "既にURLが許可されているよ\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "URLを許可しました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'url拒否':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "既にURL拒否が拒否されているよ\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "URL拒否しました\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                elif text.lower() == 'g情報':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = ""
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "リンクは閉じられています"
                        gTicket = "URL発行されていません"
                    else:
                        gQr = "許可されています"
                        gTicket = "line://ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[グループ情報]"
                    ret_ += "\nグループ名: {}".format(str(group.name))
                    ret_ += "\nグループid: {}".format(group.id)
                    ret_ += "\nグループ作成者: {}".format(str(gCreator))
                    ret_ += "\nグループ人数: {}".format(str(len(group.members)))
                    ret_ += "\n招待中: {}".format(gPending)
                    ret_ += "\nURL: {}".format(gQr)
                    ret_ += "\nURL: {}".format(gTicket)
                    ret_ += "\nです。\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gメンバー':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[グループのメンバーリスト]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n　{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[ここのグループは現在合計： {}名です]\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'gリスト':
                        groups = cl.groups
                        ret_ = "[参加グループリスト]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n現在参加しているグループの合計は　{}グループ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'all':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "合計 {} メンバー\n \n半bot提供者はσ(ﾟ∀ﾟ)です。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y".format(str(len(nama))))
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[メッセージを取り消した人は]\n%s\n[内容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]) + "\n \nこの半botは、むっくんの提供です\n \n↓botの購入などについては、この方へどうぞ↓\n \nline://ti/p/@ipq1266y")
                            print ["メッセージ回復"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 25 or op.type == 26:
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
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "何か御用でしょうか？\n \n半bot提供者は、むっくんです。\n \n↓botの購入などについては、この方へどうぞ↓\nline://ti/p/@ipq1266y")
                                    sendMessageWithMention(to, contact.mid)
                                break
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
