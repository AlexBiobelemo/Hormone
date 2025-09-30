import os
from utils.research_generator import ResearchGenerator
from utils.pdf_generator import PdfGenerator
from utils.notes_manager import NotesManager

def main():
    # --- Configuration ---
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        api_key = input("Please enter your Google API Key: ").strip()
    
    system_prompt = "You are a helpful research assistant. Provide detailed and well-structured information."

    # --- User Input for Research ---
    topic = input("Enter the research topic: ").strip()
    if not topic:
        print("Error: Topic cannot be empty!")
        return
    
    keywords_input = input("Enter keywords (comma-separated): ").strip()
    keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
    
    questions_input = input("Enter research questions (comma-separated): ").strip()
    research_questions = [q.strip() for q in questions_input.split(',') if q.strip()]

    if not keywords or not research_questions:
        print("Error: Keywords and research questions cannot be empty!")
        return

    print("\n--- Generating Research Report ---")
    try:
        research_gen = ResearchGenerator(topic, keywords, research_questions, api_key, system_prompt)
        report_content = research_gen.generate_report()
        
        print("\n--- Research Report ---")
        print(report_content)

        # --- Export Options ---
        print("\n--- Exporting Report ---")
        export_choice = input("Do you want to save the report as a PDF (p), DOCX (d), or both (b)? (p/d/b/n for none): ").lower()

        filename_base = topic.replace(' ', '_').replace('/', '_').replace('\\', '_')

        if 'p' in export_choice or 'b' in export_choice:
            print("Generating PDF report...")
            pdf_gen = PdfGenerator(topic)
            pdf_path = pdf_gen.generate_pdf_report(report_content, output_path=f"{filename_base}_report.pdf")
            print(f"PDF report saved to: {pdf_path}")

        if 'd' in export_choice or 'b' in export_choice:
            print("Generating DOCX report...")
            notes_manager = NotesManager(filepath=f"{filename_base}_notes.txt")
            notes_manager.update_notes(report_content)
            docx_path = notes_manager.save_as_docx(output_path=f"{filename_base}_report.docx")
            print(f"DOCX report saved to: {docx_path}")

        print("\nResearch process complete!")
    
    except Exception as e:
        print(f"\nError during research generation: {str(e)}")
        return

if __name__ == "__main__":
    main()
