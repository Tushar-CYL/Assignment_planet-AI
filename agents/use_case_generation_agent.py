import json

def generate_use_cases():
    # Load industry data
    with open("results/research_insights.json") as f:
        insights = json.load(f)
    
    use_cases = [
        {
            "title": "AI-Powered Chatbot",
            "problem": "Improve customer response time",
            "solution": "Implement a chatbot to handle FAQs",
            "benefit": "Reduces operational costs"
        },
        # Additional use cases...
    ]
    
    # Save use cases
    with open("results/use_cases.md", "w") as f:
        for case in use_cases:
            f.write(f"### {case['title']}\n- Problem: {case['problem']}\n")
            f.write(f"- Solution: {case['solution']}\n- Benefit: {case['benefit']}\n\n")

if __name__ == "__main__":
    generate_use_cases()
