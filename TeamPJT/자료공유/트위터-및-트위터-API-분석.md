# 트위터 및 트위터 API 분석

## 트윗 종류

### 일반 트윗

![트위터-및-트위터-API-분석-image-0](images/트위터-및-트위터-API-분석-image-0.png)

[https://twitter.com/BTS_twt/status/1347073897728929792](https://twitter.com/BTS_twt/status/1347073897728929792)

### 리트윗

![트위터-및-트위터-API-분석-image-1](images/트위터-및-트위터-API-분석-image-1.png)

[https://twitter.com/TIME/status/1337040806092414981](https://twitter.com/TIME/status/1337040806092414981)

### 답글 트윗

![트위터-및-트위터-API-분석-image-2](images/트위터-및-트위터-API-분석-image-2.png)

[https://twitter.com/BTS_twt/status/1335613670429052928](https://twitter.com/BTS_twt/status/1335613670429052928)

### 인용 트윗

![트위터-및-트위터-API-분석-image-3](images/트위터-및-트위터-API-분석-image-3.png)

[https://twitter.com/BTS_twt/status/1331808296752140288](https://twitter.com/BTS_twt/status/1331808296752140288)

## 트윗 API Response 스키마

- <details><summary>Tweet</summary>

   ```bash
   {
       "data": {
           "context_annotations": [
               {
                   "domain": {
                       "id": "65",
                       "name": "Interests and Hobbies Vertical",
                       "description": "Top level interests and hobbies groupings, like Food or Travel"
                   },
                   "entity": {
                       "id": "848920371311001600",
                       "name": "Technology",
                       "description": "Technology and computing"
                   }
               },
               {
                   "domain": {
                       "id": "66",
                       "name": "Interests and Hobbies Category",
                       "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
                   },
                   "entity": {
                       "id": "898673391980261376",
                       "name": "Web development",
                       "description": "Web Development"
                   }
               },
               {
                   "domain": {
                       "id": "119",
                       "name": "Holiday",
                       "description": "Holidays like Christmas or Halloween"
                   },
                   "entity": {
                       "id": "1319305164751163393",
                       "name": "New Years Eve",
                       "description": "This entity includes all conversations for New Years Eve for all years."
                   }
               },
               {
                   "domain": {
                       "id": "119",
                       "name": "Holiday",
                       "description": "Holidays like Christmas or Halloween"
                   },
                   "entity": {
                       "id": "1338455498958368768",
                       "name": "Happy New Year"
                   }
               },
               {
                   "domain": {
                       "id": "119",
                       "name": "Holiday",
                       "description": "Holidays like Christmas or Halloween"
                   },
                   "entity": {
                       "id": "1338455498958368768",
                       "name": "Happy New Year"
                   }
               }
           ],
           "conversation_id": "1341072021099327489",
           "lang": "en",
           "id": "1341072021099327489",
           "created_at": "2020-12-21T17:24:20.000Z",
           "attachments": {
               "media_keys": [
                   "3_1341071914127806465"
               ]
           },
           "public_metrics": {
               "retweet_count": 1530,
               "reply_count": 161,
               "like_count": 5065,
               "quote_count": 450
           },
           "text": "As 2020 comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. The demo is available now whether you want to play with it during the holiday, or when work picks back up in the new year. https://t.co/C9BgkgOI5A https://t.co/F35mvs5OaM",
           "source": "Twitter Web App",
           "possibly_sensitive": false,
           "author_id": "1566463268",
           "entities": {
               "urls": [
                   {
                       "start": 254,
                       "end": 277,
                       "url": "https://t.co/C9BgkgOI5A",
                       "expanded_url": "https://reactjs.org/server-components",
                       "display_url": "reactjs.org/server-compone…",
                       "images": [
                           {
                               "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=orig",
                               "width": 1200,
                               "height": 630
                           },
                           {
                               "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=150x150",
                               "width": 150,
                               "height": 150
                           }
                       ],
                       "status": 200,
                       "title": "Introducing Zero-Bundle-Size React Server Components – React Blog",
                       "description": "2020 has been a long year. As it comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. To introduce React Server Components, we have prepared a talk and a demo. If you want, you can check them out during the holidays, or later when work picks back up in the new year. React Server Components are still in research and development. We are sharing this work in the spirit of transparency and to get initial feedback from the React…",
                       "unwound_url": "https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html"
                   },
                   {
                       "start": 278,
                       "end": 301,
                       "url": "https://t.co/F35mvs5OaM",
                       "expanded_url": "https://twitter.com/reactjs/status/1341072021099327489/photo/1",
                       "display_url": "pic.twitter.com/F35mvs5OaM"
                   }
               ]
           }
       },
       "includes": {
           "media": [
               {
                   "media_key": "3_1341071914127806465",
                   "width": 2560,
                   "height": 1440,
                   "type": "photo",
                   "url": "https://pbs.twimg.com/media/EpxxzPPXUAE-iqM.jpg"
               }
           ],
           "users": [
               {
                   "username": "reactjs",
                   "description": "React is a declarative, efficient, and flexible JavaScript library for building user interfaces.",
                   "created_at": "2013-07-03T18:58:09.000Z",
                   "url": "http://t.co/EF5xem8t5W",
                   "pinned_tweet_id": "1341072021099327489",
                   "public_metrics": {
                       "followers_count": 451219,
                       "following_count": 263,
                       "tweet_count": 2280,
                       "listed_count": 5389
                   },
                   "protected": false,
                   "id": "1566463268",
                   "profile_image_url": "https://pbs.twimg.com/profile_images/446356636710363136/OYIaJ1KK_normal.png",
                   "verified": false,
                   "name": "React",
                   "entities": {
                       "url": {
                           "urls": [
                               {
                                   "start": 0,
                                   "end": 22,
                                   "url": "http://t.co/EF5xem8t5W",
                                   "expanded_url": "http://facebook.github.io/react/",
                                   "display_url": "facebook.github.io/react/"
                               }
                           ]
                       }
                   }
               }
           ]
       }
   }
   ```

  </details>

- <details><summary>User</summary>

   ```bash
   {
       "data": {
           "url": "http://t.co/EF5xem8t5W",
           "username": "reactjs",
           "pinned_tweet_id": "1341072021099327489",
           "id": "1566463268",
           "public_metrics": {
               "followers_count": 451220,
               "following_count": 263,
               "tweet_count": 2280,
               "listed_count": 5389
           },
           "verified": false,
           "profile_image_url": "https://pbs.twimg.com/profile_images/446356636710363136/OYIaJ1KK_normal.png",
           "created_at": "2013-07-03T18:58:09.000Z",
           "description": "React is a declarative, efficient, and flexible JavaScript library for building user interfaces.",
           "protected": false,
           "entities": {
               "url": {
                   "urls": [
                       {
                           "start": 0,
                           "end": 22,
                           "url": "http://t.co/EF5xem8t5W",
                           "expanded_url": "http://facebook.github.io/react/",
                           "display_url": "facebook.github.io/react/"
                       }
                   ]
               }
           },
           "name": "React"
       },
       "includes": {
           "tweets": [
               {
                   "source": "Twitter Web App",
                   "text": "As 2020 comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. The demo is available now whether you want to play with it during the holiday, or when work picks back up in the new year. https://t.co/C9BgkgOI5A https://t.co/F35mvs5OaM",
                   "reply_settings": "everyone",
                   "author_id": "1566463268",
                   "id": "1341072021099327489",
                   "lang": "en",
                   "possibly_sensitive": false,
                   "attachments": {
                       "media_keys": [
                           "3_1341071914127806465"
                       ]
                   },
                   "created_at": "2020-12-21T17:24:20.000Z",
                   "public_metrics": {
                       "retweet_count": 1530,
                       "reply_count": 161,
                       "like_count": 5066,
                       "quote_count": 450
                   },
                   "context_annotations": [
                       {
                           "domain": {
                               "id": "65",
                               "name": "Interests and Hobbies Vertical",
                               "description": "Top level interests and hobbies groupings, like Food or Travel"
                           },
                           "entity": {
                               "id": "848920371311001600",
                               "name": "Technology",
                               "description": "Technology and computing"
                           }
                       },
                       {
                           "domain": {
                               "id": "66",
                               "name": "Interests and Hobbies Category",
                               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
                           },
                           "entity": {
                               "id": "898673391980261376",
                               "name": "Web development",
                               "description": "Web Development"
                           }
                       },
                       {
                           "domain": {
                               "id": "119",
                               "name": "Holiday",
                               "description": "Holidays like Christmas or Halloween"
                           },
                           "entity": {
                               "id": "1319305164751163393",
                               "name": "New Years Eve",
                               "description": "This entity includes all conversations for New Years Eve for all years."
                           }
                       },
                       {
                           "domain": {
                               "id": "119",
                               "name": "Holiday",
                               "description": "Holidays like Christmas or Halloween"
                           },
                           "entity": {
                               "id": "1338455498958368768",
                               "name": "Happy New Year"
                           }
                       },
                       {
                           "domain": {
                               "id": "119",
                               "name": "Holiday",
                               "description": "Holidays like Christmas or Halloween"
                           },
                           "entity": {
                               "id": "1338455498958368768",
                               "name": "Happy New Year"
                           }
                       }
                   ],
                   "entities": {
                       "urls": [
                           {
                               "start": 254,
                               "end": 277,
                               "url": "https://t.co/C9BgkgOI5A",
                               "expanded_url": "https://reactjs.org/server-components",
                               "display_url": "reactjs.org/server-compone…",
                               "images": [
                                   {
                                       "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=orig",
                                       "width": 1200,
                                       "height": 630
                                   },
                                   {
                                       "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=150x150",
                                       "width": 150,
                                       "height": 150
                                   }
                               ],
                               "status": 200,
                               "title": "Introducing Zero-Bundle-Size React Server Components – React Blog",
                               "description": "2020 has been a long year. As it comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. To introduce React Server Components, we have prepared a talk and a demo. If you want, you can check them out during the holidays, or later when work picks back up in the new year. React Server Components are still in research and development. We are sharing this work in the spirit of transparency and to get initial feedback from the React…",
                               "unwound_url": "https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html"
                           },
                           {
                               "start": 278,
                               "end": 301,
                               "url": "https://t.co/F35mvs5OaM",
                               "expanded_url": "https://twitter.com/reactjs/status/1341072021099327489/photo/1",
                               "display_url": "pic.twitter.com/F35mvs5OaM"
                           }
                       ]
                   },
                   "conversation_id": "1341072021099327489"
               }
           ]
       }
   }
   ```

  </details>

- <details><summary>인용 트윗</summary>

   ```bash
   {
       "data": {
           "created_at": "2021-01-07T14:57:40.000Z",
           "text": "인용 테스트 https://t.co/FfHXQcjuzl",
           "referenced_tweets": [
               {
                   "type": "quoted",
                   "id": "1347110938810351617"
               }
           ],
           "conversation_id": "1347195704511397891",
           "public_metrics": {
               "retweet_count": 0,
               "reply_count": 0,
               "like_count": 0,
               "quote_count": 1
           },
           "lang": "ko",
           "source": "Twitter Web App",
           "author_id": "2801309100",
           "possibly_sensitive": false,
           "entities": {
               "urls": [
                   {
                       "start": 7,
                       "end": 30,
                       "url": "https://t.co/FfHXQcjuzl",
                       "expanded_url": "https://twitter.com/YHC_sinvibe/status/1347110938810351617",
                       "display_url": "twitter.com/YHC_sinvibe/st…"
                   }
               ]
           },
           "id": "1347195704511397891"
       },
       "includes": {
           "users": [
               {
                   "protected": false,
                   "username": "YHC_sinvibe",
                   "name": "추연호",
                   "id": "2801309100",
                   "profile_image_url": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                   "url": "",
                   "verified": false,
                   "description": "",
                   "created_at": "2014-09-10T08:03:32.000Z",
                   "public_metrics": {
                       "followers_count": 0,
                       "following_count": 1,
                       "tweet_count": 15,
                       "listed_count": 0
                   }
               }
           ],
           "tweets": [
               {
                   "attachments": {
                       "media_keys": [
                           "3_1347110931570982912"
                       ]
                   },
                   "created_at": "2021-01-07T09:20:50.000Z",
                   "text": "jpg 이미지 테스트 https://t.co/raLwILxmIH",
                   "conversation_id": "1347110938810351617",
                   "public_metrics": {
                       "retweet_count": 0,
                       "reply_count": 0,
                       "like_count": 0,
                       "quote_count": 1
                   },
                   "lang": "ko",
                   "source": "Twitter Web App",
                   "author_id": "2801309100",
                   "possibly_sensitive": false,
                   "entities": {
                       "urls": [
                           {
                               "start": 12,
                               "end": 35,
                               "url": "https://t.co/raLwILxmIH",
                               "expanded_url": "https://twitter.com/YHC_sinvibe/status/1347110938810351617/photo/1",
                               "display_url": "pic.twitter.com/raLwILxmIH"
                           }
                       ]
                   },
                   "id": "1347110938810351617"
               }
           ]
       }
   }
   ```

  </details>

- <details><summary>답글 트윗</summary>

   ```bash
   {
       "data": {
           "possibly_sensitive": false,
           "text": "@wycats Anyway, I think this confusion is unfortunate but ironic given the pedantism around the use of “argument” vs “parameter” in some circles. Maybe some people just gave up trying to remember which one is at which side.",
           "entities": {
               "mentions": [
                   {
                       "start": 0,
                       "end": 7,
                       "username": "wycats"
                   }
               ]
           },
           "referenced_tweets": [
               {
                   "type": "replied_to",
                   "id": "1346688852157747200"
               }
           ],
           "conversation_id": "1346655693785296897",
           "source": "Twitter for iPhone",
           "id": "1346690013598261248",
           "created_at": "2021-01-06T05:28:14.000Z",
           "public_metrics": {
               "retweet_count": 0,
               "reply_count": 0,
               "like_count": 2,
               "quote_count": 0
           },
           "in_reply_to_user_id": "70345946",
           "author_id": "70345946",
           "lang": "en"
       },
       "includes": {
           "users": [
               {
                   "url": "https://t.co/W27BzAGyLJ",
                   "profile_image_url": "https://pbs.twimg.com/profile_images/1336281436685541376/fRSl8uJP_normal.jpg",
                   "name": "Dan Abramov",
                   "public_metrics": {
                       "followers_count": 284503,
                       "following_count": 198,
                       "tweet_count": 76785,
                       "listed_count": 4877
                   },
                   "created_at": "2009-08-31T08:28:07.000Z",
                   "description": "I didn’t make @reactjs • Please ask technical questions on GitHub issues rather than in mentions • 🔭https://t.co/ecBhI5FZj6 • he/him",
                   "verified": false,
                   "id": "70345946",
                   "entities": {
                       "url": {
                           "urls": [
                               {
                                   "start": 0,
                                   "end": 23,
                                   "url": "https://t.co/W27BzAGyLJ",
                                   "expanded_url": "http://overreacted.io",
                                   "display_url": "overreacted.io"
                               }
                           ]
                       },
                       "description": {
                           "urls": [
                               {
                                   "start": 100,
                                   "end": 123,
                                   "url": "https://t.co/ecBhI5FZj6",
                                   "expanded_url": "http://JustJavaScript.com",
                                   "display_url": "JustJavaScript.com"
                               }
                           ],
                           "mentions": [
                               {
                                   "start": 14,
                                   "end": 22,
                                   "username": "reactjs"
                               }
                           ]
                       }
                   },
                   "username": "dan_abramov",
                   "protected": false
               },
               {
                   "location": "Portland, OR",
                   "url": "https://t.co/BQFEaD4Fvx",
                   "profile_image_url": "https://pbs.twimg.com/profile_images/861010112852262912/nbPZKMyR_normal.jpg",
                   "name": "Yehuda Katz #BlackLivesMatter",
                   "public_metrics": {
                       "followers_count": 67600,
                       "following_count": 1089,
                       "tweet_count": 48142,
                       "listed_count": 3257
                   },
                   "created_at": "2007-08-30T04:07:52.000Z",
                   "description": "Tilde Co-Founder, OSS enthusiast and @wykittens's parent. Co-author of the Extensible Web Manifesto. Front-end developer. @wifelette's husband. he/him",
                   "pinned_tweet_id": "675498087717056512",
                   "verified": true,
                   "id": "8526432",
                   "entities": {
                       "url": {
                           "urls": [
                               {
                                   "start": 0,
                                   "end": 23,
                                   "url": "https://t.co/BQFEaD4Fvx",
                                   "expanded_url": "http://yehudakatz.com",
                                   "display_url": "yehudakatz.com"
                               }
                           ]
                       },
                       "description": {
                           "mentions": [
                               {
                                   "start": 37,
                                   "end": 47,
                                   "username": "wykittens"
                               },
                               {
                                   "start": 122,
                                   "end": 132,
                                   "username": "wifelette"
                               }
                           ]
                       }
                   },
                   "username": "wycats",
                   "protected": false
               }
           ],
           "tweets": [
               {
                   "possibly_sensitive": false,
                   "text": "@wycats Maybe we should just embrace the descriptivism and always call properties of args[0] “props”, for functions whose conventions is to take a single object argument.\n\nOkay I’m kidding but just maybe?..",
                   "entities": {
                       "mentions": [
                           {
                               "start": 0,
                               "end": 7,
                               "username": "wycats"
                           }
                       ]
                   },
                   "referenced_tweets": [
                       {
                           "type": "replied_to",
                           "id": "1346687802998714369"
                       }
                   ],
                   "conversation_id": "1346655693785296897",
                   "source": "Twitter for iPhone",
                   "id": "1346688852157747200",
                   "created_at": "2021-01-06T05:23:37.000Z",
                   "public_metrics": {
                       "retweet_count": 0,
                       "reply_count": 4,
                       "like_count": 7,
                       "quote_count": 0
                   },
                   "in_reply_to_user_id": "70345946",
                   "author_id": "70345946",
                   "lang": "en"
               }
           ]
       }
   }
   ```

  </details>

- <details><summary>좋아요, 답글, 리트윗 수를 실시간으로 업데이트 할 것인지는 추후 마일스톤</summary>

   ```bash
   # 외부 링크 및 url, 미디어 첨부
   "entities": {
     "urls": [
         {
             "start": 254,
             "end": 277,
             "url": "https://t.co/C9BgkgOI5A",
             "expanded_url": "https://reactjs.org/server-components",
             "display_url": "reactjs.org/server-compone…",
             "images": [
                 {
                     "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=orig",
                     "width": 1200,
                     "height": 630
                 },
                 {
                     "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=150x150",
                     "width": 150,
                     "height": 150
                 }
             ],
             "status": 200,
             "title": "Introducing Zero-Bundle-Size React Server Components – React Blog",
             "description": "2020 has been a long year. As it comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. To introduce React Server Components, we have prepared a talk and a demo. If you want, you can check them out during the holidays, or later when work picks back up in the new year. React Server Components are still in research and development. We are sharing this work in the spirit of transparency and to get initial feedback from the React…",
             "unwound_url": "https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html"
         },
         {
             "start": 278,
             "end": 301,
             "url": "https://t.co/F35mvs5OaM",
             "expanded_url": "https://twitter.com/reactjs/status/1341072021099327489/photo/1",
             "display_url": "pic.twitter.com/F35mvs5OaM"
         }
     **]**
   },
   ```

   ```bash
   {
       "data": {
           "conversation_id": "1347110938810351617",
           "lang": "ko",
           "id": "1347110938810351617",
           "created_at": "2021-01-07T09:20:50.000Z",
           "attachments": {
               "media_keys": [
                   "3_1347110931570982912"
               ]
           },
           "public_metrics": {
               "retweet_count": 0,
               "reply_count": 0,
               "like_count": 0,
               "quote_count": 1
           },
           "text": "jpg 이미지 테스트 https://t.co/raLwILxmIH",
           "source": "Twitter Web App",
           "possibly_sensitive": false,
           "author_id": "2801309100",
           "entities": {
               "urls": [
                   {
                       "start": 12,
                       "end": 35,
                       "url": "https://t.co/raLwILxmIH",
                       "expanded_url": "https://twitter.com/YHC_sinvibe/status/1347110938810351617/photo/1",
                       "display_url": "pic.twitter.com/raLwILxmIH"
                   }
               ]
           }
       },
       "includes": {
           "media": [
               {
                   "media_key": "3_1347110931570982912",
                   "width": 359,
                   "height": 359,
                   "type": "photo",
                   "url": "https://pbs.twimg.com/media/ErHmQUVVgAAhexc.jpg"
               }
           ],
           "users": [
               {
                   "username": "YHC_sinvibe",
                   "description": "",
                   "created_at": "2014-09-10T08:03:32.000Z",
                   "url": "",
                   "public_metrics": {
                       "followers_count": 0,
                       "following_count": 1,
                       "tweet_count": 15,
                       "listed_count": 0
                   },
                   "protected": false,
                   "id": "2801309100",
                   "profile_image_url": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                   "verified": false,
                   "name": "추연호"
               }
           ]
       }
   }
   ```

  </details>

### 네이밍은 트윗 API 형태를 참조

### 트윗 미디어 형태에 대한 고민

- 모든 미디어 url을 갖고 있고,

- 텍스트에는 shorten 된 url이 담기지만 실제 display url을 전송해 주어야 제대로 보여줄 수 있고

- 동영상 또는 이미지 등은 확장자 명으로 끝나는 데이터를 보내주어야 프론트에서 보여줄 수 있다.

   - 동영상은 썸네일 이미지 까지만 보내주면 됨

   - 미디어 타입은 `video` | `photo` | `animated_gif` 배열

      - photo 는 여러 개일 경우 타일 형태 

      - video, gif 1개 까지만 첨부 가능

   - 외부 링크 url 

      - <details><summary>외부 링크 url 미리보기 형태에 맞춰서 \</summary>

         ```bash
               {
                   "start": 254,
                   "end": 277,
                   "url": "https://t.co/C9BgkgOI5A",
                   "expanded_url": "https://reactjs.org/server-components",
                   "display_url": "reactjs.org/server-compone…",
                   "images": [
                       {
                           "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=orig",
                           "width": 1200,
                           "height": 630
                       },
                       {
                           "url": "https://pbs.twimg.com/news_img/1346310900744146944/EOyaz9ZW?format=png&name=150x150",
                           "width": 150,
                           "height": 150
                       }
                   ],
                   "status": 200,
                   "title": "Introducing Zero-Bundle-Size React Server Components – React Blog",
                   "description": "2020 has been a long year. As it comes to an end we wanted to share a special Holiday Update on our research into zero-bundle-size React Server Components. To introduce React Server Components, we have prepared a talk and a demo. If you want, you can check them out during the holidays, or later when work picks back up in the new year. React Server Components are still in research and development. We are sharing this work in the spirit of transparency and to get initial feedback from the React…",
                   "unwound_url": "https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html"
               },
         ```

        </details>

   - `photo와 외부 링크 url의 조합일 경우` : url이 여러 개일 경우에는 마지막 url이 미리보기로 제공됨

      - 따라서 배열의 순서 지켜야하고 미디어의 타입을 명시해야 함

      ### 트윗 내 관계

- <details><summary>기본 트윗 데이터</summary>

   ```bash
   {
     "source": "Twitter Web App",
     "text": "인용 테스트 https://t.co/FfHXQcjuzl",
     "possibly_sensitive": false,
     "referenced_tweets": [
         {
             "type": "quoted",
             "id": "1347110938810351617"
         },
   			{
   					 "type": "replyed"
   			}
     ],
     "conversation_id": "1347195704511397891",
     "lang": "ko",
     "id": "1347195704511397891",
     "author_id": "2801309100",
     "created_at": "2021-01-07T14:57:40.000Z",
     "entities": {
         "urls": [
             {
                 "start": 7,
                 "end": 30,
                 "url": "https://t.co/FfHXQcjuzl",
                 "expanded_url": "https://twitter.com/YHC_sinvibe/status/1347110938810351617",
                 "display_url": "twitter.com/YHC_sinvibe/st…"
             }
         ]
     }
   }
   ```

  </details>

- 전체 트윗 데이터 

   - 기본 트윗 데이터 및 referenced_Tweet (인용이나 답글을 담는 배열)

      - type `quoted` , `reply` 트윗 기본 데이터 (얘네는 referenced tweet을 안가짐)

   - 인용된 트윗 기본 정보

   - 답글 트윗 기본 정보

- 리트윗

   - 일단 카운트만 증가시키는 걸로 하고, 특별히 DB에 따로 저장하지 않는 것으로 결론 내림

### 데이터 인터페이스 공유

- <details><summary>공식 문서</summary>

   [GET /2/tweets/:id](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id#Response-fields)

   | Name | Type | Description | 제목 |
   | --- | --- | --- | --- |
   | `id` **DEFAULT** | ['string'] | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |     |
   | `text` **DEFAULT** | ['string'] | The content of the Tweet.To return this field, add `tweet.fields=text` in the request's query parameter. |     |
   | `created_at` | ['date (ISO 8601)'] | Creation time of the Tweet.To return this field, add `tweet.fields=created_at` in the request's query parameter. |     |
   | `author_id` | ['string'] | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.users` by adding `expansions=author_id` in the request's query parameter. |     |
   | `conversation_id` | ['string'] | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).To return this field, add `tweet.fields=conversation_id` in the request's query parameter. |     |
   | `in_reply_to_user_id` | ['string'] | If this Tweet is a Reply, indicates the user ID of the parent Tweet's author. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.users` by adding `expansions=in_reply_to_user_id` in the request's query parameter. |     |
   | `referenced_tweets` | ['array'] | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.To return this field, add `tweet.fields=referenced_tweets` in the request's query parameter. |     |
   | `referenced_tweets.type` | ['enum (retweeted,\xa0quoted,\xa0replied_to)'] | Indicates the type of relationship between this Tweet and the Tweet returned in the response: `retweeted` (this Tweet is a Retweet), `quoted` (a Retweet with comment, also known as Quoted Tweet), or `replied_to` (this Tweet is a reply). |     |
   | `referenced_tweets.id` | ['string'] | The unique identifier of the referenced Tweet.You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |     |
   | `attachments` | ['object'] | Specifies the type of attachments (if any) present in this Tweet.To return this field, add `tweet.fields=attachments` in the request's query parameter. |     |
   | `attachments.media_keys` | ['array'] | List of unique identifiers of media attached to this Tweet. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |     |
   | `attachments.poll_ids` | ['array'] | List of unique identifiers of polls present in the Tweets returned. These are returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.polls` by adding `expansions=attachments.polls_ids` in the request's query parameter. |     |
   | `geo` | ['object'] | Contains details about the location tagged by the user in this Tweet, if they specified one.To return this field, add `tweet.fields=geo` in the request's query parameter. |     |
   | `geo.coordinates` | ['object'] | Contains details about the coordinates of the location tagged by the user in this Tweet, if they specified one.To return this field, add `tweet.fields=geo.coordinates` in the request's query parameter. |     |
   | `geo.coordinates.type` | ['string'] | Describes the type of coordinate. The only value supported at present is `Point`. |     |
   | `geo.coordinates.coordinates` | ['array'] | A pair of decimal values representing the precise location of the user (latitude, longitude). This value be `null` unless the user explicitly shared their precise location. |     |
   | `geo.place_id` | ['string'] | The unique identifier of the place, if this is a point of interest tagged in the Tweet.You can obtain the expanded object in `includes.places` by adding `expansions=geo.place_id` in the request's query parameter. |     |
   | `context_annotations` | ['array'] | Contains context annotations for the Tweet.To return this field, add `tweet.fields=context_annotations` in the request's query parameter. |     |
   | `context_annotations.domain` | ['object'] | Contains elements which identify detailed information regarding the domain classification based on Tweet text. |     |
   | `context_annotations.domain.id` | ['string'] | Contains the numeric value of the domain. |     |
   | `context_annotations.domain.name` | ['string'] | Domain name based on the Tweet text. |     |
   | `context_annotations.domain.description` | ['string'] | Long form description of domain classification. |     |
   | `context_annotations.entity` | ['object'] | Contains elements which identify detailed information regarding the domain classification bases on Tweet text. |     |
   | `context_annotations.entity.id` | ['string'] | Unique value which correlates to an explicitly mentioned Person, Place, Product or Organization |     |
   | `context_annotations.entity.name` | ['string'] | Name or reference of entity referenced in the Tweet. |     |
   | `context_annotations.entity.description` | ['string'] | Additional information regarding referenced entity. |     |
   | `entities` | ['object'] | Contains details about text that has a special meaning in a Tweet.To return this field, add `tweet.fields=entities` in the request's query parameter. |     |
   | `entities.annotations` | ['array'] | Contains details about annotations relative to the text within a Tweet. |     |
   | `entities.annotations.start` | ['integer'] | The start position (zero-based) of the text used to annotate the Tweet. |     |
   | `entities.annotations.end` | ['integer'] | The end position (zero based) of the text used to annotate the Tweet. |     |
   | `entities.annotations.probability` | ['number'] | The confidence score for the annotation as it correlates to the Tweet text. |     |
   | `entities.annotations.type` | ['string'] | The description of the type of entity identified when the Tweet text was interpreted. |     |
   | `entities.annotations.normalized_text` | ['string'] | The text used to determine the annotation type. |     |
   | `entities.urls` | ['array'] | Contains details about text recognized as a URL. |     |
   | `entities.urls.start` | ['integer'] | The start position (zero-based) of the recognized URL within the Tweet. |     |
   | `entities.urls.end` | ['integer'] | The end position (zero-based) of the recognized URL within the Tweet. |     |
   | `entities.urls.url` | ['string'] | The URL in the format tweeted by the user. |     |
   | `entities.urls.expanded_url` | ['string'] | The fully resolved URL. |     |
   | `entities.urls.display_url` | ['string'] | The URL as displayed in the Twitter client. |     |
   | `entities.urls.unwound_url` | ['string'] | The full destination URL. |     |
   | `entities.hashtags` | ['array'] | Contains details about text recognized as a Hashtag. |     |
   | `entities.hashtags.start` | ['integer'] | The start position (zero-based) of the recognized Hashtag within the Tweet. |     |
   | `entities.hashtags.end` | ['integer'] | The end position (zero-based) of the recognized Hashtag within the Tweet. |     |
   | `entities.hashtags.tag` | ['string'] | The text of the Hashtag. |     |
   | `entities.mentions` | ['array'] | Contains details about text recognized as a user mention. |     |
   | `entities.mentions.start` | ['integer'] | The start position (zero-based) of the recognized user mention within the Tweet. |     |
   | `entities.mentions.end` | ['integer'] | The end position (zero-based) of the recognized user mention within the Tweet. |     |
   | `entities.mentions.username` | ['string'] | The part of text recognized as a user mention.You can obtain the expanded object in `includes.users` by adding `expansions=entities.mentions.username` in the request's query parameter. |     |
   | `entities.cashtags` | ['array'] | Contains details about text recognized as a Cashtag. |     |
   | `entities.cashtags.start` | ['integer'] | The start position (zero-based) of the recognized Cashtag within the Tweet. |     |
   | `entities.cashtags.end` | ['integer'] | The end position (zero-based) of the recognized Cashtag within the Tweet. |     |
   | `entities.cashtags.tag` | ['string'] | The text of the Cashtag. |     |
   | `withheld` | ['object'] | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).To return this field, add `tweet.fields=withheld` in the request's query parameter. |     |
   | `withheld.copyright` | ['boolean'] | Indicates if the content is being withheld for on the basis of copyright infringement. |     |
   | `withheld.country_codes` | ['array'] | Provides a list of countries where this content is not available. |     |
   | `withheld.scope` | ['enum (tweet,\xa0user)'] | Indicates whether the content being withheld is a Tweet or a user. |     |
   | `public_metrics` | ['object'] | Engagement metrics for the Tweet at the time of the request.To return this field, add `tweet.fields=public_metrics` in the request's query parameter. |     |
   | `public_metrics.retweet_count` | ['integer'] | Number of times this Tweet has been Retweeted. |     |
   | `public_metrics.reply_count` | ['integer'] | Number of Replies of this Tweet. |     |
   | `public_metrics.like_count` | ['integer'] | Number of Likes of this Tweet. |     |
   | `public_metrics.quote_count` | ['integer'] | Number of times this Tweet has been Retweeted with a comment (also known as Quote). |     |
   | `non_public_metrics` | ['object'] | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric, and requires the use of OAuth 1.0a User Context authentication.To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |     |
   | `non_public_metrics.impression_count` | ['integer'] | Number of times the Tweet has been viewed. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `non_public_metrics.url_link_clicks` | ['integer'] | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `non_public_metrics.user_profile_clicks` | ['integer'] | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `organic_metrics` | ['object'] | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication. |     |
   | `organic_metrics.impression_count` | ['integer'] | Number of times the Tweet has been viewed organically. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `organic_metrics.url_link_clicks` | ['integer'] | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `organic_metrics.user_profile_clicks` | ['integer'] | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `organic_metrics.retweet_count` | ['integer'] | Number of times the Tweet has been Retweeted organically. |     |
   | `organic_metrics.reply_count` | ['integer'] | Number of replies the Tweet has received organically. |     |
   | `organic_metrics.like_count` | ['integer'] | Number of likes the Tweet has received organically. |     |
   | `promoted_metrics` | ['object'] | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication. |     |
   | `promoted_metrics.impression_count` | ['integer'] | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `promoted_metrics.url_link_clicks` | ['integer'] | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `promoted_metrics.user_profile_clicks` | ['integer'] | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 1.0a User Context authentication. |     |
   | `promoted_metrics.retweet_count` | ['integer'] | Number of times this Tweet has been Retweeted when that Tweet is being promoted. |     |
   | `promoted_metrics.reply_count` | ['integer'] | Number of Replies to this Tweet when that Tweet is being promoted. |     |
   | `promoted_metrics.like_count` | ['integer'] | Number of Likes of this Tweet when that Tweet is being promoted. |     |
   | `possibly_sensitive` | ['boolean'] | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.To return this field, add `tweet.fields=possibly_sensitive` in the request's query parameter. |     |
   | `lang` | ['string'] | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.To return this field, add `tweet.fields=lang` in the request's query parameter. |     |
   | `reply_settings` | ['string'] | Shows who can reply to this Tweet. Fields returned are `everyone`, `mentionedUsers`, and `following`.To return this field, add `tweet.fields=reply_settings` in the request's query parameter. |     |
   | `source` | ['string'] | The name of the app the user Tweeted from.To return this field, add `tweet.fields=source` in the request's query parameter. |     |
   | `includes` | ['object'] | If you include an [`expansion`](https://developer.twitter.com/en/docs/twitter-api/expansions) parameter, the referenced objects will be returned if available. |     |
   | `includes.tweets` | ['array'] | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |     |
   | `includes.users` | ['array'] | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |     |
   | `includes.places` | ['array'] | When including the `expansions=geo.place_id` parameter, this includes a list of referenced places in Tweets in the form of [place objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) with their default fields and any additional fields requested using the `place.fields` parameter, assuming there is a place present in the returned Tweet(s). |     |
   | `includes.media` | ['array'] | When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s). |     |
   | `includes.polls` | ['string'] | When including the `expansions=attachments.poll_ids` parameter, this includes a list of polls that are attached to Tweets in the form of [poll objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) with their default fields and any additional fields requested using the `poll.fields` parameter, assuming there is a poll present in the returned Tweet(s). |     |
   | `errors` | ['object'] | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |     |

     </details>

- <details><summary>프론트 인터페이스</summary>

   - <details><summary>사용할 필드</summary>

      ```plain text
      expansions:attachments.media_keys,author_id,entities.mentions.username,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id
      media.fields:media_key,preview_image_url,type,url
      tweet.fields:id,text,attachments,author_id,conversation_id,created_at,entities,in_reply_to_user_id,public_metrics,possibly_sensitive,referenced_tweets,source,reply_settings
      user.fields:id,name,username,profile_image_url,verified
      ```

     </details>

   - <details><summary>인터페이스 구현</summary>

      ```typescript
      /**
       * {@link https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id#Response-fields}
       */
      export interface TweetResponse {
        data?: TweetData;
        includes?: Includes;
      
        // errors
        errors?: any[];
        title?: string;
        type?: string;
        status?: number; // status code
        detail?: string;
      }
      
      /**
       * {@link https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet}
       */
      interface TweetData {
        id: string;
        message: string; // text
        attachments?: Attachments;
        author_id: string;
        conversation_id: string;
        created_at: string;
        entities: Entities;
        in_reply_to_user_id?: string;
        lang: string; // BCP47
        possibly_sensitive: false;
        public_metrics: PublicMetrics;
        referenced_tweets?: ReferencedTweet[];
        reply_settings: 'everyone' | 'mentionedUsers' | 'following';
        source: string;
      }
      
      interface ReferencedTweet {
        type: 'retweeted' | 'quoted' | 'replied_to';
        id: string;
      }
      
      interface Attachments {
        media_keys: string[];
      }
      
      interface Entities {
        urls: URLData[];
        mentions: MentionData[];
        hashtags: HashtagData[];
        cashtags: CashtagData[];
      }
      
      interface EntityData {
        start: number;
        end: number;
      }
      interface URLData extends EntityData {
        url: string;
        expanded_url: string;
        display_url: string;
        unwound_url?: string;
      }
      
      interface MentionData extends EntityData {
        username: string;
      }
      
      interface HashtagData extends EntityData {
        tag: string;
      }
      
      type CashtagData = HashtagData;
      
      interface PublicMetrics {
        retweet_count: number;
        reply_count: number;
        like_count: number;
        quote_count: number;
      }
      
      interface Includes {
        tweets?: TweetData[];
        users?: UserData[];
        media?: MediaData[];
      }
      
      /**
       * {@link https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user}
       */
      interface UserData {
        id: string; // 트위터 유저의 고유한 숫자로된 ID
        name: string; // 유저의 표시되는 이름
        username: string; // 유저의 ID @user_Id
        profile_image_url?: string; // (optional) 프로필 이미지 확장자 포맷 URL
        verified?: boolean; // (optional) 공인의 경우 뱃지를 표시하기 위해 필요
      }
      
      /**
       * {@link https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media}
       */
      interface MediaData {
        url: string;
        type: 'photo' | 'video' | 'animated_gif';
        media_key: string;
        preview_image_url?: string; // 'video' | 'animated_gif' 의 경우
      }
      ```

     </details>

     </details>

```sql
data: {
	id
	text
	attachments{media_keys}
	author_id
	conversation_id
	created_at
	entities{cashtags, hashtags, mentions, urls{start, end, url, expanded_url, display_url, unwound_url}}
	in_reply_to_user_id
	lang
	possibly_sensitive
	public_metrics
	referenced_tweets
	reply_settings
	source
	geo{place_id}
}
includes: {
	tweets: [{
		id
		text
		attachments
		author_id
		conversation_id
		created_at
		entities{cashtags, hashtags, mentions, urls{start, end, url, expanded_url, display_url, unwound_url}}
		in_reply_to_user_id
		possibly_sensitive
		public_metrics
		referenced_tweets
		reply_settings
		source
	}]
	users: [{
		id
		name
		username
		profile_image_url
		verified
	}]
	media: [{
		type
		media_key
		url
		preview_image_url
		public_metrics
	}]
	places: [{
		full_name
		id
		country_code
		country
		name
		place_type
	}]
}
```

