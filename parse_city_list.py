# coding=utf-8

##########################
# parse_city_list.py
# Parses the city data provided by cities.txt    (Source: maxmind.com)
#
# Created: 12/7

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

db = client['country_data']

with open('country_codes.txt') as country_codes_file:
    # AF,"Afghanistan"

    for line in country_codes_file:
        print line
        (code, name) = line.rstrip().split(',', 1)

        db['codes'].insert({
            'code': code.upper(),
            'name': name.strip("\""),
            'date': datetime.utcnow()
        })

with open('cities.txt') as cities_file:
    # Country,City,AccentCity,Region,Population,Latitude,Longitude  (maxmind.com)

    cities_file.next()    # Chomp the above header line

    for line in cities_file:
        (code, city, accent_city, region, population, latitude, longitude) = line.split(',')
        code_doc = db['codes'].find_one({'code': code.upper()})

        country = code_doc['name']

        db['cities'].insert({
            'country_code': code,
            'country': country,
            'date': datetime.utcnow()
        })
        print "Inserting: Country - %s (%s)\t\tCity - %s" % (country, code.upper(), city)
        db['countries'].update({'name': country}, {'$push': {'cities': city}})