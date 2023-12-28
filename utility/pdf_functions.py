import aspose.pdf as pdf


def create_pdf(sql_data: list, category_report: str):
    pdfFile = pdf.Document()
    newPage = pdfFile.pages.add()

    table = pdf.Table()
    table.default_cell_border = pdf.BorderInfo(pdf.BorderSide.ALL, 1.0, pdf.Color.black)

    create_header(category_report, table)
    for rowNumber in range(0, len(sql_data)):
        row = table.rows.add()

        if category_report == "Classes" or category_report == "Students":
            row.cells.add(str(sql_data[rowNumber][0]))
            row.cells.add(str(sql_data[rowNumber][1]))
            row.cells.add(str(sql_data[rowNumber][2]))
            row.cells.add(str(sql_data[rowNumber][3]))
        elif category_report == "Teachers":
            pass

    newPage.paragraphs.add(table)

    pdfFile.save(f"{category_report}.pdf")
    print("Table in PDF created successfully")


def create_header(category_report: str, table):
    row = table.rows.add()
    if category_report == "Classes":
        row.cells.add("ID")
        row.cells.add("CLASS NAME")
        row.cells.add("NUMBER OF STUDENTS")
        row.cells.add("AVERAGE GRADE")
    elif category_report == "Students":
        row.cells.add("ID")
        row.cells.add("STUDENT FIRST NAME")
        row.cells.add("STUDENT LAST NAME")
        row.cells.add("ABSENCES")
    elif category_report == "Teachers":
        pass