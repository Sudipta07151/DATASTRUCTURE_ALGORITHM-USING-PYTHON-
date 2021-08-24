# from StackClass import *
#
# stack=Stack(5)
# stack.push_to_stack(35)
# stack.push_to_stack(15)
# stack.push_to_stack(495)
# stack.print_stack()
#
# print('POP')
# print(f'pop_from_stack: ',(stack.pop_from_stack()).value)
# stack.print_stack()
#
# print(f'pop_from_stack: ',(stack.pop_from_stack()).value)
#
# print(f'pop_from_stack: ',(stack.pop_from_stack()).value)
#
# print(f'pop_from_stack: ',(stack.pop_from_stack()).value)
#
# print(f'pop_from_stack: ',stack.pop_from_stack())
# print('PUSH:')
# stack.push_to_stack(99)
# stack.print_stack()

from QueueClass import *
queue=Queue(4)
queue.enqueue(14)
queue.enqueue(456)

queue.print_queue()

print()
print('remove: ',(queue.dequeue()).value)

print('remove: ',(queue.dequeue()).value)


queue.enqueue(99)
print('remove: ',(queue.dequeue()).value)

print('remove: ',(queue.dequeue()))

queue.enqueue(99)
queue.print_queue()