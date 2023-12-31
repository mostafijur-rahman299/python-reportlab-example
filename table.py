data = [
    ['Dedicated Hosting', 'VPS Hosting', 'Sharing Hosting', 'Memory Management'],
    ['$200/Month', '$100/Month', '20/Month'],
    ['Free Domain', 'Free Domain', 'Free Domain'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
]

fileName = 'pdfTable.pdf'

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


pdf = SimpleDocTemplate(fileName, pagesize=A4)
table = Table(data)

style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.green),
    ('TEXTCOLOR', (0,0), (3,0), colors.whitesmoke),
    
    ('ALIGN', (0,1), (-1,-1), 'CENTER'),
    
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    
    ('FONTSIZE', (0,0), (-1,0), 14),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
])
table.setStyle(style)


# Alternate colors
for i in range(1, len(data)):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige
        
    ts = TableStyle([
        ('BACKGROUND', (0, i), (-1, i), bc)
    ])
    
    table.setStyle(ts)
    
# Add borders
ts = TableStyle([
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('LINEBEFORE', (2, 1), (2, -1), 1, colors.black),
    ('LINEAFTER', (2, 1), (2, -1), 1, colors.black),
    ('LINEABOVE', (2, 1), (2, -1), 1, colors.red),
    ('GRID', (0, 1), (-1, -1), 1, colors.green),
])


table.setStyle(ts)

elems = []
elems.append(table)

print(pdf.getPageNumber())

pdf.build(elems)
