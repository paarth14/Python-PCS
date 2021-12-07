# Prove that tuple cannot be changed in python.

t1 = (1, 2, 3)
t1[0] = 44
print(t1)

# Output :-
#   Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     t1[0] = 44
# TypeError: 'tuple' object does not support item assignment
