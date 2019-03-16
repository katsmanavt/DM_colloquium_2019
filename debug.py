from modules.classes import *
from modules.N import *


def input_Natural(message):  
    n = Natural()
    n.pop()
    string = input(message)
    for c in string:
        n.append(int(c))
        n.n += 1
    n.reverse()
    n.n -= 1
    return n
    
    
def print_Natural(n):
    num = n.copy()
    num.reverse()
    for i in range(num.n+1):
        print(num[i], end='')
    print()


def test_N_1():
    n1 = input_Natural("Введите первое число: ")
    n2 = input_Natural("Введите второе число: ")
    print("Результат: ")
    print(COM_NN_D(n1, n2))
    
    
def test_N_2():
    print(NZER_N_B(input_Natural("Введите число: ")))
    
    
def test_N_3():
    n = input_Natural("Введите число: ")
    n = ADD_1N_N(n)
    print_Natural(n)
    

def test_N_4():
    n1 = input_Natural("Введите первое число: ")
    n2 = input_Natural("Введите второе число: ")
    print("Сумма:")
    print_Natural(ADD_NN_N(n1, n2))


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки!")
        print("Команды:")
        print("1 - тест модуля N-1")
        print("2 = тест модуля N-2")
        print("3 = тест модуля N-3")
        print("4 = тест модуля N-4")
        print("\n0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            test_N_1()
        elif menu == 2:
            test_N_2()
        elif menu == 3:
            test_N_3()
        elif menu == 4:
            test_N_4()
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод")
        input("\nНажмите enter для продолжения...")
    

if __name__ == "__main__":
    main()
    