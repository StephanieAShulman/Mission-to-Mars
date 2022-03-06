# Use Flask to render a template, redirecting to another url, and creating a URL #
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact wiht Mongo DB  #
from flask_pymongo import PyMongo
# Import tool to convert from Jupyter ntbk to Python
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up Flask routes (to main HTML page; to page for scraping)
# HTML route
@app.route("/")
def index():
   # Use PyMongo to find the Mars collection in the DB
   mars = mongo.db.mars.find_one()
   # Instruction Flask to return an HTML using the 
   #   index.html file and mars collection in MongoDB
   return render_template("index.html", mars=mars)
# Scraping route
@app.route("/scrape")  # Access scraping.py script
def scrape():
   # Assign a new variable to hold newly scraped data
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   # Update the database; modifying ($set) if needed
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# Instruct Flask to run
if __name__ == "__main__":
   app.run()