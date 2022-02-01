from random import sample


class Combat():
    def enemy_turn(self,enemy_Person,player_Person,number_of_enemy = 1):
        enemy_combat_item = []
        for i in enemy_Person.skills:
            enemy_combat_item.append(i)
        choose_enemy_combat_item = sample(enemy_combat_item, 1)[0]
        enemy_damage = choose_enemy_combat_item.do_damage()
        print(f"Przeciwnik przywalil ci za {enemy_damage} punktow obrazen\n")
        if player_Person.change_HP(enemy_damage) == True:
            still_fight = 1
        else:
            input("Umarles!\n Zbytnio sie tym nie przejmuj, beda o tobie pisac piesni przez tysiace lat...\n albo szybko o tobie zapomna ")
            still_fight = 0
        return still_fight

    def player_turn(self,player_Person,enemy_Person):
        combat_item = []
        print(player_Person.ammunition)
        print(f"Twoje aktualne HP wynosi {player_Person.HP} z {player_Person.max_HP}")
        print(f"Aktualne HP twojego przeciwnika: {enemy_Person.HP} z {enemy_Person.max_HP}")
        if player_Person.skills == None:
            pass
        else:
            for i in player_Person.skills:
                combat_item.append(i)
        if player_Person.combat_item_melee == None:
            pass
        else:
            for i in player_Person.combat_item_melee:
                    combat_item.append(i)
        if player_Person.combat_item_range == None:
            pass
        else:
            for i in player_Person.combat_item_range:
                if self.can_u_shot(player_Person,i):
                    combat_item.append(i)

        for i in range(len(combat_item)):
            print(f"{i+1}: Przywal z {combat_item[i]}")

        player_weapon_choose = (int(input("Nacisnij odpowiedznia cyfre, aby wybrac odpowiednia pukawke\n"))-1)
        damage = combat_item[player_weapon_choose].do_damage()
        print(f"Zadales przeciwnikowi {damage} punkktow. obrazen\n")
        if enemy_Person.change_HP(damage) == True:
            still_fight = 1
        else:
            input("Wygrales walke! Brawo ty!")
            still_fight = 0
        return still_fight

    def can_u_shot(self,Person,weapon_range):
        if Person.ammunition[weapon_range.type_amunition] > 0:
            return True
        else:
            return False