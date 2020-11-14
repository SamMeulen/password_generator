import random


# method to generate a password
def generate_password(requested_size):
    characters_tuple = (
        "²", "&", "é", "(", "§", "è", "!", "ç", "à", ")", "-", "³", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        "°", "_", "|", "@", "#", "{", "[", "^", "{", "}", "a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "^", "$",
        "A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "¨", "*", "[", "]", "q", "s", "d", "f", "g", "h", "j", "k",
        "l", "m", "ù", "µ", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "%", "£", "ù", "µ", "<", "w", "x", "c",
        "v", "b", "n", ",", ";", ":", "=", ">", "W", "X", "C", "V", "B", "N", "?", ".", "/", "+", "~", "*")
    password = ""

    for x in range(requested_size):
        password = password + random.choice(characters_tuple)

    return password


# actual program
while True:
    try:
        requestedSize = int(input("Enter the size of your password: "))
        break
    except:
        print("Please enter a valid number instead.")

print(generate_password(requestedSize))
