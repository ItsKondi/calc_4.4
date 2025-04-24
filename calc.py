import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("""Podaj działanie, posługując się odpowiednią liczbą:
1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:""")
operation = int(input())
if operation > 4:
    logging.info("Nie ma takiego działania")
first_no = input("Podaj liczbę 1.: ")
second_no = input("Podaj liczbę 2.: ")
if operation == 1:
    logging.info(f"Dodaję {first_no} i {second_no}")
    sum = first_no + second_no
    print(f"Wynik to: {sum}")
elif operation == 2:
    logging.info(f"Odejmuję {second_no} od {first_no}")
    sum = first_no - second_no
    print(f"Wynik to: {sum}")
elif operation == 3:
    logging.info(f"Możę {first_no} i {second_no}")
    sum = first_no * second_no
    print(f"Wynik to: {sum}")
elif operation == 4:
    logging.info(f"Dzielę {first_no} przez {second_no}")
    sum = first_no / second_no
    print(f"Wynik to: {sum}")

