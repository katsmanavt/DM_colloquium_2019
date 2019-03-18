import debug_N, debug_Z


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки!")
        print("Команды:")
        print("1 - тест модулей N")
        print("2 - тест модулей Z")
        print("0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            debug_N.main()
        elif menu == 2:
            debug_Z.main()
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод!")
    
    
if __name__ == "__main__":
    main()
        
