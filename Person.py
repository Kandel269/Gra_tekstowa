from copy import deepcopy
from random import sample


class Person():
    def __init__(self,HP,max_HP,skills):
        self.HP = HP
        self.max_HP = max_HP
        self.skills = skills

    def change_HP(self,HP) -> bool:
        self.HP += HP
        return self.dead()

    def dead(self) -> bool:
        if self.HP <= 0:
            return False
        else:
            return True

    def regeneration_HP(self,regeneration) -> int:                            ## dodaje HP, zwraca wartosc o ile odzyskalismy HP, nie mozna przekroczyc MAX HP
        if self.HP + regeneration >= self.max_HP:
            value = deepcopy(self.max_HP - self.HP)
            self.HP = deepcopy(self.max_HP)
            return value
        else:
            self.HP += regeneration
            return regeneration

class Human(Person):
    def __init__(self,HP,max_HP,skills,combat_item_range = None,combat_item_melee = None,item_list = None):
        super().__init__(HP,max_HP,skills)
        self.combat_item_melee = combat_item_melee
        self.combat_item_range = combat_item_range
        self.item_list = item_list

    def change_backpack(self,item,add_or_remove) -> None:
        if add_or_remove == "add":
            self.item_list.append(item)
        elif add_or_remove == "remove":
            self.item_list.remove(item)

class Enemy(Person):
    def __init__(self,HP,max_HP,skills,drop_item,drop_item_chance,drop_exp):
        super().__init__(HP,max_HP,skills)
        self.list_of_skills = []
        self.drop_item = drop_item                    # slownik {itemek: ilosc}
        self.drop_item_chance = drop_item_chance     # pokazuje jaka jest szansa na wydropienie danego itemku proporcjonalnie do powyzszych wartosci
        self.drop_exp = drop_exp                      #do implementacji w lvlu, na razie nie tykac

    def drop(self):
        items = {}
        x = -1
        for i in self.drop_item:
            x += 1
            probability = self.drop_item_chance[x]
            for j in probability:
                quantity = sample(range(0,100),1)
                if quantity <= j:
                    items[i] = self.drop_item[i]
                    break
                else:
                    continue

class Player(Human):
    def __init__(self,HP,max_HP,skills,combat_item_melee = None,combat_item_range = None,item_list = None,money = 0,ammunition_pistol = 0,ammunition_rifle = 0, ammunition_shotgun = 0):
        super().__init__(HP,max_HP,skills,combat_item_melee,combat_item_range,item_list,)
        self.ammunition = {"amunicja pistolet":ammunition_pistol,"amunicja karabin":ammunition_rifle,"amunicja shotgun":ammunition_shotgun}
        self.money = money

    def show_backpack(self):
        choose = "-1"
        counter = 0
        backpack_list_of_actions = {"0": "Powrot"}
        backpack_list_of_actions_weapons_print = []
        backpack_list_of_actions_items_print = []
        print(f"aktualny poziom doswiadczenia twojej postaci: 1, wymagane doswiadczenie do osiagniecia kolejnego poziomu: nieskonczonosc")
        print(f"""Amunicja do: pistoletu - {self.ammunition["amunicja pistolet"]}, karabinu - {self.ammunition["amunicja karabin"]}, shotguna - {self.ammunition["amunicja shotgun"]}""")
        print(f"Twoje aktualne HP wynosi {self.HP} z maksymalnej wartosci {self.max_HP}")
        print(f"Posiadasz {self.money} hajsu")
        for i in self.skills:
            counter += 1
            backpack_list_of_actions[str(counter)] = i
            backpack_list_of_actions_weapons_print.append(f"{counter}: {i}")
        if self.combat_item_melee:
            for i in self.combat_item_melee:
                counter += 1
                backpack_list_of_actions[str(counter)] = i
                backpack_list_of_actions_weapons_print.append(f"{counter}: {i}")
        if self.combat_item_range:
            for i in self.combat_item_range:
                counter += 1
                backpack_list_of_actions[str(counter)] = i
                backpack_list_of_actions_weapons_print.append(f"{counter}: {i}")
        print(f"Twoja lista umiejetnosci/przedmiotow do walki:{backpack_list_of_actions_weapons_print}")
        if self.item_list:
            for i in self.item_list:
                counter += 1
                backpack_list_of_actions[str(counter)] = i
                backpack_list_of_actions_items_print.append(f"{counter}: {i}")
        print(f"Twoja lista przedmiotow uzytkowych: {backpack_list_of_actions_items_print}")
        print("0: wyjscie ze statusu postaci")

        while choose != "0":
            while choose not in backpack_list_of_actions.keys():
                choose = input()
                if choose not in backpack_list_of_actions.keys():
                    print("Wpisz poprawna wartosc")
            if choose != "0":
                backpack_list_of_actions[choose].describe_all()
                choose = "-1"

    def change_money(self,money) -> bool:
        if self.money + money <  0:
            return False
        else:
            self.money += money
            return True

    def change_ammunition(self,type_ammunition,number) -> None:
        self.ammunition[type_ammunition] += number



class Monster(Enemy):
    pass

class NPC(Human,Enemy):
    pass


