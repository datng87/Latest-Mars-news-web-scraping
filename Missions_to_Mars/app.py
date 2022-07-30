from flask import Flask, render_template, redirect
from scrape_mars import *
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars"
mongo = PyMongo(app)



@app.route("/")
def echo():
    listings = mongo.db.mars_scrape.find_one()
    return render_template("index.html", listings=listings)

@app.route('/scrape')
def scraper():
    mars_scrape = mongo.db.mars_scrape
    scrape_data = scrape()
    mars_scrape.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)