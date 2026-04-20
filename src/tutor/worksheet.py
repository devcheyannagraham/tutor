from fpdf import FPDF
from crewai.tools import tool


class Worksheet:
    def __init__(self, contents: str):
        self.contents = contents
        self.pdf = FPDF()

    def create_worksheet(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, self.contents)
        self.pdf.output("worksheet.pdf")


@tool("Worksheet Creator")
def create_worksheet(contents: str):
    """Given markdown, creates a worksheet PDF with the given contents."""
    print("Creating worksheet with contents:")
    ws = Worksheet(contents=contents)
    ws.create_worksheet()
    return "Worksheet created successfully and saved as worksheet.pdf"


if __name__ == "__main__":
    ws = Worksheet(
        contents="This is a sample worksheet content. You can replace this with the actual content you want to include in the worksheet."
    )
    ws.create_worksheet()
