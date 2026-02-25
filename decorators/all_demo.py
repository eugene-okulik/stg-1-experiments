trues = [True, True, True]
falses = [False, False, False]
mixed = [True, False, True]

print(all(trues)) # True
print(all(falses)) # False
print(all(mixed)) # False

inp1 = input('1: ')
inp2 = input('2: ')
inp3 = input('3: ')

user_data = [inp1, inp2, inp3]
data_len_ok = [len(value) <= 3 for value in user_data]
print(data_len_ok)

# 1: sdf
# 2: wer
# 3: sdfg
# [True, True, False]
print(all(data_len_ok))

# 1: sdf
# 2: sdf
# 3: sdfg
# [True, True, False]
# False

# 1: 234
# 2: sdf
# 3: sd
# [True, True, True]
# True