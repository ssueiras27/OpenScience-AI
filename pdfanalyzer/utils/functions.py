import os
from grobid_client import grobid_client as grobid
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup as bs

def processPdfs(input_path, output_path, config_path):
  client = grobid.GrobidClient(config_path=config_path)
  client.process("processFulltextDocument", input_path, output=output_path, consolidate_citations=True, tei_coordinates=True, force=True, n=2)
  

def processXmls(xmls_path):
    files_list = []
    file_names = []
    
    plain_abstract_text = ""
    number_of_figures = []
    lists_of_references = []
    
    for file in os.listdir(xmls_path):
        file_path = os.path.join(xmls_path, file).replace("\\","/")
        # checking if it is a file
        if os.path.isfile(file_path) and (os.path.splitext(file)[1] == ".xml"):
            files_list.append(file_path)
            content = []
            with open(file_path, "r", encoding="utf8") as file:
                content = file.readlines()
                content = "".join(content)
            #For some reason it only works using the html parser instead of lxml
            bs_content = bs(content, features="xml")
            
            #Extract the abstract
            abstract = bs_content.find("abstract")
            plain_abstract_text += abstract.find("p").contents[0]
            
            #Number of figures
            figures = bs_content.findAll("figure")
            file_names.append(os.path.splitext(os.path.basename(file.name))[0])
            number_of_figures.append(len(figures))   
            
            #List of references
            references = bs_content.find_all("ptr")
            
            lists_of_references.append(references)
    
    return files_list, file_names, plain_abstract_text, number_of_figures, lists_of_references


def abstractWordCloud(plain_text, output):
    word_cloud = WordCloud(stopwords = set(STOPWORDS),
                           background_color="rgba(255, 255, 255, 0)", 
                           mode="RGBA", width = 800, height = 600,).generate(plain_text)
    word_cloud.to_file(output)
    
def figuresPlot(file_names, number_of_figures, output):
    plt.bar(file_names, number_of_figures, color ='maroon', width = 0.9)
    
    plt.xlabel("Files")
    plt.ylabel("No. of figures per article")
    plt.savefig(output, 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")
    
