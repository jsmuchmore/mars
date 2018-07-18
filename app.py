from flask import Flask, render_template
import scrape_mars
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

import pymongo


app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)


db = client.mars_db

 

@app.route('/scrape')
def scrape():
    db.mars.drop()
    mars = scrape_mars.scrape()
    
    
    
    db.mars.insert_one(mars)
    return home()

@app.route("/")
def home():
    mars = list(db.mars.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)
