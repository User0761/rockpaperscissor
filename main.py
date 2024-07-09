from tkinter import *
import random

window = Tk()
window.geometry("700x600")
window.title('Rock Paper Scissor Game')
window.configure(bg="#f2faaf")
#heading label
heading = Label(window, text="Please Make Your Choice", width=60, bg="#bedaaa")
heading.pack(side=TOP)
#frame 1
frame1 = Frame(window)
frame1.pack(side=TOP, pady=20)
#frame 2
frame2 = Frame(window)
frame2.pack(side=TOP)
#frame 3
frame3 = Frame(window)
frame3.pack(side=TOP)
#frame 4
frame4 = Frame(window)
frame4.pack(side=TOP, pady=20)
#using images
image1 = PhotoImage(file="rock.png")
image2 = PhotoImage(file="paper.png")
image3 = PhotoImage(file="scissor.png")
#Resizing images
imageRock = image1.subsample(2, 2)
imagePaper = image2.subsample(2, 2)
imageScissor = image3.subsample(2, 2)
#dictionary for giving choice to computer
computer = {"0": "Rock", "1": "Paper", "2": "Scissor"}
#for keeping track of scores
compscore = 0  #computer
userscore = 0  #user
tie = 0  #tie


def rock():
  global compscore, userscore, tie
  computerRandomChoice = computer[str(random.randint(0, 2))]
  if computerRandomChoice == "Rock":
    tie = tie + 1
    userChoice.configure(text="Rock")
    compChoice.configure(text=computerRandomChoice)
    result.configure(text="It's a Tie")
    score.configure(text=tie)
  if computerRandomChoice == "Paper":
    compscore = compscore + 1
    compChoice.configure(text=computerRandomChoice)
    userChoice.configure(text="Rock")
    result.configure(text="COMPUTER WON SCORE IS")
    score.configure(text=compscore)
  if computerRandomChoice == "Scissor":
    userscore = userscore + 1
    userChoice.configure(text="Rock")
    compChoice.configure(text=computerRandomChoice)
    result.configure(text="USER WON SCORE IS")
    score.configure(text=userscore)


def paper():
  computerRandomChoice = computer[str(random.randint(0, 2))]
  global compscore, userscore, tie
  if computerRandomChoice == "Paper":
    tie = tie + 1
    userChoice.configure(text="Paper")
    compChoice.configure(text=computerRandomChoice)
    result.configure(text="It's a Tie")
    score.configure(text=tie)
  if computerRandomChoice == "Rock":
    userscore = userscore + 1
    userChoice.configure(text="Paper")
    compChoice.configure(text=computerRandomChoice)
    result.configure(text="USER WON SCORE IS")
    score.configure(text=userscore)
  if computerRandomChoice == "Scissor":
    compscore = compscore + 1
    compChoice.configure(text=computerRandomChoice)
    userChoice.configure(text="Paper")
    result.configure(text="COMPUTER WON SCORE IS")
    score.configure(text=compscore)


def scissor():
  global compscore, userscore, tie
  computerRandomChoice = computer[str(random.randint(0, 2))]
  if computerRandomChoice == "Scissor":
    tie = tie + 1
    compChoice.configure(text=computerRandomChoice)
    userChoice.configure(text="Scissor")
    result.configure(text="It's a Tie")
    score.configure(text=tie)
  if computerRandomChoice == "Rock":
    compscore = compscore + 1
    compChoice.configure(text=computerRandomChoice)
    userChoice.configure(text="Scissor")
    result.configure(text="COMPUTER WON SCORE IS")
    score.configure(text=compscore)
  if computerRandomChoice == "Paper":
    userscore = userscore + 1
    compChoice.configure(text=computerRandomChoice)
    userChoice.configure(text="Scissor")
    result.configure(text="USER WON SCORE IS")
    score.configure(text=userscore)


def reset():
  global compscore, userscore, tie
  result.configure(text="START THE GAME")
  score.configure(text="0")
  compscore = 0
  userscore = 0
  tie = 0


#button rock
buttonRock = Button(frame1, bg="#befafa", image=imageRock, command=rock)
buttonRock.pack(side=LEFT)
#button paper
buttonPaper = Button(frame1, bg="#befafa", image=imagePaper, command=paper)
buttonPaper.pack(side=LEFT)
#button scissor
buttonScissor = Button(frame1,
                       bg="#befafa",
                       image=imageScissor,
                       command=scissor)
buttonScissor.pack(side=LEFT)
#button reset
reset = Button(window,
               text="Reset",
               bg="#4da6ff",
               fg="black",
               width=10,
               font=("fixedsys", 18),
               command=reset)
reset.pack(side=BOTTOM)
#computer choice label
compLabel = Label(frame2,
                  text="COMPUTER'S CHOICE",
                  font=("fixedsys", 18),
                  width=25,
                  bg="white",
                  fg="red")
compLabel.pack(side=LEFT)
#user choice label
userLabel = Label(frame2,
                  text="USER'S CHOICE",
                  font=("fixedsys", 18),
                  width=25,
                  bg="white",
                  fg="green")
userLabel.pack(side=LEFT)
#display computer choice
compChoice = Label(frame3,
                   font=("fixedsys", 18),
                   width=25,
                   bg="white",
                   fg="red")
compChoice.pack(side=LEFT)
#display user choice
userChoice = Label(frame3,
                   font=("fixedsys", 18),
                   width=25,
                   bg="white",
                   fg="green")
userChoice.pack(side=LEFT)
#label to display status of the game
result = Label(frame4,
               text="Result",
               width=30,
               height=2,
               bg="#ff6683",
               fg="black",
               font=("fixedsys", 20))
result.pack(side=LEFT)
#label to display score
score = Label(frame4,
              text="Score",
              width=10,
              height=2,
              bg="#ff6683",
              fg="black",
              font=("fixedsys", 20))
score.pack(side=RIGHT)
window.mainloop()
