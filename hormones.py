import os
from utils.research_generator import ResearchGenerator
from utils.pdf_generator import PdfGenerator
from utils.notes_manager import NotesManager # Also useful for saving as DOCX

def main():
    # --- Configuration ---
    # Get API key from environment variable or user input
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        api_key = input("Please enter your Google API Key: ")
    
    system_prompt = "You are a helpful research assistant. Provide detailed and well-structured information."

    # --- User Input for Research ---
    topic = input("Enter the research topic: ")
    keywords = input("Enter keywords (comma-separated): ").split(',')
    research_questions = input("Enter research questions (comma-separated): ").split(',')

    print("\n--- Generating Research Report ---")
    research_gen = ResearchGenerator(topic, keywords, research_questions, api_key, system_prompt)
    report_content = research_gen.generate_report()
    
    print("\n--- Research Report ---")
    print(report_content)

    # --- Export Options ---
    print("\n--- Exporting Report ---")
    export_choice = input("Do you want to save the report as a PDF (p), DOCX (d), or both (b)? (p/d/b/n for none): ").lower()

    if 'p' in export_choice or 'b' in export_choice:
        print("Generating PDF report...")
        pdf_gen = PdfGenerator(topic)
        pdf_path = pdf_gen.generate_pdf_report(report_content, output_path=f"{topic.replace(' ', '_')}_report.pdf")
        print(f"PDF report saved to: {pdf_path}")

    if 'd' in export_choice or 'b' in export_choice:
        print("Generating DOCX report...")
        notes_manager = NotesManager(filepath=f"{topic.replace(' ', '_')}_notes.txt")
        notes_manager.update_notes(report_content)
        docx_path = notes_manager.save_as_docx(output_path=f"{topic.replace(' ', '_')}_report.docx")
        print(f"DOCX report saved to: {docx_path}")

    print("\nResearch process complete!")

if __name__ == "__main__":
    main()
