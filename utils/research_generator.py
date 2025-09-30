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
        model = genai.GenerativeModel('gemini-1.5-flash')
        try:
            # Format keywords and questions as readable strings
            keywords_str = ", ".join(self.keywords)
            questions_str = "\n".join([f"- {q}" for q in self.research_questions])
            
            prompt = f"""{self.system_prompt}

Create a {section_name} for a research report on the topic: {self.topic}

Keywords: {keywords_str}

Research questions:
{questions_str}

Please provide detailed, well-structured content for this section."""
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_msg = f"Error generating {section_name}: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

    def generate_report(self):
        try:
            print("Generating introduction...")
            introduction = self.generate_section("introduction")
            
            print("Generating literature review...")
            literature_review = self.generate_section("literature review")
            
            print("Generating methodology...")
            methodology = self.generate_section("methodology")
            
            print("Generating results...")
            results = self.generate_section("results")
            
            print("Generating discussion...")
            discussion = self.generate_section("discussion")
            
            print("Generating conclusion...")
            conclusion = self.generate_section("conclusion")

            report = f"""Introduction:
{introduction}

Literature Review:
{literature_review}

Methodology:
{methodology}

Results:
{results}

Discussion:
{discussion}

Conclusion:
{conclusion}"""
            
            return report
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise
