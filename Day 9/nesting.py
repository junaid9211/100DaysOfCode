travel_log = [
    {
        'country':'France',
        'cities':['Paris', 'Lille', 'Dijon'],
        'visits':12
    },
    {
        'country':'Germany',
        'cities':['Berlin', 'Hamburg', 'Stuttgart'],
        'visits':5
    }
]

def add_new_country(country, visits, cities):
    log = {'country':country, 'cities':cities, 'visits':visits}
    travel_log.append(log)


add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])

for item in travel_log:
    print(item)