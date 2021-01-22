def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]

    for char in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if char >= value:
                result += letter
                char -= value
            else:
                result += '-'

    return result