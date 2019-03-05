from tkinter import *
from tkinter import filedialog
from tensorflow_model_sample import mymodel

window = Tk()
window.title("My tensorflow app")
window.configure(background='black')
lbl = Label(window, text="Tensorflow", font=("Arial Bold", 50), bg='black', fg="#ffffff")
lbl.grid(column=0, row=0)
#lbl = Label(window, text="Find folder", bg='black', fg='#ffffff')
#lbl.grid(column=0, row=1)
lbl = Label(window, text="", bg='black')
lbl.grid(column=0, row=1)
check = 0
def fileopen():
    global train_url, check
    train_url = filedialog.askopenfilename()
    print(train_url)
btn = Button(window, text="Training File", command=fileopen, bg="black", fg='white')
btn.grid(column=0, row=2)
#lbl = Label(window, text="Click for run model", bg='black', fg='#ffffff')
#lbl.grid(column=0, row=2)
#def clicked():
#    lbl.configure(text="Start")
#btn = Button(window, text="Run session", command=clicked, bg='black', fg='white')
lbl = Label(window, text="", bg='black')
lbl.grid(column=0, row=3)
def fileopen2():
    global train_url, test_url, check
    test_url = filedialog.askopenfilename()
    print(test_url)
    mymodel(train_url, test_url)

btn = Button(window, text="Testing File", command=fileopen2, bg='black', fg='white')
btn.grid(column=0, row=4)
lbl = Label(window, text="", bg='black')
lbl.grid(column=0, row=5)

window.mainloop()

# 참고 페이지
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# 구성
# csv 파일 불러들이기
# tensorflow 모델을 radio box로 선택하게 하기
# 선택된 모델 코드로 불러오고
# run session을 돌린 후
# 저장할 곳 선택하기
# 출력은 어디로?
