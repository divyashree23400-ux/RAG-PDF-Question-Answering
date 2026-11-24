
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the PDF
reader = PdfReader("syllabus.pdf")

# Extract text from all pages
raw_text = "\n".join(
    page.extract_text() or "" for page in reader.pages
)

print("PDF loaded successfully!")
print("Total pages:", len(reader.pages))

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=80,
)

chunks = splitter.split_text(raw_text)

print("Extracted", len(chunks), "chunks from the PDF")

# Display first chunk
if chunks:
    print("\nFirst chunk:")
    print(chunks[0])
else:
    print("No text found in PDF.")
