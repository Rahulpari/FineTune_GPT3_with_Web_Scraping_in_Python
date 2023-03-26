# Import Module
import pdfx, os
import pandas as pd
 
# Setting directory path
path1="C:/Users/Lenovo/Dropbox/0_PLACEMENT/DataScience_Portfolio/Python _URL_Scraping_Fine_Tune_GPT3/raw_data"
os.chdir(path1) #Directory path1 is set

# Read PDF File
pdf = pdfx.PDFx("assignment.pdf")

# Get list of URL
ref = pdf.get_references_as_dict()

# save the DataFrame to an Excel file
df = pd.DataFrame(ref)
df.to_excel('URLs.xlsx', index=False)

# save the DataFrame to a txt file
with open('URLs.txt', 'w') as f:
    f.write(str(ref))
    