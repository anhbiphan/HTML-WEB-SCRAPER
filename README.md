# news_webscrapper

Project: New Webscrapper
url = 'https://www.dovislex.eu/en/index.php?page=news'

Objective:
1. Create a Webscrapper to grab data from url link of the news website
2. Grab the date article published, title of the new article, converted slug formate, html code for the body
3. Create a data frame for the code
4. Column names ['user_id', 'date', 'title', 'slug', 'view', 'image', 'body', 'published']

Requirements:
1. date should be a string
2. 'title' has to be in <h3 class="news_title"> format
3. for 'slug' column, use 'title' column and convert all values into a slug. 
   (all lower case characters, no <h3 class="news_title">, spaces are replaced with '-', and no special characters and symbols)
4. 'body' column should be in <ul format

Problems:
1. after webscrapping the title, some "<h3 class="news_title">" were inconsistent, missing [ ", > ] and other symbols/characters.
    Solution: used the .replace() to custom replace unique "<h3 class="news_title">"
  
  
  

  
2. converting 'title' column into a slug format. characters have latin symbols and characters.
    Solution: used slugify to convert "title" column and create a new column for "slug" format.
    
Tools:
- BeautifulSoup
- Pandas
- Slugify
- Request
- Jupyter Notebook


