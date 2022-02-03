import time
from copy import deepcopy
from random import sample
from Person import Monster,Human,Player,NPC
from Weapon import Weapon_range,Weapon,Weapon_melee,Skill
from Combat import Combat
from Item import Item
from Event import Event


class Location():
    def __init__(self,neighbours, describe,describe_numero_uno,list_of_action,player = True,visit = 0):           # visit to bedzie taka lista gdzie odpowiednie pod lokacje beda z niej korzystac do okreslania czasu
        self.neighbours = neighbours
        self.describe = describe
        self.describe_numero_uno = describe_numero_uno
        self.list_of_action = list_of_action
        self.player = player
        self.visit = visit

    def first_describe(self):                                                                          # visit[0], zawsze i wszedzie bedzie rezerwowany
        self.player = True
        if self.visit[0] == 0:
            self.visit[0] = 1
            print(self.describe_numero_uno)
        print(self.describe)

    def action_location(self):                                 ## list of action ma byc slownikiem
        if "Pokaz informacje o postaci" not in self.list_of_action.values():
            self.list_of_action[-1] = "Pokaz informacje o postaci"
        self.sort_action_list()
        for i in self.list_of_action.keys():
            print(i, end = ": ")
            print(self.list_of_action[i])


    def action_location_local(self,list_of_action_local):
        # if "Pokaz informacje o postaci" not in self.list_of_action.values():
        #     self.list_of_action[-1] = "Pokaz informacje o postaci"
        for i in list_of_action_local.keys():
            print(i, end = ": ")
            print(list_of_action_local[i])

    def ready_player_one_location(self,list_of_action_location_local):
        chosen_radio = -1
        new_list_keys = []
        for i in list_of_action_location_local.keys():
            new_list_keys.append(str(i))
        while chosen_radio not in new_list_keys:
            chosen_radio = input()
        if chosen_radio not in new_list_keys:
            print("Wpisz poprawna wartosc")
        return int(chosen_radio)

    def add_action(self,action):
        self.list_of_action.append(action)

    def delete_action(self,action):
        del(self.list_of_action[int(action)])
        self.sort_action_list()

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

    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == "Przygladnij sie radiu":
             return self.look_on_radio()
        elif chosen == "Przeszukaj szafe":
            return self.search_wardrobe(chosen_action)
        elif chosen == "Przespij sie na materacu":
            return self.sleep_on_bed(chosen_action)
        elif chosen == "Idz schodami na dol":
            return self.go_downstairs()
        elif chosen == "Idz do pomieszczenia na wprost":
            pass

    def look_on_radio(self):                        #visit[3,1]
        list_of_action_radio = {}
        if self.visit[3] == 0:
            input("Gapisz sie dluzsza chwile na radio i nie wiesz dlaczego nie dziala...\n Twoje nadzwyczaj spore umiejetnosci intelektualne podpowiadaja ci, ze cos jest z nim nie tak\n Krecisz wszystkimi dostepnymi galkami po kolei, naciskasz wszystkie guziki po kolei... dalej nic\n No tak! Wpadles na genialny pomysl, moze nie jest podlaczone do pradu?\n Gniazdka nigdzie tutaj nie ma. Zauwazyles, ze radio mozna zasilac rowniez przez baterie\n")
            self.visit[3] = 1
        if self.visit[3] == 1:
            list_of_action_radio[1] = "Pogap sie chwile na radio z nadzieja, ze jakims magicznym cudem sie uruchomi"
            if Bateria in Player_one.item_list:
                list_of_action_radio[2] = "Wloz baterie do radia"
        if self.visit[3] in [2,3]:
            list_of_action_radio[1] = "Zalacz radio"
            list_of_action_radio[2] = "Wyjmij baterie"

        self.action_location_local(list_of_action_radio)
        chosen_radio = self.ready_player_one_location(list_of_action_radio)
        if list_of_action_radio[chosen_radio] == "Pogap sie chwile na radio z nadzieja, ze jakims magicznym cudem sie uruchomi":
            input("Twoje magiczne starania spelzaja na niczym")
        elif list_of_action_radio[chosen_radio] == "Wloz baterie do radia":
            Player_one.change_backpack(Bateria,"remove")
            input("Odkryles umiejetnosc wkladania baterii do radia! Brawo ty!")
            self.visit[3] = 2
            return self.look_on_radio()
        elif list_of_action_radio[chosen_radio] == "Zalacz radio":
            if self.visit[1] == 0:
                self.visit[1] += 1
                input("Radio bzyczy...\n Uderzasz piescia w radio")
                input("No! Stara, dobra Polska szkola serwisowa dziala jak zawsze!\n")
            if self.visit[2] >= 3:
                input("Wspaniala sloneczna pogoda!\n Mamy dobre informacje, mozna (prawie) bezpiecznie wyjsc na zewnatrz\n Pamietajcie, unikajcie miejsc skazonych!\n  ")
            else:
                input("Pogoda na dzien dzisiejszy!\n Jak zwykle pelno opadow radioaktywnych, zalecamy nie wychodzi z domu\n Za kilka dni bedziecie mogli znowy wyjsc na powierzchnie\n")                # visit[2] - odlicza dni dla radia + dorzucic do materaca
        elif list_of_action_radio[chosen_radio] == "Wyjmij baterie":
            Player_one.change_backpack(Bateria,"add")
            self.visit[3] = 1


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



    def go_downstairs(self):
        self.player = False
        return Bassement_start_2

    def sleep_on_bed(self,chosen_action):
        print("Materac nie jest zbyt okazaly, wyglada jakby mial sie rozleciec\nIdziesz spac, troche to zajmie, wiec mozesz isc na spokojnie zaparzyc kawe czy herbate(Nic nie klikaj)\n")
        time.sleep(2)
        print("Zzzz")
        time.sleep(2)
        print("Zzzz")
        time.sleep(2)
        print("Zzzz")
        input(f"Brawo ty! Odzyskales {Player_one.regeneration_HP(5)} HP")
        self.visit[2] += 1
        if self.visit[2] == 3:
            choose = -1
            while choose not in ["1","2","3","4"]:
                choose = input("""Twoj wspanialy materac zaczyna trzeszczec, ewidentnie widac, ze zaraz sie rozpadnie\n
                      1: Myszy\n
                      2: Plesn\n
                      3: Kosmita\n
                      4: Inny powod\n
                      Wybierz  powod ^^\n
                      """)
                if choose not in ["1","2","3","4"]:
                    print("Podaj poprawna wartosc")
            if choose == "1":
                input("Nadgryzany wielokrotnie przez male szkodniki, w koncu zostal zjedzony niemal calkowicie")
            elif choose == "2":
                input("Zbierasz sie na wymioty jezeli tylko pomyslisz, ze masz spedzic jeszcze jedna noc na tym okropnym materacu")
            elif choose == "3":
                input("Przez magiczny portal przeszedl kosmita z obcej planety i ukradl twoj materac")
            elif choose == "4":
                txt = input("Wpisz swoj wlasny powod, nie tylko autor tej gry musi byc kreatywny!\n")
                input(f"Tak, {txt}, to dobry powod dlaczego nigdy wiecej nie skorzystasz z tego materaca")

            self.delete_action(chosen_action)

