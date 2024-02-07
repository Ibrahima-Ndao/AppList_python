from Egt import Egt
class List:
    def __init__(self):
        self.head = None

    def parcours(self):
        if self.head == None:
            print("__________________________________________________________________")
            print('                     Empty List')
            print("__________________________________________________________________")
        else:
            p = self.head
            while not p == None:
                print(" ",p.info , end=" ")
                p = p.next

    def addend(self, x):
        new = Egt(x)
        if self.head == None:
            self.head == new
        else:
            p = self.head
            while not p.next == None:
                p = p.next
            p.next = new

    def addstart(self, x):
        new = Egt(x)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def delete(self, x):
        find = False
        previous = None
        p = self.head
        if p == None:
            print("impossible to delete an empty list")
        else:
            while not p == None and find == False:
                if not p.info == x:
                    previous = p
                    p = p.next
                else:
                    find = True
            if find == True:
                if p == self.head:
                    self.head = p.next
                    p = None
                elif p.next == None:
                    previous.next = None
                    p = None
                else:
                    previous.next = p.next
                    p = None
            else:
                print(x, "is not in the list")

    def addafterkey(self, x, value):
        if self.head == None:
            print('impossible to add an empty list')
        else:
            p = self.head
            find = False
            while not p == None and find == False:
                if not p.info == x:
                    p = p.next
                else:
                    new = Egt(value)
                    find = True
                    if p.next == None:
                        p.next = new
                    else:
                        new.next = p.next
                        p.next = new
            if find == False:
                print('Key not found impossible to insert a value in the list')



