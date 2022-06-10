# **Books_to _Scrape**

## Web Scraping with Python

![Book](book.png)
***

# 1. Business Problem.

Web scraping or Web data extraction is a way to automatically extract meaningful data available on websites. When there is no direct access to gather data using API or feeds, web scraping can be an effective way to automate data extraction.

In this project, I will use Python to create a simple yet effective web scraping script. This will be my starting point to delve deep into the field of web scraping using Python.

So, let’s begin!

# 2. Business Assumptions.

The assumptions about the business problem are as follows:

**2.1. Catalogs:**

- CLASSICS
- SCIENCE FICTION
- HUMOR

In this simple scrape script, which will scrape the data from the [Books to Scrape](books.toscrape.com) . The data that we will extract from the page will be the following:


- Book title (title)
- Price (price)
- Availability (stock)
- Rating (stars)


I will extract the data from the website to convert it into structured information for further analysis.

# 3. Solution Strategy
SAPE method

***
**Step 01. Configure the BeautifulSoup library:** This way we will have all the structure we need for our scraper to work.

To extract data from a webpage, the first thing we need to do is read the HTML content of that page. To do this, we'll need to cloak our python code so that it can send a get or post request to the webpage's URL and get the HTML response bac

***
**Step 02. Data Description:** My goal is to use statistics metrics to identify data outside the scope of business.
   - [x] Perform the median calculation on the product, catalog and evaluation
   - [x] Perform the minimum calculation on the product, catalog and evaluation
   - [x] Perform the maximum calculation on the product, catalog and evaluation

***
**Step 03. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.
   - [x] Schema definition: Columns and their type
   - [x] Table with the following columns: product_name | product_price | product_stock | product_star | product_catalog
   - [x] ETL Design (Extract, Transform, and Load Scripts)

***
**Step 04. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

***
**Step 05. Data Preparation:**: Prepare data to identify specific behaviors for hypothesis validation
  
***
**Step 06. Feature Selection:**
- **Define the delivery format (View, Table, Text)**
   - [x] Defining the storage infrastructure ( csv )
   - [x] Graph with the median price of products, by catalog and evaluation
   - [x] make the visualizations
- **Decide the delivery location ( PowerBi, Telegram, Email, Streamlit, Intranet )**
   - [x] PowerBI
***

# 4. Top 3 Data Insights

**Hypothesis 01:** Which catalog has the best purchase price according to customer recommendations?
- Business

**Hypothesis 02:** Which catalog has the lowest purchase price according to customer recommendations?
- Science Fiction

**Hypothesis 03:** Which catalog has the highest purchase price according to customer recommendations?
- Humor

# 5. Business Results

***
![Dashboard](dashboard.png)

# 6. Conclusions

# 7. Lessons Learned

# 8. Next Steps to Improve

**1.** **Perform the collection for all catalogs automatically**

**2.** **Execute new insights and new discoveries**

***
- **Data source**
   * https://books.toscrape.com/
***
- **Tools**
   * Python 3.8.0
   * Libraries:Pandas, Numpy
   * Webscrapping Libraries (BS4)
   * VisualCode
   * Jupyter Notebook ( Analysis and prototyping )
   * PowerBI (Views)
 ***
