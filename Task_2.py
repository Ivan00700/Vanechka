def main():
    with open('space.txt', encoding='utf-8') as file:
        """
            считывание файла space.txt
        """
        data = file.readlines()
        ships = []
        """
            добавление данных в массив массивов
        """
        for line in data[1:]:
            ships.append(line.strip().split('*'))
            """
                Сортировка по возрастанию массива ships
            """
        for i in range(len(ships)):
            for j in range(len(ships) - i - 1):
                if int(ships[j][0].split('-')[1]) > int(ships[j + 1][0].split('-')[1]):
                    ships[j], ships[j + 1] = ships[j + 1], ships[j]
        """
        вывод итоговых первых десяти значений отсортированного массива
        """
        for i in range(10):
            print(ships[i][0].split('-')[0])


if __name__ == "__main__":
    main()
