#import publicip
#import sys
import requests
import tkinter as tk

#publicip.get()

window = tk.Tk()
window.geometry("200x225")
window.title("il mio merdoso ip pubblico")
window.configure(background = "#4C4C4C")

topLabel = tk.Label(window,text = "ip pubblico", borderwidth = 2 , relief = "solid" )#tipi di bordi "flat","raised","sunken",ridge","solid","groove" 
topLabel.pack(fill = tk.X , side = tk.TOP)

#ipText = tk.StringVar()
#ipText.set("")
#ipLabel = tk.Label(window, textvariable = ipText , background = "#6E8898")
#ipLabel.pack(fill = tk.X , pady = 15)

ipLabel = tk.Text(window, height = 1 ,background = "#6E8898")
ipLabel.pack(fill = tk.X , pady = 15)
ipLabel.insert(tk.END, "")
ipLabel.tag_configure("conf" , justify = tk.CENTER)
ipLabel.configure(state = "disabled")

def setIpLabel():
    ipStr = requests.get('https://api.ipify.org').text
    print("risultato "+ ipStr)
    ipLabel.configure(state = "normal")
    ipLabel.delete("1.0" , tk.END)
    ipLabel.insert(tk.END , ipStr , "conf")# index,text,tags
    ipLabel.configure(state = "disabled")

button = tk.Button(window ,text = "rivela" , command = setIpLabel)
button.pack(fill = tk.X , padx = 15 , pady = 60 )

window.mainloop()