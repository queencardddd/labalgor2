
import sys
import importlib

if 'tree_algo' in sys.modules:
    importlib.reload(sys.modules['tree_algo'])

from graph_algo import adjacency_matrix, incidence_matrix, connected_components
from tree_algo import BST, heap_sort

#Графы
print("\nГрафы")
vertices = [1, 2, 3, 4, 5]
edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5)
]

print("\nМатрица смежности:")
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

#BST
print("\nBST")
values_bst = [10, 20, 5, 15, 25, 2, 8]
tree = BST()
for x in values_bst:
    tree.insert(x)

print("\nСимметричный обход:")
print(tree.inorder())

print("\nПоиск 15:")
print(tree.search(15))

tree.delete(5)
print("\nПосле удаления 5:")
print(tree.inorder())

#Heap sort
print("\nHeap sort")
arr_heap = [5, 10, 20, 15, 2, 25, 8]
print("\nМассив до сортировки:")
print(arr_heap)
heap_sort(arr_heap)
print("\nМассив после сортировки:")
print(arr_heap)
!python main.py
