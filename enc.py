# coding=utf-8
from pymongo import MongoClient

client = MongoClient()

db = client['test']

str = 'Aubiny‡'

db['cities'].insert({
        'name': str
     })

