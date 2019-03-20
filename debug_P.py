from modules.classes import *
from modules.P import *
from debug_N import *
from debug_Z import *
from debug_Q import *


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки модулей P!")
        print("Команды:")
        print("1 - тест модуля P-1")
        print("2 - тест модуля P-2")
        print("3 - тест модуля P-3")
        print("4 - тест модуля P-4")
        print("5 - тест модуля P-5")
        print("6 - тест модуля P-6")
        print("7 - тест модуля P-7")
        print("8 - тест модуля P-8")
        print("9 - тест модуля P-9")
        print("10 - тест модуля P-10")
        print("11 - тест модуля P-11")
        print("12 - тест модуля P-12")
        print("13 - тест модуля P-13")
        print("\n0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            test_P_1()
        elif menu == 2:
            test_P_2()
        elif menu == 3:
            test_P_3()
        elif menu == 4:
            test_P_4()
        elif menu == 5:
            test_P_5()
        elif menu == 6:
            test_P_6()
        elif menu == 7:
            test_P_7()
        elif menu == 8:
            test_P_8()
        elif menu == 9:
            test_P_9()
        elif menu == 10:
            test_P_10()
        elif menu == 11:
            test_P_11()
        elif menu == 12:
            test_P_12()
        elif menu == 13:
            test_P_13()
        
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод")
        input("\nНажмите enter для продолжения...")
    

if __name__ == "__main__":
    main()