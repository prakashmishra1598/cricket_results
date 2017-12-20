"""
Documentation : This module retrieves html page of a website 
                in the form of a HTML    document
"""
import urllib.request
def downloadXml():
    """
    This function retrieves the html document from the url of 
    the website and saves it locally
    """
    url = "https://sports.ndtv.com/cricket/results"
    urllib.request.urlretrieve(url,'news_sports.html')#Retrieve sports url and store it locally

downloadXml()