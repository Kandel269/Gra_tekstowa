from random import sample

class Person():
    def __init__(self,HP):
        self.HP = HP
    def change_HP(self,HP) -> bool:
        self.HP += HP
        return self.dead()

    def dead(self) -> bool:
        if self.HP <= 0:
            return False
        else:
            return True

class Human(Person):
    def __init__(self,HP,combat_item_range = None,combat_item_melee = None,item_list = None):
        super().__init__(HP)
        self.combat_item_melee = [combat_item_melee]
        self.combat_item_range = [combat_item_range]
        self.item_list = [item_list]

class Player(Human):
    def __init__(self,HP,combat_item_range = None,combat_item_melee = None,money = 0,item_list = None,ammunition_pistol = 0,ammunition_rifle = 0, ammunition_shotgun = 0):
        super().__init__(HP,combat_item_melee,combat_item_range,item_list)
        self.ammunition = {"ammunition_pistol":ammunition_pistol,"ammunition_rifle":ammunition_rifle,"ammunition_shotgun":ammunition_shotgun}
        self.money = money

    def show_backpack(self):
        pass

    def change_money(self,money) -> bool:
        if self.money + money <  0:
            return False
        else:
            self.money += money
            return True

    def change_ammunition(self,type_ammunition,number) -> None:
        self.ammunition[type_ammunition] += number

    def change_backpack(self,item,add_or_remove) -> None:
        if add_or_remove == "add":
            self.item_list.append(item)
        elif add_or_remove == "remove":
            self.item_list.remove(item)


class Monster(Person):
    pass

class NPC(Human):
    pass

class Skill():
    def __init__(self,damage,crit_damage,crit_chance,accuracy):
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.accuracy = accuracy

    def hit_or_dodge(self) -> bool:
        dodge = sample(range(1,100),1)
        if dodge <= self.accuracy:
            return True             #trafienie
        else:
            return False            #unik

    def do_damage(self) -> int:
        crit = sample(range(100),1)
        if crit <= self.crit_chance:
            return self.crit_damage
        else:
            return sample(self.damage,1)

class Weapon(Skill):
    def __init__(self,damage,value,durability,crit_damage,crit_chance,accuracy):         # crit chcance - pomiedzy 0 a 100, gdzie 100 = 100%
        super().__init__(damage,crit_damage,crit_chance,accuracy)
        self.value = value
        self.durability = durability

    def change_durability(self,durability) -> None:
        self.durability += durability


class Weapon_melee(Weapon):
    pass


class Weapon_range(Weapon):
    def __init__(self,damage,value,durability,crit_damage,crit_chance,accuracy,type_amunition):
        super().__init__(damage, value, durability, crit_damage, crit_chance, accuracy)
        self.type_amunition = type_amunition

    def do_damage(self,Person) -> int:                      ### tu cos sie pluje, ze nie zgadza sie z Weapon.do_damage, ze nie sa takie same, daje to w ignoruj\\\ Signature of method 'Weapon_range.do_damage()' does not match signature of the base method in class 'Weapon'
        self.minus_ammunition(Person)
        crit = sample(range(100), 1)
        if crit <= self.crit_chance:
            return self.crit_damage
        else:
            return sample(self.damage, 1)

    def minus_ammunition(self,Person):
        Person.ammunition[self.type_amunition] -= 1


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



kalach = Weapon_range(1,1,1,1,1,1,"ammunition_rifle")


