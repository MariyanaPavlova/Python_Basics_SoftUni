animal=str(input()).lower()
type=0

if animal == 'dog' or animal == 'dolphin' or animal=='horse':
    type='mammal'
elif animal == 'snake' or animal=='crocodile' or animal=='tortoise':
    type='reptile'
else:
    type='unknown'
print(type)