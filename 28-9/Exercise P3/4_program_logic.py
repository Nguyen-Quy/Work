L = [1, 2, 4, 8, 16, 32, 64]
X = 5

######## WHILE LOOP #########
# i = 0
# while i < len(L)-1:
#     if 2**X == L[i]:
#         print('at index', i)
#         break
#     else:
#         i += 1
# else:
#     print(X, 'not found')


####### FOR LOOP #########
# for i in range(len(L)):
#     if 2**X == L[i]:
#         print('at index', i)
#         break
# else:
#     print(X, 'not found')


### LIST COMPREHENSION ###
# vitri = [i for i in range(len(L)) if 2**X == L[i]]

vitri = [print('at index', i) if 2**X == L[i] else print(X, 'not found')
         for i in range(len(L)-1)]

# vitri = [print('at index', i) for i in range(len(L)-1) if 2**X == L[i]]
