#!/usr/bin/env python
# coding: utf-8

# In[1]:




import requests

import pandas as pd

import numpy as np

import math

from datetime import datetime

from bs4 import BeautifulSoup


# In[2]:


#============================================== CLASSICS =============================================

# Browser camouflage for website request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Website URL for all ClassicS Books
url_classic = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'

# Request
page = requests.get( url_classic, headers=headers )
page

# Returning the page's HTML
page.text

# Instantiating Beautiful Soup object
soup = BeautifulSoup(page.text, 'html.parser')
soup

# HTML structure (Class) where the showcase is stored (vitrine)
products = soup.find('ol', class_ = 'row')
products

#  HTML Structure (Class) where data is stored (all)
product_list = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list

# Returning first element of product_list
product_list[0]

# Number of items in the product_list
len(product_list)

product_list[0].get_text

#  HTML Structure (Class) where data is stored (details)
product_list_details = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list_details

#============================== Name ==============================
#============================== Price =============================
#============================== Stock =============================
#============================== Botton ============================

# Details
product_list_details[0].get_text()

#List de all products withe details (Name, Price, Stock, Botton)
product_all = [list(filter(None, p.get_text().split('\n'))) for p in product_list_details]
product_all

# Create DataFrame 
df = pd.DataFrame(product_all)

# Rename colomns DataFrame
df.columns = ['product_name','product_price','none','product_stock','none1','botton']

# Delete colmun
df.drop(["none", "none1"], axis=1, inplace=True)

#============================== Classification (STARS) ==============================

product_list_classification = products.find_all('p', class_= 'star-rating')
product_list_classification

# Counting the products on the page
len(product_list_classification)

# Extracting the number of stars per book
product_star = [product.p['class'] for product in product_list_details]
product_star = [p[1] for p in product_star] 

# Create DataFrame
df_star = pd.DataFrame(product_star)

# Rename column
df_star.columns = ['star']

#============================================== DATA =============================================

# Create DataFrame Finaly
data_classic = pd.concat([df, df_star], axis=1, ignore_index=True)

data_classic['product_catalog'] = 'Classic'
data_classic

# Rename de columns
data_classic.columns = ['product_name','product_price','product_stock','product_boton', 'product_star', 'product_catalog']

data_classic


# In[3]:


#============================================== SCIENCE FICTION =============================================

# Browser camouflage for website request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Website URL for all ClassicS Books
url_science = 'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'

# Request
page = requests.get( url_science, headers=headers )
page

# Returning the page's HTML
page.text

# Instantiating Beautiful Soup object
soup = BeautifulSoup(page.text, 'html.parser')
soup

# HTML structure (Class) where the showcase is stored (vitrine)
products = soup.find('ol', class_ = 'row')
products

#  HTML Structure (Class) where data is stored (all)
product_list = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list

# Returning first element of product_list
product_list[0]

# Number of items in the product_list
len(product_list)

product_list[0].get_text

#  HTML Structure (Class) where data is stored (details)
product_list_details = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list_details

#============================== Name ==============================
#============================== Price =============================
#============================== Stock =============================
#============================== Botton ============================

# Details
product_list_details[0].get_text()

#List de all products withe details (Name, Price, Stock, Botton)
product_all = [list(filter(None, p.get_text().split('\n'))) for p in product_list_details]
product_all

# Create DataFrame 
df = pd.DataFrame(product_all)

# Rename colomns DataFrame
df.columns = ['product_name','product_price','none','product_stock','none1','botton']

# Delete colmun
df.drop(["none", "none1"], axis=1, inplace=True)

#============================== Classification (STARS) ==============================

product_list_classification = products.find_all('p', class_= 'star-rating')
product_list_classification

# Counting the products on the page
len(product_list_classification)

# Extracting the number of stars per book
product_star = [product.p['class'] for product in product_list_details]
product_star = [p[1] for p in product_star] 

# Create DataFrame
df_star = pd.DataFrame(product_star)

# Rename column
df_star.columns = ['star']

#============================================== DATA =============================================

# Create DataFrame Finaly
data_science = pd.concat([df, df_star], axis=1, ignore_index=True)
data_science

data_science['product_catalog'] = 'Science Fiction '
data_science

# Rename de columns
data_science.columns = ['product_name','product_price','product_stock','product_boton', 'product_star', 'product_catalog']

data_science


# In[4]:


#============================================== HUMOR =============================================

# Browser camouflage for website request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Website URL for all ClassicS Books
url_humor = 'https://books.toscrape.com/catalogue/category/books/humor_30/index.html'

