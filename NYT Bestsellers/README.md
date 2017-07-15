# New York Times Bestsellers: Market Share App and Review Sentiment Analysis

This code was part of a large-scale effort to analyze New York Times fiction bestsellers.  The scripts here do the following:

1. Query the NY Times API automatically to request bestseller lists meeting certain temporal parameters.

2. Clean the data and attach parent company and imprint genre data.

3. Generate a shiny dashboard to visualize this data.

4. Query the NY Times API automatically to request book review URLs and metadata.

5. Scrape the text of the book reviews at each of those URLs.

6. Analyze the data resulting from those requests.

7. Generate a word2Vec and neural network in an attempt to analyze the sentiment of the reviews.
[NOTE--This effort was not really successful.] 