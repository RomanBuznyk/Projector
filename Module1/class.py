'''
def av(salary: list[int]):
    salary = sorted(salary)
    return sum(salary[1:len(salary) - 1:]) / (len(salary))
'''
'''
def task3(arr: list) -> int:
    result = 0
    for i in set(arr):
        if arr.count(i) >= 2:
            result += i
    return result 

print(task3([1,2,2,3]))
'''

capitals = {
    'France': 'Paris',
    'Ukraine': 'Kyiv',
    'Germany': 'Berlin',
    'try_list': [1,2,3,4]
}

capitals['Italy'] = 'Rome'
print(capitals)


for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")
    
'''