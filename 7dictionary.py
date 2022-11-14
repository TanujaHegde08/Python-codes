word_dict = {}

def create_dict():
    global word_dict
    word_dict = {}
    ch = "y"
    while (ch == "y") or (ch == "Y"):
        print("\nEnter word:")
        word = input()
        print("\nEnter meaning:")
        meaning = input()
        word_dict[word] = meaning
        print("\nDo you want to continue adding words(y or n):")
        ch = input()

def add_word():
    global word_dict
    print("\nEnter word:")
    word = input()
    print("\nEnter meaning:")
    meaning = input()
    word_dict[word] = meaning

def find_meaning(w):
    return word_dict[w]

def find_word_same_meaning(mng):
    words = []
    for w, m in word_dict.items():
        if mng == m:
            words.append(w)
    return words

def display_sorted():
    for w, m in word_dict.items():
        print(f"{w} ==> {m}")
    print("Sorted list of words : ")
    print(sorted(word_dict.keys()))

def main():
    ch = "y"
    while ch == "Y" or ch == "y":
        print("1: Create new dictionary")
        print("2: Add new word")
        print("3: Find meaning")
        print("4: Find word with same meaning")
        print("5: Display sorted list of words")
        print("6: Quit")
        print("Enter Choice: ")
        option = int(input())
        if option == 1:
            create_dict()
        elif option == 2:
            add_word()
        elif option == 3:
            print("Enter word:")
            word = input()
            print("Meaning:%s" % (find_meaning(word)))
        elif option == 4:
            print("Enter meaning:")
            meaning = input()
            print("Words with same meaning:")
            print(find_word_same_meaning(meaning))
        elif option == 5:
            display_sorted()
        elif option == 6:
            exit()
            
        print("\nDo you want to continue(y or n)?")
        ch = input()

if __name__ == "__main__":
    main()
