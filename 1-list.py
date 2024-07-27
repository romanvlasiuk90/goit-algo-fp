class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

# Функція реверсування однозв'язного списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція сортування однозв'язного списку (Сортування вставками)
def insertion_sort_list(head):
    sorted_list = None

    current = head
    while current:
        next_node = current.next

        if not sorted_list or sorted_list.data >= current.data:
            current.next = sorted_list
            sorted_list = current
        else:
            sorted_node = sorted_list
            while sorted_node.next and sorted_node.next.data < current.data:
                sorted_node = sorted_node.next

            current.next = sorted_node.next
            sorted_node.next = current

        current = next_node

    return sorted_list

# Функція об'єднання двох відсортованих однозв'язних списків
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Приклад використання функцій
if __name__ == "__main__":
    # Приклад реверсування
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    print("Оригінальний список:")
    llist.print_list()

    llist.head = reverse_list(llist.head)
    print("Реверсований список:")
    llist.print_list()

    # Приклад сортування
    llist = LinkedList()
    llist.append(4)
    llist.append(3)
    llist.append(1)
    llist.append(2)

    print("Не відсортований список:")
    llist.print_list()

    llist.head = insertion_sort_list(llist.head)
    print("Відсортований список:")
    llist.print_list()

    # Приклад об'єднання
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(5)

    llist2 = LinkedList()
    llist2.append(2)
    llist2.append(4)
    llist2.append(6)

    print("Перший відсортований список:")
    llist1.print_list()

    print("Другий відсортований список:")
    llist2.print_list()

    merged_head = merge_sorted_lists(llist1.head, llist2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("Об'єднаний відсортований список:")
    merged_list.print_list()