def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"

    score = 0
    for letter in letters:
        score += combined_names.count(letter)

    return score % 101

def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter your name: ")
    name2 = input("Enter your crush's name: ")

    love_score = calculate_love_score(name1, name2)
    print(f"Your love score is: {love_score}%")

if __name__ == "__main__":
    main()