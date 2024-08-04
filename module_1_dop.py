grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

len_grades = len(grades)
list_ar_mean_gr = []
for i in range(len_grades):
    ar_mean_gr = sum(grades[i]) / len(grades[i])
    list_ar_mean_gr.append(ar_mean_gr)
# print (list_ar_mean_gr)

students = list(students)
students = sorted(students)
# print (students)

dict_stud = {}
for i in range (len_grades):
  dict_stud_item = {students [i]: list_ar_mean_gr [i]}
  dict_stud.update(dict_stud_item)
# dict_stud = dict(zip(students, list_ar_mean_gr))
print(dict_stud)
