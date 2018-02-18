from msvcrt import getch

while 1:
    try:
        choice = getch().decode('utf-8')
        if choice == 'x':
            exit(1)
    except UnicodeDecodeError:
        print("Don't press on huynya, ok da")
        continue
