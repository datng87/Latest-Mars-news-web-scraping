In this project, I'll build a web application that scrapes the data from other websites regarding MARS and displays the information in an HTML page.

The tools used in this project are:
- Flask
- BeautifulSoup
- Pandas
- Requests/Splinter.
- Mongo DB
- HTML, CSS, Bootstrap,
- Jupiter Notebook for debugging purposes on how the scraped data looks like.

How does it work:
The application has a refresh button on top. Once the refresh button is clicked, the web application will run and scrape new data from other sites. The returned data is updated to MongoDB database, and this new data is queried by the HTML and rendered to the web.

List of websites was used to scrape data:
https://redplanetscience.com/ : scrape Mars News
https://spaceimages-mars.com/ : scrape Mars surface image
https://galaxyfacts-mars.com/ : scrape Mars data table
https://marshemispheres.com/ : scape Mars Hemispheres HD images 

The below Gif showing the demo for this web app.
![alt text](Missions_to_Mars/output/webscrape.gif)