class Bassement_2(Location):
    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == "Idz schodami na gore":
            return self.go_upstairs()
        elif chosen == "Idz w ciemny korytarz":
            return self.go_front()

    def go_upstairs(self):
        self.player = False
        return Bassement_start

    def go_front(self):
        self.player = False
        return Bassement_start_3

class Bassement_3(Location):
    def player_chosen(self,chosen_action):
        chosen = self.do_action(chosen_action)
        if chosen == "Przeszukaj zwloki":
            return self.grandpa(chosen_action)
        elif chosen == "Sproboj otworzyc drzwi":
            return self.open_the_door()
        elif chosen == "Idz w strone korytarza":
            return self.go_front()

    def first_describe(self):
        self.player = True
        if self.visit[0] == 0:
            self.visit[0] = 1
            print(self.describe_numero_uno)
            input("Maly gamon nie daje ci czasu do namyslu i rzuca sie na ciebie")
            self.fight_rat()
            print("Po zakonczonej walce dostrzegasz stare, drewniane drzwi po twojej lewej stronie")
        else:
            print(self.describe)

    def fight_rat(self):
        still_fight = 1
        while still_fight == 1:
            still_fight = Fight.player_turn(Player_one,Rat_1)
            print(still_fight)
            if still_fight == 1:
                still_fight = Fight.enemy_turn(Rat_1,Player_one)
        print("koniec walki, w nagrode nic nie dostajesz")

    def grandpa(self,chosen_action):
        input("Powinna dosiegnac ciebie klatwa twojego dziadka\nMasz szczescie, ze jeszcze tworca gry nie zaimplementowal klatw")
        input("Dziadek miał przy sobie ulubiona zabawke z okresu drugiej wojny swiatowej\npistolet mauserC96, niestety nie znajdujesz zadnej amunicji")
        Player_one.change_backpack(Mauser,"add")
        self.delete_action(chosen_action)

    def open_the_door(self):
        choose = -1
        while choose != 1:
            input("""Drzwi sa zamkniete, mozesz sprobowac je otworzyc\n
            1: Uzyj loma
            """)
            if choose != 1:
                print("Wprowadz poprawna wartosc")
        print("Nie masz loma kanciarzu!")

    def go_front(self):
        self.player = False
        return Bassement_start_2

