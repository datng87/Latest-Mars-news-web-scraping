from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
import pandas as pd


#Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

def scrape():
    

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_date = soup.find('div',class_='list_date').text
    news_title = soup.find('div',class_='content_title').text
    news_p = soup.find('div',class_='article_teaser_body').text
    browser.quit()



    #scrap mar feature picture
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    featured_image_url= url + soup.find('img', class_='headerimage')['src']
    browser.quit()


    #scrap mars facts table
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df=tables[0]
    df.rename(columns={0:'Description',
                    1:'Mars',
                    2:'Earth'},inplace=True)
    df.set_index('Description',inplace=True)
    html_table = df.to_html()
    html_table=html_table.replace('\n', '')
    df.to_html('table.html')


    #scrape hesmisphere image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    base_url = "https://marshemispheres.com/"
    browser.visit(base_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    div_list = soup.find_all('div',class_='description')
    url_list=[]
    for i in div_list:
        url_list.append(f"{base_url + i.a['href']}")
    browser.quit()
    hemisphere_image_urls =[]
    images_dict ={'title':'','img_url':'','img_display':''}
    for url in url_list:
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        div_class = soup.find('div',class_='downloads')
        img_display = base_url + div_class.ul.find_all('li')[0].a['href']
        img_url = base_url + div_class.ul.find_all('li')[1].a['href']
        title = soup.find('div',class_='cover')
        title = title.h2.text.replace(' Enhanced',"")
        images_dict ={'title':'','img_url':'','img_display':''}
        images_dict.update({'title':title,'img_url':img_url,'img_display':img_display})
        hemisphere_image_urls.append(images_dict)
        browser.quit()  

    scrape_data = {'news_date':news_date,'news_title':news_title,'news_p':news_p,
                'feature_image_url':featured_image_url,
                'mars_df':df.to_dict(),
                'hemisphere_image_urls':hemisphere_image_urls}
    return (scrape_data)

