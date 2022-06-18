import os

##The code below creates a function that allows the screen (terminal) to be cleared. This makes it easier to read and follow the story
def clear_screen():
    print('\n')
    os.system('cls||clear')

##Calling the function game_start to begin the story
clear_screen()
print("Hi! Welcome to this interactive story, I hope you enjoy it.\n")
reader_name = input("What is your name? ")
clear_screen()

#######################################################################################################################
## The code below defines the function called start_story. When called, it will display an introduction to the story.##
#######################################################################################################################
def start_story():
  print("""
   _____ _     _ _        ___   ___  __  ___  
  / ____| |   (_) |      |__ \ / _ \/_ |/ _ \ 
 | |    | |__  _| | ___     ) | | | || | (_) |
 | |    | '_ \| | |/ _ \   / /| | | || |\__, |
 | |____| | | | | |  __/  / /_| |_| || |  / / 
  \_____|_| |_|_|_|\___| |____|\___/ |_| /_/  
  _______________________________________
  | A GAME OF SOCIO ECONOMIC INEQUALITY |
  |_____________________________________|""")
  print("\n")
  print("\nThanks " +reader_name+ ". The aim of this story is to raise awareness of 'Socio Economic Inequalities', by focusing on what happened in Chile, 2019.\n")
  print("You are the main character in this story, and you have to make choices along the way which will determine the ending(s) of the story.\n")

  while True:
    cont = input("Press C to continue: ")
    if cont == 'c':
        clear_screen()
    elif cont == 'C':
        clear_screen()
    else:
        print("Not an apropriate choice. Try again: ")

    print("""
    ░░░░░░░░( •̪●)░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░███████ ]▄▄▄▄▄▄▄▄▃░░░▃░░░░ ▃░░
    ▂▄▅█████████▅▄▃▂░░░░░░░░░░░░░░░░░
    I███████████████████].░░░░░░░░░░░░░░
    ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...░░░░░░░░░░░░░░\n""")
    print("The story begins on October 24th, 2019 in Santiago, Chile.\n")
    print("It’s a Thursday morning, and you should be at school, but school has been closed for the last 2 weeks.\n")
    print("On the streets you see tanks, you hear the sound of gun fire, and smell tear gas in the air.\n")
    print("The Streets now look like something from a CALL OF DUTY video game, and there is a constant feeling of tension and fear.\n")

    print("How did this all start????\n") 
    while True:
        cont = input("Press C to continue: ")
        if cont in ('c', "C"):
            clear_screen()
        else:
            print("Not an apropriate choice. Try again: ")
  
        print("""
                                                                \  /
                        __                                     \/
        _   ---===##===---_________________________--------------  _
        [ ~~~=================###=###=###=###=###=================~~ ]
        /  ||  | |~\  ;;;;     CHILE    TRANSPORT    ;;;;  /~| |  ||  
        /___||__| |  \ ;;;;            [_]            ;;;; /  | |__||
        [\        |__| ;;;;  ;;;; ;;;; ;;; ;;;; ;;;;  ;;;; |__|     |
        (=|    ____[-]_______________________________________[-]_____|
        /  /___/|#(__)=o########o=(__)#||___|#(__)=o#########o=(__)#||
        ________-=\__/=--=\__/=--=\__/=-_____-=\__/=--=\__/=--=\__/=-_\n""")
    
        print("Public transport in Chile is so expensive that a person making minimum wage is forced to spend 20% of their income on transportation alone. \n")
        print("To give you an idea of how bad this is. Imagine you have a job and work for 10 hours a day.\n")
        print("By the time you have used the bus to get to work and back, you have already lost 4 hours of your daily wage!\n")
        print("Chilean students were in a similar situation and decided to take action by gathering at every Metro station and convincing passengers to travel the Metro for free.")
    
        print("""
                            _________________________________________________________________________________________________________
                            |                                                                                                        |
        Student speaking __/  'It’s ok, Ma’am, don’t be afraid, step underneath the turnstile, we’ll take the beating so that you’ll |
                            \    be able to buy bread. Just step underneath the turnstile, and we’ll take care of you.               |
                            |                                    The metro is free today.')                                          |
                            |________________________________________________________________________________________________________|\n""")

        while True:
            cont = input("Press C to continue: ")
            if cont in ('c', "C"):
                clear_screen()
            else:
                print("Not an apropriate choice. Try again: ")
    
            print("""
            888       888 8888888888             d8888 8888888b.  8888888888             d8888 88888888888      888       888        d8888 8888888b.  888 
            888   o   888 888                   d88888 888   Y88b 888                   d88888     888          888   o   888       d88888 888   Y88b 888 
            888  d8b  888 888                  d88P888 888    888 888                  d88P888     888          888  d8b  888      d88P888 888    888 888 
            888 d888b 888 8888888             d88P 888 888   d88P 8888888             d88P 888     888          888 d888b 888     d88P 888 888   d88P 888 
            888d88888b888 888                d88P  888 8888888P"  888                d88P  888     888          888d88888b888    d88P  888 8888888P"  888 
            88888P Y88888 888               d88P   888 888 T88b   888               d88P   888     888          88888P Y88888   d88P   888 888 T88b   Y8P 
            8888P   Y8888 888              d8888888888 888  T88b  888              d8888888888     888          8888P   Y8888  d8888888888 888  T88b   "  
            888P     Y888 8888888888      d88P     888 888   T88b 8888888888      d88P     888     888          888P     Y888 d88P     888 888   T88b 888 \n""")
            print("This seemingly small incident was the spark to ignite the majority of Chileans to release their frustrations at many different socio economic inequalities that had been affecting them for decades.\n")
            print("This included inequalities with access to education, health, pensions, and wages.\n")
            print("The government reacted with an iron fist. The president (Piñera) claimed “We are at War”, and sent a military presence on the streets, imposing a curfew and closing down the city (including your school)\n")
            print("The reason why we are using the words socio economic inequality in this story, is because not all of the population feels the same frustration. \n")
            print("There is a small minority who come from privileged backgrounds, making vast amounts of money, while the majority of the population has struggled.\n")
            print("In this story, we shall refer to the difference between these two groups as UPTOWN (privileged) and DOWNTOWN (struggling).\n")
            print("\n")
            while True:
                cont = input("Press C to continue: ")
                if cont in ('c', "C"):
                    clear_screen()
                    scene_1()
                else:
                    print("Not an apropriate choice. Try again: ")




