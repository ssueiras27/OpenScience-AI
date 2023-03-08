from grobid_client import grobid_client as grobid
import os
from utils.report import Report
from utils.functions import * 


input_path = "pdfanalyzer/input"
output_path = "pdfanalyzer/output"
config_path = "pdfanalyzer/config.json"
    
wordcloud_path = 'pdfanalyzer/reports/wordcloud.png'
figuresplot_path = 'pdfanalyzer/reports/figures.png'
report_path = 'pdfanalyzer/reports/results.pdf'

if __name__ == "__main__":
    
    #Calls the funcition for proccessing the pdf into xml files using GROBID
    processPdfs(input_path, output_path, config_path)

    #Process Xml files
    files_list, file_names, plain_abstract_text, number_of_figures, lists_of_references = processXmls(output_path)
    
    #Generate Wordcloud
    abstractWordCloud(plain_abstract_text , wordcloud_path)
    

    #Number of figures
    figuresPlot(file_names, number_of_figures, figuresplot_path)
    
    #Generate report
    report = Report(file_names, wordcloud_path, figuresplot_path, lists_of_references, report_path)
        