впрпname = input("👋 Как вас зовут? ")


current_year = 2026
course_year = 1

print("\n" + "=" * 50)
print("🌟" * 10 + " ПРИВЕТСТВИЕ " + "🌟" * 10)
print("=" * 50)

print("Привет", end="")
print(", ", end="")
print(name, end="")
print("!", end="\n\n")

print("📅 Сегодня:", current_year, "год", sep=" ")

print("\n" + "─" * 45)

print("🎓", "ГОД", "ОБУЧЕНИЯ", sep=" ⚡ ", end=" 🎯\n")
print("─" * 45)

print("║", " " * 15, "║")
print("║", f"   {course_year}-Й КУРС   ", "║", sep="")
print("║", " " * 15, "║")

print("\n" + "▰" * 20)
print("СТАТУС:", "АКТИВЕН", sep=" ✦ ", end=" ✅\n")
print("▰" * 20)

print("\n" + "★" * 40)
print("✨ ИНТЕРЕСНЫЕ ФАКТЫ ✨".center(40))
print("★" * 40)

print("\n📌 Ваши данные:")
print("Имя:", name, "•", "Курс:", course_year, "•", "Год:", current_year, sep=" ", end="\n\n")

print("📊 Прогресс обучения:", end=" ")
for i in range(10):
    print("█", end="")
print(" 100%")

print("\n" + "╔" + "═" * 30 + "╗")
print("║" + "🎉 УДАЧИ В УЧЕБЕ! 🎉".center(30) + "║")
print("╚" + "═" * 30 + "╝")

print("\n🐍", "Python", "💻", "ROCKS", "🚀", sep=" ✦ ", end=" !!!\n")
print("~" * 40)

