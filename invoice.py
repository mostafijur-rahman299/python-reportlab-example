from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def add_page_numbers(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(200, 20, text)


def generate_invoice():
    doc = SimpleDocTemplate("invoice.pdf", pagesize=letter,
                            topMargin=0.5, leftMargin=15, rightMargin=15)
    story = []

    styles = getSampleStyleSheet()

    # Custom styles
    header_style = ParagraphStyle(
        name='Header',
        parent=styles['Heading5'],
        fontSize=13,
        textColor=colors.black,
        leftIndent=0,  # Align lines to the start
    )

    subheader_style = ParagraphStyle(
        name='Subheader',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        leftIndent=0,  # Align lines to the start
    )

    phone_style = ParagraphStyle(
        name='Phone',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        alignment=1,  # Center align the phone number
    )

    centered_style = ParagraphStyle(
        name='Centered',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.grey,
        alignment=1,  # Center align the content
    )

    # Header
    header_text = [
        [Paragraph("Demo Shop", header_style)],
        [Spacer(1, -1)],  # Add spacing between paragraphs
        [Paragraph("Reg.No.: (234SEJUDKL)", subheader_style)],
        [Spacer(1, -20)],  # Add spacing between paragraphs
        [Paragraph(
            "Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678", subheader_style)],
        [Spacer(1, -20)],  # Add spacing between paragraphs
        [Paragraph(
            "Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678", subheader_style)],
    ]

    header_table = Table(header_text, colWidths=[2*inch])
    header_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')]))

    center_table = Table([[header_table]], style=[
                         ('ALIGN', (0, 0), (-1, -1), 'CENTER')])
    # Add the center-aligned header table to the story
    story.append(center_table)

    # Phone number with icon
    custom_style = ParagraphStyle(
        name='CustomStyle',
        leftIndent=212,       # Left margin in points
        rightIndent=0,      # Right margin in points
        spaceBefore=10,      # Space before the paragraph in points
        spaceAfter=100       # Space after the paragraph in points
    )
    
    phone_number_text = [
        [Paragraph(
                "<img src='phone-192.png' width='15' height='15' /> +123456789 <img src='whatsapp-192.png' width='15' height='15' /> +123456789 <img src='email-50.png' width='15' height='15' /> +123456789", custom_style
            ),
        ]
    ]

    phone_table = Table(phone_number_text)
    phone_table.setStyle(TableStyle([('ALIGN', (0, 0), (0, 0), 'CENTER')]))

    # Append the table to your story

    # Append the table to your story
    story.append(phone_table)
    # Line separator
    line_color = colors.black
    story.append(Spacer(1, 0.8))  # Add some spacing before the line

    line = Table(
        [[""]],
        colWidths="100%",
        style=[("LINEABOVE", (0, 0), (-1, -1), 1, line_color)],
    )
    story.append(line)
    story.append(Spacer(1, 0.2 * inch))  # Add some spacing after the line

    # Center align content
    centered_content = Paragraph(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", centered_style)
    story.append(centered_content)  # Add the centered content to the story

    # Build the PDF document
    doc.build(story, onFirstPage=add_page_numbers,
              onLaterPages=add_page_numbers)


generate_invoice()
