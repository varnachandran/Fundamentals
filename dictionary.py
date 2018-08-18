'''Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)'''
"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locationsa={'North America':{'USA':['Mountain View','Atlanta']},
    'Asia':[{'India':'Bangalore'},{'China':'Shanghai'}],
    'Africa':{'Egypt':'Cairo'}}
print(1)
print(sorted(locationsa['North America']['USA']))
print(locationsa['Asia'])

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print(locationsa)
print(locations)
disp=[]
for country, city in locations['Asia'].iteritems():
    city_country=country+' - '+city[0]
    disp.append(city_country)


asia_cities = []

for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city