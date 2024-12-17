import random
import os
import json

from src.tools import Tools
from src.character import Character
from typing import Dict, List, Tuple, Any

 
class Events:
    def __init__(self) -> None:
        self.__MAIN_FOLDER_PATH: str = __file__[:-7]
        self.__LOADS_PATH: str = os.path.join(self.__MAIN_FOLDER_PATH, "loads")

        self.events: Dict[Any] = (
            self.meet_nigger,
            self.meet_nigger,
            self.meet_nigger
        )
    

    def __save_data(self, data: Dict[str, float]) -> None:
        '''Сохранение новых параметров игрока'''
        path_to_save: str = os.path.join(self.__LOADS_PATH, data['name']) + ".json"

        try:
            with open(path_to_save, 'w') as file:
                json.dump(data, file)
        except: print("Error - ошибка сохранения данных из события Events")
        else: print("log: Данные обновлены успешны!\n")

    
    def show_events(self) -> None:
        Tools.cls()
        if len(self.events) > 0:
            for i, el in enumerate(self.events):
                print(f"{i+1}. - {el[:-5]}")
            print()


    def get_event_count(self) -> int:
        return len(self.events)
    

    def require_event_by_number(self, n: int, character: Character) -> bool:
        self.character = character
        self.events[n]()
        return True if self.character.health <= 0 else False
    


    # Тут Начинаются ивенты, но меня уже тошнит от этого проекта...

    def meet_nigger(self) -> None:
        print("Вы повстречали негра!\n")
        self.character.coins -= 10
        print("Негр отжал у вас 10 монеток. Вы расстроены")
        self.character.health -= 3.0
        print("Негр пнул вас, у вас апатия...\n")

        self.character.show_stats()
        
        self.__save_data(self.character.get_data())


