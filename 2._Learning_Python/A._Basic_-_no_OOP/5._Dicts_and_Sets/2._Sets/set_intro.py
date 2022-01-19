# # y = {4, 5,33, 6}
# # print(y)
# all_possible_scores = set()
# for correct in range(0, 91):
#     for incorrect in range(0, 91):
#         for update in range(0, 91):
#             if correct + incorrect + update == 90:
#                 all_possible_scores.add(correct * 4 + incorrect * (-1))
# impossible_scores = set()
# for i in range(-90, 361):
#     if i not in all_possible_scores:
#         impossible_scores.add(i)
# print('Number of impossible squares', len(impossible_scores))
# print('They are:', impossible_scores)
# if (len(all_possible_scores) + len(impossible_scores) == 451):
#     print('Calculation is correct')

# x = {11, 22, 2, -13, 4, 60, 15}
# x.update((111,222,333))
x = {1, 2, 3}

