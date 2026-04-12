# Вычисление пройденного судном пути: расстояние (нм) = скорость (уз) * время (ч).
while True: #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    s = input("Введите скорость в узлах или нажмите Enter для выхода:\n").strip() #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    if s == "": #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        break #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    t = input("Введите время в часах:\n").strip() #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    try: #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        speed = float(s) #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        time = float(t) #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        if speed < 0 or time < 0: #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
            print("Не может быть отрицательным числом") #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
            continue #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    except ValueError: #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        print("Неверный ввод. Введите число") #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
        continue #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    distance = speed * time #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c
    print(f"Пройденное расстояние: {distance:.2f} нм\n") #some comment b05c8f24-ea89-4c03-bcfc-be0ed16d8b3c