from tkinter import *
import random, tkinter.messagebox

root= Tk()
root.title("TicTacToe.raja")
root.geometry("650x550+270+25")
root.config(bg="black")
root.wm_iconbitmap(r".\icon.ico")
root.resizable(False, False)

l1= Label(root, text="Welcome to Tic Tac Toe", fg="darkred", bg="black", font=("Comic Sans", 26, "bold italic"))
l1.pack(pady=26)
img= PhotoImage(file=".\pic1.png")
p1= Label(root, image=img, bg="black")
p1.pack()
sign= PhotoImage(file=r".\sign.png")
sign_l= Label(root, image=sign, bg="black")
sign_l.pack(side=BOTTOM, anchor=SE, pady=7, padx=2)

check=[]
tiecheck=''
def choose_random(*args, **kwargs):
    while True:
        r= random.randint(0,2)
        c= random.randint(0,2)
        if (r, c) not in check:
            return r, c
        elif len(check)==9:
            print("in")
            return "tie"

def check_win(mode, *args, **kwargs):
    #vertical columns
    a1,b1,c1= play[0][0], play[1][0], play[2][0]
    a2,b2,c2= play[0][1], play[1][1], play[2][1]
    a3,b3,c3= play[0][2], play[1][2], play[2][2]
    #horizontal rows
    x1,y1,z1= play[0][0], play[0][1], play[0][2]
    x2,y2,z2= play[1][0], play[1][1], play[1][2]
    x3,y3,z3= play[2][0], play[2][1], play[2][2]
    #left to right diagonal
    p1,q1,r1= play[0][0], play[1][1], play[2][2]
    #right to left disgonal
    p2,q2,r2= play[0][2], play[1][1], play[2][0]
    if mode=="single":
        if a1==b1==c1=="X" or a2==b2==c2=="X" or a3==b3==c3=="X" or x1==y1==z1=="X" or x2==y2==z2=="X" or x3==y3==z3=='X' or p1==q1==r1=='X' or p2==q2==r2=='X':
            if firstplayer=="X":
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer has WON"):
                    back(1, 's')
                    return "end"
            else:
                if tkinter.messagebox.showinfo("LOST", "Better luck next time\nComputer has won"):
                    back(2, 's')
                    return "end"
        elif a1==b1==c1=="O" or a2==b2==c2=="O" or a3==b3==c3=="O" or x1==y1==z1=="O" or x2==y2==z2=="O" or x3==y3==z3=='O' or p1==q1==r1=='O' or p2==q2==r2=='O':
            if firstplayer=="O":
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer has WON"):
                    back(1, 's')
                    return "end"
            else:
                if tkinter.messagebox.showinfo("LOST", "Better luck next time\nComputer has won"):
                    back(2, 's')
                    return "end"
                 
        elif tiecheck=="tie":
            if tkinter.messagebox.showinfo("Tie", "The game has TIED!!!"):
                back(0, 's')
                return "end"
                
    elif mode=="double":
        if a1==b1==c1=="X" or a2==b2==c2=="X" or a3==b3==c3=="X" or x1==y1==z1=="X" or x2==y2==z2=="X" or x3==y3==z3=='X' or p1==q1==r1=='X' or p2==q2==r2=='X':
            if firstplayer=="X":
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer 1 has WON"):
                    back(1, 'd')
                    return "end"
            else:
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer 2 has WON"):
                    back(2, 'd')
                    return "end"
        elif a1==b1==c1=="O" or a2==b2==c2=="O" or a3==b3==c3=="O" or x1==y1==z1=="O" or x2==y2==z2=="O" or x3==y3==z3=='O' or p1==q1==r1=='O' or p2==q2==r2=='O':
            if firstplayer=="O":
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer 1 has WON"):
                    back(1, 'd')
                    return "end"
            else:
                if tkinter.messagebox.showinfo("WINNER", "CONGRATS!!!\nPlayer 2 has WON"):
                    back(2, 'd')
                    return "end"
        elif len(check)==9:
            if tkinter.messagebox.showinfo("Tie", "The game has TIED!!!"):
                back(0, 'd')
                return "end"
    #colouring
    

