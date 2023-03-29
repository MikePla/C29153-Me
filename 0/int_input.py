def input_int(message):
    while True:
        try:
            result = float(input(message))
            print('Error not found')
        except:
            print('Error found')
        else:
            return result


a = input_int('a=')
b = input_int('b=')
