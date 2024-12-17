import os
import json
import random

from src.tools import Tools
from src.character import Character
from src.events import Events
from typing import (
    List,
    Tuple,
    Dict
)


class Game:
    def __init__(self) -> None:
        self.menu: Tuple[str] = (
            "Начать игру",
            "Загрузить игру",
            "Удалить игру",
            "Список событий",
            "Выход"
        )
        self.FOLDER_PATH: str = __file__[:-11] + "loads"
        self.FILES: List[str] = os.listdir(self.FOLDER_PATH)

        self.events: Events = Events()


    def show_menu(self) -> None:
        '''Выводит главное меню в упорядоченном виде в консоль'''
        #Tools.cls()

        for i, el in enumerate(self.menu):
            print(f"[{i+1}] - {el}")
        print()

    
    def __create_new_character(self) -> None:
        '''Создание нового персонажа'''
        Tools.cls()
        name: str = input("имя: ").strip()
        self.character = Character(name)

    
    def show_events(self) -> None:
        '''Выводит список всех событий в игре'''
        self.events.show_events()


    def load_character_data(self, name: str) -> None:
        '''Достает данные из json файла нужного перса и сохраняет их'''

        try:
            path: str = os.path.join(self.FOLDER_PATH, name) + '.json'  # Путь до файла 
            with open(path, 'r') as file:
                data: Dict[str, float] = json.load(file)
        except: 
            Tools.cls()
            print("Error - ошибка при попытке загрузке данных из json - game.py : load_character_data\n")
        else:
            self.character.name = data['name']
            self.character.coins = data['coins']
            self.character.damage = data['damage']
            self.character.health = data['health']


    def __random_event(self) -> bool:
        '''Вызывает событие генерируя его порядковый номер случайным образом'''

        event_n: int = random.randint(0, self.events.get_event_count()-1)  # Номер случайного ивента

        # Вызов ивента по его порядковому номеру с передачей экземпляра класса персонажа
        return self.events.require_event_by_number(event_n, self.character)
    

    def new_game(self, data: Dict[str, float] = None) -> None:
        '''Создает нового персонажа и загружает игру'''

        # Получение экземпляра класса Character
        if data == None: self.__create_new_character()
        else: self.character: Character = Character(data=data)
        
        
        is_flow: bool = True
        while is_flow:
            # Вывод статистики персонажа
            # self.character.show_stats()
            
            # запуск случайного события
            is_game_over: bool = self.__random_event() 

            # выгрузка данных персонажа в экземпляр класса из json файла
            self.load_character_data(self.character.name)
            input()
            
            if is_game_over: 
                is_flow = False

                # Удаление персонажа в случае проигрыша
                path_to_delete: str = os.path.join(self.FOLDER_PATH, self.character.name) + ".json"
                os.remove(path_to_delete)
                break
        

    def delete_game(self) -> None:
        '''Выводит список персонажей и исходя из выбора игрока удаляет одного из них'''

        self.__show_games()

        if len(self.FILES) > 0:
            choice: str = input("введите имя персонажа для удаления >>> ").strip() + ".json"
            if choice in self.FILES:
                Tools.cls()
                try:
                    path_to_delete: str = os.path.join(self.FOLDER_PATH, choice)
                    os.remove(path_to_delete)
                except: print("Error - ошибка удаления персонажа - game.py : delete_game")
                else: 
                    print("Персонаж успешно удален!\n")
                    self.FILES: List[str] = os.listdir(self.FOLDER_PATH)
            else: Tools.cls()


    def load_game(self) -> None:
        '''Выводит список персонажей и исходя из выбора игрока загружает одну из игр'''

        self.__show_games()
        
        if len(self.FILES) > 0:
            choice: str = input("введите имя персонажа >>> ").strip() + ".json"
            if choice in self.FILES:
                Tools.cls()
                try:
                    with open(os.path.join(self.FOLDER_PATH, choice), 'r') as file:
                        data: Dict[str, float] = json.load(file)
                        self.new_game(data)
                except: print("Error - ошибка загрузки персонажа - game.py : load_game")
                else: self.FILES: List[str] = os.listdir(self.FOLDER_PATH)
            else: Tools.cls()
                    

    def __show_games(self) -> None:
        '''Выводит список персонажей'''
        if os.path.exists(self.FOLDER_PATH):

            Tools.cls()
            if len(self.FILES) > 0:
                for i, el in enumerate(self.FILES):
                    print(f'[{i+1}] - {el[:-5]}')
                print()
            else:
                print("У вас нету сохраненных игр...\n")
        