# Графы

def adjacency_matrix(vertices, edges):     # Функция создания матрицы смежности
    n = len(vertices)                      # Определяем количество вершин

    matrix = [[0] * n for _ in range(n)]   # Создаем квадратную матрицу n×n, заполненную нулями

    for u, v in edges:                     # Перебираем все ребра графа
        matrix[u - 1][v - 1] = 1           # Устанавливаем связь между вершинами u и v
        matrix[v - 1][u - 1] = 1           # Так как граф неориентированный, ставим симметричную связь

    return matrix                          # Возвращаем готовую матрицу

def incidence_matrix(vertices, edges):     # Функция создания матрицы инцидентности
    n = len(vertices)                      # Количество вершин
    m = len(edges)                         # Количество ребер

    matrix = [[0] * m for _ in range(n)]   # Создаем матрицу n×m, заполненную нулями

    for j, (u, v) in enumerate(edges):     # Перебираем ребра вместе с их номерами
        matrix[u - 1][j] = 1               # Отмечаем, что вершина u принадлежит ребру j
        matrix[v - 1][j] = 1               # Отмечаем, что вершина v принадлежит ребру j

    return matrix                          # Возвращаем матрицу инцидентности

def dfs(v, graph, visited, component):     # Функция обхода графа в глубину (DFS)

    visited.add(v)                         # Добавляем вершину v в множество посещенных
    component.append(v)                    # Добавляем вершину в текущую компоненту связности

    for neighbor in graph[v]:              # Перебираем всех соседей вершины v
        if neighbor not in visited:        # Если сосед еще не посещен
            dfs(neighbor, graph, visited, component)  # Рекурсивно запускаем DFS для соседа

def connected_components(vertices, edges): # Функция поиска компонент связности
    graph = {v: [] for v in vertices}      # Создаем словарь: вершина -> список соседей

    for u, v in edges:                     # Перебираем все ребра
        graph[u].append(v)                 # Добавляем v в список соседей u
        graph[v].append(u)                 # Добавляем u в список соседей v

    visited = set()                        # Создаем пустое множество посещенных вершин
    components = []                        # Создаем список для хранения компонент связности

    for v in vertices:                     # Перебираем все вершины
        if v not in visited:               # Если вершина еще не посещена
            component = []                 # Создаем новую компоненту связности
            dfs(v, graph, visited, component)  # Выполняем DFS
            components.append(component)   # Добавляем найденную компоненту в список

    return components                      # Возвращаем список компонент связности

# BST

class Node:
    def __init__(self, key):          # Конструктор класса Node

        self.key = key                # Сохраняем значение узла
        self.left = None              # Левый потомок отсутствует
        self.right = None             # Правый потомок отсутствует

