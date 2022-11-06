#create and initialize a set
my_cities = {"Kampala", "Nairobi", "Arusha", "Mombasa", "Nairobi"}

print(my_cities)
print (f"There are {len(my_cities)} cities in the set")

print(type(my_cities))

my_cities.add("Kigali")
print(my_cities)

west_african_cities = {"Lagos", "Accra"}
south_african_cities = {"Cape Town", "Durban"}

master_city_list = {"New York"}
master_city_list.update(ea_cities)
print(master_city_list.update(ea_cities))

master_city_list.update(west_african_cities)
master_city_list.update(south_african_cities)
