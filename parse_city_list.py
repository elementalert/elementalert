# coding=utf-8

##########################
# parse_city_list.py
# Parses the city data provided by cities.txt    (Source: maxmind.com)
#
# Created: 12/7

from pymongo import MongoClient
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--updatecodes', dest='UPDATE_CODES', action='store_true')
args = parser.parse_args()


client = MongoClient()

db = client['country_data']


if args.UPDATE_CODES:
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

with open('cities2.txt') as cities_file:
    #     Source: GeoNames.org
    #     The main 'geoname' table has the following fields :
    # ---------------------------------------------------
    # geonameid         : integer id of record in geonames database
    # name              : name of geographical point (utf8) varchar(200)
    # asciiname         : name of geographical point in plain ascii characters, varchar(200)
    # alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
    # latitude          : latitude in decimal degrees (wgs84)
    # longitude         : longitude in decimal degrees (wgs84)
    # feature class     : see http://www.geonames.org/export/codes.html, char(1)
    # feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
    # country code      : ISO-3166 2-letter country code, 2 characters
    # cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
    # admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
    # admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
    # admin3 code       : code for third level administrative division, varchar(20)
    # admin4 code       : code for fourth level administrative division, varchar(20)
    # population        : bigint (8 byte int)
    # elevation         : in meters, integer
    # dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
    # timezone          : the timezone id (see file timeZone.txt) varchar(40)
    # modification date : date of last modification in yyyy-MM-dd format

    for line in cities_file:

        (_geonameid, city_name, ascii_name, _alternatenames, _lat, _long, _feat_class, _feat_code, country_code,
            cc2, _admin1, _admin2, _admin3, _admin4, _pop, _elev, _dem, _timezone, _mod_date) = line.rstrip().split('\t')

        print "%s\t%s\t%s" % (name, ascii_name, country_code)

        code_doc = db['codes'].find_one({'code': code.upper()})
        country = code_doc['name']

        db['cities'].insert({
            'country_code': code,
            'country': country,
            'date': datetime.utcnow()
        })

        print "Inserting: Country - %s (%s)\t\tCity - %s" % (country, code.upper(), city_name)
        db['countries'].update({'name': country}, {'$push': {'cities': city_name}})





