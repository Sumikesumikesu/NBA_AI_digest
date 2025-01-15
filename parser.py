import feedparser
from datetime import date


def parse_news(rss_link: str) -> str:
    feed = feedparser.parse(rss_link)

    # import json
    # with open('feed.json', 'w') as f:
    #     json.dump(feed, f)

    # with open('feed.json', 'r') as f:
    #     data = json.load(f)

    entries = feed['entries']
    news_list = []

    today = str(date.today())[-2:]

    for entry in entries:
        if (int(entry['published_parsed'][2]) == int(today)):
            news_list.append(
                "\n".join([entry['title'], entry['summary']])
            )

    print(f'Количество новостей: {len(news_list)}')
    result = "\n---\n".join(news_list)

    with open("news.txt", "w") as f:
        f.write(result)

    return result
