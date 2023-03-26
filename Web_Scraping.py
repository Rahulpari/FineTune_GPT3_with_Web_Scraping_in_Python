import os
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#Setting directory path
path1="directory/docs" #path of the folder "docs" to save the scraped text
os.chdir(path1) #Directory path1 is set

# URLs to scrape
urls = ['https://www.open-contracting.org/data-standard/',
        'https://www.dms.myflorida.com/agency_administration/office_of_supplier_diversity_osd/vendor_resources2/current_bid_opportunities', 
        'https://ted.europa.eu/TED/browse/browseByMap.do', 
        'https://www.adb.org/projects', 
        'https://comptroller.texas.gov/purchasing/contracts/search.php', 
        'https://opentender.eu/start', 
        'https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1', 
        'https://developer.taiyo.ai/api-doc/ProjectsandTenders/', 
        'https://www.open-contracting.org/worldwide/#/table', 
        'https://projects.worldbank.org/en/projects-operations/projects-home', 
        'https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid', 
        'https://www.txdot.gov/business/letting-bids/contract-bidding-resources.html', 
        'https://www.dgs.ca.gov/OBAS/Bid-Opportunities', 
        'https://openai.com/blog/introducing-chatgpt-and-whisper-apis', 
        'https://www.afdb.org/en/projects-and-operations', 
        'https://www.fdot.gov/procurement/advertisements.shtm', 
        'https://forms.gle/BmJU3piRG5FZMGFCA', 
        'https://pipeline.gihub.org/', 
        'https://www.aiib.org/en/projects/list/index.html', 
        'https://sam.gov/content/home'
        ]

# Initialize the text content as an empty string
text_content = ""

# Scrape data from each URL and add it to the text content
for url in urls:
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove unwanted elements from the soup
    for script in soup(["script", "style"]):
        script.extract()
        
    # Add the text content to the document without removing extra spaces
    text_content += soup.get_text()
    
# Save the text content as a file
with open("scraped.txt", "w", encoding="utf-8") as f:
    f.write(text_content)