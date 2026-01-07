def main():
    with open("results.txt", "w", encoding="utf-8") as f:
        for number in range(2, 251):
            flag = True

            for div in range(2, number):
                if number % div == 0:
                    flag = False
                    break

            if flag:
                f.write(str(number) + "\n")

if __name__ == "__main__":
    main()