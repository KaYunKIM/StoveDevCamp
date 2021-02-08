import json

raw = """{
    "UserId": "Xxx", 
    "Count": "0000"
}"""

new = json.loads(raw)

# print(raw, new)
# print(type(new))
# print(new["Count"])



exmp = (None, '"{\\n  \\"data\\": {\\n    \\"conversation_id\\": \\"1352521002207633414\\",\\n    \\"referenced_tweets\\": [\\n      {\\n        \\"type\\": \\"quoted\\",\\n        \\"id\\": \\"1352189984867016705\\"\\n      }\\n    ],\\n    \\"author_id\\": \\"32375884\\",\\n    \\"created_at\\": \\"2021-01-22T07:38:30.000Z\\",\\n    \\"entities\\": {\\n      \\"urls\\": [\\n        {\\n          \\"start\\": 15,\\n          \\"end\\": 38,\\n          \\"url\\": \\"https://t.co/PN5Qe2zQlB\\",\\n          \\"expanded_url\\": \\"https://twitter.com/drdavidsamadi/status/1352189984867016705\\",\\n          \\"display_url\\": \\"twitter.com/drdavidsamadi/\\u2026\\"\\n        }\\n      ]\\n    },\\n    \\"text\\": \\"Worlds a joke. https://t.co/PN5Qe2zQlB\\",\\n    \\"id\\": \\"1352521002207633414\\",\\n    \\"possibly_sensitive\\": false,\\n    \\"lang\\": \\"en\\",\\n    \\"public_metrics\\": {\\n      \\"retweet_count\\": 0,\\n      \\"reply_count\\": 0,\\n      \\"like_count\\": 0,\\n      \\"quote_count\\": 0\\n    },\\n    \\"source\\": \\"Twitter for iPhone\\"\\n  },\\n  \\"includes\\": {\\n    \\"users\\": [\\n      {\\n        \\"username\\": \\"Adam_Kemp\\",\\n        \\"profile_image_url\\": \\"https://pbs.twimg.com/profile_images/1339265367026364417/j_8ZqyYC_normal.jpg\\",\\n        \\"name\\": \\"Adam Kemp\\",\\n        \\"id\\": \\"32375884\\",\\n        \\"verified\\": false\\n      },\\n      {\\n        \\"username\\": \\"drdavidsamadi\\",\\n        \\"entities\\": {\\n          \\"url\\": {\\n            \\"urls\\": [\\n              {\\n                \\"start\\": 0,\\n                \\"end\\": 23,\\n                \\"url\\": \\"https://t.co/08pRLMPwpv\\",\\n                \\"expanded_url\\": \\"http://davidsamadi.com\\",\\n                \\"display_url\\": \\"davidsamadi.com\\"\\n              }\\n            ]\\n          },\\n          \\"description\\": {\\n            \\"urls\\": [\\n              {\\n                \\"start\\": 94,\\n                \\"end\\": 117,\\n                \\"url\\": \\"https://t.co/QK3ifWiRPB\\",\\n                \\"expanded_url\\": \\"http://ProstateCancer911.com\\",\\n                \\"display_url\\": \\"ProstateCancer911.com\\"\\n              }\\n            ],\\n            \\"hashtags\\": [\\n              {\\n                \\"start\\": 67,\\n                \\"end\\": 82,\\n                \\"tag\\": \\"RoboticSurgery\\"\\n              }\\n            ],\\n            \\"mentions\\": [\\n              {\\n                \\"start\\": 51,\\n                \\"end\\": 65,\\n                \\"username\\": \\"DrDavidSamadi\\"\\n              },\\n              {\\n                \\"start\\": 118,\\n                \\"end\\": 126,\\n                \\"username\\": \\"newsmax\\"\\n              }\\n            ]\\n          }\\n        },\\n        \\"profile_image_url\\": \\"https://pbs.twimg.com/profile_images/1345004936078258176/W5u79dDu_normal.jpg\\",\\n        \\"name\\": \\"Dr. David Samadi, MD\\",\\n        \\"id\\": \\"25816369\\",\\n        \\"verified\\": true\\n      }\\n    ],\\n    \\"tweets\\": [\\n      {\\n        \\"conversation_id\\": \\"1352189984867016705\\",\\n        \\"author_id\\": \\"25816369\\",\\n        \\"created_at\\": \\"2021-01-21T09:43:09.000Z\\",\\n        \\"entities\\": {\\n          \\"annotations\\": [\\n            {\\n              \\"start\\": 0,\\n              \\"end\\": 28,\\n              \\"probability\\": 0.4502,\\n              \\"type\\": \\"Organization\\",\\n              \\"normalized_text\\": \\"The World Health Organization\\"\\n            }\\n          ]\\n        },\\n        \\"text\\": \\"The World Health Organization has now released guidance to laboratories around the world to reduce the cycle count in PCR tests to get a more accurate representation of COVID cases.\\\\n\\\\nThe current cycle was much too high and resulting in any particle being declared a positive case.\\",\\n        \\"id\\": \\"1352189984867016705\\",\\n        \\"possibly_sensitive\\": false,\\n        \\"lang\\": \\"en\\",\\n        \\"public_metrics\\": {\\n          \\"retweet_count\\": 12946,\\n          \\"reply_count\\": 3385,\\n          \\"like_count\\": 25410,\\n          \\"quote_count\\": 4204\\n        },\\n        \\"source\\": \\"Twitter for iPhone\\"\\n      }\\n    ]\\n  },\\n  \\"matching_rules\\": [\\n    {\\n      \\"id\\": 1352504259611291648,\\n      \\"tag\\": null\\n    }\\n  ]\\n}"')
# print(type(exmp[1]))
# data = json.loads(exmp[1])
# data = json.loads(data)
# for i in data:
#     print(i)
# print(type(data))
# print(data)
# for i in data:
#     print(i)



