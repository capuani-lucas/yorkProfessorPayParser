from parse import Parser
import json

p = Parser("./2020-OPSSD-York-University.pdf")

# Put all items in final output dictionary
output = {}


# Use json module to dump
def dump_json():
    with open("output.json", 'w') as f:
        json.dump(output, f)


# Filter valid data
def add_data(prof):
    stripped = [x for x in prof.split("\n") if x.strip() != ""]

    # For some reason only one item in pdf does not like to play nice
    if stripped[3] != "York University":
        stripped.insert(2, "Dean’s Liaison Officer")

    output["{} {}".format(stripped[1], stripped[0])] = {
        "title": stripped[2],
        "salary": stripped[4],
        "taxable_benefits": stripped[5]
    }


# Extract text from pdf page. Remove first useless element
def extract_text(pdf_page):
    return pdf_page.extractText().split("2020\nUniversities")[1:]


# Go through all pages of pdf and isolate each employee
def main():
    reader = p.parse_pdf()

    if reader == -1:
        return

    for i in range(reader.getNumPages()):

        page = reader.getPage(i)
        out = extract_text(page)

        for prof in out:
            add_data(prof)

    p.close_file()

    dump_json()


if __name__ == '__main__':
    main()
