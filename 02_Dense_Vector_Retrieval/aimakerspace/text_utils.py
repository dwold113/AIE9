import os
from typing import List


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding
        self.metadata = {}

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    with open(
                        os.path.join(root, file), "r", encoding=self.encoding
                    ) as f:
                        self.documents.append(f.read())

    def load_by_section(self):
        current_category = ""
        current_title = ""
        buffer = []
        # Grouping documents by section 
        documents = []
    
        with open(self.path, "r", encoding=self.encoding) as f:
            for line in f:
                stripped = line.strip()
                # Check if it's a PART heading
                if stripped.startswith("PART"):
                    if buffer:
                        documents.append({
                            "text": "\n".join(buffer),
                            "metadata":{
                                "category": current_category,
                                "title": current_title
                            }
                        })
                    current_category = stripped
                    buffer = [line]
                elif stripped.startswith("Chapter"):
                    if buffer:
                         documents.append({
                            "text": "\n".join(buffer),
                            "metadata":{
                                "category": current_category,
                                "title": current_title
                            }
                        })
                    current_title = stripped
                    buffer = [line]
                else:
                    buffer.append(line)
        if buffer:
             documents.append({
                "text": "\n".join(buffer),
                "metadata":{
                    "category": current_category,
                    "title": current_title
                }
            })
                
        return documents


    def load_documents(self):
        self.load()
        return self.documents


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 2000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks

    def split_sections(self, sections: List[dict]) -> List[dict]:
        chunked_with_metadata = []
        for section in sections:
            chunks = self.split(section["text"])
            for chunk in chunks:
                chunked_with_metadata.append({
                    "text": chunk,
                    "metadata": section["metadata"]
                })
        return chunked_with_metadata


if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
