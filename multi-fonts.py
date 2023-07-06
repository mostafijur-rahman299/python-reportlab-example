from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, BaseDocTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet

# Define your header content (e.g., a paragraph)
header_text = "Header Text Here"

# Define a function to add the header to each page
def add_header(canvas, doc):
    canvas.saveState()
    header_paragraph = Paragraph(header_text, style=getSampleStyleSheet()["BodyText"])
    header_paragraph.wrap(doc.width, doc.topMargin)
    header_paragraph.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - 12)
    canvas.restoreState()

# Custom BaseDocTemplate class with modified build method
class CustomBaseDocTemplate(BaseDocTemplate):
    def __init__(self, *args, **kwargs):
        BaseDocTemplate.__init__(self, *args, **kwargs)

    def build(self, story):
        # Create a PageTemplate with the header
        frame = Frame(
            self.leftMargin, self.bottomMargin, self.width, self.height,
            id='normal'
        )
        template = PageTemplate(id='with_header', frames=[frame], onPage=add_header)
        self.addPageTemplates([template])

        # Build the PDF using the story list and the doc object
        BaseDocTemplate.build(self, story)

# Create a list of story elements (main content of the document)
story = []

# Add paragraphs or other elements to the story list
# For example:
story.append(Paragraph("Page 1 Content", style=getSampleStyleSheet()["Normal"]))

# Define the filename for the PDF
filename = "my_report_with_header.pdf"

# Create a CustomBaseDocTemplate object with the specified filename and margins
doc = CustomBaseDocTemplate(filename, pagesize=letter, topMargin=82, leftMargin=72, rightMargin=72, bottomMargin=72)

# Build the PDF by calling the build method with the story list
doc.build(story)
