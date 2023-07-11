from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# Define styles
styles = getSampleStyleSheet()
right_col_style = styles['Normal']
right_colon_style = styles['Normal']
right_col_val_style = styles['Normal']
left_col_style = styles['Normal']
left_colon_style = styles['Normal']
left_col_value = styles['Normal']

# Create the document
doc = SimpleDocTemplate("dynamic_invoice.pdf", pagesize=letter)

# Define the data for the left and right tables
left_data = [
    [
        Paragraph('Invoice No.', right_col_style),
        Paragraph(':', right_colon_style),
        Paragraph('234', right_col_val_style),
    ],
    [
        Paragraph('D/O No.', right_col_style),
        Paragraph(':', right_colon_style),
        Paragraph('234', right_col_val_style),
    ],
    # Add more rows as needed
]

right_data = [
    [
        Paragraph('Tel', left_col_style),
        Paragraph(':', left_colon_style),
        Paragraph('telephone_no', left_col_value),
    ],
    [
        Paragraph('Email', left_col_style),
        Paragraph(':', left_colon_style),
        Paragraph('email', left_col_value),
    ],
    # Add more rows as needed
]



# Create the left table
left_table = Table(left_data)
left_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONT', (0, 0), (-1, -1), 'Helvetica', 12),
    # Add more table styles as needed
]))

# Create the right table
right_table = Table(right_data)
right_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONT', (0, 0), (-1, -1), 'Helvetica', 12),
    # Add more table styles as needed
]))

# Build the elements for the document
elements = []
elements.append(left_table)
elements.append(right_table)

# Add the elements to the document
doc.build(elements)
