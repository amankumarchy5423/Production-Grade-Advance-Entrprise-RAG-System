
from pathlib import Path

import logfire
from langchain_community.document_loaders import PyPDFLoader


def parse_pdf(file_path: str):
    """Load PDF pages as LangChain Documents."""


    with logfire.span("PDF Parsing", filename=file_path):
        try:
            if not Path(file_path).is_file():
                raise FileNotFoundError(
                    f"PDF file not found: {file_path}"
                )

            loader = PyPDFLoader(file_path)
            documents = loader.load()

            # Remove pages that contain no extractable text.
            documents = [
                doc for doc in documents
                if doc.page_content.strip()
            ]

            if not documents:
                logfire.warning(
                    "PDF contains no extractable text",
                    filename=file_path,
                )
                return []

            logfire.info(
                "PDF parsing completed",
                filename=file_path,
                page_count=len(documents),
                extracted_characters=sum(
                    len(doc.page_content) for doc in documents
                ),
            )

            return documents

        except Exception:
            logfire.error(
                "PDF parsing failed",
                filename=file_path,
            )
            raise
