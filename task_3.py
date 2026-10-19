world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for year in world_champions:
    champion = world_champions[year]
    print(year, '-', champion)

country = 'Италия'

is_country = False

for year in world_champions:
    if world_champions[year] == country:
        is_country = True
    
if is_country:
        print('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
        print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')