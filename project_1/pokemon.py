from IPython.display import Image, display #to pull up pokecard image
import time #to wait before running the next line
import random #use random integers to simulate 'chance'
import sys #to end the game, you have to restart kernal if you want to play again
from threading import Timer #want to make an input timer for easter egg game

def Blast():
    time_up = 3
    t = Timer(time_up, print, ['Too slow! They got away!'])
    t.start()
    stoprocket = "Quick! Type BLAST to get stop Team Rocket!"
    response = input(stoprocket)
    t.cancel()
    if response == "BLAST": print("Looks like Team Rocket's blasting off again!")
    else:print('They got away!')

class Character():
    def __init__(self,person='',personality ='',image=''):
        self.person = person
        self.personality = personality
        self.image = image
        display(Image(filename=self.image))
        print(self.person,self.personality+'!')
    
    def __repr__(self):
        return"%s" % (self.name)

class Pokemon(): #initialized the pokemon class
    
    def __init__(self, name = '',element = '', HP = 0, Move_1 = '', Move_2 = '',image = ''):
        self.name = name
        self.element = element
        self.HP = HP
        self.HP_bar = ['■' for i in range(1,self.HP,5)] # ■■ = 10 HP
        self.Move_1 = Move_1 # all move_1 does a base of 10 damage
        self.Move_2 = Move_2 # all move_2 does a base of 30 damage
        self.image = image #pokecard image
        
        print(self.name +'!!!')
        display(Image(filename=self.image))
    
    def __repr__(self):
        return"%s" % (self.name)
    
    def card_stats(self): # prints below the card
        name = self.name
        print(self.name,'is a',self.element+'-type pokemon.')
        print('\nCurrent HP:',self.HP,'\n',''.join(self.HP_bar),"\n\n\n______________________________________________\n")



class Actions(Pokemon):
    def __init__(self,user,enemy):
        #def __init__(self,name,element = '', HP = 0, Move_1 = '', Move_2 = '',image='',user,enemy):
        #super().__init__(name,element,HP,Move_1,Move_2)
        #self.action = Actions(user,enemy)
        self.user = user
        self.enemy = enemy
        self.potions = 3 # potions in your bag... +10 HP per use
        self.elixirs = 3 #elixirs add 5 PP to each move, 10 total
        self.pokeballs = 3 # pokeballs in your bag...  chance to capture opponent
        self.user.M1_PP = 15 #power points for first move
        self.user.M2_PP = 5 #will subtract 1 every time user attempts to use move
        time.sleep(1)
        print('''
            ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
            ◈                          ◈
            ◈   LET THE BATTLE BEGIN   ◈
            ◈                          ◈
            ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
            ''')
    
    def damage_x(self):
        
        if user.element == 'Electric': #Pikachu is strong against water and weak against grass
            if enemy.element == 'Water': self.damage_multiplier = 2
            if enemy.element == 'Grass': self.damage_multiplier = 0.5
            else:self.damage_multiplier = 1
        
        elif user.element == 'Fire': #Charmander is strong against Bulbasaur and weak against Squirtle
            if enemy.element == 'Grass':self.damage_multiplier = 2
            if enemy.element == 'Water':self.damage_multiplier = 0.5
            else:self.damage_multiplier = 1
        
        elif user.element == 'Grass': #this makes sense now right
            if enemy.element == 'Water':self.damage_multiplier = 2
            if enemy.element == 'Fire':self.damage_multiplier = 0.5
            else:self.damage_multiplier = 1
        
        elif user.element == 'Water': #one of the errors I ran into was multiplying by 0.5 made it a floater I could not iterate while printing out the HP_bar
            if enemy.element == 'Fire':self.damage_multiplier = 2
            if enemy.element == 'Grass':self.damage_multiplier = 0.5
            else:self.damage_multiplier = 1

        if self.damage_multiplier == 2: self.adverb = 'very'
        if self.damage_multiplier == 0.5: self.adverb = 'not'
        if self.damage_multiplier == 1: self.adverb = 'kinda'
                return(self.damage_multiplier,self.adverb)

