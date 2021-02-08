from cassandra.cluster import Cluster
from datetime import datetime
import json
import pandas as pd


def reform_message(message, urls):
    '''
        :param message: str, tweet->text
        :param urls: str, entities->urls
        :return: (str, urls), new message with expanded url and new urls with filtering
        '''
    for url in urls:
        new_msg = message[:url['start'] - 1] + url['expanded_url'] if url['start'] > 0 else url['expanded_url']
        new_msg = new_msg + message[url['end']:] if url['end'] < len(message) else new_msg

        for key in list(set(['status', 'title', 'description', 'images']) & set(url.keys())):
            del url[key]

    return new_msg, urls


def reshape(dataframe, topic):
    '''
    :param dataframe: dataframe, a set of data, includes, and matching_rules
    :param topic: str, topic of the json_file
    :return: dataframe, reshaped data for insert into tweets
    '''
    json_file = json.loads(dataframe.to_json(orient='table'))
    # print('json_file', json_file, type(json_file))
    # print(json_file['data'])
    row = json_file['data'][0]['data'].copy()
    # print(type(row), len(row), row)
    # for key in row.keys():
    # print(key)
    if 'includes' in json_file['data'][0]:
    # print(type(row), row)
        row['includes'] = json_file['data'][0]['includes']

        if 'tweets' in row['includes']:
            for tweet in row['includes']['tweets']:
                if 'entities' in tweet and 'urls' in tweet['entities']:
                    tweet['text'], tweet['entities']['urls'] = reform_message(tweet['text'], tweet['entities']['urls'])

        if 'media' in row['includes']:
            for medium in row['includes']['media']:
                if 'public_metrics' in medium:
                    medium['view_count'] = medium['public_metrics']['view_count']

            del medium['public_metrics']

    # print(type(row), row)
    row['id'] = int(row['id'])

    row['topic'] = topic

    if 'referenced_tweets' in row and row['referenced_tweets'][0]['type'] == 'retweeted':
        row['text'] = row['includes']['tweets'][0]['text']

    elif 'entities' in row and 'urls' in row['entities']:
        row['text'], row['entities']['urls'] = reform_message(row['text'], row['entities']['urls'])

    if 'geo' in row:
        row['place_id'] = row['geo']['place_id']

        del row['geo']

    created_at = row['created_at'].split('T')

    row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))

    row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    result = json.loads(json.dumps(row).replace('\"text\":', '\"message\":'))

    return pd.DataFrame(data=[result.values()], columns=list(result.keys()))

f = open('sample.json', 'r', encoding='utf8')
lines = json.loads(''.join(f.readlines()))
print(datetime.now())
cluster = Cluster(['10.250.93.207'])

session = cluster.connect('tweetrend')

for line in lines:
    re_line = reshape(json_file=line, topic='temp')

    for re_ in re_line:
        print(re_, re_line[re_], type(re_line[re_]))
    print()
    session.execute('INSERT INTO tweets JSON \'{}\''.format(reshape(json_file=line, topic='temp')))

result = session.execute('select * from tweets')
for row in result:
    print(row)


cluster.shutdown()
print(datetime.now())


f = open('sample.json', 'r', encoding='utf8')
lines = json.loads(''.join(f.readlines()))
print(datetime.now())
cluster = Cluster(['10.250.93.207'])

session = cluster.connect('tweetrend')

for line in lines:
    re_line = reshape(json_file=line, topic='temp')

    for re_ in re_line:
        print(re_, re_line[re_], type(re_line[re_]))
    print()
    session.execute('INSERT INTO tweets JSON \'{}\''.format(reshape(json_file=line, topic='temp')))

result = session.execute('select * from tweets')
for row in result:
    print(row)


cluster.shutdown()
print(datetime.now())
