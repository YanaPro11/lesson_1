proceed=int(input("Введи продолжительность"))
outlay=int(input("Введите затраты:"))
if proceed > outlay:
    profitability= proceed- outlay
    rent=profitability/proceed
    print(f"Молодцом. Вот ваша {profitability}доходность")
    worker=int(input("Сколько человек работает:"))
    print(f"{profitability/worker} на одного работника такая доходность")
elif proceed==outlay:
    print("Неплохо")
else:
    print("Удачи")