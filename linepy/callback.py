# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' on your LINE for smartphone in 2 minutes")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('Open this link ' + notice + 'on your LINE for smartphone in 2 minutes\n' + url)
        if showQr:
            try:
                with open("QR.txt","w") as f:
                    f.write(url)
                import qrcode
                img = qrcode.make(url)
                img.save("QRcode.png")
                import tkinter
                from PIL import Image, ImageTk

                # windowを描画
                window = tkinter.Tk()
                # windowサイズを変更
                window.geometry("700x500")
                # windowタイトルを設定
                window.title("Plz open the QRcode")

                # 画像を表示するための準備
                img = Image.open("QRcode.png")
                img = ImageTk.PhotoImage(img)
                # 画像を表示するためのキャンバスの作成（黒で表示）
                canvas = tkinter.Canvas(width=600, height=400)
                canvas.place(x=100, y=50) # 左上の座標を指定
                # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
                canvas.create_image(30, 30, image=img, anchor=tkinter.NW)
                text = tkinter.Label(window,text="読み込んだ後はウィンドウを閉じてください",anchor=tkinter.SW)
                text.pack()
                window.mainloop()
            except Exception as e :
                print(e)

    def default(self, str):
        self.callback(str)