from cassandra.cluster import Cluster
from datetime import datetime
from cassandra.query import dict_factory
import UDT


print(datetime.now())
cluster = Cluster(['10.250.93.207'])

session = cluster.connect('tweettrend')
session.row_factory = dict_factory


################################# source #################################
# rows = list(session.execute('select source from tweets'))

# result = dict()
# for row in rows:
#     if row['source'] in result.keys(): result[row['source']] += 1
#     else: result[row['source']] = 1
#
# print(sorted(result.items(), key=(lambda x: x[1]), reverse=True))

################################# datehour #################################
# rows = list(session.execute('select datehour from tweets'))
#
# datehour = set()
# for row in rows:
#     datehour.add(row['datehour'])
#
# print(sorted(datehour, reverse=True))

################################# place #################################
# rows = list(session.execute('select place_id, datehour from tweets'))
#
# dh = dict()
# for row in rows:
#     if 'place_id' in row and row['place_id']:
#         if row['datehour'] in dh: dh[row['datehour']] += 1
#         else: dh[row['datehour']] = 1
#
# print(sorted(dh.items(), key=(lambda x: x[1]), reverse=True))

################################# place, country code #################################
# rows = list(session.execute('select place_id, datehour, includes from tweets'))
#
# dh = dict()
# for row in rows:
#     if 'place_id' in row and row['place_id']:
#         inc = UDT.include(row['includes'])
#         inc_pl = UDT.place(inc.places[0])
#         print(row['datehour'], inc_pl.country_code)

cluster.shutdown()
print(datetime.now())