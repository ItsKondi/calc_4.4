import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("""Podaj działanie, posługując się odpowiednią liczbą:
1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:""")
operation = int(input())

if operation not in [1,2,3,4]:
    logging.info("Nie ma takiego działania!!!!")




if operation == 1:
    how_many = int(input("Ile liczb chcesz dodać? "))
    nr_list = []
    for i in range(1, how_many+1):
        nr = float(input(f"Podaj {i}. liczbę: "))
        nr_list.append(nr)
    logging.info(f"Możę liczby {nr_list}")
    suma = sum(nr_list)
    print(f"Wynik to: {suma:.2f}")

elif operation == 2:
    first_no = float(input("Podaj liczbę 1.: "))
    second_no = float(input("Podaj liczbę 2.: "))
    logging.info(f"Odejmuję {second_no:.2f} od {first_no:.2f}")
    suma = first_no - second_no
    print(f"Wynik to: {suma:.2f}")

elif operation == 3:
    how_many = int(input("Ile liczb chcesz mnożyć? "))
    nr_list = []
    for i in range(1, how_many+1):
        nr = float(input(f"Podaj {i}. liczbę: "))
        nr_list.append(nr)

    logging.info(f"Możę liczby {nr_list}")
    suma = 1
    for j in nr_list:
        suma *= j
    print(f"Wynik to: {suma:.2f}")

elif operation == 4:
    first_no = float(input("Podaj liczbę 1.: "))
    second_no = float(input("Podaj liczbę 2.: "))
    if second_no == 0:
        logging.warning("Dzielenie przez zero!")
        print("Nie można dzielić przez zero. Spróbuj ponownie.")
        exit(1)
    logging.info(f"Dzielę {first_no:.2f} przez {second_no:.2f}")
    suma = first_no / second_no
    print(f"Wynik to: {suma:.2f}")


