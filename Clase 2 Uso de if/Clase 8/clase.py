
def load_file():
    filepath = input("Enter the path of the file to load: ")

    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    return lines

my_file = load_file()
print(my_file)