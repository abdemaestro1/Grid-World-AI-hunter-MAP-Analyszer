#TUPLES is a data structur that cannot be changed so there are nothing to learn for now 
#we use () to defind a Tuple

#SETS is a non order data structur, we use {} to defind a SET 
set1 = {'kimetsu','nanatsu','bleach','hunter x hunter','one piece'}
set2={'Naruto','Attack on titan','kimetsu'}

#SHOW the items that exist in both of sets us 'INSTERSECTION' method 
print(set2.intersection(set1))

#SHOW the defference items between the sets us 'DIFFERENCE' method 
print(set2.difference(set1))
print(set1.difference(set2))

#COMBINE all the sets use 'UNION' method 
print(set2.union(set1))

#CREAT empty tuples 
empty_tuple = ()
empty_tuple = tuple()

#CREAT empty set 
empty_set = set()
