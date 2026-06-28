"""
Generate PDF report from final_report.md
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf():
    with open("report/final_report.md", "r", encoding="utf-8") as f:
        content = f.read()

    os.makedirs("results/report", exist_ok=True)
    pdf_path = "results/report/final_report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["Title"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Heading2"]))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.strip():
            story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 6))

    doc.build(story)
    print(f"PDF generated successfully: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()