
confere = False

while True:
    entrada = input("\nAdicione uma cadeia qualquer de 0 e 1:\n")
    q0 = ""

    for caracter in entrada:

        if ((caracter == "0") or (caracter == "1")):
            print(f"O caracter ({caracter}) Ta dentro dos termo")
            confere = True

        else:
            print(f"O caracter ({caracter}) não está de acordo")

    if confere == True:
        q0 = (entrada[-1]) + q0

        if q0 == "1":
            print("\nSUCESSO: Terminou em 1")

        else :
            print("\nFRACASSO: Terminou em 0")
    