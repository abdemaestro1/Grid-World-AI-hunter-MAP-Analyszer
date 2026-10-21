list2 =['play','eat']
 #Lists
courses = ['history','CI,CD','MATHE','PC']
print(courses[-6:])
print(len(courses))

#ADD somthing into the end of the list use "APPEND" method
courses.append('ESP')
print(courses)

#ADD somthing into the top of the list use "INSERT" method
courses.insert( 0,'geography')
print(courses)

#ADD multiple values into our list use "EXTEND" method
courses.extend(list2)
print(courses)

#REMOVE some item use "REMOVE" method 
courses.remove('CI,CD')
print(courses)

#REMOVE the last item use "POP" method 
courses.pop()
print(courses)

#use pop as a variable to show the last item from the list
var = courses.pop()
print(var)

#SHOW the reverse of the list use "REVERSE" method
courses.reverse()
print(courses)

#SORT the list use the "SORT" method
courses.sort() 
print(courses)
#TEST sort method in numbers case
num = [0,99,3,77,2.5,1]
num.sort()
print(num)

#sort with revers just add the reverse mrthod as an argument in pop
num.sort(reverse = True)
print(num)

#FIND the index use "INDEX" method
print(courses.index('PC'))

#SHOW the list separated use "JOIN" method 
courses_str = ' '.join(courses)
print(courses_str.capitalize())

#CREAT empty list
empty_list = []
empty_list = list()
