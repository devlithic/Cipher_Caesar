Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
def encode (message_e,shift_number):
    message_final = message_e.lower()
    liste = []
    index_encode1 = 0
    for char in message_final:
        if char == " " :
            liste.append(" ")
            continue
        if  char =="'":
            liste.append("'")
            continue
        index = Alphabet.index(char)
        index_encode1 = index + shift_number
        if index_encode1 < 25:
            liste.append(Alphabet[index_encode1])

        elif index_encode1 >= 25:
            index_encode2 = 26 - shift_number
            index_encode_plus_25 = Alphabet.index(char) - index_encode2
            liste.append(Alphabet[index_encode_plus_25])

    message_encode = ""
    for chare in liste:
        message_encode += chare

    print(message_encode)


def decode(message_d,shift_number_decode):
    message_final = message_d.lower()
    liste = []
    index_decode1 = 0
    for char in message_final:

        if char == " ":
            liste.append(" ")
            continue
        if char =="'":
            liste.append("'")
            continue
        inndex_decode1 = Alphabet.index(char) - shift_number_decode
        liste.append(Alphabet[inndex_decode1])

    message_decode = ""
    for chare in liste:
        message_decode += chare

    print(message_decode)




user_continue = ""

while True:
    choix = input("Entrer votre choix soit 1 pour encode ou 2 pour décoder :  ")
    if choix == "1":
        message_encode= input("Type your message: ")
        shift_number = int(input("Type the shift number: "))
        encode (message_encode,shift_number)

    elif choix == "2":
        message_decode= input("Type your message: ")
        shift_number_decode= int(input("Type the shift number: "))
        decode(message_decode,shift_number_decode)

    user_continue = input("Do you want to continue? (yes/no) : ")
    if user_continue== "yes":
        continue
    elif user_continue == "no":
        break

print("The program has finished.")