en_ua_dictionary = {}

en_ua_dictionary['red'] = 'червоний'
print(en_ua_dictionary)


if 'blue' in en_ua_dictionary:
    print(en_ua_dictionary)
elif 'purple' in en_ua_dictionary:
    print(en_ua_dictionary)
else: en_ua_dictionary = {'red': 'червоний', 'blue': '', 'purple': ''} 


for key in en_ua_dictionary:
    print(key.title(), 'in Ukranian is', en_ua_dictionary[key])


res = {key: value for key, value in en_ua_dictionary.items() if len(value) > 5}
print(res)

