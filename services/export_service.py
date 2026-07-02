from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def export_pdf(text, filename):
    doc = SimpleDocTemplate(filename)

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)