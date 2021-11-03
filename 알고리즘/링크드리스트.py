"""
안녕하세요 다제입니다. 
이곳에서는 링크드 리스트 관련된 메소드를 직접 구현해보았습니다. 

먼저 Node와 LinkedList가 필요하므로 클래스로 생성하여 줍니다. 

노드에는 데이터를 저장하는 기능과 다음 데이터를 가르키는 역할 2가지를 합니다. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
"""
링크드 리스트는 총 8가지의 기능을 구현해보았습니다. 
가지 수가 다른 링크드 리스트보다 많은 이유는 기능별로 함수를 정의하는 것이 관리하기 편하기 때문입니다. 

1. append : 링크드 리스트 추가 연산 메소드 
2. str : 링크드 리스트를 문자열로 표현해서 리턴하는 메소드
3. find_node_with_index : 인덱스를 받아 해당 인덱스를 찾는 메소드
4. find_node_with_data : 원하는 값을 찾는 메소드
5. insert_after : previous_node 다음에 data를 삽입하는 메소드
6. prepend : 링크드 리스트 맨 앞 데이터 삽입하는 메소드
7. delete : 링크드 리스트 중간에 있는 노드를 삭제하는 메소드 
8. popleft : head를 삭제하는 메소드 
"""

class LinkedList:
    """링크드리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
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
        """링크드 리스트 중간에 있는 노드를 삭제하는 메소드"""
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