#######################################################################################################################
## The code below defines the function called scene_1. This is where the reader needs to choose who to call.         ##
#######################################################################################################################
def scene_1():
    clear_screen()                                                                                 
    print("""
   
   ------------------------Scene 1------------------------\n""")
    print("As you are not at school, you decide to hang out with a friend.\n")
    while True:
        choice = input("Who do you want to call? Type U for your UPTOWN friend or type D for your DOWNTOWN friend: ")
        if choice in ("U", "u"):
            clear_screen()
            print("""                                                .
                    .              .   .'.     \   /
                \   /      .'. .' '.'   '  -=  o  =-
                -=  o  =-  .'   '              / | \
                / | \                          |
                    |                            |
                    |                            |
                    |                      .=====|
                    |=====.                |.---.|
                    |.---.|                ||=o=||
                    ||=o=||                ||   ||
                    ||   ||                ||   ||
                    ||   ||                ||___||
                    ||___||                |[:::]|
                    |[:::]|                '-----'
                    '-----'\n""")
            print("THE PHONE RINGS....\n")
            print("Your friend Cata from uptown answers\n")
            print("Cata: Hey " +reader_name+ ", how’s it going?\n")
            print(reader_name + ": Great! No school so chilling and enjoying the freedom\n")
            print("Cata: Oh…i totally agree. I am sitting here chilling by the pool and enjoying the sun.\n")
            print("Cata: I’m glad I live uptown. There are no poor people here, so it means that there are no police, or military presence on the streets.\n")
            print("Cata: But I am still afraid that the poor people might come and take their anger out on us. We have put up extra security cameras.\n") 
            print("Cata: You know that there is no such thing as inequality........only envy...\n")
            while True:
                choice = input("Type 'A' if you agree with Cata. Type 'D' if you disagree and decide to call your Downtown friend: ")
                if choice in ('A', 'a'):
                    scene_2b()
                elif choice in ('D', 'd'):
                    clear_screen()
                    scene_1()
                else:
                    print("Not an apropriate choice. Try again")


        elif choice in ("D", "d"):
            clear_screen()
            print("""
                                                    .
                    .              .   .'.     \   /
                \   /      .'. .' '.'   '  -=  o  =-
                -=  o  =-  .'   '              / | \
                / | \                          |
                    |                            |
                    |                            |
                    |                      .=====|
                    |=====.                |.---.|
                    |.---.|                ||=o=||
                    ||=o=||                ||   ||
                    ||   ||                ||   ||
                    ||   ||                ||___||
                    ||___||                |[:::]|
                    |[:::]|                '-----'
                    '-----'\n""")
            print("THE PHONE RINGS....\n")
            print("Your friend Yared from downtown answers\n")
            print("Yared: Hey "+reader_name+ " , how’s it going?\n")
            print(reader_name +": Great! No school so chilling and enjoying the freedom\n")
            print("Yared: You know this isn’t just an excuse to have a holiday right? This is serious!\n")
            print("Yared: It’s 30’C outside but I have to live with the windows closed because of the tear gas in the air.\n")
            print("Yared: I can’t walk on the streets, and I haven't seen my family for over a week because there is no public transport.\n")
            print("Yared: As a Chilean you should care more about these socio economic inequalities. What do you feel about this situation?\n")
            while True:
                choice = input("Type 'A' if you agree with Yared. Type 'D' if you disagree and decide to call your Uptown friend: ")
                if choice in ('A', 'a'):
                    scene_2a()
                elif choice in ('D', 'd'):
                    clear_screen()
                    scene_1()
                else:
                    print("Not an apropriate choice. Try again")