def damage_y(self):
    self.damage_multiplier2 = 1
        if enemy.element == 'Electric': #Pikachu is strong against water and weak against grass
            if user.element == 'Water': self.damage_multiplier2 = 2
            if user.element == 'Grass': self.damage_multiplier2 = 0.5
            else:self.damage_multiplier2 = 1
    
        if enemy.element == 'Fire': #Charmander is strong against Bulbasaur and weak against Squirtle
            if user.element == 'Grass':self.damage_multiplier2 = 2
            if user.element == 'Water':self.damage_multiplier2 = 0.5
            else:self.damage_multiplier2 = 1
        
        elif enemy.element == 'Grass': #this makes sense now right
            if user.element == 'Water':self.damage_multiplier2 = 2
            if user.element == 'Fire':self.damage_multiplier2 = 0.5
            else:self.damage_multiplier2 = 1
        
        elif enemy.element == 'Water': #one of the errors I ran into was multiplying by 0.5 made it a floater I could not iterate while printing out the HP_bar
            if user.element == 'Fire':self.damage_multiplier2 = 2
            if user.element == 'Grass':self.damage_multiplier2 = 0.5
            else:self.damage_multiplier2 = 1

        if self.damage_multiplier2 == 2: self.adverb2 = 'very'
        elif self.damage_multiplier2 == 0.5: self.adverb2 = 'not'
        elif self.damage_multiplier2 == 1: self.adverb2 = 'kinda'

return(self.damage_multiplier2,self.adverb2)

    def enemy_move(self):
        if enemy.HP == 0: self.end_message()#end the game if enemy is dead
        else:self.rand_fight_pick = random.randint(1,2)
        self.damage_y()
        print('multiplier check enemy',self.damage_multiplier2)
        
        if enemy.HP <= 20 and self.damage_multiplier>=1: #LOW HP gives opportunity for CPU to heal
            self.rand_heal = random.randint(1,5)
            if self.rand_heal > 1: enemy.HP += 5
            if self.rand_heal == 1: enemy.HP += 20
            print('\n\n>>>The wild',enemy.name,'used a potion!\n\n______________________________________________\n')
        
        if self.rand_fight_pick == 1:
            display(Image(filename='hit.jpg'))
            self.damage = int(10*self.damage_multiplier2)
            print("\n\n\n______________________________________________\n>>>",enemy.name,'used',enemy.Move_1,'and it was',self.adverb2,'effective')
        
        if self.rand_fight_pick == 2:
            display(Image(filename='hit2.jpg'))
            self.damage = int(30*self.damage_multiplier2)
            print("\n\n\n______________________________________________\n>>>",enemy.name,'used',enemy.Move_2,'and it was',self.adverb2,'effective')
        
        print('>>>',self.damage,'damage done. \n______________________________________________')
        user.HP -= self.damage
        if user.HP <= 0: user.HP = 0 #no negative HP
        time.sleep(1)
        self.enemy.HP_bar = ['■' for i in range(0,enemy.HP,5)]
        self.user.HP_bar = ['■' for i in range(0,user.HP,5)]
        #self.pick_actions()
        print('\n\n╔══════════════════════════════════════════╗\n   Your',user.name + "'s",'Current HP:',user.HP,'\n',''.join(self.user.HP_bar),'\n\n__________________________________________\n\n   The Wild',enemy.name + "'s",'Current HP:',enemy.HP,'\n',''.join(self.enemy.HP_bar),'\n\n\n╚══════════════════════════════════════════╝')
        time.sleep(1)
    
    def Fight(self):
        self.user.M1_PPbar = ''.join(['●' for i in range(0,user.M1_PP)])
        self.user.M2_PPbar = ''.join(['●' for i in range(0,user.M2_PP)])
        print("\n\n\n______________________________________________\n",user.name+"'s moves:",'\n[1]',user.Move_1,' PP:',user.M1_PP,self.user.M1_PPbar,'\n[2]',user.Move_2,' PP:',user.M2_PP,self.user.M2_PPbar,'\n[3] Go Back')
        self.fight_pick = int(input('Which move:'))
        self.damage_x()
        time.sleep(1)
        print('multiplier check for user',self.damage_multiplier)
        print("\n\n\n______________________________________________\n")
        
        if self.fight_pick == 1:
            self.user.M1_PP -= 1
            self.chance = random.randint(0,5)
            #print('chance is',self.chance)
            if self.chance >= 1:
                display(Image(filename='hit.jpg'))
                print('>>>',user.name,'used',user.Move_1,'and it was',self.adverb,'effective')
                self.damage = int(10*self.damage_multiplier)
            if self.chance == 0:
                print('>>>',user.name,'attacked but missed.')
                self.damage = 0
        
        elif self.fight_pick == 2:
            self.user.M2_PP -= 1
            self.chance = random.randint(0,5)
            #print('chance is',self.chance)
            if self.chance >= 2:
                display(Image(filename='hit.jpg'))
                print('>>>',user.name,'used',user.Move_2,'and it was',self.adverb,'effective')
                self.damage = int(30*(self.damage_multiplier))
            if self.chance <= 1:
                print('>>>',user.name,'attacked but missed.')
                self.damage = 0

