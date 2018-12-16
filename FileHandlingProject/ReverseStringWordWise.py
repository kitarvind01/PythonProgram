def reverseAString():
    st= input("Enter any String")
    seprateword= st.split(" ")
    st= st[-1::-1]
    output=''.join(st)
    return output

revStr=reverseAString();
print(revStr)
