#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[8]:


def getSubject():
    subjects = []
    request = requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")
    html = request.text
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.findAll("div", {"class": "tcb-flex-col"})
    for div in divs:
        chapters = div.findAll("a")
        for chapter in chapters:
            subjects.append(chapter.text)
    return subjects


# In[16]:


if __name__ == "__main__":
    subjects = getSubject()
    for i in range(len(subjects)):
        print("{0:2d}. {1}".format(i + 1, subjects[i]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




