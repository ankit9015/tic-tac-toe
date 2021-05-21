# tic-tac-toe
def print_table(_table):
    print('-' * 9)
    for r in range(3):
        print(f"| {' '.join(_table[r])} |")
    print('-' * 9)


def check(_table):
    if _table[0][0] == _table[1][1] and _table[1][1] == _table[2][2]:
        if _table[0][0] != '_':
            print(f"{_table[0][0]} wins")
            return 1
    if _table[0][2] == _table[1][1] and _table[1][1] == _table[2][0]:
        if _table[0][2] != '_':
            print(f"{_table[0][2]} wins")
            return 1
    for i in range(3):
        if _table[i][0] == _table[i][1] and _table[i][1] == _table[i][2]:
            if _table[i][0] != '_':
                print(f"{_table[i][0]} wins")
                return 1
        if _table[0][i] == _table[1][i] and _table[1][i] == _table[2][i]:
            if _table[0][i] != '_':
                print(f"{_table[0][i]} wins")
                return 1
    return 0


def main():
    table = [['_' for _ in range(3)] for _ in range(3)]
    print_table(table)
    while True:
        x, y = input("Enter the coordinates:").split()
        try:
            x, y = int(x), int(y)
        except TypeError:
            print("You should enter numbers!")
        finally:
            if x not in range(1, 4) or y not in range(1, 4):
                print("Coordinates should be from 1 to 3!")
            elif table[x - 1][y - 1] != '_':
                print("This cell is occupied! Choose another one!")
            else:
                table[x - 1][y - 1] = 'X'
                print_table(table)
                if check(table) == 1:
                    break


if __name__ == '__main__':
    main()
