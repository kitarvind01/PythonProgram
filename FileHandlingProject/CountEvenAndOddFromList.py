def count(lst):
    cnteven=0
    cntodd=0
    for i in lst:
        if i%2==0:
            cnteven+=1
        else:
            cntodd+=1
    return cnteven,cntodd



lst=[34,22,4,5,66,75,22,34]
even, odd=count(lst)
print(even)
print(odd)