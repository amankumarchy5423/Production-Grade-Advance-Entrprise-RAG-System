from langchain_community.document_loaders import TextLoader
import logfire
from pathlib import Path


def text_loader(file_path:str):
    with logfire.span("text loading starts ",filename = file_path):
        try:

            if not Path(file_path).is_file():
                logfire.error(f" text file not found at{file_path} ")
                raise FileNotFoundError(f" text file not found at{file_path} ")
            
            loader = TextLoader(file_path=file_path)

            doc = loader.load()

            logfire.info(f'''document loaded with the length
                            of content ''',
                            filename = file_path,
                            page_content = len(doc))

            return doc.page_content()
        except Exception as e:
            logfire.error(e,file_path=file_path)
            raise e 