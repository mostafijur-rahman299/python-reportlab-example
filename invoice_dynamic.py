from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, TableStyle, Image, Indenter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


class GenerateInvoice:
    def __init__(self, name_of_pdf):
        
        self.doc = SimpleDocTemplate(name_of_pdf, pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)
        self.story = []
        self.styles = getSampleStyleSheet()
        self.primary_color = colors.HexColor("#443d3d")
        
        self.centered_style = ParagraphStyle(
            name='Centered',
            parent=self.styles['title'],
            fontSize=28,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=1,  # Center align the content
        )
        
    def top_header(self, shop_name, reg_number, address1="", address2="", phone_number="", whatsapp_number="", email=""):
        # Custom styles
        header_style = ParagraphStyle(
            name='Header',
            parent=self.styles['Heading5'],
            fontSize=13,
            textColor=colors.black,
            leftIndent=0,  # Align lines to the start
        )

        subheader_style = ParagraphStyle(
            name='Subheader',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            leftIndent=0,  # Align lines to the start
        )

        # Header
        header_text = [
            [Paragraph(shop_name, header_style)],
            [Spacer(1, -1)],  # Add spacing between paragraphs
            [Paragraph(reg_number, subheader_style)],
            [Spacer(1, -20)],  # Add spacing between paragraphs
            [Paragraph(
                address1, subheader_style)],
            [Spacer(1, -20)],  # Add spacing between paragraphs
            [Paragraph(
                address2, subheader_style)],
        ]

        header_table = Table(header_text, colWidths=[2*inch])
        header_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')]))

        center_table = Table([[header_table]], style=[
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER')])
        # Add the center-aligned header table to the story
        self.story.append(center_table)

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
                    f"<img src='phone-192.png' width='15' height='15' />{phone_number}<img src='whatsapp-192.png' width='15' height='15' />{whatsapp_number}<img src='email-50.png' width='15' height='15' />{email}", custom_style
                ),
            ]
        ]

        phone_table = Table(phone_number_text)
        phone_table.setStyle(TableStyle([('ALIGN', (0, 0), (0, 0), 'CENTER')]))
        self.story.append(phone_table)
        
    def invoice_header(self, invoice_to="", invoice_no="", DO_No="", PO_No="", invoice_date="", handled_by="", payment_term="", telephone_no="", email=""):
        # Center align Header
        centered_invoice_header = Paragraph("Invoice", self.centered_style)
        self.story.append(centered_invoice_header)  # Add the centered content to the story
        
        self.story.append(Spacer(1, 0.2 * inch))  # Add some spacing after the invoice
        
        styles = getSampleStyleSheet()

        # Custom styles
        left_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            leftIndent=0.9 * inch,  # Align lines to the start
        )

        left_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
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
            textColor=self.primary_color,
            leftIndent=-0.8 * inch,  # Align lines to the start
        )

        right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=0,  # Right align the content
            leftIndent=0.8 * inch
        )

        right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            leftIndent=-0.2 * inch,  # Align lines to the start
        )

        right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=0,  # Right align the content
            leftIndent=-0.2 * inch
        )

        data = [
            [
                Paragraph('Invoice To', left_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(invoice_to, left_col_username),
                Paragraph('Invoice No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_no, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('D/O No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(DO_No, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('P/O No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(PO_No, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('Invoice Date', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_date, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('Handled By', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(handled_by, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('Payment Term', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(payment_term, right_col_val_style),
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
                Paragraph(telephone_no, left_col_value),
                Paragraph(''),
                Paragraph(''),
                Paragraph(''),
            ],
            [
                Paragraph('Email', left_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(email, left_col_value),
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

        self.story.append(table)
           
    def header(self, header_data):
        self.top_header(header_data.get("shop_name", ""), header_data.get("reg_number", ""), header_data.get("address1", ""), header_data.get("address2", ""), header_data.get("phone_number", ""), header_data.get("whatsapp_number", ""), header_data.get("email", ""))
        self.line_separator("100%", 1)
        self.story.append(Spacer(1, -0.2 * inch))  # Add some spacing after the line
        
        self.invoice_header(header_data.get("invoice_to", ""), header_data.get("invoice_no", ""), header_data.get("DO_No", ""), header_data.get("PO_No", ""), header_data.get("invoice_date", ""), header_data.get("handled_by", ""), header_data.get("payment_term", ""), header_data.get("telephone_no", ""), header_data.get("email", ""))
                 
    def line_separator(self, width, thickness):
        # Line separator
        line = Table(
            [[""]],
            colWidths=width,
            style=[("LINEABOVE", (0, 0), (-1, -1), thickness, self.primary_color)],
        )
        self.story.append(line)
            
    def invoice_table(self, invoice_data):
        # invoice_data = [
        #     ['1', 'Hair Cut', '120.00', '1', '120.00'],
        #     ['2', 'Cut Girl', '130.00', '13', '1320.00'],
        # ]
        
        wrap_style_val = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
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
        
        self.story.append(Spacer(1, 0.2*inch))

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
            ('TEXTCOLOR', (0, 1), (-1, -1), self.primary_color),
            
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
        self.story.append(invoice_table)
        
        line_color = colors.black
        
        self.story.append(Spacer(1, 0.3*inch))
        
        self.line_separator("97%", 1)
        
        self.story.append(Spacer(1, -0.2 * inch))
        

        table_calculation_right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            rightIndent=-260,
            alignment=2,
            wordWrap='RTL',
        )

        table_calculation_right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            alignment=2,
            rightIndent=-200
        )

        table_calculation_right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
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
        self.story.append(table_calculation_data)
            
    def terms_and_remark(self, account_number=""):
        remark_underline_style = ParagraphStyle(
            name='Underline',
            parent=self.styles['title'],
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
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=self.primary_color,
            underline=True,
            underlineColor=self.primary_color,
            alignment=0,
        )
        remark_underlined_text = Paragraph('<u>Remark:</u>', remark_underline_style)
        text1 = Paragraph('Please make cash / cheque payable to PARTY WORLD TENT ENTERPRISE', remark_text_style)
        text2 = Paragraph(f'Account number: {account_number}', remark_text_style)
        
        self.story.append(remark_underlined_text)
        self.story.append(Spacer(1, -0.08*inch))
        self.story.append(text1)
        self.story.append(Spacer(1, 0.06*inch))
        self.story.append(text2)
        
    def acceptance_signature(self, shop_name, reg_no="", ):
        left_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            leftIndent=0.78 * inch,  # Align lines to the start
        )

        left_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            leftIndent=-1 * inch,  # Align lines to the start
        )

        left_col_username = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.black,
            leftIndent=-1.1 * inch,  # Align lines to the start
        )

        right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=0,  # Right align the content
            leftIndent=0.8 * inch
        )

        
        # demo section
        shop_style = ParagraphStyle(
            name='ShopName',
            parent=self.styles['title'],
            fontSize=14,
            textColor=colors.HexColor('#000000'),
            underline=True,
            underlineColor=self.primary_color,
            alignment=0,
        )
        shop_name = Paragraph(shop_name, shop_style)
        
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(shop_name)
        self.story.append(Spacer(1, -0.1*inch))
        
        data = [
            [
                Paragraph('Reg No.', left_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(reg_no, left_col_username),
                Paragraph('Acceptance & Confirmation', right_col_style),
            ],
        ]
        col_widths = [2.5 * inch, 0.2 * inch, 2.5 * inch, 4.2 * inch]

        table = Table(data, colWidths=col_widths)

        # Enable word wrapping for the content
        table.setStyle(TableStyle([
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))
        self.story.append(table)
        
        self.story.append(Spacer(1, 0.5*inch))
        
        
        
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
        self.story.append(left_line)
        
        self.story.append(Spacer(1, -0.2 * inch))

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
        self.story.append(right_line)
        
        signature_rubber_stamp = ParagraphStyle(
            name='signature_rubber_stamp',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            alignment=2,
        )
        signature_company_rubber_stamp = Paragraph('Signature / Company Rubber Stamp', signature_rubber_stamp)
        self.story.append(signature_company_rubber_stamp)
        
        # Attachment & Remark
        attachment_tile = ParagraphStyle(
            name='attachment_tile',
            parent=self.styles['title'],
            fontSize=12,
            textColor=self.primary_color,
            alignment=0,
        )
        attachment = Paragraph('<u>Attachment:</u>', attachment_tile)
        self.story.append(attachment)
        
        attachment_subtile = ParagraphStyle(
            name='attachment_subtile',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.primary_color,
            alignment=0,
            leftIndent=0.5 * inch
        )
        attachment_subtitle = Paragraph('Square request of the area is ahead name kia koarina', attachment_subtile)
        self.story.append(attachment_subtitle)
            
    def attachments(self, attachments):
        self.story.append(Spacer(1, 0.2 * inch))
        flowables = []

        for attachment_path in attachments:
            # Create an Image object with adjusted width and height
            image = [Image(attachment_path, width=450, height=250)]

            # Create a spacer for left and right margins
            left_margin = [Spacer(6.7*inch, 0)]

            # Append the left margin, image, and right margin to the flowables list
            flowables.append(left_margin)
            flowables.append(image)
            
        self.story.append(Table(flowables))
        
    def build_pdf(self, data={}):
        
        header = data.get("header", {})
        self.header(header)
        
        self.invoice_table([])
        
        self.terms_and_remark()
        
        self.doc.build(self.story)
        
invoice = GenerateInvoice("dynamic_invoice.pdf")

invoice.build_pdf({})

