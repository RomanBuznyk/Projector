#1
my_tuple = ('Jonh', 'Wick', 40)
#2
print(my_tuple[1])
#3
(first_name, last_name, age) = my_tuple
#4
for index in first_name:
    print(index, end = ' ')
#5
my_tuple2 = (first_name[1:], last_name[1:])
print(my_tuple2)
#6, 7
my_tuple3 = ((1, 2), (3, 4))
print(sum(list(map(sum, list(my_tuple3)))))