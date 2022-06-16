#!/usr/bin/env python
# coding: utf-8

# Biblioteca Beautiful Soup
# 
# - biblioteca própria pra se coletar dados HTML

# In[3]:


from bs4 import BeautifulSoup


# In[4]:


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[5]:


soup = BeautifulSoup( html_doc, 'html.parser')


# In[6]:


soup


# In[7]:


# Retornando o títuto do html
soup.title


# In[8]:


# Retornando o corpo do html
soup.body


# In[9]:


# Retornando todo o html
soup.html


# In[10]:


# Retornando o primeiro parágrafo do corpo do html
soup.body.p


# In[11]:


# Retornando todos os parágrafo do corpo do html
soup.find_all('p')


# In[12]:


# Retornando todos o primeiro parágrafo do corpo do html
soup.find_all('p')[1]


# In[17]:


# Retornando todos o segundo parágrafo do corpo do html
soup.find_all('p')[2]


# In[20]:


# Retornando todos os parágrafos onde a classes se chama 'story'
soup.find_all('p', class_ = 'story')


# In[21]:


# Retornando todos os parágrafos onde a classes se chama 'title'
soup.find_all('p', class_ = 'title')


# In[23]:


# Retornando todos links 
soup.find_all('a', class_ = 'sister')


# In[24]:


# Retornando apenas um link
soup.find_all('a', id = 'link1')


# In[25]:


# Retornando apenas um link fora da lista []
soup.find_all('a', id = 'link1')[0]


# In[26]:


# Retornando apenas um elemento Elsie
soup.find_all('a', id = 'link1')[0].get_text()


# In[27]:


# Retornando apenas um elemento Elsie - outra forma
soup.find_all('a', id = 'link1')[0].string