###############################################################################################################################
## The code below defines the function called scene_2. This is where you have to choose to go with your friends ideas or not ##
###############################################################################################################################
def scene_2a():
    clear_screen()                                                                                 
    print("""
   
   ------------------------Scene 2------------------------\n""")
    print("Yared: I am glad you agree with me.")
    print("Yared: Hey, there is going to be a massive march tomorrow. The biggest yet!\n") 
    print("All the different groups of protesters are coming together at the same time in a show of solidarity. It will be totally peaceful, and there there will be a great atmosphere.\n") 
    print("Yared: Do you want to join me?")
    while True:
        choice = input("Type 'Y' if you want to join Yared. Type 'N' if you prefer not to go: ")
        if choice in ('Y', 'y'):
            clear_screen()
            scene_3a()
        elif choice in ('N', 'n'):
            clear_screen()
            scene_3b()
        else:
            print("Not an apropriate choice. Try again")


def scene_2b():
    clear_screen()                                                                                 
    print("""
   
   ------------------------Scene 2------------------------\n""")
    print("Cata: I am glad you agree with me. Now let’s really enjoy the time off. Come round my place!\n")
    print("You, head to Cata’s house and are greeted by the doorman. When you enter her house, the cook asks you what you’d like to drink and if you want some snacks.\n") 
    print("You start to think, how did these people get uptown when there is no public transport? It must have been really difficult.\n")
    print("Cata is by the pool, you join her and start fooling around with Instagram and Tik Tok.\n")
    print("\n")
    print("Cata: Hey, let’s start Tweeting about what’s happening in Chile. Let’s make sure that people know the truth, and that the poor people are destroying their own neighbourhoods because they are jealous of what they don't have.\n")
    print("What do you think?")
    while True:
        choice = input("Type 'Y' if you think it's a good idea. Type 'N' if you prefer not to: ")
        if choice in ('Y', 'y'):
            clear_screen()
            scene_3c()
        elif choice in ('N', 'n'):
            clear_screen()
            scene_3d()
        else:
            print("Not an apropriate choice. Try again")


###############################################################################################################################
## The code below defines the function called scene_3. These are the 4 alternative endings to the story.                     ##
###############################################################################################################################
def scene_3a():
    clear_screen()  
    print("""                                                                            
                            &@@@                                                
                           %@@@*                                                
                           @@@                               @@&                
   #@@@@                   @@@@                              .@@@@              
   &@@@@*                  @@@%                               (@@%        @@@   
   .@@@&                   @@@                                &@@.        @&    
    @@@@                   @@@%                              .@@@       #@@     
    .@@@@                  @@@@      @@@                    @@@@.      @@@     
     &@@@@      &@@@@      @@@@.    @@@@@                   @@@@@      &@@&     
      @@@@    @@@@@@@@,    @@@@@  #@@@@@@@/        .%%(     @@@@@     &@@@ &@,  
      @@@@#  %@@@@@@@@,    #@@@@@, /@@@@@@       @@@@@@@@@ /@@@@@     @@@@@@@@@*
      @@@@@  @@@@@@@@@@    *@@@@@@@@@@@@*       ,@@@@@@@@@.&@@@@(    @@@@#@@@@@ 
      @@@@@@ @@@@@@@&@@    @@@@@@@@@@(           @@@@@@@@@ @@@@@%   @@@@@@@@@&  
      @@@@@@@@@@@@@&       @@@@@@@@@@@@           @(@@@@@@@@@@@@@ ,@@@@@@@@     
       @@@@@@@@@@@@@@@@@.  @@@@@@@@@@@@@           @@@@@@@@@@@@@@.@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@(    
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@&@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     (@@@@@@@@@@@@@@@@@%@@@@@@@@@@*    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(@ @@@@@@@@@@@@@@@@@@@@@#@@@@@@@@,  \n""")                                                                                 
    print("""
   
   ------------------------Scene 3------------------------\n""")
    print("You go with Yared, and 1.2 million people join the march!\n")
    print("This gets the attention of world media, and a wave of solidarity spreads across the whole country.\n")
    print("The government decide to make amendments to the constitution, taking steps to improve access to education, health care and pensions.\n")
    print("You feel empowered and proud to have taken part.\n")
    print("\n")
    while True:
        cont = input("Press 'C' to continue: ")
        if cont in ('sc','C'):
            clear_screen()
            end_scene()
        else:
            print("Not an apropriate choice. Try again: ")


