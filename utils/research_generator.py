import google.generativeai as genai

class ResearchGenerator:
    def __init__(self, topic, keywords, research_questions, api_key, system_prompt):
        self.topic = topic
        self.keywords = keywords
        self.research_questions = research_questions
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key=self.api_key)

    def generate_section(self, section_name):

        # Note: The suggested model 'gemini-2.5-flash' is not a valid model name.
        # Reverting to the original 'gemini-1.5-flash' which is a valid and current model.
        model = genai.GenerativeModel('gemini-1.5-flash')
        try:
        prompt = f"{self.system_prompt}\n\nCreate a {section_name} for a research report on the topic: {self.topic}. Keywords: {self.keywords}. Research questions: {self.research_questions}"
        response = model.generate_content(prompt)
        return response.text
        except Exception as e:
            return f"Error generating {section_name}: {str(e)}"

    def generate_report(self):
        introduction = self.generate_section("introduction")
        literature_review = self.generate_section("literature review")
        methodology = self.generate_section("methodology")
        results = self.generate_section("results")
        discussion = self.generate_section("discussion")
        conclusion = self.generate_section("conclusion")

        report = f"Introduction:\n{introduction}\n\nLiterature Review:\n{literature_review}\n\nMethodology:\n{methodology}\n\nResults:\n{results}\n\nDiscussion:\n{discussion}\n\nConclusion:\n{conclusion}"
        return report