from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

w, h = A4

# creating a pdf object
c = canvas.Canvas("texts.pdf")

text = c.beginText(50, h - 50)
text.setFont("Times-Roman", 12)

text.textLine("Hello world!")
text.textLine("From ReportLab and Python!")
text.textLines("Hello world!\n\n\n\n\nFrom ReportLab and Python!")

c.drawText(text)

c.save()
