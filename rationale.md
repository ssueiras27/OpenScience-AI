In this file I am going to describe the thinking I followed to validate my answers

- Draw a keyword cloud based on the words found in the abstract of your papers.
    I use the wordcloud library (https://pypi.org/project/wordcloud/)
- Create a visualization showing the number of ﬁgures per article.
    I generated a plot graph using matplotlib (https://pypi.org/project/matplotlib/)
- Create a list of the links found in each paper.
    A list of the references directly countered from the xml files

For exploring the xml files generated by grobid I decided to use Beautiful soup 4 (https://pypi.org/project/beautifulsoup4/)