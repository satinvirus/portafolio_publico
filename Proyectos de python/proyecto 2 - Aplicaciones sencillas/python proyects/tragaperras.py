import random
import time

def tragaperras():
    simbolos = ["7",":D","D:","PTM"]
    input("\nPresiona Enter")
    resultado = []

    for x in range(3):
        rueda = random.choice(simbolos)
        resultado.append(rueda)
        print(f"{rueda}", end=" ", flush = True)
        time.sleep(.5)

    if resultado[0] == resultado[1] == resultado[2]:
        print("\n!jackpot!")

while True:
    tragaperras()