import time
import random
import string
import os
import hashlib

User = ''

#Grids for both the inital state and the finished which will be shown to the Players.
initial_grid =  [['#', '#', '#', '8', '9', '5', '10', '11', '5'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '7', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '1', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '2', '#', '6', '#', '#', '#'],
                ['#', '#', '#', '6', '#', '2', '#', '#', '#'],
                ['H', '1', '2', '3', 'R', '5', '3', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]


finished_grid = [['#', '#', '#', 'P', 'L', 'E', 'A', 'S', 'E'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', 'T', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', 'U', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', 'N', '#', 'O', '#', '#', '#'],
                 ['#', '#', '#', 'O', '#', 'N', '#', '#', '#'],
                 ['H', 'U', 'N', 'D', 'R', 'E', 'D', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]



#This function is used to print the grid out in a readable and concise format
def print_grid():

    for x in range(len(initial_grid)):
        place_holder = "  "
        for y in range(len(initial_grid[x])):
            place_holder += initial_grid[x][y]
            place_holder += "  "
        print(place_holder)


#Function prints the finished grid in a readable and concise format
def print_finished_grid():

    for x in range(len(finished_grid)):
        place_holder = "  "
        for y in range(len(finished_grid[x])):
            place_holder += finished_grid[x][y]
            place_holder += "  "
        print(place_holder)



#Player keys which will be shown to the Players
player_key = [[0,'H'], [1,'_'], [2,'_'], [3,'_'], [4,'R'], [5,'_'], [6,'_'],
    [7,'_'], [8,'_'], [9,'_'], [10,'_'], [11,'_']]


final_key = [[0,'H'], [1,'U'], [2,'N'], [3,'D'] ,[4,'R'] ,[5,'E'], [6,'O'],
    [7,'T'], [8,'P'], [9,'L'], [10,'A'], [11,'S']]





#This function is used to retrieve the firstname and surname of the Admin
def name_admin():
    global admin_firstname
    global surname
    admin_firstname = input('What is your firstname? ')
    surname = input('What is your surname? ')
    return 'Welcome, ' + admin_firstname + ' ' + surname


#This function is used to create a generated password return it and store the encrypted password into the Admin Class.
def password_admin():
    global admin_passwords
    global admin_encrypted_password
     
    length = int(input('How many characters do you want within your password? '))

    lower = string.ascii_uppercase
    upper = string.ascii_uppercase
    punctuation = string.punctuation
    num = string.digits

    all = lower + upper + punctuation + num

    
    admin_passwords = "".join(random.sample(all,length))
    admin_encrypted_password = hashlib.sha256(admin_passwords.encode('utf-8')).hexdigest()
    return('Your password is:' , admin_passwords)
     
#This function is used generate a random username for the Admin and storing the encrypted username in the Admin Class.
def username_admin():
     global admin_usernames
     global admin_encrypted_username
     
     length = int(input('How many characters do you want within your username? '))

     first = admin_firstname
     last = surname

     both = first + last

     admin_usernames = "".join(random.sample(both,length))
     admin_encrypted_username = hashlib.sha256(admin_usernames.encode('utf-8')).hexdigest()
     return('Your username is:', admin_usernames)


#This function creates entire account for the Admin and stores in variables in which later would be stored in the Admin Class.
def create_user_admin():
            global firstname_admin
            global encrypted_username_admin
            global encrypted_password_admin
            print(name_admin())
            print('----------------------------------------')
            print(username_admin())
            print('----------------------------------------')
            print(password_admin())
            

            firstname_admin = admin_firstname
            encrypted_username_admin = admin_encrypted_username
            encrypted_password_admin = admin_encrypted_password
 

            return



"""-------------------------------------------------------------------------------------------------------------------------------"""

#This function is used to retrieve the firstname and surname of the first Player.
def Player1_name():
    global firstname
    global surname
    firstname = input('What is your firstname? ')
    surname = input('What is your surname? ')
    return 'Welcome, ' + firstname + ' ' + surname


#This function is used generate a random password for the Player1 and storing the encrypted password in the Player1 Class.
def Player1_password():
    global player1_passwords
    global encrypted_password
     
    length = int(input('How many characters do you want within your password? '))

    lower = string.ascii_uppercase
    upper = string.ascii_uppercase
    punctuation = string.punctuation
    num = string.digits

    all = lower + upper + punctuation + num

    
    player1_passwords = "".join(random.sample(all,length))
    encrypted_password = hashlib.sha256(player1_passwords.encode('utf-8')).hexdigest()
    return('Your password is:' , player1_passwords)
     

#This function is used generate a random username for the Player1 and storing the encrypted username in the Player1 Class.
def Player1_username():
     global player1_usernames
     global encrypted_username
     
     length = int(input('How many characters do you want within your username? '))

     first = firstname
     last = surname

     both = first + last

     player1_usernames = "".join(random.sample(both,length))
     encrypted_username = hashlib.sha256(player1_usernames.encode('utf-8')).hexdigest()
     return('Your username is:', player1_usernames)


#This function creates entire account for the Player1 and stores in variables in which later would be stored in the Player1 Class.
def create_user_Player1():
            global Player1_firstname
            global Player1_encrypted_username
            global Player1_encryped_username
            global Player1_health
            print('----------------------------------------')
            print(Player1_name())
            print('----------------------------------------')
            print(Player1_username())
            print('----------------------------------------')
            print(Player1_password())
            print('----------------------------------------')
            

            Player1_firstname = firstname
            Player1_encrypted_username = encrypted_username
            Player1_encryped_username = encrypted_password
            Player1_health = 5

            return

"""-------------------------------------------------------------------------------------------------------------------------------"""

#This function is used to retrieve the firstname and surname of the second Player.
def Player2_name():
    global firstname2
    global surname2
    firstname2 = input('What is your firstname? ')
    surname2 = input('What is your surname? ')
    return 'Welcome, ' + firstname2 + ' ' + surname2




#This function is used generate a random password for the Player2 and storing the encrypted password in the Player2 Class.
def Player2_password():
    global player2_passwords2
    global encrypted_password2
     
    length = int(input('How many characters do you want within your password? '))

    lower = string.ascii_uppercase
    upper = string.ascii_uppercase
    punctuation = string.punctuation
    num = string.digits

    all = lower + upper + punctuation + num

    
    player2_passwords2 = "".join(random.sample(all,length))
    encrypted_password2 = hashlib.sha256(player2_passwords2.encode('utf-8')).hexdigest()
    return('Your password is:' , player2_passwords2)
     
#This function is used generate a random username for the Player2 and storing the encrypted username in the Player2 Class.
def Player2_username():
     global player2_usernames2
     global encrypted_username2
     
     length = int(input('How many characters do you want within your username? '))

     first = firstname
     last = surname

     both = first + last

     player2_usernames2 = "".join(random.sample(both,length))
     encrypted_username2 = hashlib.sha256(player2_usernames2.encode('utf-8')).hexdigest()
     return('Your username is:', player2_usernames2)
     



#This function creates entire account for the Player2 and stores in variables in which later would be stored in the Admin Class.
def create_user_Player2():
            global Player2_firstname
            global Player2_encrypted_username
            global Player2_encrypted_password
            global Player2_health
            print(Player2_name())
            print('----------------------------------------')
            print(Player2_username())
            print('----------------------------------------')
            print(Player2_password())
            

            Player2_firstname = firstname2
            Player2_encrypted_username = encrypted_username2
            Player2_encrypted_password = encrypted_password2
            Player2_health = 5

            return
"""-------------------------------------------------------------------------------------------------------------------------------"""

#Class for Player1 which has the attributes name, encrypted username, encrypted password and health. It stores them within the class.
class Player_1():
    def __init__(self, name, encrypted_username, encrypted_password, health):
        self.name = name
        self.encrypted_username = encrypted_username
        self.encrypted_password = encrypted_password
        self.health = health

        #Prints the details of the Class attributes
    def info(self):
        print("Name: " +  self.name, "USERNAME: " + self.encrypted_username, "PASSWORD: "  + self.encrypted_password, "HEALTH: "  + str(self.health))

#Class for Player2 which has the attributes name, encrypted username, encrypted password and health. It stores them within the class.
class Player_2():
    def __init__(self, name, encrypted_username, encrypted_password, health):
        self.name = name
        self.encrypted_username = encrypted_username
        self.encrypted_password = encrypted_password
        self.health = health

        #Prints the details of the Class attributes
    def info(self):
        print("Name: " +  self.name, "USERNAME: " + self.encrypted_username, "PASSWORD: "  + self.encrypted_password, "HEALTH: "  + str(self.health))

#Class for Admin which has the attributes name, encrypted username, encrypted password and health. It stores them within the class.
class Admin():
    def __init__(self, name, encrypted_username, encrypted_password):
        self.name = name
        self.encrypted_username = encrypted_username
        self.encrypted_password = encrypted_password

        #Prints the details of the Class attributes
    def info(self):
        print("Name: " +  self.name, "USERNAME: " + self.encrypted_username, "PASSWORD: "  + self.encrypted_password)


"""-------------------------------------------------------------------------------------------------------------------------------"""


    
#This is where the User decides what account he wants to create; either an admin or a Player.
def Account_creations():
    global Player1
    global Player2
    register = input('Hello, what are you registaring for,\n1 = Players\n2 = Admin\n3 = Quit\n')
    if register == '2':
        print('WELCOME! ADMIN')
        ready = input('Sign up = 1\nQuit = 2\n')
        if ready == '1':

            #The user account will be created here, the variables within the create_user_admin will be the attributes of the class held within Admin

            print(create_user_admin())
            Admin1 = Admin(firstname_admin, encrypted_username_admin, encrypted_password_admin)
            Admin1.info()
            time.sleep(5)
            os.system('cls')

        elif ready == '2':
            exit()


    if register == '1':
        print('WELCOME! PLAYER1')
        ready = input('Sign up = 1\nQuit = 2\n')
        if ready == '1':

            #The user account will be created here, the variables within the create_user_Player1 will be the attributes of the class held within Player1

            print(create_user_Player1())
            Player1 = Player_1(Player1_firstname, Player1_encrypted_username, Player1_encryped_username, Player1_health)
            Player1.info()
            time.sleep(5)
            os.system('cls')
            
                
                

        elif ready == '2':
            exit()


        print('WELCOME! PLAYER2')
        ready = input('Sign up = 1\nQuit = 2\n')
        if ready == '1':
            print(create_user_Player2())

            #The user account will be created here, the variables within the create_user_Player2 will be the attributes of the class held within Player2

            Player2 = Player_2(Player2_firstname, Player2_encrypted_username, Player2_encrypted_username, Player2_health)
            Player2.info()
            time.sleep(5)
            os.system('cls')
            
                
                
        elif ready == '2':
            exit()
            
            
    if register == '3':
        exit()
    
    
    return

Account_creations()



#This funciton allows the user to select what they want to log into, the function checks if the input is the same as when they created the account, else it returns error up to 3 times before closing.
def initial_choice_menu():
    print('Choose one of the following and sign up.')
    Q = input('1 = Player\n2 = Admin\n3 = Quit\n')
    x = True
    global Player1_login
    global Player2_login
    global User
    global admin
    global Game
    global Gameover
    wrong = 3
    wrong2 = 3
    wrong3 = 3
    Player1_login = False
    Player2_login = False
    while x:
        if wrong == 0:
            print('Failed to log in..')
            x = False
            exit()
        
        if Q == '1' and Player1_login == False:
            User = 'Player'
            print('Welcome, Player1')
            print('-------------------------------------------\nLog in below:')
            log_user = input('Username: ')

            #checks to see if its the same as the username they created, does the same with the password too.

            if log_user == player1_usernames:
                log_pass = input('Password: ')
                if log_pass == player1_passwords:
                    print('Sucessful..')
                    time.sleep(3)
                    os.system('cls')
                    Player1_login = True
                    #if successful, player2 now has to login.




                    #if its wrong then they lose 1 attempt from their initial 3.
                else:
                    wrong = wrong - 1
                    print('Invalid, try again ' + str(wrong) + ' attempts left.')
                    time.sleep(3)
                    os.system('cls')
            
            if log_user != player1_usernames:
                wrong = wrong - 1
                print('Invalid, try again ' + str(wrong) + ' attempts left.')
                time.sleep(3)
                os.system('cls')

        
        if wrong2 == 0:
            print('Failed to log in..')
            exit()
        if Q == '1' and Player1_login == True:
            User = 'Player'
            print('Welcome, Player2')
            print('-------------------------------------------\nLog in below:')
            log_user2 = input('Username: ')
            if log_user2 == player2_usernames2:

                #checks to see if its the same as the username they created, does the same with the password too.

                log_pass2 = input('Password: ')
                if log_pass2 == player2_passwords2:
                    print('Sucessful..')
                    time.sleep(3)
                    os.system('cls')
                    Player2_login = True
                    x = False
                    Game = True
                    #Once both logins are successful the game starts hence the Game = True, where its taken into the while loop.
                
                else:
                    wrong2 = wrong2 - 1
                    print('Invalid, try again ' + str(wrong2) + ' attempts left.')
                    time.sleep(3)
                    os.system('cls')

            #if its wrong then they lose 1 attempt from their initial 3.
            if log_user2 != player2_usernames2:
                wrong2 = wrong2 - 1
                print('Invalid, try again ' + str(wrong2) + ' attempts left.')
                time.sleep(3)
                os.system('cls')





        if wrong3 == 0:
            print('Failed to log in..')
            exit()
        if Q == '2':
            User = 'Admin'
            print('Welcome, Admin')
            print('-------------------------------------------\nLog in below:')
            log_admin_user = input('Username: ')

            #checks to see if its the same as the username they created, does the same with the password too.

            if log_admin_user == admin_usernames:
                log_admin_pass = input('Password: ')
                if log_admin_pass == admin_passwords:
                    print('Sucessful..')
                    time.sleep(3)
                    os.system('cls')
                    x = False
                    admin = True
                    Game = True
                    Gameover = False
                    #Once successful game starts and is taken to the loop called Game below.

                else:
                    wrong3 = wrong3 - 1
                    print('Invalid, try again ' + str(wrong3) + ' attempts left.')
                    time.sleep(3)
                    os.system('cls')
            
            if log_admin_user != admin_usernames:
                wrong3 = wrong3 - 1
                print('Invalid, try again ' + str(wrong3) + ' attempts left.')
                time.sleep(3)
                os.system('cls')



        elif Q == '3':
             print('Quitting..')
             exit()
             







    return

initial_choice_menu()

play1 = ''
play2 = ''




#Variables for switching from Player 1 and Player2, and deciding if their input is right or wrong respectfully.
switch = False
right_or_wrong = ''




#variables for game stats
Player1_correct_guesses = 0
Player2_correct_guesses = 0
Player1_incorrect_guesses = 0
Player2_incorrect_guesses = 0


while Game:
    global accept1
    global accept2
    if User == 'Player':
        if Player1_login == True and Player2_login == True:
            play1 = input('Would you like to play Player1\n1 = yes\n2 = no\n')
            play2 = input('Would you like to play Player2\n1 = yes\n2 = no\n')

            #Asks the users to confirm if they want to play if so continue the loop.

        accept1 = play1
        accept2 = play2

        #if not the loop ends.

        if accept1 == '2' or accept2 == '2':
            Gameover = True
            admin = False
            break



        #If it follows the instructions needed below the game gets started with Player 1 starting first.
        if Player1.health >= 2 and accept1 == '1' and accept2 =='1' and switch == False:
            print(player1_usernames + ' Your turn, get ready..')          
            time.sleep(3)
            os.system('cls')

            print_grid()
            print(player_key)




            #Asks to enter key, if wrong deducts 2 health if correct adds 2.
            key = int(input('Which cell would you like to complete? '))
            if key > 11 or key < 0:
                print('Invalid input, try again..')
                key = int(input('Which cell would you like to complete? '))
            print(player_key[key])
            

            guess = input('What is your guess? ').upper()
            for x in range(len(initial_grid)):
                for i in range(len(initial_grid[x])):
                    if str(key) == initial_grid[x][i]:
                        initial_grid[x][i] = guess
                        player_key[key].pop()
                        player_key[key].append(guess)
                        

                        #Shows the changes after choosing the keys
            print('----------------------"CHANGES"--------------------------------------')
            print_grid()
            print(player_key)
            print('---------------------------------------------------------------------')
            time.sleep(3)

            if player_key[key] == final_key[key]:
                right_or_wrong = '1'


                if right_or_wrong == '1':
                    Player1.health = Player1.health + 2
                    Player1_correct_guesses += 1
                    

            if player_key[key] != final_key[key]:
                right_or_wrong = '2'
                
                if right_or_wrong == '2':
                    for x in range(len(initial_grid)):
                        for i in range(len(initial_grid[x])):
                            if guess == initial_grid[x][i]:
                                initial_grid[x][i] = str(key)
                    player_key[key].pop()
                    player_key[key].append('_')
                    Player1.health = Player1.health - 2
                    Player1_incorrect_guesses += 1
                
                #This is where the calculations of the Player's hp takes place; if correct +2, if wrong -2.
                            
            if Player1.health < 2:
                print('No more lives.')
                Gameover = True
                admin = False
                break

                            

            print(player1_usernames +  ' your current health is: ' + str(Player1.health))
            print_grid()
            print(player_key)
            switch = True
            time.sleep(3)
            #Switches to Player 2 using the variable switch = True.



        #If it follows the instructions needed below the game gets started with Player 2 starting since switch now  = True.
        if Player2.health >= 2 and accept1 == '1' and accept2 =='1' and switch == True:
            print(player2_usernames2 + ' Your turn, get ready..')              
            time.sleep(3)
            os.system('cls')

            print_grid()
            print(player_key)




            #Asks to enter key, if wrong deducts 2 health if correct adds 2.
            key = int(input('Which cell would you like to complete? '))
            if key > 11 or key < 0:
                print('Invalid input, try again..')
                key = int(input('Which cell would you like to complete? '))
            print(player_key[key])
            

            guess = input('What should it have? ').upper()
            for x in range(len(initial_grid)):
                for i in range(len(initial_grid[x])):
                    if str(key) == initial_grid[x][i]:
                        initial_grid[x][i] = guess
                        player_key[key].pop()
                        player_key[key].append(guess)
                        

                        #Shows the changes after choosing the keys
            print('----------------------"CHANGES"--------------------------------------')
            print_grid()
            print(player_key)
            print('---------------------------------------------------------------------')
            time.sleep(3)

            if player_key[key] == final_key[key]:
                right_or_wrong = '1'


                if right_or_wrong == '1':
                    Player2.health = Player2.health + 2
                    Player2_correct_guesses += 1
     
                    

            if player_key[key] != final_key[key]:
                right_or_wrong = '2'
                
                if right_or_wrong == '2':
                    for x in range(len(initial_grid)):
                        for i in range(len(initial_grid[x])):
                            if guess == initial_grid[x][i]:
                                initial_grid[x][i] = str(key)
                    player_key[key].pop()
                    player_key[key].append('_')
                    Player2.health = Player2.health - 2
                    Player2_incorrect_guesses += 1
                

                 #This is where the calculations of the Player's hp takes place; if correct +2, if wrong -2.
                            
            if Player1.health < 2:
                print('No more lives.')
                Gameover = True
                admin = False
                break

                            

            print(player2_usernames2  +  ' your current health is: ' + str(Player2.health))
            print_grid()
            print(player_key)
            switch = False
            time.sleep(3)
            #Switches to Player 2 using the variable switch = True.


            if initial_grid == finished_grid:
                Gameover = True
                admin = False
                break
            #If they codeword grid is finished the game ends and the stats are shown.






            #If the user signs up as admin then they're automatically taken here where they can make adjustments
    if User == 'Admin':
        print('HELLO')
        time.sleep(3)
        os.system('cls')

        print('-----------------"FINAL"-----------------------')
        print_finished_grid()
        time.sleep(3)
        print('-------------------"INITIAL"-------------------')
        print_grid()
        time.sleep(3)


        #Displays the current and player keys and grids

        print('-----------------"FINAL"-----------------------')
        print(final_key)
        time.sleep(3)
        print('-------------------"INITIAL"-------------------')
        print(player_key)
        Changes = input('Would you like to change anything?\n1 = yes\n2 = no\n')
        if Changes == '1':
            add_or_remove = input('Add a word and Remove a word = 1\Change puzzle = 2\n')
            if add_or_remove == '1':
                new_grid = [['#', '#', '#', '8', '9', '5', '10', '11', '5'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                            ['#', '#', '#', '7', '#', '#', '#', '#', '#'],
                            ['#', '#', '#', '1', '#', '#', '#', '#', '#'],
                            ['#', '#', '#', '2', '#', '#', '4', '#', '#'],
                            ['#', '#', '#', '6', '#', '#', '5', '#', '#'],
                            ['H', '1', '2', '3', 'R', '5', '3', '#', '#'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]
                
                finished_new_grid = [['#', '#', '#', 'P', 'L', 'E', 'A', 'S', 'E'],
                                    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                    ['#', '#', '#', 'T', '#', '#', '#', '#', '#'],
                                    ['#', '#', '#', 'U', '#', '#', '#', '#', '#'],
                                    ['#', '#', '#', 'N', '#', '#', 'R', '#', '#'],
                                    ['#', '#', '#', 'O', '#', '#', 'E', '#', '#'],
                                    ['H', 'U', 'N', 'D', 'R', 'E', 'D', '#', '#'],
                                    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]

                initial_grid = new_grid
                finished_grid = finished_new_grid
                print('Change is successful')
                print_grid()
                time.sleep(10)

                #If the user adds a word then the initial player key and grid are switched with the above.

            if add_or_remove == '2':        
                for x in range(len(initial_grid)):
                        for i in range(len(initial_grid[x])):
                            initial_grid[x][i] = '#'


                for m in player_key:
                    for l in  m:
                        chosen = 0
                        chosen += 1
                        if chosen % 2 == 0:
                            print(l)
                        
                        
                for x in range(len(finished_grid)):
                        for i in range(len(finished_grid[x])):
                            finished_grid[x][i] = '#'

                changed_grid_final = [['#', '#', '#', '#', 'P', 'L', 'A', 'C', 'E'],
                                      ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                      ['#', '#', '#', 'T', '#', '#', '#', '#', '#'],
                                      ['#', '#', '#', 'F', '#', '#', '#', '#', '#'],
                                      ['#', '#', '#', 'A', '#', '#', 'B', '#', '#'],
                                      ['#', '#', '#', 'R', '#', '#', 'E', '#', '#'],
                                      ['H', 'A', 'N', 'D', 'F', 'E', 'D', '#', '#'],
                                      ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                      ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                      ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]              

                changed_grid_initial = [['#', '#', '#', '#', '9', '10', '1', '11', '5'],
                                        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                        ['#', '#', '#', '7', '#', '#', '#', '#', '#'],
                                        ['#', '#', '#', '4', '#', '#', '#', '#', '#'],
                                        ['#', '#', '#', 'A', '#', '#', '8', '#', '#'],
                                        ['#', '#', '#', '6', '#', '#', 'E', '#', '#'],
                                        ['0', 'A', '2', '3', '4', 'E', '3', '#', '#'],
                                        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],]     

                changed_initial_key = [[0,'_'], [1,'A'], [2,'_'], [3,'_'] ,[4,'_'] ,[5,'E'], [6,'_'],[7,'_'], [8,'_'], [9,'_'], [10,''], [11,'']]




                changed_final_key = [[0,'H'], [1,'A'], [2,'N'], [3,'D'] ,[4,'F'] ,[5,'E'], [6,'R'],[7,'T'], [8,'B'], [9,'P'], [10,'L'], [11,'C']]



                for x in range(len(changed_grid_initial)):
                        for i in range(len(changed_grid_initial[x])):
                            if changed_grid_initial[x][i] != '#':
                                initial_grid[x][i] = changed_grid_initial[x][i]

                for x in range(len(changed_grid_final)):
                        for i in range(len(changed_grid_final[x])):
                            if changed_grid_final[x][i] != '#':
                                finished_grid[x][i] = changed_grid_final[x][i]

                player_key = changed_initial_key
                final_key = changed_final_key

                #If the user requests to change puzzle, then the grid goes through every element within a list making them all #, then going over it again to find positions for new words.
                #Keys are just switched.
        
        if Changes == '2':
            os.system('cls')
            Account_creations()
            initial_choice_menu()
            #After that is done the user is requested to go back and decide what he wants to sign up as, where he could play with the new puzzles after signing up as a Player.
        

    
    
    
        
#Stats of the game, displaying everything about the user, guesses, wrong guesses, etc..
if Gameover == True:
    print('------------------------"PLAYER 1 INFO"-------------------------------')
    print(Player1.info())
    print('Coreect guesses: ' + str(Player1_correct_guesses))
    print('Wrong guesses: ' + str(Player1_incorrect_guesses))
    print('---------------------------------------------------------------------')


    print('------------------------"PLAYER 2 INFO"-------------------------------')
    print(Player2.info())
    print('Coreect guesses: ' + str(Player2_correct_guesses))
    print('Wrong guesses: ' + str(Player2_incorrect_guesses))
    print('---------------------------------------------------------------------')


                






        
                


    