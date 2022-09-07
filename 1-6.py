proceeds=float(input("Введите выручку фирмы:"))
costs=float(input("Введите издержки фирмы:"))
if proceeds > costs:
    print("Фирма работает с прибылью")
income=proceeds-costs
print("Рентабельность фирмы {:%}".format(income/proceeds))
employees=int(input("Введите пожалуйста количество сотрудников фирмы:"))
print(f"Доходность фирмы на сотрудника составляет {income/employees}y.e.")
#else:
#print("Фирма работает без окупаемости")