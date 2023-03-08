import os
import unittest

input_path = "pdfanalyzer/input"
output_path = "pdfanalyzer/output"
config_path = "pdfanalyzer/config.json"
    
wordcloud_path = 'pdfanalyzer/reports/wordcloud.png'
figuresplot_path = 'pdfanalyzer/reports/figures.png'
report_path = 'pdfanalyzer/reports/results.pdf'


class TestPdfAnalyzer(unittest.TestCase):

    def test_grobid(self):
        n = 0
        for file in os.listdir(input_path):
            if (os.path.splitext(file)[1] == ".pdf"):
                n = n+1
        for file in os.listdir(output_path):
            if (os.path.splitext(file)[1] == ".xml"):
                n = n-1
        self.assertEqual(n, 0)
            
    def test_wordcloud(self):
        self.assertTrue(os.path.isfile(wordcloud_path))

    def test_figures(self):
        self.assertTrue(os.path.isfile(figuresplot_path))
        
    def test_report(self):
        self.assertTrue(os.path.isfile(report_path))

if __name__ == '__main__':
    unittest.main()