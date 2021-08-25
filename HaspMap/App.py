from HashTableClassUsingList import *

hashTable=HashTable()
hashTable.set_item('ilicic',4)
hashTable.set_item('morata',5)
hashTable.set_item('halland',8)
hashTable.set_item('rakitic',4)
hashTable.set_item('lewandowski',5)
hashTable.set_item('modric',8)

hashTable.print_table()
print('get')
print(hashTable.get_item("modric"))

print(hashTable.get_all_keys())