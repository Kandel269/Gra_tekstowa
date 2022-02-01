from copy import deepcopy
from random import sample
from Person import Monster,Human,Player,NPC
from Weapon import Weapon_range,Weapon,Weapon_melee,Skill
from Combat import Combat
from Item import Item

class Location():
    def __init__(self,neighbours, describe,list_of_action,player = True,visit = 0):           # visit to bedzie taka lista gdzie odpowiednie pod lokacje beda z niej korzystac do okreslania czasu
        self.neighbours = neighbours
        self.describe = describe
        self.list_of_action = list_of_action
        self.player = player
        self.visit = visit


    def first_describe(self):                                 ## descirbe musi byc wprowadzone w formie listy, ktora zawiera stringi
        for i in self.describe:
            print(i)
        self.player = True

    # def action_location(self):                                 ## list of action ma byc slownikiem
    #     self.sort_action_list()
    #     for i in self.list_of_action.values():
    #         print(i)
    def action_location(self):                                 ## list of action ma byc slownikiem
        self.sort_action_list()
        for i in self.list_of_action.keys():
            print(i, end = ": ")
            print(self.list_of_action[i])

    def action_location_local(self,list_of_action_local):
        for i in list_of_action_local.keys():
            print(i, end = ": ")
            print(list_of_action_local[i])

    def add_action(self,action):
        self.list_of_action.append(action)

    def delete_action(self,action):
        del(self.list_of_action[int(action)])

    def take_loot(self,number_loot: int,person):
        person.item_list.append(self.loot[number_loot])

    def do_action(self,chosen_action):
        x = 0
        for i in self.list_of_action:
            x += 1
            if x == int(chosen_action):
                return self.list_of_action[i]

    def sort_action_list(self):
        new_action_list = {}
        counter = 0
        for i in self.list_of_action:
            counter += 1
            new_action_list[counter] = self.list_of_action[i]
        self.list_of_action = deepcopy(new_action_list)

    def change_person_here(self,in_our_out):
        self.player = in_our_out

    def good_input_location(self,chose):
        new_list_keys = []
        for i in self.list_of_action.keys():
            new_list_keys.append(str(i))
        if chose in new_list_keys:
            return False
        else:
            print("Wpisz poprawna wartosc")
            return True

class Bassement_1(Location):
    def player_chosen(self,chosen_action):               #visit[0]
        chosen = self.do_action(chosen_action)
        if chosen == "Przygladnij sie radiu":
             return self.look_on_radio()
        elif chosen == "Przeszukaj szafe":
            return self.search_wardrobe(chosen_action)
        elif chosen == "Przespij sie na materacu":
            pass
        elif chosen == "Idz schodami na dol":
            return self.go_down_stairs()
        elif chosen == "Idz do pomieszczenia na wprost":
            pass

    def look_on_radio(self):
        chosen_radio = -1
        new_list_keys = []
        if self.visit[0] == 0:
            input("Gapisz sie dluzsza chwile na radio i nie wiesz dlaczego nie dziala...\n Twoje nadzwyczaj spore umiejetnosci intelektualne podpowiadaja ci, ze cos jest z nim nie tak\n Krecisz wszystkimi dostepnymi galkami po kolei, naciskasz wszystkie guziki po kolei... dalej nic\n No tak! Wpadles na genialny pomysl, moze nie jest podlaczone do pradu?\n Gniazdka nigdzie tutaj nie ma. Zauwazyles, ze radio mozna zasilac rowniez przez baterie")
            self.visit[0] += 1
        if self.visit == 1:
            list_of_action_radio = {1: "Pogap sie chwile na radio z nadzieja, ze jakims magicznym cudem sie uruchomi"}
            if Bateria in Player_one.item_list:
                list_of_action_radio[2] = "Wloz baterie do radia"
            self.action_location_local(list_of_action_radio)
            for i in list_of_action_radio.keys():
                new_list_keys.append(str(i))
            while chosen_radio not in new_list_keys:
                chosen_radio = input()
                if chosen_radio not in new_list_keys:
                    print("Wpisz poprawna wartosc")
            if list_of_action_radio[chosen_radio] ==  "Pogap sie chwile na radio z nadzieja, ze jakims magicznym cudem sie uruchomi":
                input("Twoje magiczne starania spelzaja na niczym")
            elif list_of_action_radio[chosen_radio] == "Wloz baterie do radia":
                Player_one.change_backpack(Bateria,"remove")


    def search_wardrobe(self,chosen_action):
        chosen_wardrobe = -1
        new_list_keys = []
        list_of_action_wardrobe = {1:"Zabierz ze soba baterie"}
        print("Szafa jest niemal pusta, poza dwoma samotnie leżącymi bateriami... Ciekawe czy jeszcze działają?")
        self.action_location_local(list_of_action_wardrobe)
        for i in list_of_action_wardrobe.keys():
            new_list_keys.append(str(i))
        while chosen_wardrobe not in new_list_keys:
            chosen_wardrobe = input()
            if chosen_wardrobe not in new_list_keys:
                print("Wpisz poprawna wartosc")
        Player_one.change_backpack(Bateria,"add")
        print(self.list_of_action[int(chosen_action)])
        self.delete_action(chosen_action)
        print("\n")
        self.sort_action_list()


    def go_down_stairs(self):
        self.player = False
        return Bassement_start_2


