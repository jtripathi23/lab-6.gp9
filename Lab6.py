def decode(encoded_string):
    decoded_string = ""
    for i in range(0, len(encoded_string)):
        try:
            temp = int(encoded_string[i])
            if temp < 3:
                decoded_string =""
                break
            decoded_string += str(temp-3)
        except:
            decoded_string = ""
            break
    return decoded_string
#encode_decode_menu = ("Menu\n"
#                      "-------------\n"
#                      "1. Encode\n"
#                      "2. Decode\n"
#                      "3. Quit")
#print(encode_decode_menu)