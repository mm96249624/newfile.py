def prompt_and_write(filename):
    file = open(filename, "w")
    while True:
        line = input("Enter text: ")
        if line != "":
            file.write(line+"\n")
        else:
            file.close()
            break

prompt_and_write(input("Enter file name: "))