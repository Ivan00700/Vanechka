def main():
    ship_name = input()
    while ship_name != 'stop':
        with open('space.txt', encoding='utf-8') as file:
            data = file.readlines()
            ships = []
            for line in data[1:]:
                ships.append(line.strip().split('*'))

        flag = False
        for arr in ships:
            if ship_name == arr[0].split('-')[0]:
                flag = True
        if flag:
            print(f'Корабль <{arr[0].split("-")[0]}> был отправлен с планеты: <{arr[1]}> и его направление движения было: <{arr[3]}>')
        else:
            print('error.. er.. ror..')
        ship_name = input()

if __name__ == "__main__":
    main()