class Bassement_2(Location):
    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == 1:
            self.look_on_your_ass()
        elif chosen ==2:
            return self.go_front()

    def look_on_your_ass(self):
        input("fajne masz dupsko")

    def go_front(self):
        self.player = False
        return Bassement_start_3

class Bassement_3(Location):
    def player_chosen(self,chosen_action):
            chosen = self.do_action(chosen_action)

    def visit_1st(self):
        self.visit += 1
        input("maly gamon nie daje ci czasu do namyslu i rzuca sie na ciebie")
        self.fight_rat()

    def fight_rat(self):
        still_fight = 1
        while still_fight == 1:
            still_fight = Fight.player_turn(Player_one,Rat_1)
            print(still_fight)
            if still_fight == 1:
                still_fight = Fight.enemy_turn(Rat_1,Player_one)
        print("koniec walki, w nagrode nic nie dostajesz")


######### Lokacje
Bassement_start = Bassement_1(["Bassement_2"],["Budzisz sie z ogromnym bolem glowy", "Probujesz sobie przypomniec, co sie wydarzlo","Zeszlej nocy zostales sam w domu, imprezowales cala noc","Aaa... tak... alarm bombowy, wojna atomowa, tylko kilkadziesiat atomowek spadlo na twoj kraj", "slychac bylo wycie syren, zlapales co miales pod reka i wskoczyles do piwnicy","w sumie dawno do niej nie zagladales, jakos tak... od urodzenia","Masz teraz chwile czasu, aby sie po niej rozgladnac\n\n","Znajdujesz sie w malym pomieszczeniu, po prawej stronie znajduje sie wielka szafa", "na wprost widzisz kolejne,ciemne pomieszczenie","pod tylnia sciana dostrzegasz materac oraz polke na ktorej stoi radio","po lewej stronie sa schody, ktore prowadza do nizej polozonego korytarza","Ehhh autor mogl pokusic sie o lepsze opisy... "],{1:"Przygladnij sie radiu",2:"Przeszukaj szafe",3:"Przespij sie na materacu",4:"Idz schodami na dol",5:"Idz do pomieszczenia na wprost"},True,[0])
Bassement_start_2 = Bassement_2(["Bassement_start","Bassement_start_3"],["Za soba masz schody", "Przed soba ciemny korytarz"],{"1: Spojrz na dupsko":1,"2: Idz w korytarz":2},False,[0])
Bassement_start_3 = Bassement_3(["Bassement_start_2"],["Widzisz przed soba zwloki, byc moze to zwloki kogos tobie bliskiego","Np.twojego dziadka, ktory pewnego razu poszedl po ziemniaki i nie wrocil...","Dostrzegasz siedzacego na nim ogromnego szczura, ktory groznie lypie na ciebie swymi oczyma"],{"1: Spojrz na dupsko, ale tylko tak troche":1},False,[0])
################################# Skile
############## Skile, potwory
Bite = Skill([1,2],0,-1,60)
Punch = Skill([1,2],3,15,60)
######## Gracz
Player_one = Player(HP = 30, max_HP = 30,skills = [Punch], item_list = [])
######## Itemy
Bateria = Item(value = 10, describe = ["Para Baterii"])
########### Potwory
Rat = Monster(HP = 5,max_HP = 5,skills = [Bite],drop_item = 0,drop_item_chance = 0,drop_exp = 1)
Rat_1 = deepcopy(Rat)
###################
Fight = Combat()


def Ready_player_one(actuall_location):
    actuall_location.first_describe()
    input("")
    while  actuall_location.player == True:
        if actuall_location.visit == 0:
            actuall_location.visit_1st()
        actuall_location.action_location()
        good_value = True
        while good_value == True:
            choose = input("")
            good_value = actuall_location.good_input_location(choose)
        x = actuall_location.player_chosen(choose)
        if actuall_location.player == False:
            return x

turn = 1
actuall_location = Bassement_start

while True:
    actuall_location = Ready_player_one(actuall_location)
    turn += 1
