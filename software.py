from random import*
from tkinter import filedialog
from tkinter import*

num = "0123456789"
alphanum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum = "0123456789abcdefghijklmnopqrstuvwxyzABCDE  FGHIJKLMNOPQRSTUVWXYZ()*&^%$#@!"

def Create_pass():
  global result
  TheChoice = Tchoice.get()
 
  if TheChoice == "":
    resultBox.delete(0.0,END)
    resultBox.insert(END, "\n Select the type of password you would like")
   
  length = int(pass_length.get())
  randPass = []
  for i in range(length):
    randPass.append(choice(TheChoice))
   
    result = "".join(randPass)
   
    TheResult = "\n***your Password is: "+result
   
    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)
  return result


window = Tk()
window.geometry("800x500")
window.title("password generator")

ProgName = Label(window,font=('ariel',30,'bold'),text="password generator")
ProgName.grid(row=1,column=3,padx=200,pady=30)

Choosetype = Label(window,font=('ariel',15,'bold'),text="choose among the 3")
Choosetype.place(relx=.03, rely=.25)

Tchoice = StringVar()
NumChoice = Radiobutton(window,font=('ariel',10,'bold'),text="Numeric", variable = Tchoice,value = num)
NumChoice.place(relx=.09, rely=.3)
AlphaNumChoice = Radiobutton(window,font=('ariel',10,'bold'),text="AlphaNumeric", variable = Tchoice,value = alphanum)
AlphaNumChoice.place(relx=.09, rely=.4)
SpecialChoice = Radiobutton(window,font=('ariel',10,'bold'),text="SpalphaNumeric", variable = Tchoice,value = spalphanum)
SpecialChoice.place(relx=.09, rely=.5)


size = Label(window,text="Size")
size.place(relx=.36 , rely= .4)

pass_length = Spinbox(window,from_= 5, to=100)
pass_length.place(relx=.4,rely=.4)
pass_length.config(state="readonly")

GenButton = Button(window,text = "Generate",command=Create_pass)
GenButton.place(relx=.1,rely = .6)

resultBox = Text(window, height=6, width = 70)
resultBox.place(relx=.1,rely = .7)

def save():
   with open('test.txt', 'w') as x:
      x.write( 'your saved password' ), x.write('\n')
      x.write( f'  PASSWORD: = {result}' ), x.write('\n')
      import subprocess
      subprocess.Popen(["notepad","test.txt"])
savebutton = Button(window, text='Save',command=save)
savebutton.place(relx=.4,rely=.6)

window.mainloop()
