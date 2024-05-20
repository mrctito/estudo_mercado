
import json
import os
import random
from typing import Set

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


class AgentTools():

  processed_pages = Set()

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""

    if website in AgentTools.processed_pages:
      return "This website has already been processed"
    else:
      AgentTools.processed_pages.add(website)

    user_agents = [
      "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
      "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
    ]
    random_user_agent = random.choice(user_agents)
    headers = {
      'User-Agent': random_user_agent
    }
    response = requests.get(
      url=os.getenv('SCRAPE_PROXY'),
      headers=headers,
      params={
        'api_key': os.getenv('SCRAPE_API_KEY'),
        'url': website, 
      },
    )        
    if response.status_code != 200:
      return "An error occurred while trying to scrape the website"
    
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []

    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)


  #@tool("Scrape website content")
  def scrape_and_summarize_website_ok(website):
    """Useful to scrape and summarize a website content"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)
