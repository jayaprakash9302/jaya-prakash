#Lists : A list is an immutable one.it is denoted as[].it is similar array in a java and c..
NUMBERS=[1,2,3,4,5,6,0]
print(NUMBERS)
NUMBERS.insert(6,'h')
print(NUMBERS)
NUMBERS.append('i')
print(NUMBERS)
NUMBERS.remove('i')
print(NUMBERS)
#slicing 
NUMBERS=['a','b','c','d','e','f']
print(NUMBERS)
print(NUMBERS[0:3])
print(NUMBERS[-3:-1])
print(NUMBERS[9:90])
print(NUMBERS[-4:-3])
#tuples 
#these are denoted as ()...
VEGETABLES=('ONION','CARROT','BEETROOT','PUMPKIN')
print(VEGETABLES) 
#Slicing in tuples..
print(VEGETABLES[0:3])
print(VEGETABLES[4:6])
print(VEGETABLES[-5:-1])
print(VEGETABLES[-90:-4])
print(VEGETABLES[-1:0])
#Dictionary
#example
BIKES={'KTM','ENFIELD'}
print(BIKES)
BIKES.update({'KTM':'120cr'})
print(BIKES)
BIKES.update({'ENFIELD':'70cr'})
print(BIKES)
BIKES.clear()
print(BIKES)
#del BIKES['rangerover']
print(BIKES)
#BIKES.pop('Benz')
print(BIKES)
#slicing in an Dictionary..
cars={'KTM','REDBULL'}
print(BIKES)
keys_for_slicing=["KTM","REDBULL"]
sliced_BIKES = {key:cars[key] for key in keys_for_slicing}
print(BIKES)
keys_for_slicing=["KTM"]
sliced_BIKES = {key:BIKES[key] for key in keys_for_slicing} 
print(BIKES)

output
[1, 2, 3, 4, 5, 6, 0]
[1, 2, 3, 4, 5, 6, 'h', 0]
[1, 2, 3, 4, 5, 6, 'h', 0, 'i']
[1, 2, 3, 4, 5, 6, 'h', 0]
['a', 'b', 'c', 'd', 'e', 'f']
['a', 'b', 'c']
['d', 'e']
[]
['c']
('ONION', 'CARROT', 'BEETROOT', 'PUMPKIN')
('ONION', 'CARROT', 'BEETROOT')
()
('ONION', 'CARROT', 'BEETROOT')
()
()
{'KTM', 'ENFIELD'}
{'KTM', 'ENFIELD'}
{'KTM', 'ENFIELD'}
set()
set()
set()
set()