######### Lokacje
Bassement_start = Bassement_1(["Bassement_2"],"Znajdujesz sie w malym pomieszczeniu, po prawej stronie znajduje sie wielka szafa\nna wprost widzisz kolejne,ciemne pomieszczenie\npod tylnia sciana dostrzegasz materac oraz polke na ktorej stoi radio\npo lewej stronie sa schody, ktore prowadza do nizej polozonego korytarza\nEhhh autor mogl pokusic sie o lepsze opisy... ","Budzisz sie z ogromnym bolem glowy\nProbujesz sobie przypomniec, co sie wydarzlo\nZeszlej nocy zostales sam w domu, imprezowales cala noc\nAaa... tak... alarm bombowy, wojna atomowa, tylko kilkadziesiat atomowek spadlo na twoj kraj\nslychac bylo wycie syren, zlapales co miales pod reka i wskoczyles do piwnicy\nw sumie dawno do niej nie zagladales, jakos tak... od urodzenia\nMasz teraz chwile czasu, aby sie po niej rozgladnac\n",{1:"Przygladnij sie radiu",2:"Przeszukaj szafe",3:"Przespij sie na materacu",4:"Idz schodami na dol",5:"Idz do pomieszczenia na wprost"},True,[0,0,0,0])
Bassement_start_2 = Bassement_2(["Bassement_start","Bassement_start_3"],"Schodzisz po schodach na dol\nwidzisz przed soba ciemny korytarz",None,{1:"Idz schodami na gore",2:"Idz w ciemny korytarz"},False,[1])
Bassement_start_3 = Bassement_3(["Bassement_start_2"],"Widzisz na srodku pomieszczenia zwloki\npo lewej stronie dostrzegasz stare, drewniane drzwi","Korytarz sie skonczyl\nWidzisz przed soba zwloki, byc moze to zwloki kogos tobie bliskiego\nnp.twojego dziadka, ktory pewnego razu poszedl po ziemniaki i nie wrocil...\nDostrzegasz siedzacego na nim ogromnego szczura, ktory groznie lypie na ciebie swymi oczyma\n",{1:"Przeszukaj zwloki",2:"Sproboj otworzyc drzwi",3:"Idz w strone korytarza"},False,[0,0])
################################# Skile
############## Skile, potwory
Bite = Skill(damage = [1,2],crit_damage = 0,crit_chance = -1,accuracy = 60,describe = "")
Punch = Skill(damage = [1,2],crit_damage = 3,crit_chance = 15,accuracy = 60,describe = "Twoje wspanile piesci")
################# Bron zasiegowa
Mauser = Weapon_range(damage = [4,5,5,6],value = 15, durability = 60, crit_damage = 8,crit_chance = 5,accuracy = 70,type_amunition = "amunicja pistolet",describe = "Pistolet z okresu II wojny swiatowej, kiedys nalezal do twojego dziadka")
######## Gracz
Player_one = Player(HP = 30, max_HP = 30,skills = [Punch], item_list = [])
######## Itemy
Bateria = Item(value = 10, describe = ["Para Baterii"])
########### Potwory
Rat = Monster(HP = 5,max_HP = 5,skills = [Bite],drop_item = 0,drop_item_chance = 0,drop_exp = 1)
Rat_1 = deepcopy(Rat)
##################### Questy i eventy
Bassement_radiation = Event(True)
####################
Fight = Combat()


def Ready_player_one(actuall_location):
    actuall_location.first_describe()
    input("")
    while  actuall_location.player == True:
        actuall_location.action_location()
        good_value = True
        while good_value == True:
            choose = input("")
            good_value = actuall_location.good_input_location(choose)
        if actuall_location.list_of_action[int(choose)] == "Pokaz informacje o postaci":
            print("dupsko")
            Player_one.show_backpack()
        x = actuall_location.player_chosen(choose)
        if actuall_location.player == False:
            return x

turn = 1
actuall_location = Bassement_start

while True:
    actuall_location = Ready_player_one(actuall_location)
    turn += 1
