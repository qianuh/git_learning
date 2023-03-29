with open('test.txt') as my_file:
    # text = my_file.read()
    # print(text)
    for line in my_file.readlines():
        a = line.split(' ')
        print('name= %s' % (a[0]))
        print('id= %s' % (a[1]))

