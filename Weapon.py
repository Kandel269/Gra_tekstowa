from random import sample


class Skill():
    def __init__(self,damage,crit_damage,crit_chance,accuracy):
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.accuracy = accuracy

    def __repr__(self):
        return "taka Fajna pukawa"

    def hit_or_dodge(self) -> bool:
        dodge = sample(range(1,100),1)
        if dodge <= self.accuracy:
            return True             #trafienie
        else:
            return False            #unik

    def do_damage(self) -> int:
        crit = sample(range(100),1)[0]

        if crit <= self.crit_chance:
            print("TRAFIENIE KRYTYCZNE!")
            return -int(self.crit_damage)
        else:
            return -int(sample(self.damage,1)[0])


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


