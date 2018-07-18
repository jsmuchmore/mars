
# coding: utf-8

# In[172]:


# dependencies
def scrape():

    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    import pandas as pd

    # ## ------------------------NEWS----------------------------------

    # In[280]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[282]:


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html_news = browser.html
    soup_news = BeautifulSoup(html_news, 'html.parser')


    # In[284]:


    news_title = soup_news.find('div', {"class": "content_title"}).text
    print(news_title)



    # In[285]:


    news_p = soup_news.find('div', {"class": "article_teaser_body"}).text
    print(news_p)


    # ## ------------------------FEATURED IMAGE----------------------------------

    # In[70]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[92]:


    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)


    # In[130]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[131]:


    image = soup.find('article', class_="carousel_item")


    # In[132]:


    image = str(image)


    # In[133]:


    image = image.split(" url('")[1]


    # In[135]:


    image = image.split("');")[0]


    # In[136]:


    print(image)


    # In[137]:


    featured_image_url = "https://www.jpl.nasa.gov/" + image


    # In[138]:


    browser.visit(featured_image_url)


    # ## ------------------------WEATHER----------------------------------

    # In[142]:


    url_twit = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_twit)


    # In[143]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[163]:


    weather = soup.find('div', class_ = "js-tweet-text-container")


    # In[164]:


    weather = str(weather)


    # In[165]:


    weather = weather.split('lang="en">')[1]


    # In[166]:


    print(weather)


    # In[167]:


    weather = weather.split("</p>")[0]


    # In[168]:


    print(weather)


    # ## ------------------------FACTS----------------------------------

    # In[257]:


    url_facts = "https://space-facts.com/mars/"
    tables = pd.read_html(url_facts)
    tables


    # In[258]:


    df = tables[0]


    # In[259]:


    df.columns = ["Fact", "Value"]


    # In[263]:


    df = df.set_index(df["Fact"])


    # In[270]:


    df = df.drop(columns=['Fact'])


    # In[271]:


    df


    # In[274]:


    html_table = df.to_html()


    # In[278]:


    html_table = html_table.replace('\n', '')


    # In[279]:


    html_table


    # ## ------------------------HEMISPHERES----------------------------------

    # In[273]:


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]





    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "weather": weather,
        "facts": html_table,
        "hemispheres": hemisphere_image_urls
            
            }

    return mars_dict