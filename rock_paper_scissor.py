import tkinter  as tk
from tkinter import PhotoImage


import random

root =tk.Tk()

root.geometry("500x500")
root.maxsize(500,500)


image = PhotoImage(file="pngwing.com.png")
label = tk.Label(root, image=image,background="pink",width=450,height=400)


label.pack()


root.title("Rock Paper Scissor")
root.configure(background="pink")

#dialouge box to ask user name
# user_input=askstring("Rock Paper Scissor", "Enter your Name")

def get_user_input():
    global user_name_input
    global enter_button
    global  username_info 
    username_info=tk.Label(root,text="Enter your Name",font='Arial 12 italic',padx=20)
    username_info.place(x=0,y=428)

    user_name_input=tk.Entry(root,width=30,bd=3)
    user_name_input.place(x=180,y=430)
    user_name=user_name_input.get()
   

    # enter button to perform the task after getting the user name
    enter_button=tk.Button(root,text="Enter",command=enter,bd=3)
    enter_button.place(x=400,y=429)


    

def enter():
    global username_info
    
    global user_name
    
    user_name=user_name_input.get()
    user_name_input.destroy()
    enter_button.destroy()
    start_button.destroy()
    username_info.destroy()
    choice_screen()


    

# 1.How to add the dialouge box to the screen
start_button=tk.Button(root,text="Start",command=get_user_input,justify='right')
start_button.pack()





#2.choose rock paper sccisor screen


def choice_screen():

    global user_name
    global lets_play_label

    root.configure(background="pink")
    lets_play_label=tk.Label(root,text=f"LET'S PLAY!!! {user_name} Choose your choice",font='Arial 18 italic',padx=20)
    lets_play_label.pack()
    #Buttons for choosing the choice
    rock_button=tk.Button(root,text="Rock",command=lambda:choose('rock'))
    rock_button.place(x=100,y=200)
    paper_button=tk.Button(root,text="Paper",command=lambda:choose('paper'))
    paper_button.place(x=200,y=200)
    scissor_button=tk.Button(root,text="Scissor",command=lambda:choose('scissor'),)
    scissor_button.place(x=300,y=200)
    
    


def choose(user_choice):
    root.configure(background="green")
    # destroy the choice buttons
    global computer_choice
    global declaration1
    global result

    global play_again_button
    global exit_button

    computer_choice=random.choice(['rock','paper','scissor'])
    out=decision(user_choice,computer_choice)
    lets_play_label.destroy()


    declaration1= tk.Label(root,text=f"You Chose {user_choice.capitalize()} Computer chose {computer_choice.capitalize()}",font='Arial 15 italic',padx=20)
    declaration1.pack()
    result=tk.Label(root,text=f"{out}",font='Arial 18 italic',padx=20)
    result.pack()

    #play again button
    play_again_button=tk.Button(root,text="Play Again",command=lambda:play_again())
    play_again_button.place(x=100,y=300)

    #exit button
    exit_button=tk.Button(root,text="Exit",command=root.destroy)
    exit_button.place(x=350,y=300)


def play_again():
    
    
    root.configure(background="pink")
    play_again_button.destroy()
    exit_button.destroy()
    declaration1.destroy()
    result.destroy()
    choice_screen()
    



   
    





    

    

   
         

  
        
    
        
def decision(user_choice,computer_choice):
     print(user_choice,computer_choice)
     if user_choice==computer_choice: 
        return "It's a tie"
     
     elif user_choice=='rock':
        if computer_choice=='paper':
            return "You Win"
        else:
         return "You Lose"
        
     elif user_choice=='paper':
        if computer_choice=='scissor':
            return "You lose"
        else:
            return "You win"
        

     elif user_choice=='scissor':
        if computer_choice=='rock':
            return "You lose"
        else:
            return "You win"

def show_result():
    root.configure(background="bluegreen")
    tk.Label(root,text=f"YOU CHOSE {user_choice} COMPUTER CHOSE {computer_choice}",font='Arial 18 italic',padx=20).pack()




















root.mainloop()