# Request
page = requests.get( url_humor, headers=headers )
page

# Returning the page's HTML
page.text

# Instantiating Beautiful Soup object
soup = BeautifulSoup(page.text, 'html.parser')
soup

# HTML structure (Class) where the showcase is stored (vitrine)
products = soup.find('ol', class_ = 'row')
products

#  HTML Structure (Class) where data is stored (all)
product_list = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list

# Returning first element of product_list
product_list[0]

# Number of items in the product_list
len(product_list)

product_list[0].get_text

#  HTML Structure (Class) where data is stored (details)
product_list_details = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list_details

#============================== Name ==============================
#============================== Price =============================
#============================== Stock =============================
#============================== Botton ============================

# Details
product_list_details[0].get_text()

#List de all products withe details (Name, Price, Stock, Botton)
product_all = [list(filter(None, p.get_text().split('\n'))) for p in product_list_details]
product_all

# Create DataFrame 
df = pd.DataFrame(product_all)

# Rename colomns DataFrame
df.columns = ['product_name','product_price','none','product_stock','none1','botton']

# Delete colmun
df.drop(["none", "none1"], axis=1, inplace=True)

#============================== Classification (STARS) ==============================

product_list_classification = products.find_all('p', class_= 'star-rating')
product_list_classification

# Counting the products on the page
len(product_list_classification)

# Extracting the number of stars per book
product_star = [product.p['class'] for product in product_list_details]
product_star = [p[1] for p in product_star] 

# Create DataFrame
df_star = pd.DataFrame(product_star)

# Rename column
df_star.columns = ['star']

#============================================== DATA =============================================

# Create DataFrame Finaly
data_humor = pd.concat([df, df_star], axis=1, ignore_index=True)
data_humor

data_humor['product_catalog'] = ' Humor '
data_humor

# Rename de columns
data_humor.columns = ['product_name','product_price','product_stock','product_boton', 'product_star', 'product_catalog']

data_humor


# In[5]:


#============================================== BUSINESS =============================================

# Browser camouflage for website request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Website URL for all ClassicS Books
url_business = 'https://books.toscrape.com/catalogue/category/books/business_35/index.html'

# Request
page = requests.get( url_business, headers=headers )
page

# Returning the page's HTML
page.text

# Instantiating Beautiful Soup object
soup = BeautifulSoup(page.text, 'html.parser')
soup

# HTML structure (Class) where the showcase is stored (vitrine)
products = soup.find('ol', class_ = 'row')
products

#  HTML Structure (Class) where data is stored (all)
product_list = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list

# Returning first element of product_list
product_list[0]

# Number of items in the product_list
len(product_list)

product_list[0].get_text

#  HTML Structure (Class) where data is stored (details)
product_list_details = products.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
product_list_details

#============================== Name ==============================
#============================== Price =============================
#============================== Stock =============================
#============================== Botton ============================

# Details
product_list_details[0].get_text()

#List de all products withe details (Name, Price, Stock, Botton)
product_all = [list(filter(None, p.get_text().split('\n'))) for p in product_list_details]
product_all

# Create DataFrame 
df = pd.DataFrame(product_all)

# Rename colomns DataFrame
df.columns = ['product_name','product_price','none','product_stock','none1','botton']

# Delete colmun
df.drop(["none", "none1"], axis=1, inplace=True)

#============================== Classification (STARS) ==============================

product_list_classification = products.find_all('p', class_= 'star-rating')
product_list_classification

# Counting the products on the page
len(product_list_classification)

# Extracting the number of stars per book
product_star = [product.p['class'] for product in product_list_details]
product_star = [p[1] for p in product_star] 

# Create DataFrame
df_star = pd.DataFrame(product_star)

# Rename column
df_star.columns = ['star']

#============================================== DATA =============================================

# Create DataFrame Finaly
data_business = pd.concat([df, df_star], axis=1, ignore_index=True)
data_business

data_business['product_catalog'] = ' Business '
data_business

# Rename de columns
data_business.columns = ['product_name','product_price','product_stock','product_boton', 'product_star', 'product_catalog']

data_business


# In[6]:


data_row = pd.concat([data_classic, data_science, data_humor, data_business],ignore_index=True)

# Delete colmun
data_row.drop(['product_boton'], axis=1, inplace=True)

data_row


# In[7]:


data_row


# In[8]:


data_row['product_price'] = data_row['product_price'].apply(lambda x: x[-5:])


# In[9]:


data_row


# In[10]:


data_row.to_csv('data_row.csv')