ex = {'data': {
        'conversation_id': '1352530488947322880', 
        'referenced_tweets': [{'type': 'retweeted', 'id': '1352507617852190720'}], 
        'attachments': {'media_keys': ['3_1352507615843123200']}, 
        'author_id': '743553354', 
        'created_at': '2021-01-22T08:16:12.000Z', 
        'entities': {
            'mentions': [{'start': 3, 'end': 11, 'username': 'Reuters'}], 
            'annotations': [{'start': 13, 'end': 17, 'probability': 0.9434, 'type': 'Place', 'normalized_text': 'Japan'}, {'start': 51, 'end': 55, 'probability': 0.4835, 'type': 'Place', 'normalized_text': 'COVID'}], 
            'urls': [{
                'start': 78, 'end': 101, 
                'url': 'https://t.co/QMvjB8nq0f', 
                'expanded_url': 'http://reut.rs/3pbCjFl', 
                'display_url': 'reut.rs/3pbCjFl', 
                'images': [{
                    'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=orig', 
                    'width': 800, 
                    'height': 533
                    }, 
                    {'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=150x150', 
                    'width': 150, 
                    'height': 150
                }], 
                'status': 200, 
                'title': 'Japan tourism push linked to surge in COVID-19 infections -study', 
                'description': "A domestic tourism campaign promoted by Japan's Prime Minister Yoshihide Suga may have contributed to a sharp increase in coronavirus infection cases in the country, a prominent adviser to the government's pandemic response said.", 
                'unwound_url': 'https://www.reuters.com/article/us-health-coronavirus-japan-travel-idUSKBN29R0J2?taid=600a747ec8ffe70001f649db&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter'},
                {'start': 102, 
                'end': 125, 
                'url': 'https://t.co/vQjiY8G6h6', 
                'expanded_url': 'https://twitter.com/Reuters/status/1352507617852190720/photo/1', 
                'display_url': 'pic.twitter.com/vQjiY8G6h6'
            }]
        },
        'text': 'RT @Reuters: Japan tourism push linked to surge in COVID-19 infections -study https://t.co/QMvjB8nq0f https://t.co/vQjiY8G6h6', 'id': '1352530488947322880', 'possibly_sensitive': False, 'lang': 'en', 'public_metrics': {'retweet_count': 49, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}, 'source': 'Twitter for iPhone'}, 'includes': {'media': [{'media_key': '3_1352507615843123200', 'type': 'photo', 'url': 'https://pbs.twimg.com/media/EsUSgr5XAAAZK7j.jpg'}], 'users': [{'username': 'ptialex77', 'profile_image_url': 'https://pbs.twimg.com/profile_images/1042991180399534080/zkqzsDkh_normal.jpg', 'name': 'Alessio S 🇫🇷🇮🇹⭐️⭐️', 'id': '743553354', 'verified': False}, {'username': '    Reuters', 'entities': {'url': {'urls': [{'start': 0, 'end': 22, 'url': 'http://t.co/BmHxhkm3Mh', 'expanded_url': 'http://www.reuters.com', 'display_url': 'reuters.com'}]}, 'description': {'mentions': [{'start': 97, 'end': 108, 'username': 'ReutersBiz'}]}}, 'profile_image_url': 'https://pbs.twimg.com/profile_images/1194751949821939712/3VBu4_Sa_normal.jpg', 'name': 'Reuters', 'id': '1652541', 'verified': True}], 'tweets': [{'conversation_id': '1352507617852190720', 'attachments': {'media_keys': ['3_1352507615843123200']}, 'author_id': '1652541', 'created_at': '2021-01-22T06:45:19.000Z', 'entities': {'annotations': [{'start': 0, 'end': 4, 'probability': 0.9445, 'type': 'Place', 'normalized_text': 'Japan'}, {'start': 38, 'end': 42, 'probability': 0.5325, 'type': 'Place', 'normalized_text': 'COVID'}], 'urls': [{'start': 65, 'end': 88, 'url': 'https://t.co/QMvjB8nq0f', 'expanded_url': 'http://reut.rs/3pbCjFl', 'display_url': 'reut.rs/3pbCjFl', 'images': [{'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=orig', 'width': 800, 'height': 533}, {'url': 'https://pbs.twimg.com/news_img/1352507620070985728/HpUbReYS?format=jpg&name=150x150', 'width': 150, 'height': 150}], 'status': 200, 'title': 'Japan tourism push linked to surge in COVID-19 infections -study', 'description': "A domestic tourism campaign promoted by Japan's Prime Minister Yoshihide Suga may have contributed to a sharp increase in coronavirus infection cases in the country, a prominent adviser to the government's pandemic response said.", 'unwound_url': 'https://www.reuters.com/article/us-health-coronavirus-japan-travel-idUSKBN29R0J2?taid=600a747ec8ffe70001f649db&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter'}, {'start': 89, 'end': 112, 'url': 'https://t.co/vQjiY8G6h6', 'expanded_url': 'https://twitter.com/Reuters/status/1352507617852190720/photo/1', 'display_url': 'pic.twitter.com/vQjiY8G6h6'}]}, 'text': 'Japan tourism push linked to surge in COVID-19 infections -study https://t.co/QMvjB8nq0f https://t.co/vQjiY8G6h6', 'id': '1352507617852190720', 'possibly_sensitive': False, 'lang': 'en', 'public_metrics': {'retweet_count': 49, 'reply_count': 4, 'like_count': 87, 'quote_count': 13}, 'source': 'True Anthem'}]}, 'matching_rules': [{'id': 1352504259611291648, 'tag': None}]}
ex = str(ex)
print(type(ex))
ex = eval(ex)