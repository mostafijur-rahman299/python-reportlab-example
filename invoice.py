from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def add_page_numbers(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(200, 20, text)


def generate_invoice():
    doc = SimpleDocTemplate("invoice.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)
    story = []

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#443d3d")

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
        fontSize=11,
        textColor=primary_color,
        leftIndent=0,  # Align lines to the start
    )

    centered_style = ParagraphStyle(
        name='Centered',
        parent=styles['title'],
        fontSize=28,
        textColor=colors.HexColor("#5e5b5b"),
        alignment=1,  # Center align the content
    )

    # Header
    header_text = [
        [Paragraph("Demo Shop", header_style)],
        [Spacer(1, -1)],  # Add spacing between paragraphs
        [Paragraph("Reg.No.: (234SEJUDKL)", subheader_style)],
        [Spacer(1, -20)],  # Add spacing between paragraphs
        [Paragraph(
            "Address 1", subheader_style)],
        [Spacer(1, -20)],  # Add spacing between paragraphs
        [Paragraph(
            "Address 2", subheader_style)],
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
    story.append(phone_table)
    
    # Line separator
    line_color = primary_color
    story.append(Spacer(1, 0.1*inch))  # Add some spacing before the line

    line = Table(
        [[""]],
        colWidths="100%",
        style=[("LINEABOVE", (0, 0), (-1, -1), 1, line_color)],
    )
    story.append(line)
    
    story.append(Spacer(1, -0.2 * inch))  # Add some spacing after the line

    # Center align Header
    centered_invoice_header = Paragraph("Invoice", centered_style)
    story.append(centered_invoice_header)  # Add the centered content to the story
    
    story.append(Spacer(1, 0.2 * inch))  # Add some spacing after the invoice
    
    
    styles = getSampleStyleSheet()

    # Custom styles
    left_col_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=0.9 * inch,  # Align lines to the start
    )

    left_colon_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-0.8 * inch,  # Align lines to the start
    )

    left_col_username = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        leftIndent=-0.8 * inch,  # Align lines to the start
    )
    left_col_value = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-0.8 * inch,  # Align lines to the start
    )

    right_col_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        rightIndent=0,  # Align lines to the end
        alignment=0,  # Right align the content
        leftIndent=0.8 * inch
    )

    right_colon_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-0.2 * inch,  # Align lines to the start
    )

    right_col_val_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        rightIndent=0,  # Align lines to the end
        alignment=0,  # Right align the content
        leftIndent=-0.2 * inch
    )

    data = [
        [
            Paragraph('Invoice To', left_col_style),
            Paragraph(':', left_colon_style),
            Paragraph('Sajib Mahmud', left_col_username),
            Paragraph('Invoice No.', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('89484KFJ-9089235', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('D/O No.', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('-', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('P/O No.', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('-', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('Invoice Date', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('20-Jun-2023', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('Invoice Date', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('20-Jun-2023', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('Handled By', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('admin', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('Payment Term', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('', right_col_val_style),
        ],
        [
            Paragraph(''),
            Paragraph('',),
            Paragraph('',),
            Paragraph('Page No.', right_col_style),
            Paragraph(':', right_colon_style),
            Paragraph('1/2', right_col_val_style),
        ],
        [
            Paragraph('Tel', left_col_style),
            Paragraph(':', left_colon_style),
            Paragraph('(+60)01283683', left_col_value),
            Paragraph(''),
            Paragraph(''),
            Paragraph(''),
        ],
        [
            Paragraph('Email', left_col_style),
            Paragraph(':', left_colon_style),
            Paragraph('example@gmail.com', left_col_value),
            Paragraph(''),
            Paragraph(''),
            Paragraph(''),
        ],
    ]

    col_widths = [2.5 * inch, 0.2 * inch, 2.5 * inch, 2.2 * inch, 0.2 * inch, 2.1 * inch]

    table = Table(data, colWidths=col_widths)

    # Enable word wrapping for the content
    table.setStyle(TableStyle([
        ('WORDWRAP', (0, 0), (-1, -1), True),
    ]))

    story.append(table)
    
    
    # Table data
    invoice_data = [
        ['1', 'Hair Cut', '120.00', '1', '120.00'],
        ['2', 'Cut Girl', '130.00', '13', '1320.00'],
    ]
    
    wrap_style_val = ParagraphStyle(
        name='WrapStyle',
        parent=getSampleStyleSheet()['Normal'],
        wordWrap='RTL',  # Set word wrap to Left To Right
        textColor=primary_color,
        fontSize=11,
        alignment=0
    )
    wrap_style_title = ParagraphStyle(
        name='WrapStyle',
        parent=getSampleStyleSheet()['Normal'],
        wordWrap='RTL',  # Set word wrap to Left To Right
        textColor=colors.black,
        fontSize=11,
    )
    
    wrapped_data = []
    for row in invoice_data:
        wrapped_row = [Paragraph(cell, wrap_style_val) for cell in row]
        wrapped_data.append(wrapped_row)

    wrapped_data.insert(0, [Paragraph(cell, wrap_style_title) for cell in ['No.', 'Description', 'Unit Price', 'Quantity', 'Price']])
    
    story.append(Spacer(1, 0.2*inch))

    # Create the table using wrapped data and column widths
    col_widths = [0.5 * inch, 3.8 * inch, 1 * inch, 1.4 * inch, 1 * inch]
    invoice_table = Table(wrapped_data, colWidths=col_widths)
        
    ts = TableStyle([
        ('TOPPADDING', (1, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 15),
        ('WIDTH', (0, 0), (-1, -1), '100%'),
        
        # Values style
        ('ALIGN', (1, 1), (-1, -1), "RIGHT"),
        ('TEXTCOLOR', (0, 1), (-1, -1), primary_color),
        
        # Top Line
        ('LINEABOVE', (0, 0), (-1, 0), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
        ('ALIGN', (1, 1), (1, len(invoice_data)), "LEFT"),
    ])
    
    num_rows = len(wrapped_data)
    dotted_line = (0, 3, 1, 0)  # Dot line pattern
    for row in range(1, num_rows):
        ts.add('LINEABOVE', (0, row), (-1, row), 0.5, colors.black, 1, dotted_line)
        
    invoice_table.setStyle(ts)
    story.append(invoice_table)
    
    line_color = colors.black
    
    story.append(Spacer(1, 0.3*inch))

    line = Table(
        [[""]],
        colWidths="97%",
        style=[("LINEABOVE", (0, 0), (-1, -1), 1, line_color)],
    )
    story.append(line)
    story.append(Spacer(1, -0.2 * inch))
    

    table_calculation_right_col_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        rightIndent=-260,
        alignment=2,
        wordWrap='RTL',
    )

    table_calculation_right_colon_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        alignment=2,
        rightIndent=-200
    )

    table_calculation_right_col_val_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        alignment=0,  # Right align the content
        leftIndent=3.5*inch,
        rightIndent=0.1*inch,
        wordWrap='RTL'
    )

    table_calculation_data = [
        [
            Paragraph('Subtotal', table_calculation_right_col_style),
            Paragraph(':', table_calculation_right_colon_style),
            Paragraph('9485823.00', table_calculation_right_col_val_style),
        ],
        [
            Paragraph('Discount', table_calculation_right_col_style),
            Paragraph(':', table_calculation_right_colon_style),
            Paragraph('0.00', table_calculation_right_col_val_style),
        ],
        [
            Paragraph('Total', table_calculation_right_col_style),
            Paragraph(':', table_calculation_right_colon_style),
            Paragraph('120.00', table_calculation_right_col_val_style),
        ],
        [
            Paragraph('Payment', table_calculation_right_col_style),
            Paragraph(':', table_calculation_right_colon_style),
            Paragraph('0.00', table_calculation_right_col_val_style),
        ],
        [
            Paragraph('Balance', table_calculation_right_col_style),
            Paragraph(':', table_calculation_right_colon_style),
            Paragraph('120.00', table_calculation_right_col_val_style),
        ],
    ]

    col_widths = [2.2 * inch, 1 * inch, 4.6 * inch]
    table_calculation_data = Table(table_calculation_data, colWidths=col_widths)
    story.append(table_calculation_data)
    
    # Create a paragraph with underlined text
    underline_style = ParagraphStyle(
        name='Underline',
        parent=styles['title'],
        fontSize=11,
        textColor=colors.HexColor("#000000"),
        underline=True,
        underlineColor=colors.HexColor("#000000"),
        underlineGap=1,
        underlineOffset=-2,
        alignment=0,
    )
    underlined_text = Paragraph('<u>Terms & Payment Remark:</u>', underline_style)
    
    story.append(underlined_text)
    story.append(Spacer(1, 0.5*inch))
    
    # Create a paragraph with underlined text
    remark_underline_style = ParagraphStyle(
        name='Underline',
        parent=styles['title'],
        fontSize=12,
        textColor=colors.HexColor("#000000"),
        underline=True,
        underlineColor=colors.HexColor("#000000"),
        underlineGap=1,
        underlineOffset=-2,
        alignment=0,
    )
    remark_text_style = ParagraphStyle(
        name='Remark Text',
        parent=styles['Normal'],
        fontSize=12,
        textColor=primary_color,
        underline=True,
        underlineColor=primary_color,
        alignment=0,
    )
    remark_underlined_text = Paragraph('<u>Remark:</u>', remark_underline_style)
    text1 = Paragraph('Please make cash / cheque payable to PARTY WORLD TENT ENTERPRISE', remark_text_style)
    text2 = Paragraph('Account number: 2-029383HF9378', remark_text_style)
    
    story.append(remark_underlined_text)
    story.append(Spacer(1, -0.08*inch))
    story.append(text1)
    story.append(Spacer(1, 0.06*inch))
    story.append(text2)
    
    # Custom styles
    left_col_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=0.78 * inch,  # Align lines to the start
    )

    left_colon_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-1 * inch,  # Align lines to the start
    )

    left_col_username = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        leftIndent=-1.1 * inch,  # Align lines to the start
    )
    left_col_value = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-0.8 * inch,  # Align lines to the start
    )

    right_col_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        rightIndent=0,  # Align lines to the end
        alignment=0,  # Right align the content
        leftIndent=0.8 * inch
    )

    right_colon_style = ParagraphStyle(
        name='LeftColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        leftIndent=-0.2 * inch,  # Align lines to the start
    )

    right_col_val_style = ParagraphStyle(
        name='RightColumn',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        rightIndent=0,  # Align lines to the end
        alignment=0,  # Right align the content
        leftIndent=-0.2 * inch
    )

    
    # demo section
    shop_style = ParagraphStyle(
        name='ShopName',
        parent=styles['title'],
        fontSize=14,
        textColor=colors.HexColor('#000000'),
        underline=True,
        underlineColor=primary_color,
        alignment=0,
    )
    shop_name = Paragraph('Demo Shop', shop_style)
    
    story.append(Spacer(1, 0.3*inch))
    story.append(shop_name)
    story.append(Spacer(1, -0.1*inch))
    
    data = [
        [
            Paragraph('Reg No.', left_col_style),
            Paragraph(':', left_colon_style),
            Paragraph('(+94894879KJIF45)', left_col_username),
            Paragraph('Acceptance & Confirmation', right_col_style),
        ],
    ]
    col_widths = [2.5 * inch, 0.2 * inch, 2.5 * inch, 4.2 * inch]

    table = Table(data, colWidths=col_widths)

    # Enable word wrapping for the content
    table.setStyle(TableStyle([
        ('WORDWRAP', (0, 0), (-1, -1), True),
    ]))
    story.append(table)
    
    story.append(Spacer(1, 0.5*inch))
    
    
    
    line_color = colors.black

    # Create the left line
    left_line = Table(
        [[""]],
        colWidths=["32%"],
        style=[
            ("LINEABOVE", (0, 0), (-1, -1), 1, line_color),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ],
        hAlign="LEFT",
    )
    story.append(left_line)
    
    story.append(Spacer(1, -0.2 * inch))

    # Create the right line
    right_line = Table(
        [[""]],
        colWidths=["32%"],
        style=[
            ("LINEABOVE", (0, 0), (-1, -1), 1, line_color),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ],
        hAlign="RIGHT",
    )
    story.append(right_line)
    
    signature_rubber_stamp = ParagraphStyle(
        name='signature_rubber_stamp',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        alignment=2,
    )
    signature_company_rubber_stamp = Paragraph('Signature / Company Rubber Stamp', signature_rubber_stamp)
    story.append(signature_company_rubber_stamp)
    
    # Attachment & Remark
    attachment_tile = ParagraphStyle(
        name='attachment_tile',
        parent=styles['title'],
        fontSize=12,
        textColor=primary_color,
        alignment=0,
    )
    attachment = Paragraph('<u>Attachment:</u>', attachment_tile)
    story.append(attachment)
    
    attachment_subtile = ParagraphStyle(
        name='attachment_subtile',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        alignment=0,
        leftIndent=0.5 * inch
    )
    attachment_subtitle = Paragraph('Square request of the area is ahead name kia koarina', attachment_subtile)
    story.append(attachment_subtitle)
        
    story.append(Spacer(1, 0.2 * inch))
    
    attachments = ["image.jpg", "image.jpg"]
    attachments = []
    for attachment_path in attachments:
        image = Image(attachment_path, width=200, height=200, hAlign="LEFT")  # Adjust the width and height as needed

        # Create a spacer for indentation
        left_indent = Spacer(1, 0.1*inch)  # Adjust the indentation as needed

        # Add the indented image to the story
        # story.append(left_indent)
        # story.append(image)
        
        attachments.append(image)
        
    left_line = Table(
        [[""]],
        colWidths=["32%"],
        style=[
            ("LINEABOVE", (0, 0), (-1, -1), 1, line_color),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ],
        hAlign="LEFT",
    )

    
    # Build the PDF document
    # doc.build(story, onFirstPage=add_page_numbers, onLaterPages=add_page_numbers)
    
    doc.build(story)


generate_invoice()