def board(mode,*args, **kwargs):
    global frame
    frame=Frame(root, width=650, height=570, bg="black")
    frame.place(x=0, y=0)
    if mode=="single":
        l= Label(frame, text="Single Player Tic Tac Toe", fg="darkred", bg="black", font=("Comic Sans", 22, "bold italic"))
        l.place(x=125, y=10)
    elif mode=="double":
        l= Label(frame, text="Double Player Tic Tac Toe", fg="darkred", bg="black", font=("Comic Sans", 22, "bold italic"))
        l.place(x=125, y=10)
    global var
    var= StringVar()
    global c1
    c1= Label(frame, text="Choose Player 1:", font=("Ariel", 15, "bold"), fg="blue", bg="black")
    c1.place(x=5, y=55)
    global r1
    r1= Radiobutton(frame, text= "X", font=("Ariel", 16, "bold"), fg="#DE7501", bg="black", variable=var, value=1)
    r1.place(x=175, y=55)
    global r2
    r2= Radiobutton(frame, text= "O", font=("Ariel", 16, "bold"), fg="#DE7501", bg="black", variable=var, value=2)
    r2.place(x=235, y=55)
    global btn_r
    if mode=="single":
        global ll
        ll= Label(frame, text="Choose Level: ", font=("Ariel", 15, "bold"), fg="blue", bg="black")
        ll.place(x=5, y=100)
        global var2
        var2= StringVar()
        global rl1
        rl1= Radiobutton(frame, text= "Easy", font=("Ariel", 16, "bold"), fg="#DE7501", bg="black", variable=var2, value=1)
        rl1.place(x=160, y=100)
        global rl2
        rl2= Radiobutton(frame, text= "Hard", font=("Ariel", 16, "bold"), fg="#DE7501", bg="black", variable=var2, value=2)
        rl2.place(x=250, y=100)

    btn_r= Button(frame, text="Play Game", font=("Comic Sans", 14, 'bold'), bg= "#FACC2E", borderwidth=3, cursor="hand2")
    btn_r.place(x=220, y=160)
    if mode=="single":
        btn_r.config(command=single)
    elif mode=="double":
        btn_r.config(command=double)
    global back
    def back(s, mode, *args, **kwargs):
        check.clear()
        global tiecheck
        tiecheck=''
        global score1s, score2s, score1d, score2d
        if s==1 and mode=='s':
            score1s+=1
            score_l.config(text=f"Score: {score1s}\t\t\t\t\t\tScore: {score2s}")
        elif s==2 and mode=='s':
            score2s+=1
            score_l.config(text=f"Score: {score1s}\t\t\t\t\t\tScore: {score2s}")
        elif s==1 and mode=='d':
            score1d+=1
            score_l.config(text=f"Score: {score1d}\t\t\t\t\t\tScore: {score2d}")
        elif s==2 and mode=='d':
            score2d+=1
            score_l.config(text=f"Score: {score1d}\t\t\t\t\t\tScore: {score2d}")
        for i in b:
            for j in i:
                j.config(state="disabled")
        def replay(*args, **kwargs):
            global b, play, player
            play=[[0,0,0],[0,0,0],[0,0,0]]
            for i in b:
                for j in i:
                    j.config(text="", state="normal")
            player=firstplayer
            turn.config(text=f"{player}'s turn")
            rebtn.destroy()
            
        rebtn= Button(frame, text="Play\nAgain", bg='brown',font=("Comic Sans", 20, "bold"), fg="orange", cursor="hand2", command=replay)
        rebtn.place(x=510, y=250)
    def returnn(*args, **kwargs):
        frame.destroy()
        check.clear()
        global tiecheck
        tiecheck=''
    btn_back=Button(frame, text="Back", font="Ariel 13 bold", bg="brown", cursor="hand2",command=returnn)
    btn_back.place(x=460, y=500)
    btn_close=Button(frame, text="Close", font="Ariel 13 bold", bg="brown", cursor="hand2",command=lambda *args, **kwargs: root.destroy())
    btn_close.place(x=530, y=500)

