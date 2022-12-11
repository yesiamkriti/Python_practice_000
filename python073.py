# difference between is and ==
fruits1=['orange','mango','apple','papya']
fruits2=['orange','mango','apple','papya']
fruits3=['banana','mango','apple','papya']
print(fruits1==fruits2)#True # it will check only list are equal or not if equal then True else False
print(fruits1==fruits3)#False
print(fruits1 is fruits2)# False
