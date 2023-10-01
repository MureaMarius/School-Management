from reportlab.pdfgen import canvas


def create_pdf():
    c = canvas.Canvas("my_data.pdf")
    c.drawString(100, 750, "Hello, I am a PDF document created with Python!")
    c.save()
