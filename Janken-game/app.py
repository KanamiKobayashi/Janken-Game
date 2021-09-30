import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g, flash
import pandas as pd
import numpy as np
import random

app = Flask(__name__)

#フロントエンドでフォルダを認識させるためのおまじないコード
SAVE_DIR = "image"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

#ここで認識させている
@app.route('/image/<path:filepath>')
def send_js(filepath):
    return send_from_directory(SAVE_DIR, filepath)

# メインルーチン
@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        # myhand = int(request.form.get('myhand_path'))
        myhand_str = request.form.get('myhand_path')

        if myhand_str:
            myhand = int(myhand_str)

            yourhand = random.randint(0, 2)

            if myhand == 0:
                myhand_s = "グー"
                myhand_pic = "./image/gu.png"
            elif myhand == 1:
                myhand_s = "チョキ"
                myhand_pic = "./image/choki.png"
            elif myhand == 2:
                myhand_s = "パー"
                myhand_pic = "./image/pa.png"
# ここにコンピュータの手の文字列と画像を定義するコードをいれる
            if yourhand == 0:
                yourhand_s = "グー"
                yourhand_pic = "./image/gu.png"
                if myhand == 0:
                    result="あいこ"
                    result_img="./image/aiko.gif"
                elif myhand == 1:
                    result='負け'
                    result_img="./image/make.gif"
                elif myhand == 2:
                    result='勝ち'
                    result_img="./image/kachi.gif"
            elif yourhand == 1:
                yourhand_s = "チョキ"
                yourhand_pic = "./image/choki.png"
                if myhand == 0:
                    result='勝ち'
                    result_img="./image/kachi.gif"
                elif myhand == 1:
                    result='あいこ'
                    result_img="./image/aiko.gif"
                elif myhand == 2:
                    result='負け'
                    result_img="./image/make.gif"
            elif yourhand == 2:
                yourhand_s = "パー"
                yourhand_pic = "./image/pa.png"
                if myhand == 0:
                    result='負け'
                    result_img="./image/make.gif"
                elif myhand == 1:
                    result='勝ち'
                    result_img="./image/kachi.gif"
                elif myhand == 2:
                    result='あいこ'
                    result_img="./image/aiko.gif"

            return render_template("index.html", 
                                    result=result,
                                    result_img=result_img,
                                    myhand_s=myhand_s, 
                                    myhand_pic=myhand_pic,
                                    yourhand_s=yourhand_s,
                                    yourhand_pic=yourhand_pic)
        else:
            error_message="グー、チョキ、パーを選んでください"
            return render_template("index.html", 
                                    error_message=error_message)

#ここで英語バージョンを入力認識させている
@app.route('/enversion', methods=["GET","POST"])
#変えたところ↓
def show_en():
    if request.method == "GET":
        return render_template("enversion.html")

    if request.method == "POST":

        # myhand = int(request.form.get('myhand_path'))
        myhand_str = request.form.get('myhand_path')

        if myhand_str:
            myhand = int(myhand_str)

            yourhand = random.randint(0, 2)

            if myhand == 0:
                myhand_s = "Rock"
                myhand_pic = "./image/gu.png"
            elif myhand == 1:
                myhand_s = "Scissors"
                myhand_pic = "./image/choki.png"
            elif myhand == 2:
                myhand_s = "Paper"
                myhand_pic = "./image/pa.png"
# コンピュータの手の文字列と画像を定義するコード
            if yourhand == 0:
                yourhand_s = "Rock"
                yourhand_pic = "./image/gu.png"
                if myhand == 0:
                    result="Draw"
                    result_img="./image/aiko.gif"
                elif myhand == 1:
                    result='Lose'
                    result_img="./image/make.gif"
                elif myhand == 2:
                    result='Win'
                    result_img="./image/kachi.gif"
            elif yourhand == 1:
                yourhand_s = "scissors"
                yourhand_pic = "./image/choki.png"
                if myhand == 0:
                    result='Win'
                    result_img="./image/kachi.gif"
                elif myhand == 1:
                    result='Draw'
                    result_img="./image/aiko.gif"
                elif myhand == 2:
                    result='Lose'
                    result_img="./image/make.gif"
            elif yourhand == 2:
                yourhand_s = "Paper"
                yourhand_pic = "./image/pa.png"
                if myhand == 0:
                    result='Lose'
                    result_img="./image/make.gif"
                elif myhand == 1:
                    result='Win'
                    result_img="./image/kachi.gif"
                elif myhand == 2:
                    result='Draw'
                    result_img="./image/aiko.gif"
            #変えたところ↓
            return render_template("enversion.html", 
                                    result=result,
                                    result_img=result_img,
                                    myhand_s=myhand_s, 
                                    myhand_pic=myhand_pic,
                                    yourhand_s=yourhand_s,
                                    yourhand_pic=yourhand_pic)
        else:
            error_message="Select Rock, Scissors or Paper!"
            #変えたところ↓
            return render_template("enversion.html", 
                                    error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=9999) # ポートの変更
