# class Stack:
#     def __init__(self):
#         self.Stack = []
#         self.Length = 0

#     def Calc_Length(self):
#         self.Length = len(self.Stack)

#     def auto_update_length(func):
#         """Decorator to update length after modifying the stack"""
#         def wrapper(self, *args, **kwargs):
#             result = func(self, *args, **kwargs)  # Call the original function
#             self.Calc_Length()  # Update length after modification
#             return result
#         return wrapper

#     def __repr__(self):
#         return f"{self.Stack}"

#     @auto_update_length
#     def Push(self, element):
#         if isinstance(element, (tuple, list)):
#             self.Stack.extend(element)
#         else:
#             self.Stack.append(element)

#     @auto_update_length
#     def Pop(self):
#         if self.Stack:
#             self.Stack.pop()

# # Test the stack
# stack = Stack()
# stack.Push(4)
# print(stack)  # Output: [4]
# print(stack.Length)  # Output: 1

# stack.Push([1, 2, 3])
# print(stack)  # Output: [4, 1, 2, 3]
# print(stack.Length)  # Output: 4

# stack.Pop()
# print(stack)  # Output: [4, 1, 2]
# print(stack.Length)  # Output: 3

d = {1 : "gad", 2 : "sad", 3 : "bad"}
print(d.values())