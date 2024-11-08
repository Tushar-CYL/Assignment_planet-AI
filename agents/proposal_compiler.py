from fpdf import FPDF

class ProposalPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AI Use Cases for Customer Support", 0, 1, "C")

    def add_use_cases(self, use_cases):
        self.set_font("Arial", "", 10)
        for case in use_cases:
            self.cell(0, 10, f"{case['title']}", 0, 1)
            self.multi_cell(0, 10, f"Problem: {case['problem']}\nSolution: {case['solution']}\nBenefit: {case['benefit']}\n")

def compile_proposal():
    pdf = ProposalPDF()
    pdf.add_page()
    
    # Add insights and use cases
    pdf.add_use_cases([
        {
            "title": "AI-Powered Chatbot",
            "problem": "Improve customer response time",
            "solution": "Implement a chatbot to handle FAQs",
            "benefit": "Reduces operational costs"
        },
       
    ])
    
    pdf.output("results/final_proposal.pdf")

if __name__ == "__main__":
    compile_proposal()
