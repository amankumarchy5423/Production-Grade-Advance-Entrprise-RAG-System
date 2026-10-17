from langchain_community.document_loaders import BSHTMLLoader
import logfire

def parse_html(file_path: str):
    with logfire.span("HTML Parsing", filename=file_path):
        try:
            loader = BSHTMLLoader(
                file_path=file_path,
                open_encoding="utf-8",
                get_text_separator="\n",
            )

            documents = loader.load()

            logfire.info(
                "HTML parsing completed",
                document_count=len(documents),
                extracted_characters=sum(
                    len(doc.page_content) for doc in documents
                ),
            )

            return documents.page_content()

        except Exception:
            logfire.error("HTML parsing failed", file_path=file_path)
            raise