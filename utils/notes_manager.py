import os
from docx import Document
from fpdf import FPDF
from datetime import datetime

class NotesManager:
    def __init__(self, filepath="research_notes.txt"):
        self.filepath = filepath
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Error loading notes: {str(e)}")
            return ""

    def update_notes(self, new_notes):
        self.notes = new_notes
        self.save_notes()

    def save_notes(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                f.write(self.notes)
        except Exception as e:
            print(f"Error saving notes: {str(e)}")
            raise

    def format_notes(self):
        # Add formatting logic here (e.g., using markdown)
        return self.notes  # Placeholder

    def save_as_pdf(self, output_path="research_notes.pdf"):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Handle Unicode by encoding to latin-1 with errors ignored
            safe_notes = self.notes.encode('latin-1', errors='ignore').decode('latin-1')
            pdf.multi_cell(0, 10, safe_notes)
            
            pdf.output(output_path)
            return output_path
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
            raise

    def save_as_docx(self, output_path="research_notes.docx"):
        try:
            document = Document()
            document.add_paragraph(self.notes)
            document.save(output_path)
            return output_path
        except Exception as e:
            print(f"Error generating DOCX: {str(e)}")
            raise