score1s=0
score2s=0
def single(*args, **kwargs):
    # def selected(*args, **kwargs):
    x= var.get()
    y= var2.get()
    if x in ("1", "2") and y in ("1",):
        r1.destroy()
        r2.destroy()
        btn_r.destroy()
        rl1.destroy()
        rl2.destroy()
        if y=='1':
            ll.config(text="Level: Easy", fg="#F79E80")
        elif y=='2':
            ll.config(text='Level: Hard', fg="#F79E80")
        ll.place(x=5, y=135)
        global firstplayer
        global player
        if x=="1":
            c1.config(text="Player: X\t\t\t\t\t       Computer: O")
            player= "X"
            firstplayer="X"
        elif x=='2':
            c1.config(text="Player: O\t\t\t\t         Computer: X")
            player="O"
            firstplayer="O"
        canvas= Canvas(frame, width=350, height=300, bg="black")
        canvas.place(x=120, y=180)
        global turn
        turn= Label(frame, text=f"{player}'s turn", font="Ariel 17 bold", fg="orange", bg="black")
        turn.place(x=260, y=130)
        global score_l
        score_l= Label(frame, text=f"Score: {score1s}\t\t\t\t\t\tScore: {score2s}", font="Tickerbit 15 bold", fg="#FE4001", bg="black")
        score_l.place(x=5, y=90)
        global b
        b=[[0,0,0], [0,0,0],[0,0,0]]
        global play
        play= [[0,0,0], [0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                def callback(i=i, j=j):
                    global player
                    b[i][j].config(text=player, state="disabled")
                    play[i][j]= player
                    player="X" if player=="O" else "O"
                    turn.config(text=f"{player}'s turn")
                    check.append((i,j))
                    cw=check_win("single")
                    if y=="1":
                        cr= choose_random()
                        if cr!="tie" and cw!="end":
                            r, c= cr[0], cr[1]
                            try:
                                b[r][c].config(text=player, state="disabled")
                                play[r][c]= player
                            except:
                                return
                            player="X" if player=="O" else "O"
                            turn.config(text=f"{player}'s turn")
                            check.append((r,c))
                            check_win("single")
                        elif cr=="tie":
                            global tiecheck
                            tiecheck="tie"
                            check_win("single")
                    elif y=="2":
                        print("Under Construction")
                
                b[i][j]= Button(canvas,font=("Ariel", 35, "bold"), bg="beige", width=4, height=1, command= callback)
                b[i][j].grid(row=i, column=j)
    elif y=="2":
        tkinter.messagebox.showinfo("Under Construction", "This mode is under construction\nKindly visit later\nThank you:)")

score1d=0
score2d=0
def double(*args, **kwargs):
    # def selected(*args, **kwargs):
    x= var.get()
    if x in ("1", "2"):
        r1.destroy()
        r2.destroy()
        btn_r.destroy()
        global firstplayer
        global player
        if x=="1":
            c1.config(text="Player 1: X\t\t\t\t\tPlayer 2: O")
            player= "X"
            firstplayer="X"
        elif x=='2':
            c1.config(text="Player 1: O\t\t\t\t\tPlayer 2: X")
            player="O"
            firstplayer="O"
        canvas= Canvas(frame, width=350, height=300, bg="black")
        canvas.place(x=120, y=180)
        global turn
        turn= Label(frame, text=f"{player}'s turn", font="Ariel 16 bold", fg="orange", bg="black")
        turn.place(x=260, y=130)
        global score_l
        score_l= Label(frame, text=f"Score: {score1d}\t\t\t\t\t\tScore: {score2d}", font="Ariel 15 bold", fg="#FE4001", bg="black")
        score_l.place(x=5, y=90)
        global b
        b=[[0,0,0], [0,0,0],[0,0,0]]
        global play
        play= [[0,0,0], [0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                def callback(i=i, j=j):
                    global player
                    b[i][j].config(text=player, state="disabled")
                    play[i][j]= player
                    if player=="X":
                        player="O"
                    else:
                        player="X"
                    turn.config(text=f"{player}'s turn")
                    check.append((i,j))
                    check_win("double")
                
                b[i][j]= Button(canvas,font=("Ariel", 35, "bold"), bg="beige", width=4, height=1, command= callback)
                b[i][j].grid(row=i, column=j)

b1= Button(root, text= "Single Player vs Computer", bg="yellow", font=("Comic Sans", 16, "bold"), cursor="hand2", borderwidth=7, activebackground="green", command= lambda *args, **kwargs: board("single"))
b1.pack(pady=20)
b2= Button(root, text= "Player vs Player", bg="yellow", font=("Comic Sans", 16, "bold"), cursor="hand2", borderwidth=7, activebackground="green", command= lambda *args, **kwargs: board("double"))
b2.pack()

root.mainloop()