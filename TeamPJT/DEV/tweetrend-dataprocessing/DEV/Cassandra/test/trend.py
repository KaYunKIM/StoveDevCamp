from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import UDT


def person_popularity(row, start, end):
    sum = 0
    for key in row.keys():
        if key.startswith('count') and start <= int(key.split('_')[1]) <= end:
            sum += row[key] if row[key] else 0

    return sum


def select_n_people(topic, start, end, n=5):
    rows = sorted(list(session.execute('select * from count_by_user where topic=\'{}\''.format(topic))),
                  key=lambda row: person_popularity(row, start=start, end=end), reverse=True)[:n]

    return rows


def tweet_popularity(row):
    public_metrics = UDT.public_metric(row['public_metrics']) if row['public_metrics'] else None
    first = public_metrics.sum() if public_metrics else 0
    media = UDT.include(row['includes']).media
    second = media.view_count if media else 0

    return (first, second)


def select_n_tweets(topic, start, end, n=5):
    rows = sorted(list(session.execute('select * from tweets where topic=\'{}\' and datehour>={} and datehour<={} allow filtering'.format(topic, start, end))),
                  key=lambda row: tweet_popularity(row), reverse=True)[:n]

    return rows


cluster = Cluster(['10.250.93.207'])

session = cluster.connect('temp_trend')
session.row_factory = dict_factory

for person in select_n_people(topic='temp', start=2021010101, end=2021010102):
    print(person)

session.execute('use tweetrend')

for tweet in select_n_tweets(topic='temp', start=2021011300, end=2021011502):
    print(tweet['public_metrics'])

cluster.shutdown()