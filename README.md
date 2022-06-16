# **Books_to _Scrape**

## Web Scraping with Python

Web scraping or Web data extraction is a way to automatically extract meaningful data available on websites. When there is no direct access to gather data using API or feeds, web scraping can be an effective way to automate data extraction.

In this project, I will use Python to create a simple yet effective web scraping script. This will be my starting point to delve deep into the field of web scraping using Python.

So, let’s begin!

<div align="center">
<p float="left">
  <img src="/images/book.png" width="1000" height="500"/>
</p>
</div>

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
:------------: | :-------------:
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

<div align="center">
<p float="left">
  <img src="/images/h1.png" width="750" height="500" />
</p>
</div>

**Hypothesis 02:** Science fiction books should have a lower price value
 - *Reply:* **False**.

<div align="center">
<p float="left">
  <img src="/images/h2.png" width="750" height="500" />
</p>
</div>

**Hypothesis 03:** Humor books had the best average price value (average price)
 - *Reply:* **False.** 

<div align="center">
<p float="left">
  <img src="/images/h3.png" width="750" height="500" />
</p>
</div>

**Hypothesis 04:** Business books having lower price value than average
 - *Reply* **True.** 

<div align="center">
<p float="left">
  <img src="/images/h4.png" width="750" height="500" />
</p>
</div>

**Hypothesis 05:** Books with fewer stars got a lower price value
 - *Reply:* **True**

<div align="center">
<p float="left">
  <img src="/images/h5.png" width="750" height="500" />
</p>
 </div>
 
**Hypothesis 06:** Books with fewer stars should have a lower price
 - *Reply:* **False**

<div align="center">
<p float="left">
  <img src="/images/h6.png" width="750" height="500" />
</p>
</div>
 
**Hypothesis 07:** The number of stars should influence the price (direct proportionality)
 - *Reply:* **False**

<div align="center">
<p float="left">
  <img src="/images/h7.png" width="750" height="500" />
</p>
</div>

***
# 5. BUSINESS RESULTS 
***

<div align="center">
<p float="left">
  <img src="/images/dashboard.png" width="1000" height="500"/>
  <img src="/images/classic.png" width="500" height="500" />
  <img src="/images/humor.png" width="500" height="500" />
  <img src="/images/business.png" width="500" height="500" />
  <img src="/images/science_fiction.png" width="500" height="500" />
</p>
</div>

***
# 6. CONCLUSIONS

The purpose of the project was to extract data from a website and extract structured information to answer the business team's question.

Therefore, the most cost-effective catalog should be **Business**. Because it has the lowest average selling price with the highest customer recommendation rate. The **Humor** catalog follows, as it has the second lowest selling price, although it has the highest rating (four stars) according to the customer recommendation index.

I believe I have managed to deliver all the demands of the business problems, which can be accessed in the books available in this project can be accessed in the books available in this project.

# 7. LESSONS LEARNED

# 8. NEXT STEPS TO IMPROVE

Improvements to be made in a next cycle

 - Perform the collection for all catalogs automatically.
 - Execute new insights and new discoveries.
 - If you have any improvements to suggest, you can contact me through my [LinkedIn](https://www.linkedin.com/in/camiladangelotempesta/)

***
# TOOLS

- Python 3.9.0;
   * Libraries:Pandas, Numpy
   * Webscrapping Libraries (BS4)
- Jupyter Notebook ( Analysis and prototyping );
- Git e Github;
- VisualCode 
- PowerBI (Views)
- 
***
Made By **Camila D'Angelo**

- 🔭 I’m currently working on DS community
- 🌱 I’m currently learning Data Science
- 📫 How to reach me: 
[LinkeldIn](https://www.linkedin.com/in/camiladangelotempesta/)
