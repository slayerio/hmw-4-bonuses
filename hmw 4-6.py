while True:
    b = input("give me a word");
    c = input("give me another word");
    if b == c:
        break
    else:
        print(f"{b} {c}")



print("you broke the loop \nthanks for playing!")



word: str = ""
total: str = ""
while True:
    a = input("give me a word");
    total = total + " " + a + " "
    if a == word:
        break
    else:
        word = a
print(f"{total}")



print("you broke the loop \nthanks for playing!")