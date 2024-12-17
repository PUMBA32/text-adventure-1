import os
import sys
import time

from typing import List


class Tools:
    @staticmethod
    def cls() -> None:
        os.system("cls" if sys.platform == 'win32' else "clear")


    @staticmethod
    def show_text(text: str) -> None:
        words: List[str] = text.split(" ")
        for word in words:
            print(word, end=' ', flush=True)
            time.sleep(0.1)
            
