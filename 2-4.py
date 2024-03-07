primary_colors = ["красный", "синий", "желтый"]
mixing_map = {
    ("красный", "синий"): "фиолетовый",
    ("красный", "желтый"): "оранжевый",
    ("синий", "желтый"): "зеленый"
}

color1 = input("Введите первый основной цвет: ").lower()
color2 = input("Введите второй основной цвет: ").lower()

if color1 in primary_colors and color2 in primary_colors:
    if (color1, color2) in mixing_map:
        print("Результат смешивания:", mixing_map[(color1, color2)])
    else:
        print("Результат смешивания:", mixing_map[(color2, color1)])
else:
    print("Ошибка: введены неверные цвета.")
