from reportlab.pdfgen import canvas


def create_pdf(sql_data: list, category_report: str):
    pdf = canvas.Canvas(f"{category_report}.pdf".format(category_report=category_report))

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "DATA REPORT")

    pdf.setFont("Helvetica", 12)
    y = 700

    for row in sql_data:
        pdf.drawString(50, y, "Id: " + str(row[0]))
        pdf.drawString(50, y - 20, "Class name: " + row[1])
        pdf.drawString(50, y - 40, "Number of students: " + str(row[2]))
        pdf.drawString(50, y - 60, "Average grade: " + str(row[3]))
        y -= 120

    pdf.save()
