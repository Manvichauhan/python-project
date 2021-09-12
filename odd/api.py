from tkinter.constants import END, X
from typing import Text
import requests
import json
import tkinter
from tkinter.messagebox import showinfo, showerror


def sendsms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params={
        "authorization":'JDSGNPFlesuLtWqp5TxwyEXZIj410Y79cnfiBdQKmag6ARzOVkFTxn6r1HBGzehPEKRtI5vkp4gOsZay',
        "sender_id":'FSTSMS',
        "message":message,
        "language":'english',
        "route":'v3',
        "numbers":number
    }
    response=requests.get(url,params=params)
    a=response.json()
    # print(a)
    return a.get("return")

sendsms("6232769986","hello Manvi here")
def btnclick():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = sendsms(num,msg)
    if r:
        showinfo("send success","successfully send")
    else:
        showerror("send error", "something went wrong")

#creating gui

root= tkinter.Tk()
root.title("message sender")
root.geometry("400x500")
font = ("helvetica", 22, "bold")
textNumber=tkinter.Entry(root,font=font)
textNumber.pack(fill=X, pady=20)
TextMsg=Text(root)
TextMsg=tkinter.Pack(fill=X, pady=10)
sendBtn=tkinter.Button(root,text="SEND MESSAGE",command=tkinter.Btnclick)
sendBtn.pack()
root.mainloop()