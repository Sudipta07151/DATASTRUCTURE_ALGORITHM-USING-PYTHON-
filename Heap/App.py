from HeapClass import *

m_heap=MaxBinaryHeap()
m_heap.insert(41)
m_heap.insert(39)
m_heap.insert(33)
m_heap.insert(18)
m_heap.insert(56)
m_heap.insert(100)
print(m_heap.get_heap())


print(m_heap.extract_maximum())

print(m_heap.get_heap())
print(m_heap.extract_maximum())

m_heap.insert(99)

print(m_heap.get_heap())