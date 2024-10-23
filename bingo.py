import tkinter as tk
import random

number_list = []

def random_number():
    if len(number_list) < 75:  #リストの長さが75未満のとき
        while True:
            number = random.randint(1,75) #ランダムで数字を生成
            if number not in number_list:  #出た数字が重複していない場合
                number_list.append(number) #リストの中に生成した数字を入れる

                bango.config(text=number)   #bangoを今出た数字に更新
                break
    else:
        bango.config(text="終わり")

    rireki.config(text=number_list)    #rirekiを今出た数字を追加したリストに更新

root = tk.Tk()
root.title("ビンゴ")
root.geometry("800x600")

bango = tk.Label(root, text="", font=("Book Antiqua", 120))
bango.place(x=300,y=50) #number(出た番号)を表示

rireki = tk.Message(root, text = "",font=("Book Antiqua", 30), width=780)
rireki.place(x=0, y=300)   #これまで出た番号を表示


entry = tk.Button(root, text="番号を出す", command=lambda: random_number())
entry.place(x=300,y=250)



root.mainloop()
