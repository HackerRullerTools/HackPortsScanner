#глобал: импорты библиотек
import os
os.system("cls")
os.system("clear")
print("Запуск HackPorts")
import socket, time #импорт os, socket и time

try: #импорт platform
    from platform import platform
except:
    #установка и импорт platform
    os.system("pip install platform")
    from platform import platform

try: #импорт art
    from art import *
except:
    #установка и импорт platform
    os.system('pip install art')
    from art import *

#глобал: переменные
text_title = text2art("Port   Scanner")
text_error = text2art("ERROR")
test = platform()[0:7]
if test == "Windows":
    clear = 'cls'
else:
    clear = 'clear'

#глобал: функции
def clear_console(): #очистка консоли
    os.system(clear)

def title(text): #вывод текста Port checked
    os.system(clear)
    print(text_title)
    print(f"{text}\n")

def error(text): #ошибка
    clear_console()
    print(text_error)
    input(f"Помощь: {text}.")

#глобал: запрос данных
title('Введите айпи на котором будет проводится проверка.\nПроверка своего устройства: "check me"!')
ip_adress = input("Введите айпи: ")
if ip_adress == "check me":
    ip_adress = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
while True:
    try:
        title('Введите порты через ":" которые будут проверятся.\nПример: 0:10.')
        port = input('Введите порты: '); port = port.replace(":", " ")
        port1 = int(port.split(" ")[0])
        port2 = int(port.split(" ")[1])
        if port1 <= port2:
            if port1 < 0 or port1 > 65535:
                error(f"Радиус портов: 0-65535")
            else:
                if port2 < 0 or port2 > 65535:
                    error(f"Радиус портов: 0-65535")
                else:
                    if port1 == port2:
                        error("Порты должны быть разными")
                    break
        else:
            error(f"Первый порт должен быть меньше второго порта!")
    except ValueError as err:
        error(f"Порт должен состоять из цифр.\nОшибка: {err}")
    except IndexError as err:
        error(f"Вы написали один порт вместо двух. Пример: 0:10.\nОшибка: {err}")
port3 = port1
title("Поиск портов..")
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = client.connect_ex((ip_adress, port3))
    if result == 0:
        print(f"Порт: {port3} открыт!")
    else:
        print(f"Порт: {port3} закрыт!")
    client.close()
    if port3 == port2:
        break
    port3 += 1
print("Закончено!")