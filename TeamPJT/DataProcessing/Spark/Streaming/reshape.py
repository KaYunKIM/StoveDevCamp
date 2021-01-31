from datetime import datetime
import json
import collections.abc
import copy


def update(source, overrides):
    '''
    :param source: the one should be updated
    :param overrides: the one has new values
    :return: updated source
    '''
    for key, value in overrides.items():
        if isinstance(value, collections.abc.Mapping) and value:
            returned = update(source.get(key, {}), value)
            source[key] = returned
        elif type(value) is list and len(value):
            src = copy.deepcopy(source[key])
            if source[key]: del source[key][0]
            for i in range(len(value)):
                if isinstance(value[i], collections.abc.Mapping):
                    source[key].append(update(copy.deepcopy(src[0]), value[i]))
                else:
                    source[key] = value
        else:
            source[key] = overrides[key]

    return source


def remove_unused_url_fields(urls):
    '''
    :param urls: list of url
    :return: list of filtered url
    '''
    for url in urls:
        for key in list(set(['status', 'title', 'description', 'images']) & set(url.keys())):
            del url[key]

    return urls


def reform_message(message, urls):
    '''
    :param message: str, tweet->text
    :param urls: str, entities->urls
    :return: (str, urls), new message with expanded url and new urls with filtering
    '''
    if not urls[0]['url']:
        return message, remove_unused_url_fields(urls)

    urls = sorted(urls, key=lambda url: url['start'])
    new_msg = ''
    end = 0

    for url in urls:
        new_msg += message[end:url['start']] + url['expanded_url'] if url['start'] > 0 else url['expanded_url']
        end = url['end']

    new_msg += message[end:len(message)]

    return new_msg, remove_unused_url_fields(urls)


def reshape(json_list, topic):
    '''
    :param json_file: list(dict/json), a set of data and includes
    :param topic: str, topic of the json_file
    :return: list(dict/json), reshaped data for insert into tweets
    '''
    result = []

    # get data backbone
    backbone = json.loads(''.join(open('initial_data.json', 'r', encoding='utf8').readlines()))

    for json_row in json_list:
        row = copy.deepcopy(backbone)

        # fills data from json
        row = update(row, json_row['data'])
        row['includes'] = update(row['includes'], json_row['includes'])

        # filter include tweet
        if row['includes']['tweets']:
            for idx, tweet in enumerate(row['includes']['tweets']):
                if 'urls' in tweet['entities'] and tweet['entities']['urls']:
                    tweet['text'], row['includes']['tweets'][idx]['entities']['urls'] = reform_message(tweet['text'], tweet['entities']['urls'])

                tweet['place_id'] = tweet['geo']['place_id']
                del tweet['geo']

        # filter include media
        if row['includes']['media']:
            for medium in row['includes']['media']:
                medium['view_count'] = medium['public_metrics']['view_count']

                del medium['public_metrics']

        # if tweet is retweet of other, change text to origin
        if row['referenced_tweets'] and 'retweeted' in [x['type'] for x in row['referenced_tweets']]:
            row['text'] = [in_tweet['text'] for in_tweet in row['includes']['tweets']
                           if in_tweet['id']==[rf_tweet['id'] for rf_tweet in row['referenced_tweets'] if rf_tweet['type']=='retweeted'][0]][0]

            remove_unused_url_fields(row['entities']['urls'])

        elif 'urls' in row['entities']:
            row['text'], row['entities']['urls'] = reform_message(row['text'], row['entities']['urls'])

        row['topic'] = topic

        row['id'] = int(row['id'])
        row['author_id'] = int(row['author_id'])
        if row['conversation_id']: row['conversation_id'] = int(row['conversation_id'])
        if row['in_reply_to_user_id']: row['in_reply_to_user_id'] = int(row['in_reply_to_user_id'])

        row['place_id'] = row['geo']['place_id']
        del row['geo']

        created_at = row['created_at'].split('T')
        row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))

        row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        result.append(json.loads(json.dumps(row).replace('\"text\":', '\"message\":')))

    return result
