# HTML-WEB-SCRAPER

Project: News Webscrapper
target_url:'https://www.dovislex.eu/en/index.php?page=news'

Objective:
1. Create a Webscrapper using BeautifulSoup, to grab data on news articles from url link website.
2. Grab the date published, the title of the news article, html format of the body, create a slug format of title.
3. Create a data frame with column names ['user_id', 'date', 'title', 'slug', 'view', 'image', 'body', 'published']
4. Save final result data frame as a .csv

This is an image of one article on the news article list:
![alt text](https://github.com/anhbiphan/news_webscrapper/blob/master/images/new_article_1.png?raw=true)


Requirements/Contraints:
1. date should be a string data type
2. 'title' has to be in "<h3 class=>" format
3. for 'slug' column, use 'title' column and convert all values into a slug
   (all lower case characters, no <h3 class=>, spaces are replaced with '-', and no special characters and symbols)
4. 'body' column should be in <ul format

Problems:
1. after webscrapping the title, some "<h3 class=>" were inconsistent, missing [ ", > ] and other symbols/characters.

- **Solution**: used the .replace() to replace unique "<h3 class=>"
    
![alt text](https://github.com/anhbiphan/news_webscrapper/blob/master/images/title.png?raw=true)
- (As you can tell some <h3 formats are not consistent)

  
2. converting 'title' column into a slug format. characters have latin symbols and characters. 

- **Solution**: used slugify to convert "title" column and create a new column for "slug" format.(pip install unicode-slugify-latin)



### Title Column

![alt text](https://github.com/anhbiphan/news_webscrapper/blob/master/images/title_h3.png?raw=true)

### Slugged format of Title column

![alt text](https://github.com/anhbiphan/news_webscrapper/blob/master/images/title_slug.png?raw=true)


**The .csv contains the final data frame edit**


Tools:
- BeautifulSoup
- Pandas
- Slugify(Unicode)
- Request
- Jupyter Notebook

Project Team Members:

- Anh Phan: [https://github.com/anhbiphan]
- Anh Dang: Github [https://github.com/anhtdang92]

