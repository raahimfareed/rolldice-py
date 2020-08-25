from random import randint


def main():
    while True:
        decision = input("Roll a dice? Y/N: ").upper()

        if decision != "Y":
            break

        print(f"You rolled a dice.\nIt was a {randint(1, 6)}")

    print("Ended dice roll")


if __name__ == '__main__':
    main()
