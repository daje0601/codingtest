class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """링크드리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연사 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f' {iterator.data} |'
            iterator = iterator.next

        return res_str
# str 예제
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# print(linked_list)

    def find_node_with_index(self, index):
        """인덱스를 받아 해당 인덱스를 찾는 메소드"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        return iterator
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# print(linked_list)
# print(linked_list.find_node(1).data)
# linked_list.find_node(1).data = 100
# print(linked_list.find_node(1).data)

    def find_node_with_data(self, data):
        """원하는 값을 찾는 메소드"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            else:
                iterator = iterator.next
# linked_list = LinkedList()
# linked_list.append(2)
# print(linked_list.find_node_with_data(2).data)

    def insert_after(self, previous_node, data):
        """previous_node 다음에 data를 삽입하는 메소드"""
        new_node = Node(data)

        new_node.next = previous_node.next
        previous_node.next = new_node
# linked_list = LinkedList()
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# node_2 = linked_list.find_node_with_data(3)
# linked_list.insert_after(node_2, 6)
# print(linked_list)

    def prepend(self, data):
        """링크드 리스트 맨 앞 데이터 삽입하는 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
# linked_list = LinkedList()
# linked_list.prepend(2)
# linked_list.prepend(3)
# linked_list.prepend(4)
# 
# print(linked_list)
# 
# linked_list.prepend(100)
# 
# print(linked_list)

    def delete(self, previous_node):
        """삭제하는 메소드"""
        data = previous_node.next.data

        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
        return data

    def popleft(self):
        """head를 삭제하는 메소드"""
        data = self.head.data

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data
#
