def main():
    with open('input.txt', 'r') as file:
        search_word = input('Enter the search word: ')
        lines = file.readlines()
        for line in lines:
            if line.find(search_word) == -1:
                continue
            print(line.strip())

if __name__ == "__main__":
    main()