try:
    with open("file1.txt", "w", encoding="utf-8") as file_1:
        line = input('Напишите что-нибудь: \n')
        while True:
            if KeyboardInterrupt:
                break
        file_1.writelines(line)
        print(line)
except IOError as err:
    print(err)
