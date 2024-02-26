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
        space_new_ships = []

        for arr in ships:
            """
            обозначение переменных для последующих удобных преобразований
            """
            n = int(arr[0].split('-')[1][0])
            m = int(arr[0].split('-')[1][1])
            t = len(arr[1])
            x_d, y_d = int(arr[3].split()[0]), int(arr[3].split()[1])
            x, y = int(arr[2].split()[0]), int(arr[2].split()[1])
            x_new, y_new = 0, 0

            """
            преобразования по тз из задачи
            """
            if n > 5:
                x_new = n + x_d
            elif n <= 5:
                x_new = -4 * (x_d + n) + t
            if m > 3:
                y_new = m + t + y_d
            elif m <= 3:
                y_new = -m * (n + y_d)
            space_new_ships.append('<' + arr[0] + '> - (<' + str(x_new) + '>, ' + str(y_new) + '>)')

            """
            добавление ответов в новый файл для вывода
            """
    with open('space_new.txt', 'w', encoding='utf-16') as file_w:
        file_w.writelines(space_new_ships)


if __name__ == "__main__":
    main()
