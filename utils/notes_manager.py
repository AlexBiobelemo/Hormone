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
            with open(self.filepath, "r") as f:
                return f.read()
        except FileNotFoundError:
            return ""

    def update_notes(self, new_notes):
        self.notes = new_notes
        self.save_notes()

    def save_notes(self):
        with open(self.filepath, "w") as f:
            f.write(self.notes)

    def format_notes(self):
        # Add formatting logic here (e.g., using markdown)
        return self.notes  # Placeholder

    def save_as_pdf(self, output_path="research_notes.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, self.notes)
        pdf.output(output_path)
        return output_path

    def save_as_docx(self, output_path="research_notes.docx"):
        document = Document()
        document.add_paragraph(self.notes)
        document.save(output_path)
        return output_path
