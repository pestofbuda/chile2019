from optparse import Values
from tkinter import font
from PIL import Image
import PySimpleGUI as pg

#############
# functions #
#############

def welcome_window_function():
    welcome_window_layout = [
        [pg.Text("This is an interactive story where your choices determine the endings.")],
        [pg.Text("Your ultimate goal is to show empathy and support for people impacted by socio economic inequalities.")],
        [pg.Text("In this story, you are in Chile in 2019. 95% of the popeulation are suffering becaue of inequalities in opportunities for education, health, and employment.")],
        [pg.Text("However, you belong to the 5% that are comfortable, so should you really care?")],
        [pg.Text("To show that you care, you can go and visit downtown where all the problems are happening. Or you can forget this and go back to playing on your xbox and end this story now.")],
        [pg.Button('Visit Downtown'), pg.Button('End Story')]
        ]
    # Step 3: Make window
    welcome_window = pg.Window("Welcome", welcome_window_layout)
    while True:
        event, values = welcome_window.read()
        if event == 'End Story' or event == pg.WIN_CLOSED: 
            welcome_window.close()
            break
        if event == 'Visit Downtown':
            welcome_window.close()
            visit_downtown_window()
            break
    #welcome_window.close()

def visit_downtown_window():
    visit_downtown_layout = [
        [pg.Text("The suffering has caused people to protest and the governemnt has reacted by sending the military on the streets.")],
        [pg.Text("You go to a freinds house and have to close the windows becasue of the tear gas that is always in the air, and you cant go to chat in cafe because everything has been closed down.")],
        [pg.Text("Your friend explains that there will be a march the next day to show solidarity against the inequalities and suffering. She invites you to join. ")],
        [pg.Text("You are not sure if its a good idea as you think it has nothing to do with you. You are lucky, you are in the wealthiest 5% of the population. ")],
        [pg.Text("Do you choose to join or not join the march?")],
        [pg.Button("Join March"), pg.Button("Don't Join March")]
    ]
    visit_downtown_window = pg.Window("You go Downtown...", visit_downtown_layout)
    while True:
        event = visit_downtown_window.read()
        if event == "Don't Join March" or event == pg.WIN_CLOSED:
            visit_downtown_window.close()
            print(event)
            break
        else:
            event == "Join March"
            visit_downtown_window.close()
            join_march_window()
            print(event)
            break



def join_march_window():
    join_march_layout = [
        [pg.Text("1.2 million people attend the march. Its peaceful and empowering.")],
        [pg.Text("You feel an enormous sense of solidarity with the rest of the population.")],
        [pg.Text("The world takes notice, the government takes notice, the result is a change in the constitution and the beginning of more euqal opportunities in Chile for all.")],
        [pg.Text("You made a good choice!")],
        [pg.Button("Final Comments")]
    ]
    join_march_window = pg.Window("You join the march!", join_march_layout)
    while True:
        event = join_march_window.read()
        if event == pg.WIN_CLOSED:
            join_march_window.close()
            print(event)
            break
        else:
            event == "Final Comments"
            join_march_window.close()
            print(event)
            break


def not_join_march_window():
    not_join_march_layout = [
        [pg.Text("You go back to your comfortable home and wonder if you made th eright choice.")],
        [pg.Text("You find out on the news later that 1.2 million people attend the march. ")],
        [pg.Text("The images and comments show that it was a life changing moment, where the country cam together in a show of solidarity.")],
        [pg.Text("The world took notice, the government took notice, the result was a change in the constitution and the beginning of more euqal opportunities in Chile for all. ")],
        [pg.Text("You regret your decision, and know that in the future you should show more support and empathy to those with less opportunities than you.")]
        [pg.Button("Final Comments")]
    ]
    not_join_march_window = pg.Window("You join the march!", not_join_march_layout)
    while True:
        event = not_join_march_window.read()
        if event == pg.WIN_CLOSED:
            not_join_march_window.close()
            print(event)
            break
        else:
            event == "Final Comments"
            not_join_march_window.close()
            print(event)
            break



###################
# Start of script #
###################
# Step 1: Set theme
pg.theme("BrightColors")


# Step 2: Call the first function
welcome_window_function()

