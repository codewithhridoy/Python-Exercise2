'''
Dictionaries are python version of Has Tables.
Like Objects in javaScript.
Allows us to create a Mapping with key-value pairs.
They don't retain any order.

'''
myDict = {'key1': 'value1', 'key2': 123, 'key3' : {'key4' : [1,2,'grabit']}}
print(myDict)

print(myDict['key3']['key4'][2])
print(myDict['key3']['key4'][2].capitalize())


#Add key and value1

employee = {'fname': 'Hridoy', 'lname': 'Ahmed' }
print(employee)
employee['age'] = '25'
print(employee)


d3 = {'k1':[{'nest_key':['this_is_deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
