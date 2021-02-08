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

    print(json_file)

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

    if 'referenced_tweets' in row and row['referenced_tweets'][0]['type']=='retweeted':
        row['text'] = row['includes']['tweets'][0]['text']

    elif 'entities' in row and 'urls' in row['entities']:
        row['text'], row['entities']['urls'] = reform_message(row['text'], row['entities']['urls'])

    if 'geo' in row:
        row['place_id'] = row['geo']['place_id']
        
        del row['geo']

    created_at = row['created_at'].split('T')
    row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))
    print(created_at, row['datehour'])
    
    row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    result = json.loads(json.dumps(row).replace('\"text\":', '\"message\":'))
    
    return pd.DataFrame(data=[result.values()], columns=list(result.keys()))


tweet = {'data': {'conversation_id': '1352530488947322880', 'referenced_tweets': [{'type': 'retweeted', 'id': '1352507617852190720'}], 'attachments': {'media_keys': ['3_1352507615843123200']}, 'author_id': '743553354', 'created_at': '2021-01-22T08:16:12.000Z', 'entities': {'mentions': [{'start': 3, 'end': 11, 'username': 'Reuters'}], 'annotations': [{'start': 13, 'end': 17, 'probability': 0.9434, 'type': 'Place', 'normalized_text': 'Japan'}, {'start': 51, 'end': 55, 'probability': 0.4835, 'type': 'Place', 'normalized_text': 'COVID'}], 'urls': [{'start': 78, 'end': 101, 'url': 'https://t.co/QMvjB8nq0f', 'expanded_url': 'http://reut.rs/3pbCjFl', 'display_url': 'reut.rs/3pbCjFl', 'images': [{'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=orig', 'width': 800, 'height': 533}, {'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=150x150', 'width': 150, 'height': 150}], 'status': 200, 'title': 'Japan tourism push linked to surge in COVID-19 infections -study', 'description': "A domestic tourism campaign promoted by Japan's Prime Minister Yoshihide Suga may have contributed to a sharp increase in coronavirus infection cases in the country, a prominent adviser to the government's pandemic response said.", 'unwound_url': 'https://www.reuters.com/article/us-health-coronavirus-japan-travel-idUSKBN29R0J2?taid=600a747ec8ffe70001f649db&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter'}, {'start': 102, 'end': 125, 'url': 'https://t.co/vQjiY8G6h6', 'expanded_url': 'https://twitter.com/Reuters/status/1352507617852190720/photo/1', 'display_url': 'pic.twitter.com/vQjiY8G6h6'}]}, 'text': 'RT @Reuters: Japan tourism push linked to surge in COVID-19 infections -study https://t.co/QMvjB8nq0f https://t.co/vQjiY8G6h6', 'id': '1352530488947322880', 'possibly_sensitive': False, 'lang': 'en', 'public_metrics': {'retweet_count': 49, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}, 'source': 'Twitter for iPhone'}, 'includes': {'media': [{'media_key': '3_1352507615843123200', 'type': 'photo', 'url': 'https://pbs.twimg.com/media/EsUSgr5XAAAZK7j.jpg'}], 'users': [{'username': 'ptialex77', 'profile_image_url': 'https://pbs.twimg.com/profile_images/1042991180399534080/zkqzsDkh_normal.jpg', 'name': 'Alessio S 🇫🇷🇮🇹⭐️⭐️', 'id': '743553354', 'verified': False}, {'username': '    Reuters', 'entities': {'url': {'urls': [{'start': 0, 'end': 22, 'url': 'http://t.co/BmHxhkm3Mh', 'expanded_url': 'http://www.reuters.com', 'display_url': 'reuters.com'}]}, 'description': {'mentions': [{'start': 97, 'end': 108, 'username': 'ReutersBiz'}]}}, 'profile_image_url': 'https://pbs.twimg.com/profile_images/1194751949821939712/3VBu4_Sa_normal.jpg', 'name': 'Reuters', 'id': '1652541', 'verified': True}], 'tweets': [{'conversation_id': '1352507617852190720', 'attachments': {'media_keys': ['3_1352507615843123200']}, 'author_id': '1652541', 'created_at': '2021-01-22T06:45:19.000Z', 'entities': {'annotations': [{'start': 0, 'end': 4, 'probability': 0.9445, 'type': 'Place', 'normalized_text': 'Japan'}, {'start': 38, 'end': 42, 'probability': 0.5325, 'type': 'Place', 'normalized_text': 'COVID'}], 'urls': [{'start': 65, 'end': 88, 'url': 'https://t.co/QMvjB8nq0f', 'expanded_url': 'http://reut.rs/3pbCjFl', 'display_url': 'reut.rs/3pbCjFl', 'images': [{'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=orig', 'width': 800, 'height': 533}, {'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=150x150', 'width': 150, 'height': 150}], 'status': 200, 'title': 'Japan tourism push linked to surge in COVID-19 infections -study', 'description': "A domestic tourism campaign promoted by Japan's Prime Minister Yoshihide Suga may have contributed to a sharp increase in coronavirus infection cases in the country, a prominent adviser to the government's pandemic response said.", 'unwound_url': 'https://www.reuters.com/article/us-health-coronavirus-japan-travel-idUSKBN29R0J2?taid=600a747ec8ffe70001f649db&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter'}, {'start': 89, 'end': 112, 'url': 'https://t.co/vQjiY8G6h6', 'expanded_url': 'https://twitter.com/Reuters/status/1352507617852190720/photo/1', 'display_url': 'pic.twitter.com/vQjiY8G6h6'}]}, 'text': 'Japan tourism push linked to surge in COVID-19 infections -study https://t.co/QMvjB8nq0f https://t.co/vQjiY8G6h6', 'id': '1352507617852190720', 'possibly_sensitive': False, 'lang': 'en', 'public_metrics': {'retweet_count': 49, 'reply_count': 4, 'like_count': 87, 'quote_count': 13}, 'source': 'True Anthem'}]}, 'matching_rules': [{'id': 1352504259611291648, 'tag': None}]}
example = reshape(tweet, 'covid-19')
print(example)