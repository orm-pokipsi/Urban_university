my_dict = {'Ilnur':1993,'Misha':1994,'Roma':2000}
print('Dict: ',my_dict)
print('Existing value: ',my_dict.get('Ilnur'))
print('Not existing value: ',my_dict.get('Almira'))
my_dict.update({'Almira':1989,'Emir':1985})
a = my_dict.pop('Roma')
print('Deleted value: ',a)
print('Modified dictionary',my_dict)

my_set = {'Day',20.07,1993,20.07,'Day',1993}
print('Set',my_set)
my_set.add('July')
my_set.discard('Day')
my_set.discard(1993)
print('Modified set:' ,my_set)