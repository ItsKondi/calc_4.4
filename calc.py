import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("""Podaj działanie, posługując się odpowiednią liczbą:
1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:""")
operation = int(input())
if operation > 4:
    logging.info("Nie ma takiego działania")
first_no = float(input("Podaj liczbę 1.: "))
second_no = float(input("Podaj liczbę 2.: "))

if operation == 1:
    logging.info(f"Dodaję {first_no:.2f} i {second_no:.2f}")
    sum = first_no + second_no
    print(f"Wynik to: {sum:.2f}")

elif operation == 2:
    logging.info(f"Odejmuję {second_no:.2f} od {first_no:.2f}")
    sum = first_no - second_no
    print(f"Wynik to: {sum:.2f}")

elif operation == 3:
    logging.info(f"Możę {first_no:.2f} i {second_no:.2f}")
    sum = first_no * second_no
    print(f"Wynik to: {sum:.2f}")

elif operation == 4:
    logging.info(f"Dzielę {first_no:.2f} przez {second_no:.2f}")
    sum = first_no / second_no
    print(f"Wynik to: {sum:.2f}")


