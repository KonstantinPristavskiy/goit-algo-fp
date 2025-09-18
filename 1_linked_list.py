class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self.head

    def sort_list(self):
        current = self.head
        while current:
            next = current.next
            while next:
                if current.data > next.data:
                    current.data, next.data = next.data, current.data
                next = next.next
            current = current.next
        return self.head


def merge_sorted_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.data < list2.data:
        list1.next = merge_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_sorted_lists(list1, list2.next)
        return list2

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()


print("Зв'язний список після зворотного перевертання:")
llist.reverse_list()
llist.print_list()


print("Зв'язний список після сортування:")
llist.sort_list()
llist.print_list()


llist2 = LinkedList()
llist2.insert_at_beginning(12)
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(4)
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(8)

print("Зв'язний відсортований список 2:")
llist2.sort_list()
llist2.print_list()

print("Зв'язний список після злиття:")
merged_list = LinkedList()
merged_list.head = merge_sorted_lists(llist.head, llist2.head)
merged_list.print_list()