
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

reader = PdfReader("syllabus.pdf")
raw_text = "\n".join(page.extract_text() or "" for page in reader.pages)

for size in [200, 1000]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=50
    )

    chunks = splitter.split_text(raw_text)

    print("\nChunk size:", size)
    print("Total chunks:", len(chunks))