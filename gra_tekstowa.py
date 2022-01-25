from random import sample
from Person import Monster,Human,Player,NPC
from Weapon import Weapon_range,Weapon,Weapon_melee,Skill


class Combat():
    def enemy_turn(self,enemy_Person,player_Person,number_of_enemy = 1):
        pass
    def player_turn(self,player_Person,enemy_Person):
        combat_item = []
        print(player_Person.ammunition)

        for i in player_Person.combat_item_melee:
                combat_item.append(i)
        for i in player_Person.combat_item_range:
            if self.can_u_shot(player_Person,i):
                combat_item.append(i)

        for i in range(len(combat_item)):
            print(f"{i+1} Przywal z {combat_item[i]}")

        player_weapon_choose = int(input("Nacisnij odpowiedznia cyfre, aby wybrac odpowiednia pukawke"))
        damage = combat_item[player_weapon_choose].do_damage()
        enemy_Person.change_HP(damage)


    def can_u_shot(self,Person,weapon_range):
        if Person.ammunition[weapon_range.type_amunition] > 0:
            return True
        else:
            return False

class Location():
    def __init__(self,neighbours, describe,list_of_action,player = True, enemy = 0,npc = 0,secret_room = 0,loot = 0,visit = 0):
        self.neighbours = neighbours
        self.enemy = enemy
        self.npc = npc
        self.secret_room = secret_room
        self.describe = describe
        self.list_of_action = list_of_action
        self.loot = loot
        self.player = player
        self.visit = visit

    def first_describe(self):                                 ## descirbe musi byc wprowadzone w formie listy, ktora zawiera stringi
        for i in self.describe:
            print(i)
        self.player = True

    def action_location(self):                                 ## list of action ma byc slownikiem
        for i in self.list_of_action.keys():
            print(i)

    def add_action(self,action):
        self.list_of_action.append(action)

    def delete_action(self,action):
        del(self.list_of_action[action])

    def take_loot(self,number_loot: int,person):
        person.item_list.append(self.loot[number_loot])

    def do_action(self,chosen_action):
        x = 0
        for i in self.list_of_action:
            x += 1
            if x == int(chosen_action):
                return self.list_of_action[i]


    def change_person_here(self,in_our_out):
        self.player = in_our_out

class Bassement_1(Location):
    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == 1:
            self.look_on_radio()
        elif chosen == 2:
            self.look_around()
        elif chosen == 3:
            return self.go_down_stairs()

    def look_on_radio(self):
        print("gapisz sie na radio")

    def look_around(self):
        print("gapisz sie na brzydkie sciany")
        input("potwierdz, ze sie pogapiles")

    def go_down_stairs(self):
        self.player = False
        return Bassement_start_2


class Bassement_2(Location):
    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == 1:
            self.look_on_your_ass()
        elif chosen ==2:
            self.go_front()

    def look_on_your_ass(self):
        input("fajne masz dupsko")

    def go_front(self):
        self.player = False
        return Bassement_start_3

class Bassement_3(Location):
    def player_chosen(self,chosen_action):
        if self.visit == 0:
            self.visit += 1
            input("maly gamon nie daje ci czasu do namyslu i rzuca sie na ciebie")
            self.fight_rat()
        chosen = self.do_action(chosen_action)

    def fight_rat(self):



Bassement_start = Bassement_1(["Bassement_2"],["Budzisz sie w piwnicy", "Czujesz sie bardzo XD"],{"1: Spojrz na radio":1,"2: Rozgladnij sie":2,"3: Idz schodami na dol":3},True,0,0,0,0,0)
Bassement_start_2 = Bassement_2(["Bassement_start","Bassement_start_3"],["Za soba masz schody", "Przed soba ciemny korytarz"],{"1: Spojrz na dupsko":1,"2: Idz w korytarz":2},False,0,0,0,0,0)
Bassement_start_3 = Bassement_3(["Bassement_start_2"],["Widzisz przed soba zwloki, byc moze to zwloki kogos tobie bliskiego","Np.twojego dziadka, ktory pewnego razu poszedl po ziemniaki i nie wrocil...","Dostrzegasz siedzacego na nim ogromnego szczura, ktory groznie lypie na ciebie swymi oczyma"],{"1: Spojrz na dupsko, ale tylko tak troche":1},False,0,0,0,0,0)



def Ready_player_one(actuall_location):
    actuall_location.first_describe()
    input("")
    while  actuall_location.player == True:
        actuall_location.action_location()
        choose = input("")
        x = actuall_location.player_chosen(choose)
        if actuall_location.player == False:
            return x

turn = 1
actuall_location = Bassement_start

while True:
    actuall_location = Ready_player_one(actuall_location)
    turn += 1
