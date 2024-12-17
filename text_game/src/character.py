import json
import os

from . tools import Tools
from typing import Dict, List


class Character:
    def __init__(self, name: str = None, data: Dict[str, int] = None) -> None:
        self.PATH_TO_FOLDER: str = __file__[:-16] + "loads"
        print(self.PATH_TO_FOLDER)
        input()
        if name != None:
            print("niggers")
            self.name = name
            self.damage = 15.0
            self.health = 100.0
            self.coins = 10

            self.__save_new_character()
        else:
            self.name = data['name']
            self.damage = data['damage']
            self.health = data['health']
            self.coins = data['coins']
        

    def show_stats(self) -> None:
        '''Выводит статистику персонажа'''
        Tools.cls()

        str_arr: List[str] = list(map(str, [self.name, self.damage, self.health, self.coins]))
        len_arr: List[int] = [len(el) for el in str_arr]
        mx_len: int = max(len_arr)+10

        print("+"+"-"*(mx_len+2)+"+")
        print(f"| имя:      {self.name}"+" "*(mx_len-10-len_arr[0])+" |")
        print(f"| урон:     {self.damage}"+" "*(mx_len-10-len_arr[1])+" |")
        print(f"| здоровье: {self.health}"+" "*(mx_len-10-len_arr[2])+" |")
        print(f"| монеты:   {self.coins}"+" "*(mx_len-10-len_arr[3])+" |")
        print("+"+"-"*(mx_len+2)+"+")


    def __save_new_character(self) -> None:
        '''Сохраняет нового персонажа в файле .json'''
        data: Dict[str, float] = {
            "name": self.name,
            "coins": self.coins,
            "health": self.health,
            "damage": self.damage
        }
        
        try:
            with open(os.path.join(self.PATH_TO_FOLDER, self.name)+".json", 'w') as file:
                json.dump(data, file)
        except:
            print("Error: ошибка записи файла при создании нового персонажа\n")

    
    def get_data(self) -> Dict[str, float]:
        return {
            'name': self.name,
            'coins': self.coins,
            'health': self.health,
            'damage': self.damage
        }