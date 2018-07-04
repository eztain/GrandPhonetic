# Name:  Jake Colson
# Student Number: 10472749

# This file is provided to you as a starting point for the "logviewer.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 1, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary modules.
from tkinter import *
import tkinter.messagebox
import json

with open("log.txt","r") as logFile:
            log = json.load(logFile)
            logFile.close()

print(log)

class ProgramGUI():
    def __init__(self):
        


        
        
        # This is the constructor of the class.
        # It is responsible for loading the log file data and creating the user interface.
        # See the "Constructor of the GUI Class of 'logviewer.py'" section of the assignment brief.
        
        self.main = Tk()
        self.main.title('LogViewer')
        self.main.geometry("400x300")


        self.logNumber = 0
        self.logLength = int(len(log))
        self.showStatsWndw = None
        



        #frames
        self.frm0 = tkinter.Frame(self.main)
        self.frm1 = tkinter.Frame(self.main)
        self.frm2 = tkinter.Frame(self.main)
        self.frm3 = tkinter.Frame(self.main)
        self.frm5 = tkinter.Frame(self.main)
        self.frm6 = tkinter.Frame(self.main)
        self.frm7 = tkinter.Frame(self.main)
        self.sfrm1 = tkinter.Frame(self.main)
        self.sfrm2 = tkinter.Frame(self.main)

        #widgets
        self.txtLogNumber = tkinter.Label(self.frm0, width=10, justify='left', text="Log Number: ")
        self.ansLogNumber = tkinter.Label(self.frm0, width=10, justify='left', text= self.logNumber)
        self.txtPlayers = tkinter.Label(self.frm1, width=10, justify='left', text="Players: ")
        self.ansPlayers = tkinter.Label(self.frm1, width=10, justify='left', text=log[self.logNumber]["Players"])
        self.txtNames = tkinter.Label(self.frm2, width=10, justify='left', text="Names: ")
        self.ansNames = tkinter.Label(self.frm2, width=10, justify='left', text=log[self.logNumber]["Names"])
        self.txtChain = tkinter.Label(self.frm3, width=10, justify='left', text="Chain: ")
        self.ansChain = tkinter.Label(self.frm3, width=10, justify='left', text=log[self.logNumber]["Chain"])
        #self.txtWrdsUsd = tkinter.Label(self.frm4, width=10, justify='left', text="Words Used: ")
        self.ansWrdsUsd = tkinter.Button(self.frm5, text="Words used", command=self.wordsUsed)
        self.nextLog = tkinter.Button(self.frm6,text="Next Log", command=self.logUp)
        self.prevLog = tkinter.Button(self.frm6,text="Previous Log", command=self.logDown)
        self.showStatsBtn = tkinter.Button(self.frm7,text="ShowStats", command=self.showStats)

        
        
        self.txtWinner = tkinter.Label(self.sfrm1, width=10, justify='left', text="Winner: ")
        self.ansWinner = tkinter.Label(self.sfrm1, width=10, justify='left', text=log[self.logNumber]["Winner"])
        #self.txtScoreboard = tkinter.Label(self.sfrm2, width=10, justify='left', text="Scoreboard: ")
        self.ansScoreboard = tkinter.Button(self.frm5,text="Scoreboard", command=self.scoreBoard)
        self.txtWinner.pack(side='left')
        self.ansWinner.pack(side='right')
        #self.txtScoreboard.pack(side='left')
        self.ansScoreboard.pack(side="right")
        
      
        #packing
        self.txtLogNumber.pack(side='left')
        self.ansLogNumber.pack(side='right')
        self.txtPlayers.pack(side='left')
        self.ansPlayers.pack(side='right')
        self.txtNames.pack(side='left')
        self.ansNames.pack(side='right')
        self.txtChain.pack(side='left')
        self.ansChain.pack(side='right')
        #self.txtWrdsUsd.pack(side='left')
        self.ansWrdsUsd.pack(side="left")
        self.nextLog.pack(side='right')
        self.prevLog.pack(side='left')
        self.showStatsBtn.pack(side='left')
        self.frm0.pack()
        self.frm1.pack()
        self.frm2.pack()
        self.frm3.pack()
        self.sfrm1.pack()
        self.sfrm2.pack()
        self.frm5.pack()
        self.frm6.pack()
        
        self.frm7.pack()
        tkinter.mainloop()

        
        
    def logUp(self):
        if self.logNumber < self.logLength - 1:
            self.logNumber += 1
            self.showLog()
        elif self.logNumber == self.logLength - 1:
            self.logError("No new logs")


        print(self.logNumber)

    def logDown(self):
        if self.logNumber > 0:
            self.logNumber -= 1
            self.showLog()

        print(self.logNumber)

    def showLog(self):
        

        self.ansLogNumber.configure(text=self.logNumber)
        self.ansPlayers.configure(text=log[self.logNumber]["Players"])
        self.ansNames.configure(text=log[self.logNumber]["Names"])
        self.ansChain.configure(text=log[self.logNumber]["Chain"])
        #self.ansWrdsUsd.configure(text=log[self.logNumber]["Words used"])
        self.ansWinner.configure(text=log[self.logNumber]["Winner"])
        #self.ansScoreboard.configure(text=log[self.logNumber]["Scores"])
     
        
        # This method is responsible for displaying the details of a log in the GUI.
        # See Point 1 of the "Methods in the GUI Class of 'logviewer.py'" section of the assignment brie


    def showStats(self):
        # This method is responsible for determining and displaying some statistics about the logs,
        # and displaying them in a messagebox.
        # See Point 2 of the "Methods in the GUI Class of 'logviewer.py'" section of the assignment bri
        self.x = 0
        self.maxChain = 0
        for i in range(0, len(log)):
            self.x += log[i]["Players"]

            if log[i]["Chain"] > self.maxChain:
                self.maxChain = log[i]["Chain"]


        self.avgPlayers = round(self.x / len(log),2)

        tkinter.messagebox.showinfo("Stats", "Number of games: " + str(len(log)) + "\nAvarage Number of players: " + str(self.avgPlayers) + "\nLargest chain length: " + str(self.maxChain))


    
    def wordsUsed(self):
        tkinter.messagebox.showinfo("Words Used", str(log[self.logNumber]["Words used"]))

    def scoreBoard(self):
        tkinter.messagebox.showinfo("Scoreboard", log[self.logNumber]["Scores"])

    def logError(self,msg):
        tkinter.messagebox.showinfo("Error", msg)




# Create an object of the ProgramGUI class to begin the program.


gui = ProgramGUI()





