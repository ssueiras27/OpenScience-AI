from bs4 import BeautifulSoup as bs
from grobid_client import grobid_client as grobid
import os





#PROCESSING PDF => XML
def processPdfs():
  client = grobid.GrobidClient(config_path="pdfanalyzer/config.json")
  client.process("processFulltextDocument", input_path, output=output_path, consolidate_citations=True, tei_coordinates=True, force=True)


if __name__ == "__main__":
    input_path = "pdfanalyzer/input"
    output_path = "pdfanalyzer/output"
    
    #Calls the funcition for proccessing the pdf into xml files using GROBID
    processPdfs()
    
    
    
    #Get the path of all xml files
    files_list = []
    
    for file in os.listdir(output_path):
        file_path = os.path.join(output_path, file)
        # checking if it is a file
        if os.path.isfile(file_path):
            files_list.append(file_path)
    
    content = []
    # Read the XML file
    with open("sample.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")