class BST:
    def __init__(self):               # Конструктор дерева BST
        self.root = None              # Корень дерева отсутствует

    def insert(self, key):            # Метод вставки элемента в дерево
        self.root = self._insert(self.root, key)  # Вызываем рекурсивную вставку

    def _insert(self, node, key):     # Рекурсивная функция вставки

        if node is None:              # Если место пустое
            return Node(key)          # Создаем новый узел
        if key < node.key:            # Если ключ меньше значения узла
            node.left = self._insert(node.left, key)  # Идем в левое поддерево
        else:                         # Иначе
            node.right = self._insert(node.right, key)  # Идем в правое поддерево
        return node                   # Возвращаем узел

    def search(self, key):            # Метод поиска элемента

        return self._search(self.root, key)  # Вызываем рекурсивный поиск


    def _search(self, node, key):     # Рекурсивный поиск

        if node is None:              # Если узел не найден
            return False              # Возвращаем False
        if node.key == key:           # Если значение найдено
            return True               # Возвращаем True
        if key < node.key:            # Если искомый ключ меньше
            return self._search(node.left, key)  # Ищем слева
        return self._search(node.right, key)     # Ищем справа


    def delete(self, key):            # Метод удаления элемента

        self.root = self._delete(self.root, key)  # Вызываем рекурсивное удаление

    def _delete(self, node, key):     # Рекурсивная функция удаления

        if node is None:              # Если узла нет
            return node               # Возвращаем None

        if key < node.key:            # Если ключ меньше значения узла
            node.left = self._delete(node.left, key)  # Удаляем в левом поддереве
        elif key > node.key:          # Если ключ больше значения узла
            node.right = self._delete(node.right, key)  # Удаляем в правом поддереве
        else:                         # Если узел найден
            if node.left is None:     # Если нет левого потомка
                return node.right     # Возвращаем правого потомка
            if node.right is None:    # Если нет правого потомка
                return node.left      # Возвращаем левого потомка

            temp = self.min_value(node.right)  # Ищем минимальный элемент справа
            node.key = temp.key       # Заменяем значение удаляемого узла
            node.right = self._delete(node.right, temp.key)  # Удаляем заменяющий узел

        return node                   # Возвращаем узел

    def min_value(self, node):        # Функция поиска минимального значения

        current = node                # Начинаем с переданного узла
        while current.left:           # Пока есть левый потомок
            current = current.left    # Переходим влево

        return current                # Возвращаем минимальный узел

    def inorder(self):                # Симметричный обход дерева

        result = []                   # Создаем пустой список
        self._inorder(self.root, result)  # Выполняем обход

        return result                 # Возвращаем результат

    def _inorder(self, node, result): # Рекурсивный симметричный обход

        if node:                      # Если узел существует
            self._inorder(node.left, result)   # Обходим левое поддерево
            result.append(node.key)            # Добавляем значение узла
            self._inorder(node.right, result)  # Обходим правое поддерево


# Heap Sort

def heapify(arr, n, i):               # Функция построения кучи

    largest = i                       # Считаем корень наибольшим элементом
    left = 2 * i + 1                  # Индекс левого потомка
    right = 2 * i + 2                 # Индекс правого потомка

    if left < n and arr[left] > arr[largest]:  # Если левый потомок больше
        largest = left                # Запоминаем индекс левого потомка

    if right < n and arr[right] > arr[largest]:  # Если правый потомок больше
        largest = right               # Запоминаем индекс правого потомка

    if largest != i:                  # Если найден элемент больше корня
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем элементы местами
        heapify(arr, n, largest)      # Рекурсивно восстанавливаем кучу

def heap_sort(arr):                   # Функция сортировки кучей
    n = len(arr)                      # Определяем размер массива

    for i in range(n // 2 - 1, -1, -1):  # Строим максимальную кучу
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):     # Перемещаем максимальный элемент в конец
        arr[0], arr[i] = arr[i], arr[0]  # Меняем местами первый и последний элемент
        heapify(arr, i, 0)            # Восстанавливаем кучу

    return arr                        # Возвращаем отсортированный массив


# main.py


# ГРАФ
vertices = [1, 2, 3, 4, 5]
edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5)
]

print("Матрица смежности:")
adj = adjacency_matrix(vertices, edges)

for row in adj:
    print(row)

print("\nМатрица инцидентности:")
inc = incidence_matrix(vertices, edges)

for row in inc:
    print(row)

print("\nКомпоненты связности:")

components = connected_components(vertices, edges)
print(components)

# BST
print("\nBST")
values = [10, 20, 5, 15, 25, 2, 8]
tree = BST()

for x in values:
    tree.insert(x)

print("Симметричный обход:")
print(tree.inorder())

print("Поиск 15:")
print(tree.search(15))

tree.delete(5)
print("После удаления 5:")
print(tree.inorder())

# HEAP SORT
print("\nHeap Sort")
arr = [5, 10, 20, 15, 2, 25, 8]
print("До сортировки:")
print(arr)
heap_sort(arr)

print("После сортировки:")
print(arr)
