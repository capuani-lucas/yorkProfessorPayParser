import PyPDF2 as pdf


class Parser:

    def __init__(self, path):
        self.path = path
        self.file = self.open_file()

    def open_file(self):
        try:
            return open(self.path, "rb")
        except FileNotFoundError:
            print("Error: specified file cannot be located.")

        return -1

    def parse_pdf(self):

        if self.file == -1:
            print("Unable to parse pdf")
            return -1

        return pdf.PdfFileReader(self.file)

    def close_file(self):
        if self.file == -1:
            return

        self.file.close()
