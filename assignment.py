import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://topai.tools/browse"


response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

tool_names = []
tool_urls = []
descriptions = []
pricings = []
tags = []
use_cases = []

for tool in soup.find_all("div", class_="tool"):

    tool_name = tool.find("h4").text.strip()
    tool_names.append(tool_name)


    tool_url = tool.find("a", class_="title")["href"]
    tool_urls.append(tool_url)


    description = tool.find("div", class_="description").text.strip()
    descriptions.append(description)


    pricing = tool.find("div", class_="price").text.strip()
    pricings.append(pricing)

    tag = tool.find("span", class_="tag").text.strip()
    tags.append(tag)

    use_case = tool.find("div", class_="use-cases").text.strip()
    use_cases.append(use_case)

data = {
    "Tool Name": tool_names,
    "Tool URL": tool_urls,
    "What is": descriptions,
    "Pricing": pricings,
    "Tag": tags,
    "Tool possible use cases": use_cases,
}
df = pd.DataFrame(data)

df.to_excel("scraped_tools.xlsx", index=False)