def scene_3b():
    clear_screen() 
    print("""                                                                            
                            &@@@                                                
                           %@@@*                                                
                           @@@                               @@&                
   #@@@@                   @@@@                              .@@@@              
   &@@@@*                  @@@%                               (@@%        @@@   
   .@@@&                   @@@                                &@@.        @&    
    @@@@                   @@@%                              .@@@       #@@     
    .@@@@                  @@@@      @@@                    @@@@.      @@@     
     &@@@@      &@@@@      @@@@.    @@@@@                   @@@@@      &@@&     
      @@@@    @@@@@@@@,    @@@@@  #@@@@@@@/        .%%(     @@@@@     &@@@ &@,  
      @@@@#  %@@@@@@@@,    #@@@@@, /@@@@@@       @@@@@@@@@ /@@@@@     @@@@@@@@@*
      @@@@@  @@@@@@@@@@    *@@@@@@@@@@@@*       ,@@@@@@@@@.&@@@@(    @@@@#@@@@@ 
      @@@@@@ @@@@@@@&@@    @@@@@@@@@@(           @@@@@@@@@ @@@@@%   @@@@@@@@@&  
      @@@@@@@@@@@@@&       @@@@@@@@@@@@           @(@@@@@@@@@@@@@ ,@@@@@@@@     
       @@@@@@@@@@@@@@@@@.  @@@@@@@@@@@@@           @@@@@@@@@@@@@@.@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@(    
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@&@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     (@@@@@@@@@@@@@@@@@%@@@@@@@@@@*    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(@ @@@@@@@@@@@@@@@@@@@@@#@@@@@@@@,  \n""")                                                                                  
    print("""
   
   ------------------------Scene 3------------------------\n""")
    print("You don't go with Yared, and watch the events from the confort of your TV.\n")
    print("1.2 million people join the march!\n")
    print("This gets the attention of world media, and a wave of solidarity spreads across the whole country.\n")
    print("The government decide to make amendments to the constitution, taking steps to improve access to education, health care and pensions.\n")
    print("You are happy, but deep inside you regret not giving your support.\n")
    print("You promise yourself to be more informed about socio economic inequalities in the future.\n")
    print("\n")
    while True:
        cont = input("Press 'C' to continue: ")
        if cont in ('sc','C'):
            clear_screen()
            end_scene()
        else:
            print("Not an apropriate choice. Try again: ")