elif self.fight_pick == 3: self.pick_actions()
    else:
        print('Please enter a valid response.')
        self.Fight()
        
        print('>>>',self.damage,'damage done by your',user.name,'!')# with multiplier x',self.damage_multiplier,'\n\n______________________________________________')
        time.sleep(1)
        enemy.HP -= self.damage
        if enemy.HP <= 0: enemy.HP = 0
        self.enemy.HP_bar = ['■' for i in range(1,enemy.HP,5)]
        self.user.HP_bar = ['■' for i in range(1,user.HP,5)]
        self.user.M1_PPbar = ''.join(['●' for i in range(0,user.M1_PP)])
        self.user.M2_PPbar = ''.join(['●' for i in range(0,user.M2_PP)])
        print('\n\n╔══════════════════════════════════════════╗\n   Your',user.name+ "'s",'\n Current HP:',user.HP,''.join(self.user.HP_bar),"\n",user.Move_1,'PP:',user.M1_PP,self.user.M1_PPbar,"\n",user.Move_2,'PP:',user.M2_PP,self.user.M2_PPbar)
        print('\n\n__________________________________________\n\n', '   The Wild',enemy.name + "'s",'Current HP:',enemy.HP,''.join(self.enemy.HP_bar),'\n\n╚══════════════════════════════════════════╝')
        if enemy.HP <= 0:self.end_message() #self.pick_actions()
        time.sleep(1)
    
    
    def Bag(self):
        self.bag = int(input('What would you like to use: \n[1] Potion \n[2] Elixir \n[3] Pokeball \n[4] Go Back'))
        print('\n\n\n______________________________________________\n\n')
        
        if self.bag == 1:
            if self.potions == 0: print('Sorry, you have no potions')
            else:
                print('You have',self.potions,'potions!')
                self.enter_potion = input('Press ENTER to use a potion \n')
                time.sleep(1)
                display(Image(filename='potion.jpg'))
                user.HP += 30
                print(user.name,'gained 30 HP!\n',user.name + "'s",'Current HP:',user.HP,'\n',''.join(user.HP_bar),'\n\n\n______________________________________________\n\n')
                self.potions -= 1
        
        elif self.bag == 2:
            if self.elixirs == 0: print('Sorry, you have no elixirs')
            else:
                print('You have',self.elixirs,'elixirs!')
                self.enter_elixirs = input('Press ENTER to use a elixir \n')
                time.sleep(1)
                display(Image(filename='elixir.jpg'))
                user.M1_PP += 5
                user.M2_PP += 5
                print(user.name,'gained 10 PP!\n',user.name + "'s",'Current:\n',user.Move_1,'PP:',user.M1_PP,self.user.M1_PPbar,"\n",user.Move_2,'PP:',user.M2_PP,self.user.M2_PPbar,'\n\n\n______________________________________________\n\n')
                self.elixirs -= 1

        elif self.bag == 3:
            if self.pokeballs == 1: print('Sorry, you have no more pokeballs \n\n\n______________________________________________\n\n')
            else:
                print('You have',self.pokeballs,'pokeballs!')
                self.enter_pokeball = input('Press ENTER to throw \n')
                time.sleep(1)
                display(Image(filename='pokeball.jpg'))
                print()
                if enemy.HP<=25:
                    self.ran2 = random.randint(0,1)
                    if self.ran2 == 0:
                        print('Congratulations! You caught the wild',enemy.name+'!!!')
                        print('\n\n\n\n\nGAMEOVER')
                        sys.exit("Bye Bye")
                    if self.ran2 == 1:
                        self.pokeballs -= 1
                        print('You missed! \n\n\n______________________________________________\n\n')
                else:
                    self.pokeballs -= 1
                    print('You missed! \n\n\n______________________________________________\n\n')

elif self.bag == 4: self.pick_actions()

else:
    print('Please enter a valid response.')
    self.Bag()
        time.sleep(1)
    
    def Run(self):
        self.run_chance = random.randint(0,5)
        if self.run_chance >= 1:
            print( 'You have left the battle.')
            print('\n\n\n\n\nGAMEOVER')
            sys.exit("Bye Bye")
            return 'done'
        else:print('\n\n\n______________________________________________\n\nYou cannot escape!\n\n______________________________________________\n\n')
    
    def end_message(self):
        if user.HP == 0:
            print('YOU LOSE THIS BATTLE \nYour',user.name,'died. \n\n\n\n\nGAMEOVER')
            sys.exit("Bye Bye")
        if enemy.HP == 0:
            print('YOU WIN THIS BATTLE \nThe wild',enemy.name,'died.\n\n\n\n\nGAMEOVER')
            sys.exit("Bye Bye")

