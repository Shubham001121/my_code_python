from pypdf import PdfWriter
def merge_pdfs(pdfs, output):
  pdf_writer = PdfWriter()
  for pdf in pdfs:
    pdf_writer.append(pdf)

  with open(output, 'wb') as out:
    pdf_writer.write(out)


def main():
  pdfs = ["basic-text.pdf", "dev-example.pdf"]
  merge_pdfs(pdfs, output='merged.pdf')
main()
