from core.tools import measure_execution_time
from pymongo import MongoClient
from bson import ObjectId
con = MongoClient('mongodb://localhost:27017', connectTimeoutMS=1000)
db = con['benchmark']
col = db['users']

TOTAL_RECORDS = 100000

SAMPLE_DATA = {'name': 'ehsan'}


@measure_execution_time
def do_simple():
    for i in range(TOTAL_RECORDS):
        col.insert_one(SAMPLE_DATA)


@measure_execution_time
def do_bulk():
    pack = []
    for i in range(TOTAL_RECORDS):
        pack.append(SAMPLE_DATA)
    col.insert_many(pack)


do_simple()
do_bulk()
