#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import sqlite3

import sqlalchemy
from sqlalchemy import create_engine


# In[4]:


path = 'C:/Users/Utilizador/repos/Python_ds_ao_dev/Projeto_Book_to_Scrape/data_product_book_cleaned.csv'
data = pd.read_csv(path)

data.drop(["Unnamed: 0"], axis=1, inplace=True)
data = data.reset_index(drop=True)

data.head()


# In[5]:


data.dtypes


# In[6]:


data.columns


# In[7]:


# Creat query
query_showroom_schema = """
    CREATE TABLE book (
        product_name             INTEGER,
        product_price            REAL,
        product_stock            TEXT,
        product_star             TEXT,
        product_catalog          TEXT,
        )
"""


# In[8]:


# Connect to dataset
# Planning the query execution in DB
# Run
# Close conection

try:
    conn = sqlite3.connect('book_db.sqlite')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    query_showroom_schema = "select sqlite_version();"
    cursor.execute(query_showroom_schema)
    conn.commit()
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed")


# In[9]:


conn = create_engine('sqlite:///book_db.sqlite',echo=False, pool_pre_ping=True)
conn


# In[10]:


# insert data to table
data.to_sql( 'book', con=conn, if_exists='append', index=False )


# In[11]:


query = """
    SELECT * FROM book
"""
df = pd.read_sql_query( query, conn )
df.head()


# In[ ]:


#Command - UPDATE
#query = """
#   UPDATE book_vitrine
#  SET product_catalog = 'New'
#  WHERE product_name = 'The Secret Garden'
#"""


## Command - DROP TABLE
#query = """
#   DROP TABLE vitrine
#"""

## Command - ALTER TABLE
#query = """
# ALTER TABLE vitrine
# RENAME TO vitrine_two
#"""

## Command - CREATE INDEX
#query = """
# CREATE INDEX idx_product_id
# ON vitrine_two ( product_id )
#"""

#conn = sqlite3.connect( 'hm_db.sqlite' )
#cursor = conn.execute( query )
#conn.commit()
#conn.close()

