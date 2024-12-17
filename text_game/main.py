from src.game import Game


def main() -> None:
    game: Game = Game()
    is_flow: bool = True

    while is_flow:
        game.show_menu()
        choice: str = input(">>> ").strip()

        match choice:
            case "1": game.new_game()
            case "2": game.load_game()
            case "3": game.delete_game()
            #case "4": game.show_events()  # не доделано
            case _: is_flow = False

    print("Игра завершена!")


if __name__ == '__main__':
    main()