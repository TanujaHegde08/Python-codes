class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_duplicate(self):
        current = self.head
        index = None
        temp = None

        if self.head == None:
            return
        else:
            while current != None:
                temp = current
                index = current.next

                while index != None:
                    if current.data == index.data:
                        temp.next = index.next
                    else:
                        temp = index
                    index = index.next
                current = current.next

    def display(self):
        current = self.head
        if self.head == None:
            print("List is empty")
            return
        while current != None:
            print(current.data)
            current = current.next

def user_input():
    slist = LinkedList()
    data_list = input("Enter the elements in the linked list: ").split()
    for data in data_list:
        slist.add_node(int(data))

    print("Original List: ")
    slist.display()
    slist.remove_duplicate()

    print("List after removing duplicate nodes: ")
    slist.display()
if __name__ == "__main__":
    user_input()