def count_words(text):
    return len(text.lower().split())

def main():
    with open("sample.txt" , "r" , encoding="utf-8") as f:
        text = f.read()
    print("Word count:" , count_words(text))

if __name__ == "__main__":
    main()