from fpdf import FPDF

def generate_pdf_report(role, score, matched, missing, roadmap):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Role: {role}", ln=True)
    pdf.cell(200, 10, txt=f"Match Score: {score}%", ln=True)
    pdf.cell(200, 10, txt="Matched Skills: " + ", ".join(matched), ln=True)
    pdf.cell(200, 10, txt="Missing Skills: " + ", ".join(missing), ln=True)
    pdf.cell(200, 10, txt="Roadmap:", ln=True)
    for item in roadmap:
        pdf.cell(200, 10, txt=f"- {item}", ln=True)
    pdf.output("report.pdf")