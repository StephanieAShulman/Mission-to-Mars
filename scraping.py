# Define dependencies
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# Create a function for Splinter (initialize the browser)
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Set news title and paragraph variables; tell Python pull data with mars news fxn
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere": hemisphere(browser)}

    # Stop webdriver and return data
    browser.quit()
    return data

# Create a function for Mars News
def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
    return news_title, news_p

# Create a function for Mars Image
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    return img_url

# Create a function for Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table striped")

# Create a function for Hemisphere Images
def hemisphere(browser):
    # Visit URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    #hmtl = browser.html
    
    # Create list to hold images and titles
    hemisphere_image_urls = []
    
    # Retrieve elements
    imgs_links = browser.find_by_css("a.product-item")['src']
    
    for i in range(4):
        hemisphere={}
        # Click on each hemisphere link
        browser.find_by_css("a.product-item h3")[i].click()
        # Retrieve the href from the full-resolution image page with Sample anchor tag
        sample_img = browser.links.find_by_text("Sample").first
        hemisphere['img_url'] = sample_img['href']    
        # Retrieve the title for the full hemisphere image
        hemisphere['title'] = browser.find_by_css("h2.title").text    
        # Add the objects to the hemisphere_img_urls list
        hemisphere_image_urls.append(hemisphere)    
        # Navigate back for next image
        browser.back()  

    # Retrieve the information
    return hemisphere_image_urls

# Tell Flask script is complete and ready for action
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())