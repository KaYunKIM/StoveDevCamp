from cassandra.cluster import Cluster
from datetime import datetime
import json


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


def reshape(json_file, topic):
    '''
    :param json_file: dict/json, a set of data and includes
    :param topic: str, topic of the json_file
    :return: dict/json, reshaped data for insert into tweets
    '''
    row = json_file['data'].copy()

    if 'includes' in json_file:
        row['includes'] = json_file['includes']

        if 'tweets' in row['includes']:
            for tweet in row['includes']['tweets']:
                if 'entities' in tweet and 'urls' in tweet['entities']:
                    tweet['text'], tweet['entities']['urls'] = reform_message(tweet['text'], tweet['entities']['urls'])

        if 'media' in row['includes']:
            for medium in row['includes']['media']:
                if 'public_metrics' in medium:
                    medium['view_count'] = medium['public_metrics']['view_count']

                    del medium['public_metrics']

    row['topic'] = topic

    if 'referenced_tweets' in row and 'retweeted' in [x['type'] for x in row['referenced_tweets']]:
        row['text'] = [in_tweet['text'] for in_tweet in row['includes']['tweets']
                       if in_tweet['id']==[rf_tweet['id'] for rf_tweet in row['referenced_tweets'] if rf_tweet['type']=='retweeted'][0]][0]

    elif 'entities' in row and 'urls' in row['entities']:
        row['text'], row['entities']['urls'] = reform_message(row['text'], row['entities']['urls'])

    if 'geo' in row:
        row['place_id'] = row['geo']['place_id']

        del row['geo']

    created_at = row['created_at'].split('T')
    row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))
    print(created_at, row['datehour'])

    row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return json.loads(json.dumps(row).replace('\"text\":', '\"message\":'))

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