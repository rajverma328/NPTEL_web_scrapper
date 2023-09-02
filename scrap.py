# Specify the URL you want to scrape
url = 'https://archive.nptel.ac.in/content/storage2/courses/112104117/chapter_1/1_intro.html'
old_url = 'https://archive.nptel.ac.in/content/storage2/courses/112104117'

import requests
from bs4 import BeautifulSoup
import pdfkit

response = requests.get(url)
print('webpage found')
condi = 0
old_href = ''
href_value = ''
# Check if the request was successful (status code 200)
while(1):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:   
        # Parse the HTML content of the webpage
        html_content = response.text
        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')   
        frames_with_id_mainframe = soup.find_all(['frame', 'iframe'], attrs={'name': 'mainFrame'})
        if(len(frames_with_id_mainframe)>0):
            str = frames_with_id_mainframe[0].get('src')
            j = url.rfind('/')
            base_url = old_url
            str1 = str[str.find('/'):len(str)]
            url = base_url+str1
            response = requests.get(url)
            print(url)
            html_content = response.text
            # Create a BeautifulSoup object
            soup = BeautifulSoup(html_content, 'html.parser') 
            print('webpage found')
    
        atag = soup.find_all('a')
        
        if(len(atag) == 1 ):
            href_value = atag[0].get('href')
            if(href_value == old_href):
                break 
        else:
            old_href = href_value
            href_value = atag[1].get('href')

        #print(href_value)
        options = {
            'page-size': 'A4',  # Paper size (A4 is a common choice)
            'zoom': 1.0,        # Zoom factor (1.0 means "fit width")
            'encoding': 'UTF-8', # Encoding for the input HTML content
        }
        
        condi = condi +1
        if(condi<10):
            output_pdf = "./individual_pdf/0" + f"{condi}" +".pdf"
        else:
            output_pdf = "./individual_pdf/" + f"{condi}" +".pdf"
        # Convert the webpage to a PDF
        
        pdfkit.from_url(url, output_pdf, options=options)
        
        print(f"Webpage '{href_value}' printed to '{output_pdf}' with 'fit width' as default.")
        
        j = url.rfind('/')
        base_url = url[0:j+1]
        #print(base_url+href_value)
        url = base_url+href_value        
        
    else:
        print(f'Error: Unable to fetch the webpage. Status code: {response.status_code}')
    
print('extraction completed')
