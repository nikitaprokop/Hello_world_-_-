donor_blood = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

print(f"\nДонор: {donor_blood}, Пациент: {recipient_blood}")
print("-" * 30)

if donor_blood == recipient_blood:
    print("✅ Переливание возможно: группы крови совпадают.")
elif donor_blood == "I":
    print("✅ Переливание возможно: донор с группой I (0) — универсальный донор.")
else:
    print("❌ Переливание НЕВОЗМОЖНО: группы несовместимы.")

print("\nПримечание: Группа I (0) является универсальной для донорства.")
