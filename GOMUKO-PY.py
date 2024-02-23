from lib2to3.pytree import NodePattern
from os import symlink
import os
from pickle import FALSE, TRUE
import random
from telnetlib import NOP
from tkinter import N
from turtle import position

gamerunning= True
currentplayer="x"
winner=None



   

    
   


def updateboard(r,c,Turn):
    B[r][c]=sym[Turn-1]


def printboard(B,Dim):
     os.system('cls')
     for r in range(0,Dim):
         for c in range(0,Dim):
             print(B[r][c], end="")
         print()   

def turnmsg(name):
    print(f"{name}'s turn: ")

def selectposition(Dim):
    pr=int(input(f" select position(1.....{Dim}): "))
    if (pr>=1 and pr<=Dim and B[pr-1]):
        B[pr-1]=currentplayer
    else:
        print("wrong input")



def placemove(B,pr,pc,Symbol):
    B[pr][pc]=Symbol

def turnchange():
    if currentplayer=='x':
        currentplayer=='/'
    else:
        currentplayer=='x'

def playerwin(B,player):
    pass



def iswin(B,n,x,y):
    end=len(B)
    sym=B[x][y]
    
    def check(values):
        c=0
        for i in values:
            if i==sym:
                c+=1
            else:
                c=0
            if c==n:
                return True
        return False

    if check([B[j][y] for j in range(max(0,x-n+1),min(end,x+n))]):
             winner=B[0]
             print("winner is:", (winner))
    elif check([B[x][j] for j in range(max(0,y-n+1),min(end,y+n))]):
          winner=B[0]
          print("winner is:", (winner))
    elif check([B[x+j][y+j] for j in range(max(-x,-y,1-n),min(end-x,end-y,n))]):
          winner=B[0]  
          print("winner is:", (winner))
    elif  check([B[x+j][y-j] for j in range(max(-x,y-end+1,1-n),min(end-x,y+1,n))]):
         winner=B[0]    
         print("winner is:" ,(winner))






def game_over():
    if (ecells(B)==0):
        return True

def ecells(B):
    count=0
    for r in range(len(B)):
         for c in range(len(B[r])):
             if(B[r][c]=='-'):
                 count+=1
    return count

def tie(B,Dim):
    if"-" not in B:
        printboard(B,Dim)
        print("it is a tie")
        gamerunning=False

def computer(B,Dim):
    while currentplayer==B[0]:
         position=random.randint(0,Dim)
         if B[position]=='-':
             B[position]=='x'
             turnchange()





   


while gamerunning:
    B=[]
    Dim=int(input("Dim: "))
    NOP=int(input("Number of players: "))

    for r in range (0,Dim):
        row=[]
        for c in range(0,Dim):
            row.append('-')
        B.append(row)
    
        sym=[]
        pname= []
  
    for i in range(0,NOP):
        pname.append(input(f"player {i+1}'s name "))
        sym.append(input(f"player {i+1}'s symbol "))
   
    Turn= random.randint(0,NOP-1)
    printboard(B,Dim)
    selectposition(Dim)
    iswin(B,NOP,Dim,Dim)
    tie(B,Dim)
    turnchange()
    


