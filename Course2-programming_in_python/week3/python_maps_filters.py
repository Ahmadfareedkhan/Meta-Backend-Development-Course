menu = ["espresso", "mocha", "latte" , "cappuccino", "cortado", "americano"]

def find_coffee(coffe):
    if coffe[0] == 'c':
        return coffe
    
map_coffe =  map(find_coffee, menu)
print (map_coffe)
for x in map_coffe:
    print(x)

filter_coffe = filter(find_coffee, menu)
print(filter_coffe)
for x in filter_coffe:
    print(x)


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)