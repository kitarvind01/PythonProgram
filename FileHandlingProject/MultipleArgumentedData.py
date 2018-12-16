def person(name,**data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i,j)



person(name='Arvind',age=23,mob=233453)