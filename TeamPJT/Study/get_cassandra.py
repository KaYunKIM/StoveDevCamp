from cassandra.cluster import Cluster
import json

cluster = Cluster()
session = cluster.connect('streaming_test')

result = session.execute('select * from words limit 5')


remove=['id_str', 'truncated', 'in_reply_to_status_id',
        'in_reply_to_status_id_str', 'in_reply_to_user_id_str',

]
for i in result:
    words = json.loads(json.loads(i[0]))
    print(type(words), words)
    for j in words.keys():
        print(j)

