from fpdf import FPDF
from crewai.tools import tool


class Worksheet:
    def __init__(self, contents: str):
        self.contents = contents
        self.pdf = FPDF()

    def create_worksheet(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        # self.pdf.multi_cell(0, 10, self.contents)
        self.pdf.write_html(self.contents)
        self.pdf.output("worksheet.pdf")


@tool("Worksheet Creator")
def create_worksheet(contents: str):
    """Given HTML, creates a worksheet PDF with the given contents."""
    print("Creating worksheet with contents:")
    ws = Worksheet(contents=contents)
    ws.create_worksheet()
    return "Worksheet created successfully and saved as worksheet.pdf"


if __name__ == "__main__":
    ws = Worksheet(
        contents="""
            <h1>Sample Worksheet</h1>
            <p>This is a sample worksheet created using the Worksheet tool.</p>
            <ul>
            <li>Question 1: What is the capital of France?</li>
            <li>Question 2: Solve the equation 2x + 3 = 7.</li>
            <li>Question 3: Write a short essay on the importance of AI in education.</li
            </ul>
        """
    )
    ws.create_worksheet()
