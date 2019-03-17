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
    

def test_N_5():
    n1 = input_Natural("Введите первое число: ")
    n2 = input_Natural("Введите второе число: ")
    print("Разность:")
    print_Natural(SUB_NN_N(n1, n2))
    

def test_N_6():
    n = input_Natural("Введите число: ")
    d = int(input("Введите цифру: "))
    print("Произведение:")
    print_Natural(MUL_ND_N(n, d))
    

def test_N_7():
    n = input_Natural("Введите число: ")
    k = int(input("Введите k: "))
    print("Число, умноженное на 10^k:")
    print_Natural(MUL_Nk_N(n, k))


def test_N_8():
    n1 = input_Natural("Введите первое число: ")
    n2 = input_Natural("Введите второе число: ")
    print("Произведение:")
    print_Natural(MUL_NN_N(n1, n2))
    

def test_N_9():
    n1 = input_Natural("Введите первое число: ")
    n2 = input_Natural("Введите второе число: ")
    d = int(input("Введите цифру: "))
    print("Результат:")
    print_Natural(SUB_NDN_N(n1, n2, d))


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки!")
        print("Команды:")
        print("1 - тест модуля N-1")
        print("2 = тест модуля N-2")
        print("3 = тест модуля N-3")
        print("4 = тест модуля N-4")
        print("5 = тест модуля N-5")
        print("6 = тест модуля N-6")
        print("7 = тест модуля N-7")
        print("8 = тест модуля N-8")
        print("9 = тест модуля N-9")
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
        elif menu == 5:
            test_N_5()
        elif menu == 6:
            test_N_6()
        elif menu == 7:
            test_N_7()
        elif menu == 8:
            test_N_8()
        elif menu == 9:
            test_N_9()
        
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод")
        input("\nНажмите enter для продолжения...")
    

if __name__ == "__main__":
    main()
    