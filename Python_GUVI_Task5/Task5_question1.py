people = [{'name':'loki', 'age':29},{'name':'lokesh','age':13},{'name':'nibhi','age':1.8},{'name':'Dee','age':27},{'name':'meena','age':52},{'name':'chandra','age':65}]
adults = filter(lambda x: x['age'] >= 18, people)
names = map(lambda x: x['name'],adults)
final_list = list(names)
print(f"names of people 18 and older is here:{final_list}")