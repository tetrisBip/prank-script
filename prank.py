import time
import os
import webbrowser
import subprocess 

def dramatic_countdown():
    print("=" * 50)
    print(" ПОДКЛЮЧЕНИЕ К СЕРВЕРАМ СБЕРБАНКА... УСПЕШНО.")
    print(" Инициализация взлома баланса...")
    print("=" * 50)
    print("\n[ВНИМАНИЕ] Не закрывайте окно до окончания процесса!")
    time.sleep(2)
    
    # Драматичный отсчет
    for i in range(10, 0, -1):
        print(f"Запуск через: {i}...")
        time.sleep(1)
        
    print("\n[ СТАРТ ] ПОЕХАЛИ!\n")
    time.sleep(0.5)

def launch_rickroll():
    # Ссылка на официальный клип Rick Astley
    url = "https://youtu.be/dQw4w9WgXcQ?si=mMRrTHq9TUXeyzmw"
    
    # Открываем 20 вкладок
    for _ in range(20):
        webbrowser.open_new_tab(url)
        time.sleep(0.01) # Небольшая задержка, чтобы браузер успевал обрабатывать запросы

if __name__ == "__main__":
    if os.name == 'nt':
        subprocess.run("title Sberbank Cheat v1.4.88", shell=True)
        
    dramatic_countdown()
    launch_rickroll()