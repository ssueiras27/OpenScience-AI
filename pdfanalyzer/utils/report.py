from fpdf import FPDF

class Report(FPDF):
    def __init__(self, file_names, wordcloud, figuresplot, lists_of_references, output):
        super().__init__()
        self.add_page()
        self.set_font('Arial', 'B', 28)
        self.cell(w=0, h=20, txt="Results report", ln=1)
        self.set_font('Arial', '', 20)
        self.ln(8)
        self.ln(8)
        self.multi_cell(w=0, h=5, txt="Keyword cloud based on the words found in the abstract:")
        self.ln(8)
        self.image(wordcloud, x = 10, y = None, w = 100, h = 0, type = 'PNG')
        self.ln(8)
        self.multi_cell(w=0, h=5, txt="Number of figures per article:")
        self.ln(8)
        self.image(figuresplot, x = 10, y = None, w = 100, h = 0, type = 'PNG')
        self.ln(8)
        self.multi_cell(w=0, h=5, txt="List of links per article:")
        self.ln(8)

        i = 0
        for references in lists_of_references:
            self.set_font('Arial', 'B', 18)
            self.multi_cell(w=0, h=5, txt=file_names[i])
            self.ln(4)
            self.set_font('Arial', '', 16)
            for reference in references:
                self.multi_cell(w=0, h=5, txt=reference["target"])
            i = i + 1
            self.ln(4)
    
        self.output(output, 'F')
        
    def header(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 8, 'PdfAnalyzer', 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')