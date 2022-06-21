import PySimpleGUI as pg
from PIL import Image

# Get one PNG file from website and save to file


#############
# functions #
#############

def welcome_window_function():
    welcome_window_layout = [
        [pg.Image('/Users/grampas/Documents/Python_Projects/chile_2019/chile2019/Flag_of_Chile.png')],
        [pg.Text("This is an interactive story where your choices determine the endings.")],
        [pg.Text("Your ultimate goal is to show empathy and support for people impacted by socio economic inequalities.")],
        [pg.Text("In this story, you are in Chile in 2019. 95% of the popeulation are suffering becaue of inequalities in opportunities for education, health, and employment.")],
        [pg.Text("However, you belong to the 5% that are comfortable, so should you really care?")],
        [pg.Text("To show that you care, you can go and visit downtown where all the problems are happening. Or you can forget this and go back to playing on your xbox and end this story now.")],
        [pg.Button('Visit Downtown'), pg.Button('End Story')]
        ]
    # Step 3: Make window
    welcome_window = pg.Window("Welcome", welcome_window_layout, font='_ 15')
    while True:
        event, values = welcome_window.read()
        if event in (pg.WIN_CLOSED, 'End Story'): 
            welcome_window.close()
            break
        if event == 'Visit Downtown':
            welcome_window.close()
            visit_downtown_window()
            break
    welcome_window.close()

def visit_downtown_window():
    visit_downtown_layout = [
        [pg.Image('/Users/grampas/Documents/Python_Projects/chile_2019/chile2019/Marching_People.png')],
        [pg.Text("The suffering has caused people to protest and the governemnt has reacted by sending the military on the streets.")],
        [pg.Text("You go to a freinds house and have to close the windows becasue of the tear gas that is always in the air, and you cant go to chat in cafe because everything has been closed down.")],
        [pg.Text("Your friend explains that there will be a march the next day to show solidarity against the inequalities and suffering. She invites you to join. ")],
        [pg.Text("You are not sure if its a good idea as you think it has nothing to do with you. You are lucky, you are in the wealthiest 5% of the population. ")],
        [pg.Text("Do you choose to join or not join the march?")],
        [pg.Button("Join March"), pg.Button("Don't Join March")]
    ]
    visit_downtown_window = pg.Window("You go Downtown...", visit_downtown_layout, font='_ 15')
    while True:
        event, values = visit_downtown_window.read()
        if event == pg.WIN_CLOSED:
            visit_downtown_window.close()
            break
        if event == "Join March":
            visit_downtown_window.close()
            join_march_window()
            break
        if event == "Don't Join March":
            visit_downtown_window.close()
            not_join_march_window()
            break
    visit_downtown_window.close()



def join_march_window():
    join_march_layout = [
        [pg.Image('/Users/grampas/Documents/Python_Projects/chile_2019/chile2019/Solidarity.png')],
        [pg.Text("1.2 million people attend the march. Its peaceful and empowering.")],
        [pg.Text("You feel an enormous sense of solidarity with the rest of the population.")],
        [pg.Text("The world takes notice, the government takes notice, the result is a change in the constitution and the beginning of more euqal opportunities in Chile for all.")],
        [pg.Text("You made a good choice!")],
        [pg.Button("Final Comments")]
    ]
    join_march_window = pg.Window("You join the march!", join_march_layout, font='_ 15')
    while True:
        event, values = join_march_window.read()
        if event == pg.WIN_CLOSED:    
            break
        if event == 'Final Comments':
            join_march_window.close()
            final_comments()
            break
    join_march_window.close()


def not_join_march_window():
    not_join_march_layout = [
        [pg.Image('/Users/grampas/Documents/Python_Projects/chile_2019/chile2019/Regret.png')],
        [pg.Text("You go back to your comfortable home and wonder if you made th eright choice.")],
        [pg.Text("You find out on the news later that 1.2 million people attend the march. ")],
        [pg.Text("The images and comments show that it was a life changing moment, where the country cam together in a show of solidarity.")],
        [pg.Text("The world took notice, the government took notice, the result was a change in the constitution and the beginning of more euqal opportunities in Chile for all. ")],
        [pg.Text("You regret your decision, and know that in the future you should show more support and empathy to those with less opportunities than you.")],
        [pg.Button("Final Comments")]
    ]
    not_join_march_window = pg.Window("You don't join the march...", not_join_march_layout, font='_ 15')
    while True:
        event = not_join_march_window.read()
        if event == pg.WIN_CLOSED:
            not_join_march_window.close()
            break
        else:
            event == "Final Comments"
            not_join_march_window.close()
            final_comments()
            break
    not_join_march_window.close()


def final_comments():
    final_comments_layout = [
        [pg.Text("Socio economic inequality relates to disparities that individuals might have in both their economic and social resources that are linked to their social class.")],
        [pg.Text("These disparities include earnings, education, income and more.")],
        [pg.Text("Just because someone is not directly impacted by socio economic inequalities, doesn't mean they should ignore it.")],
        [pg.Text("Stay informed, show empathy, try and help make the world a more equal place for everybody. ")],
        [pg.Text("Thanks for reading my story! See ya!")],
        [pg.Button("Quit")]
    ]
    final_comments_window = pg.Window("What was this all about?", final_comments_layout, font='_ 15')
    while True:
        event, values = final_comments_window.read()
        if event in ('Quit', pg.WIN_CLOSED):
            break
    final_comments_window.close()



###################
# Start of script #
###################
# Step 1: Set theme
pg.theme("BrightColors")


# Step 2: Call the first function
welcome_window_function()

