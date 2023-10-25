# Jahnavi Tripathi encode()


def encode_password(password):
    enc_password = "" # empty string
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10  # digit will add 3 to the original digit
        enc_password += str(encoded_digit)  # the digit will become a string
    return enc_password

def decode(encoded_string):
    decoded_string = ""
    for i in range(0, len(encoded_string)):
        try:
            temp = int(encoded_string[i])
            if temp < 3:
                print("Invalid encoded string")
                decoded_string =""
                break
            decoded_string += str(temp-3)
        except:
            print("Invalid encoded string")
            decoded_string = ""
            break
    return decoded_string
encode_decode_menu = ("Menu\n"
                      "-------------\n"
                      "1. Encode\n"
                      "2. Decode\n"
                      "3. Quit")
print(encode_decode_menu)

if __name__ == '__main__':
    enc_password = ""
    no_exit = True
    while no_exit:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option_input = int(input("Please enter an option: "))
        # option 1 will encode password_to_decode
        if option_input == 1:
            password_to_decode = input("Please enter your password to encode: ")  # asks user for input to encode
            enc_password = encode_password(password_to_decode)  # stores value in variable to then decode
            print("Your password has been encoded and stored!")
        elif option_input == 2:
            # decode options
        elif option_input == 3:
            no_exit = False
