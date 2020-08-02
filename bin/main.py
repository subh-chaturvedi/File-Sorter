#main program file
#will give option to add(and run) or run

print('')
print('')
print('ENTER 1 TO SORT A FOLDER')
print('ENTER 2 TO ADD A NEW SORTING CRITEREA')


input=input(('input= '))


if input=='1':
    import sorter

elif input=='2':
    import adder
    inputnew= input(('Should a folder be sorted?'))
    if inputnew=='yes':
        import sorter