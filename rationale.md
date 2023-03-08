In order to execute the extraction you need to follow the next steps:

1. Use this commands in order to pull and start running the grobid container
    docker pull grobid/grobid:0.7.2
    docker run --rm --gpus all -p 8070:8070 grobid/grobid:0.7.2

2. Make sure your terminal is at the inside the OpenScience-AI directory
    OpenScience-AI>

3. Generate and activate the python virtual enviroment
    python3 -m venv venv
    . venv/bin/activate && pip install -r requirements.txt

4. Execute main.py
    py .\pdfanalyzer\main.py

5. Execute test.py to check if everything went ok
    py .\pdfanalyzer\test.py

6. Go to .\pdfanalyzer\reports\ to see the results
    -results.pdf a report with all the results of the analysis
    -figures.png an image with the number of figures per article
    -wordcloud.png an image of a wordcloud extracter from the articles

*Notice* that on top of main.py and test.py right after the imports there is 
a section where the folder paths used by the program are specified