age = 20
#mutable
country = ["Uganda","Kenya","Tanzania","Rwanda","Congo"]
print(country[0])
#immutable
lakes = ("Victoria","George","Albert","Mburo")
print(lakes[0])
#keys with there values. This is a dictionary.the one one the right is the value and the one on the left is the key.
#a dictionary stores in key-value pairs
cities = {"Uganda":"Kampala","Kenya":"Nairobi","Tanzania":"Dodoma","Rwanda":"Kigali"}
#square brackets are used when creating list and identifying values in a given variables that is dictionaries,list and tuples.
#polymophism is the ablility to use somethin for more than one purpose.
print(cities["Uganda"])
print(cities.keys())
print(cities.values())
currency = {1000,2000,5000,10000,20000,50000,1000,2000,5000,10000,20000,50000}
#storage of more than one thing in one memory unit is called a set. it doesn't allow and duplicates becuae the computer ignores them.
#a set is a collection of unordered items. It doesn't follow any order.
print(currency)
country.sort()
print(country)
country.insert(0,"Ghana")
print(country)
country.remove("Ghana")
print(country)
country.reverse()
print(country)