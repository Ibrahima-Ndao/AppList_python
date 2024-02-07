# This is a sample Python script.
from List import List


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    L1 = List()
    while True:
        print()
        print('1.Add a list at the end')
        print('2.Add a list at the beginning')
        print('3.Retrieve a list')
        print('4.Delete a kay in the list')
        print('5.insert an item after the key')
        print('6.sort')
        choice = int(input('Your choice: '))
        if choice == 1:
            x = int(input('Enter a number:'))
            L1.addend(x)
        elif choice == 2:
            x = int(input('enter another number:'))
            L1.addstart(x)
        elif choice == 3:
            L1.parcours()
        elif choice == 4:
            x = int(input('enter another number:'))
            L1.delete(x)
        elif choice == 5:
            x = int(input('enter another number:'))
            value = int(input('enter another number:'))
            L1.addafterkey(x, value)
        elif choice == 6:
            break
        else:
            print('invalid choice')
    print('At the end of the application')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
