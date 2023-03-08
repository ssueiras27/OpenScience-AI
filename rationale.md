In order to execute the extraction you need to follow the next steps:

1. Use this command in order to start running the grobid container
    docker run --rm --gpus all -p 8070:8070 grobid/grobid:0.7.2

2. Make sure your terminal is at the inside the OpenScience-AI directory
    OpenScience-AI>

3. Activate the python virtual enviroment
    (In Code terminal run) .\venv\Scripts\Activate.ps1

4. Execute main.py
    (In Code terminal run) py .\pdfanalyzer\main.py

5. Execute test.py to check if everything went ok
    (In Code terminal run) py .\pdfanalyzer\test.py

6. Go to .\pdfanalyzer\reports to see the results
    -results.pdf a report with all the results of the analysis
    -figures.png an image with the number of figures per article
    -wordcloud.png an image of a wordcloud extracter from the articles

*Notice* that on top of main.py and test.py right after the imports there is 
a section where the folder paths used by the program are specified