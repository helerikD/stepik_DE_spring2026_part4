# Вычисление пройденного судном пути: расстояние (нм) = скорость (уз) * время (ч).
while True:
    s = input("Введите скорость в узлах").strip()
    if s == "":
        break
    t = input("Введите время в часах: ").strip()
    try:
        speed = float(s)
        time = float(t)
        if speed < 0 or time < 0:
            print("Не может быть отрицательным числом")
            continue
    except ValueError:
        print("Неверный ввод. Введите число")
        continue
    distance = speed * time
    print(f"Пройденное расстояние: {distance:.2f} нм\n")