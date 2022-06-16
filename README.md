# **Books_to _Scrape**

## Web Scraping with Python

Web scraping or Web data extraction is a way to automatically extract meaningful data available on websites. When there is no direct access to gather data using API or feeds, web scraping can be an effective way to automate data extraction.

In this project, I will use Python to create a simple yet effective web scraping script. This will be my starting point to delve deep into the field of web scraping using Python.

So, let’s begin!

![Book](book.png)
***


## 1. BUSINESS PROBLEMS

Definition of which catalog presents the best cost benefit

### 1.1 **Context:**

 * Extraction of data from a web page (Webscraping);
 * Read the HTML content of that page;

### 1.2 **Solution:**

 * Using the BeatifulSoup library for scraping;
 * Extraction of structured information for further analysis.
 * Visualization in PowerBI;

***
## 2. BUSINESS ASSUMPTIONS

* Dataset was obtained from [Books to Scrape](books.toscrape.com) 

The variables created during project development are

Variable | Definition
------------ | -------------
|product_name | Book title|
|product_price	 |Sale price|
|product_stock |  Availability|
|product_star | Evaluation|
|product_catalog | Theme to which the book belongs|

***
## 3. SOLUTION PLANNING

As a data scientist, I believe in the CRISP-DS methodology for project resolution and rapid value delivery. My project followed the following steps based on this methodology:


- [x] **Step 01:** **Data Description**:  My goal is to use statistics metrics to identify data outside the scope of business.
  - Data Dimension
  - Data types
  - Check NA
  - Descriptive Statistivas
    * Numerical Attributes
    * Categorical Attributes
 
 - [x] **Step 02:** **Feature Engineering**: Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.
  - Hypoteses Mindmap
  - Missing values
  - Grouping

- [x] **Step 03:** **Data Filtering**: Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business
  - Line filtering
  - Selection of columns

- [x] **Step 04:** Exploratory Data Analysis:Explore the data to find insights and better understand the impact of variables on model learning. - Line filtering
  - Univariate Analysis
  - Bivariate Analysis

***
## 4. TOP 5 DATA INSIGHTS

**Hypothesis 01:** The Chosen Books reached a higher price value
 - *Reply:* **True**. 

**Hypothesis 02:** Science fiction books should have a lower price value
 - *Reply:* **False**. 

**Hypothesis 03:** Humor books had the best average price value (average price)
 - *Reply:* **False.** 
 
**Hypothesis 04:** Business books having lower price value than average
 - *Reply* **True.** 
 
**Hypothesis 05:** Books with fewer stars got a lower price value
 - *Reply:* **True**
 
**Hypothesis 06:** Books with fewer stars should have a lower price
 - *Reply:* **False**
 
**Hypothesis 07:** The number of stars should influence the price (direct proportionality)
 - *Reply:* **False**


***
# 5. Business Results
***
![Dashboard](dashboard.png)

# 6. Conclusions

The objective of the project was to extract data from a website and extract structured information in order to answer the business team's question.

Therefore, the preferred catalog in sales recommendations to customers should be **Business**. Because it has the lowest average selling price with the highest rate of customer recommendation. Followed by the **Humor** catalogue, as it has the lowest selling price, although it has the highest rating according to the customer recommendation index.

I believe I have managed to deliver all the demands of the business problems, which can be accessed in the books available in this project can be accessed in the books available in this project.

# 7. Lessons Learned

# 8. Next Steps to Improve

Improvements to be made in a next cycle

 - Perform the collection for all catalogs automatically.
 - Execute new insights and new discoveries.
 - If you have any improvements to suggest, you can contact me through my [LinkedIn](https://www.linkedin.com/in/camiladangelotempesta/)


# Tools

- Python 3.9.0;
   * Libraries:Pandas, Numpy
   * Webscrapping Libraries (BS4)
- Jupyter Notebook ( Analysis and prototyping );
- Git e Github;
- VisualCode 
- PowerBI (Views)
***
Made By **Camila D'Angelo**

[Portfólio](https://github.com/camila-dangelo-tempesta?tab=repositories)

[LinkeldIn](https://www.linkedin.com/in/camiladangelotempesta/)
