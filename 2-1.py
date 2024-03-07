seat_number = int(input("Введите номер места: "))

if seat_number % 2 == 0:
    side = "боковое"
else:
    side = "коридорное"

if seat_number <= 36:
    place = "верхнее"
else:
    place = "нижнее"

print(f"Место {seat_number} - {place} место, {side}")
