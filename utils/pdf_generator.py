from fpdf import FPDF
from datetime import datetime

class PdfGenerator:
    def __init__(self, topic, author="Research Assistant"):
        self.topic = topic
        self.author = author

    def generate_cover_page(self, pdf):
        pdf.add_page()
        pdf.set_font("Arial", "B", 24)
        pdf.cell(0, 20, "Research Report", ln=True, align="C")
        pdf.set_font("Arial", "B", 16)
        
        # Handle Unicode in topic
        safe_topic = self.topic.encode('latin-1', errors='ignore').decode('latin-1')
        pdf.cell(0, 10, safe_topic, ln=True, align="C")
        
        pdf.set_font("Arial", "", 12)
        safe_author = self.author.encode('latin-1', errors='ignore').decode('latin-1')
        pdf.cell(0, 10, f"Author: {safe_author}", ln=True, align="C")
        pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="C")

    def generate_table_of_contents(self, pdf):
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Table of Contents", ln=True, align="C")
        # Add table of contents entries here (placeholder)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, "1. Introduction ..................... 1", ln=True)
        pdf.cell(0, 10, "2. Literature Review ................ 2", ln=True)
        pdf.cell(0, 10, "3. Methodology ..................... 3", ln=True)
        pdf.cell(0, 10, "4. Results ......................... 4", ln=True)
        pdf.cell(0, 10, "5. Discussion ...................... 5", ln=True)
        pdf.cell(0, 10, "6. Conclusion ...................... 6", ln=True)

    def generate_content(self, pdf, content):
        pdf.add_page()
        pdf.set_font("Arial", "", 12)
        
        # Handle Unicode in content
        safe_content = content.encode('latin-1', errors='ignore').decode('latin-1')
        pdf.multi_cell(0, 10, safe_content)

    def generate_pdf_report(self, content, output_path="research_report.pdf"):
        try:
            pdf = FPDF()
            self.generate_cover_page(pdf)
            self.generate_table_of_contents(pdf)
            self.generate_content(pdf, content)
            pdf.output(output_path)
            return output_path
        except Exception as e:
            print(f"Error generating PDF report: {str(e)}")
            raise
