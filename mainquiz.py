from tkinter import Tk, Frame, Label, Button


class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter


    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!",font="monospace 30 bold",fg="green", bg="light blue")
            right += 1
        else:
            label = Label(view, text="Wrong!",font="monospace 30 bold",fg="Red",bg="light blue")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        lala.destroy()
        lala2.destroy()
        lala3.destroy()
        lala4.destroy()
        view = Frame(window,bg="light blue")
        Label(view, text=self.question, font="monospace 17 bold",bg="light blue").pack(pady=(100,0))
        Button(view, text=self.answers[0],bg="yellow", command=lambda *args:         self.check("A", view)).pack()
        Button(view, text=self.answers[1],bg="yellow", command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2],bg="yellow", command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3],bg="yellow", command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the Quiz.\n " + str(right) + " of " + str(number_of_questions) + "\n questions answered right",font="monospace 20 bold",bg="light blue").pack(pady=(300,0))
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.config(background="light blue")
window.title("Quizzer")
window.geometry("500x700")
lala=Label(window,text="Welcome to Quizzer!", bg="light blue", font="monospace 22 bold", fg="black")
lala.pack(pady=(40,0))
lala2=Label(window,text="There are 4 questions that are to be answered", bg="light blue", font="monospace 16 bold", fg="orange")
lala2.pack(pady=(50,0))
lala3=Label(window,text="All the very Best! \n Don't cheat!", bg="light blue", font="monospace 10 italic", fg="red")
lala3.pack(pady=(60,0))
button = Button(window, text="Start", width="20", command=askQuestion,fg="green")
button.pack(pady=(70,0))
lala4=Label(window,text="Designed and made by \n Vibhav,Tathagata and Vandana(Team 13)\n For the Sem 1 CS Project. \n Made using tkinter and python", bg="light blue", font="monospace 19 italic", fg="black")
lala4.pack(pady=(80,0))
window.mainloop()