from parser import parse_news
from gigachat_module import get_gigachat_answer
from dotenv import load_dotenv
import os

load_dotenv()
id = os.getenv('ID')

rss_link = "https://sports.yahoo.com/nba/rss.xml"
news = []

with open("post_instruction.txt", "r") as f:
    instruction = f.read()

news = parse_news(rss_link)
result = get_gigachat_answer(id, news, instruction)

with open('digest.txt', 'w') as f:
    f.write(result)

print(result)
