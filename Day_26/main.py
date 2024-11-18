# # Day 26/100
# # Python Bootcamp!!!
# # List Comprehension
#
# # numbers=[1,2,3,4,5]
# # # new_list=[]
# # # for n in numbers:
# # #     add_1=n+1
# # # new_list.append(add_1)
# # # this can be done by :-
# # # list comprehension:-
# # new_list=[n+1 for n in numbers]
# # print(new_list)
#
# # name='Utkarsh'
# # new_list=[letter for letter in name]
# # print(new_list)
#
# # list,tuple,ranges are sequence in python language
#
# # numbers=[1,2,3,4]
# # new_list=[range *2 for range in numbers]
# # print(new_list)
#
# # conditional list comprehension
#
# # names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# # new_list=[name.upper() for name in names if len(name) >4]
# # print(new_list)
#
# # DICT COMPREHENSION
# #
# # import random
# #
# # # Syntax:- new_dict={new_key:new_value for (key,value) in dict.items() if condition}
# #
# # student_dict={
# #     "Alex":89,
# #     "Raj":78,
# #     "Utkarsh":90,
# #     "Rohan":100
# # }
# # students=['Raj','Utkarsh','Ayush','Rohan','Bishop']
# # my_dict={student:random.randint(1,100) for student in students}
# # print(my_dict)
# #
# # passed_students={student:value for (student,value) in my_dict.items() if value > 33}
# # print(passed_students)
#
#
# student_dict={
#     "Student":['Utkarsh','Ayush','Bishop','Rahul'],
#     "Score":[85,85,84,67]
# }
# # for (key,value) in student_dict.items():
# #     print(key,value)
#
# import pandas
#
# student_data_frame=pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# # loop through a data frame
# for (index,row) in student_data_frame.iterrows():
#     #print(row.Student)
#     if row.Student== 'Utkarsh':
#         print(row.Score)
#
#
# # for (key,value) in student_data_frame.items():
# #     print(value)
#


# keyword method with iterrows()
# {new_key:new_value for (index,row) in df.iterrows()}
import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())
phonetic_dict={row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

word=input("Enter the word:- ").upper()
output_list=[phonetic_dict[letter] for letter in word]
print(output_list)






















