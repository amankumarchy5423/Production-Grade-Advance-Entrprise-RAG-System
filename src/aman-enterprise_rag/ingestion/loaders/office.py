import logfire
from langchain_community.document_loaders import UnstructuredFileLoader
from pathlib import Path

def parse_office(file_path: str):
    """Parse supported Office documents into LangChain Documents."""

    with logfire.span("Office Document Parsing", filename=file_path):
        try:
            if not Path(file_path).is_file():
                logfire.error(f"file not found {file_path}")
                raise FileNotFoundError(f"file not found {file_path}")
            
            loader = UnstructuredFileLoader(
                file_path,
                mode="single",
            )

            documents = loader.load()

            full_text = "\n".join(
                doc.page_content for doc in documents
            )

            if not full_text.strip():
                logfire.warning(
                    "Unstructured returned empty text",
                    file_path=file_path,
                )
            else:
                logfire.info(
                    "Office document parsed successfully",
                    file_path=file_path,
                    extracted_characters=len(full_text),
                    document_count=len(documents),
                )

            return documents

        except Exception:
            logfire.exception("Office document parsing failed")
            raise