def scene_3c():
    clear_screen()
    print("""                                                                            
                            &@@@                                                
                           %@@@*                                                
                           @@@                               @@&                
   #@@@@                   @@@@                              .@@@@              
   &@@@@*                  @@@%                               (@@%        @@@   
   .@@@&                   @@@                                &@@.        @&    
    @@@@                   @@@%                              .@@@       #@@     
    .@@@@                  @@@@      @@@                    @@@@.      @@@     
     &@@@@      &@@@@      @@@@.    @@@@@                   @@@@@      &@@&     
      @@@@    @@@@@@@@,    @@@@@  #@@@@@@@/        .%%(     @@@@@     &@@@ &@,  
      @@@@#  %@@@@@@@@,    #@@@@@, /@@@@@@       @@@@@@@@@ /@@@@@     @@@@@@@@@*
      @@@@@  @@@@@@@@@@    *@@@@@@@@@@@@*       ,@@@@@@@@@.&@@@@(    @@@@#@@@@@ 
      @@@@@@ @@@@@@@&@@    @@@@@@@@@@(           @@@@@@@@@ @@@@@%   @@@@@@@@@&  
      @@@@@@@@@@@@@&       @@@@@@@@@@@@           @(@@@@@@@@@@@@@ ,@@@@@@@@     
       @@@@@@@@@@@@@@@@@.  @@@@@@@@@@@@@           @@@@@@@@@@@@@@.@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@(    
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@&@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     (@@@@@@@@@@@@@@@@@%@@@@@@@@@@*    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(@ @@@@@@@@@@@@@@@@@@@@@#@@@@@@@@,  \n""")                                                                                   
    print("""
   
   ------------------------Scene 3------------------------\n""")
    print("Your Tweets are read by family members and friends who feel ashamed by your ill-informed views.\n")
    print("1.2 million people join the march!\n")
    print("This gets the attention of world media, and a wave of solidarity spreads across the whole country.\n")
    print("The government decide to make amendments to the constitution, taking steps to improve access to education, health care and pensions.\n")
    print("This loss of friends, and rise in solidarity causes you to regret your actions.\n")
    print("In the future, you promise to keep yourself more informed about socio economic inequalities, and top be more careful when using social media to express views./n")
    while True:
        cont = input("Press 'C' to continue: ")
        if cont in ('sc','C'):
            clear_screen()
            end_scene()
        else:
            print("Not an apropriate choice. Try again: ")

def scene_3d():
    clear_screen()
    print("""                                                                            
                            &@@@                                                
                           %@@@*                                                
                           @@@                               @@&                
   #@@@@                   @@@@                              .@@@@              
   &@@@@*                  @@@%                               (@@%        @@@   
   .@@@&                   @@@                                &@@.        @&    
    @@@@                   @@@%                              .@@@       #@@     
    .@@@@                  @@@@      @@@                    @@@@.      @@@     
     &@@@@      &@@@@      @@@@.    @@@@@                   @@@@@      &@@&     
      @@@@    @@@@@@@@,    @@@@@  #@@@@@@@/        .%%(     @@@@@     &@@@ &@,  
      @@@@#  %@@@@@@@@,    #@@@@@, /@@@@@@       @@@@@@@@@ /@@@@@     @@@@@@@@@*
      @@@@@  @@@@@@@@@@    *@@@@@@@@@@@@*       ,@@@@@@@@@.&@@@@(    @@@@#@@@@@ 
      @@@@@@ @@@@@@@&@@    @@@@@@@@@@(           @@@@@@@@@ @@@@@%   @@@@@@@@@&  
      @@@@@@@@@@@@@&       @@@@@@@@@@@@           @(@@@@@@@@@@@@@ ,@@@@@@@@     
       @@@@@@@@@@@@@@@@@.  @@@@@@@@@@@@@           @@@@@@@@@@@@@@.@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@(    
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@&@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     (@@@@@@@@@@@@@@@@@%@@@@@@@@@@*    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&(@ @@@@@@@@@@@@@@@@@@@@@#@@@@@@@@,  \n""")  
    print("""
   
   ------------------------Scene 3------------------------\n""")
    print("1.2 million people join the march!\n")
    print("This gets the attention of world media, and a wave of solidarity spreads across the whole country.\n")
    print("The government decide to make amendments to the constitution, taking steps to improve access to education, health care and pensions.\n")
    print("You now feel that your views were wrong, and you are so happy that you didn't share your views on social media.\n")
    print("The consequences of this could have been very bad and long lasting.\n")
    print("In the future, you promise to keep yourself more informed about socio economic inequalities.\n")
    while True:
        cont = input("Press 'C' to continue: ")
        if cont in ('sc','C'):
            clear_screen()
            end_scene()
        else:
            print("Not an apropriate choice. Try again: ")


###############################################################################
## The end scene with message behind the story                               ##
###############################################################################
def end_scene():
    print("Socio economic inequality relates to disparities that individuals might have in both their economic and social resources that are linked to their social class.\n")
    print("These disparities include earnings, education, income and more.\n")
    print("Just because someone is not directly impacted by socio economic inequalities, doesn't mean they should ignore it.\n")
    print("Stay informed, show empathy, try and help make the world a more equal place for everybody.\n")
    print("\n")
    print("Thanks for reading my story, I recommend you read it again but make different choices to see alternative endings.\n")
    print("See ya!")
    while True:
        cont = input("Press S to start again: ")
        if cont in ('s', 'S'):
            clear_screen()
            start_story()
        else:
            print("Not an apropriate choice. Try again: ")




###############################################################################
## The story actually starts here, with the call of the function start_story ##
###############################################################################
start_story()



