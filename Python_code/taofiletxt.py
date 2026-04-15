lst = [
    "Ca dao",
    "Cá không ăn muối cá ương",
    "Con cãi cha mẹ",
    "Trăm đường con hư"
]

with open("cadao.txt", "w", encoding="utf-8") as f:
    for cau in lst:
        f.write(cau + "\n")

print("Da ghi noi dung vao file cadao.txt")
