import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="D:\Konrad\Desktop\codding\kodilla\4_dzial\calc_4.4\logfile.log")

logging.info("""\nPodaj działanie, posługując się odpowiednią liczbą:
1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:""")
operation = logging.info(input())