def pick_actions(self):
    if user.HP > 0 and enemy.HP > 0:
        what = int(input('''
            What would you like to do:
            [1] Fight  ¸.•*¨*•♪¸¸.•*¨*•♫
            [2] Bag   ¸¸.•*¨*•♫¸¸.•¨*•.♬
            [3] Run  ♪¸¸.•*¨*•♫
            '''))
        if what == 1: self.Fight()
        elif what == 2: self.Bag()
        elif what == 3: self.Run()
        else:
            print('Please enter a valid response.')
            self.pick_actions()
            
            if enemy.HP >= 0:self.enemy_move()
            self.end_message()
            self.pick_actions()





poke_art = """
    ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
    \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
    \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
    \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
    \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
    \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
    \_.-'       |__|    `-._ |              '-.|     '-.| |   |
    `'                            '-._|
    """

print(poke_art)
user_char =''
user = ''
enemy = ''

#initialize the user class
def start():
    def char_pick():
        pick = int(input('CHOOSE YOUR CHARACTER: \n[1] Ash \n[2] Brock \n[3] Misty \n[4] Random \n\n(Input a number and press ENTER)\n'))
        print('You picked...', end =" ")
        global user_char
        if pick == 1: user_char = Character('Ash','is a brave pokemon trainer!','ash.jpg')
        elif pick == 2: user_char = Character('Misty','is a cheerful gym leader!','misty.jpg')
        elif pick == 3: user_char = Character('Brock','is a passionate pokemon doctor!','brock.jpg')
        elif pick == 4:
            rand_assign == random.randint(1,4)
            if rand_assign == 1: user_char = Character('Ash','is a brave pokemon trainer!','ash.jpg')
            elif rand_assign == 2: user_char = Character('Misty','is a cheerful gym leader!','misty.jpg')
            elif rand_assign == 3: user_char = Character('Brock','is a passionate pokemon doctor!','brock.jpg')
            elif rand_assign == 4:
                user_character = Character('Team Rocket','is a power-hungry trio!','teamrocket.jpg')
                print("Team Rocket is trying to steal all the pokemon!")
                Blast()
    else:
        print("nothing! \nPlease enter a valid response.")
        char_pick()
        Character():
def __init__(self,person='',personality ='',image=''):
    def user_pick():
        pick = int(input('CHOOSE YOUR POKEMON: \n[1] Pikachu \n[2] Charmander \n[3] Bulbasaur \n[4] Squirtle \n\n(Input a number and press ENTER)\n'))
        print('You picked...', end =" ")
        
        global user
        if pick == 1: user = Pokemon('Pikachu','Electric',40,'Gnaw','Thunder Jolt','Pikachu_Image.jpg')
        elif pick == 2: user = Pokemon('Charmander','Fire',50,'Scratch','Ember','Charmander_Image.jpg')
        elif pick == 3: user = Pokemon('Bulbasaur','Grass',60,'Tackle','Razor Leaf','Bulbasaur_Image.jpg')
        elif pick == 4: user = Pokemon('Squirtle','Water',50,'Bite','Skull Bash','Squirtle_Image.jpg')
        else:
            print("nothing! \nPlease enter a valid response.")
            user_pick()

user_pick()
user.card_stats()
time.sleep(1)


print('''
    ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
    ◈                          ◈
    ◈    You will battle ...   ◈
    ◈                          ◈
    ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
    ''')
        display(Image(filename='card.jpg'))
        time.sleep(1)

        #intialize the random opponent
def enemy_opponent():
    print('a wild... ',end='')
    time.sleep(1)
    
    global enemy
        #opponent = random.randint(1,4)
        opponent = 2
        if opponent == 1:enemy = Pokemon('Pikachu','Electric',40,'Gnaw','Thunder Jolt','Pikachu_Image.jpg')
        if opponent == 2:enemy = Pokemon('Charmander','Fire',50,'Scratch','Ember','Charmander_Image.jpg')
        if opponent == 3:enemy = Pokemon('Bulbasaur','Grass',60,'Tackle','Razor Leaf','Bulbasaur_Image.jpg')
        if opponent == 4:enemy= Pokemon('Squirtle','Water',50,'Bite','Skull Bash','Squirtle_Image.jpg')
        time.sleep(1)
        enemy.card_stats()
        time.sleep(1)
    
    enemy_opponent()

start()

actions = Actions(user,enemy)
time.sleep(1)
actions.pick_actions()
