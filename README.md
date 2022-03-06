# Mission-to-Mars
![Mars_small](https://user-images.githubusercontent.com/30667001/154660422-28e46291-e34a-4ee6-908f-19b5fdd24ab6.png)

A web browser was automated to visit four different websites and extract pertient data about planet Mars. Data were then stored in a a NoSQL database and rendered in a web application created with Flask, with a resulting site that can be used to scrape the most current information about the Mission to Mars.

## Resources
- Data Sources: https links to NASA news, Mars facts and images
- Software: Python 3.7.6, Jupyter Notebook 6.4.5, Visual Studio Code 1.65.0
- Libraries: Flask-PyMongo 2.3.0, lxml 4.7.1, html5lib 1.1, Python Pandas
- Applications: MongoDB Community Edition (5.0.6), pymongo 4.0.1, Splinter 0.17.0, webdriver_manager 3.5.3, bs4 0.0.1 (beautifulsoup 2.3.1)

## Project
For this project an app was built to scrape websites and a HTML page created to display the findings. Steps included:
* Python script was created to automate web browsing with Splinter.
* Data were extracted with a BeautifulSoup html parser.
* HTML components were identified with Chrome Developer Tools.
* Structured and unstructred data were stored using MongoDB (a NoSQL database) via GitBash access.
* A web application was built to display the data using Flask.
* A button feature was included to execute code scraping. Updated information displays following data retrieval.
* Bootstrap components were applied to modifying features, such as:
  1. Increasing the size of button: *btn-block*.
  2. Making headers bold: <strong>Mission to Mars</strong>.
  3. Changing the colors of text: style=color:darkblue.

## Final Result
The finished HTML site was accessed through the http://127.0.0.1:5000/ link with the most recent iteration appearing below:
![Mars PIX](https://user-images.githubusercontent.com/30667001/156939207-54be66c7-d8a2-4bfc-8d58-3369c18edd06.png)
