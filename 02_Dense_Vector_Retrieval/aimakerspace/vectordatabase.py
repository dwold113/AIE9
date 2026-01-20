import numpy as np
from collections import defaultdict
from typing import Any, List, Tuple, Callable, Dict
from aimakerspace.openai_utils.embedding import EmbeddingModel
import asyncio


def cosine_similarity(vector_a: np.array, vector_b: np.array) -> float:
    """Computes the cosine similarity between two vectors."""
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)


class VectorDatabase:
    def __init__(self, embedding_model: EmbeddingModel = None):
        self.vectors = defaultdict[Any, Any](np.array)
        self.embedding_model = embedding_model or EmbeddingModel()
        # embeded categories to filter query and avoid scoring irrelevant vectors
        self.category_descriptions = {
        "PART 1: EXERCISE AND MOVEMENT": "exercise, stretching, workouts, fitness",
        "PART 2: NUTRITION AND DIET": "food, eating, diet, nutrition, meals",
        "PART 3: SLEEP AND RECOVERY": "sleep, rest, insomnia, recovery",
        "PART 4: STRESS MANAGEMENT AND MENTAL WELLNESS": "stress, anxiety, mental health",
        "PART 5: BUILDING HEALTHY HABITS": "habits, routines, behavior change",
        "PART 6: COMMON HEALTH CONCERNS": "health issues, medical concerns, symptoms",
        "PART 7: LIFESTYLE AND WELLNESS": "lifestyle, wellness, balance, overall health"
        }
        self.category_embeddings = None
        if self.category_embeddings is None:
           self.category_embeddings = {}
           for category, description in self.category_descriptions.items():
                self.category_embeddings[category] = self.embedding_model.get_embedding(description) 


    def insert(self, key: str, vector: np.array) -> None:
        self.vectors[key] = vector

    def insert_with_metadata(self, key: str, vector: np.array, metadata: dict) -> None:
        self.vectors[key] = {
            "vector": vector,
            "metadata": metadata
        }
        
    def classify_query(
        self, 
        query_vector: np.array, 
        distance_measure: Callable = cosine_similarity,
        ) -> str:
        scores = [
            (category, distance_measure(query_vector, category_vector))
            for category, category_vector in self.category_embeddings.items()
        ]
        return sorted(scores, key=lambda x: x[1], reverse=True)[0][0]

    def search(
        self,
        query_vector: np.array,
        k: int,
        filter_enabled: bool = False,
        distance_measure: Callable = cosine_similarity,
    ) -> List[Tuple[str, float]]:
        sorted_scores = []
        scores = []
        if filter_enabled:
            category = self.classify_query(query_vector)
            for key, value in self.vectors.items():
                if isinstance(value, dict):
                    if "metadata" in value and value["metadata"] is not None:
                        metadata = value["metadata"]
                        if metadata.get("category") == category:
                            scores.append((key, distance_measure(query_vector, value["vector"])))
        else:
            for key, value in self.vectors.items():
                if isinstance(value, dict):
                    if "vector" in value and value["vector"] is not None:
                        vector = value["vector"]
                        scores.append((key, distance_measure(query_vector, vector)))
                else:
                    scores.append((key, distance_measure(query_vector, value)))
           
        if scores:   
            sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:k]
       
        return sorted_scores


    def search_by_text(
        self,
        query_text: str,
        k: int,
        filtered_enabled: bool = False,
        distance_measure: Callable = cosine_similarity,
        return_as_text: bool = False,
    ) -> List[Tuple[str, float]]:
        query_vector = self.embedding_model.get_embedding(query_text)
        results = []
        if filtered_enabled:
            results = self.search(query_vector, k, True, distance_measure)
        else:
            results = self.search(query_vector, k, False, distance_measure)

        return [result[0] for result in results] if return_as_text else results

    def retrieve_from_key(self, key: str) -> np.array:
        return self.vectors.get(key, None)

    async def abuild_from_list(self, list_of_text: List[str]) -> "VectorDatabase":
        embeddings = await self.embedding_model.async_get_embeddings(list_of_text)
        for text, embedding in zip(list_of_text, embeddings):
            self.insert(text, np.array(embedding))
        return self
        
    async def abuild_from_list_with_metadata(self, list_of_docs: List[dict]) -> "VectorDatabase":
        texts = [doc["text"] for doc in list_of_docs]
        embeddings = await self.embedding_model.async_get_embeddings(texts)
        for doc, embedding in zip(list_of_docs, embeddings):
            self.insert_with_metadata(doc["text"], np.array(embedding), doc["metadata"])
        return self


if __name__ == "__main__":
    list_of_text = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
        "Chinchillas and kittens are cute.",
        "My sister adopted a kitten yesterday.",
        "Look at this cute hamster munching on a piece of broccoli.",
    ]

    vector_db = VectorDatabase()
    vector_db = asyncio.run(vector_db.abuild_from_list(list_of_text))
    k = 2

    searched_vector = vector_db.search_by_text("I think fruit is awesome!", k=k)
    print(f"Closest {k} vector(s):", searched_vector)

    retrieved_vector = vector_db.retrieve_from_key(
        "I like to eat broccoli and bananas."
    )
    print("Retrieved vector:", retrieved_vector)

    relevant_texts = vector_db.search_by_text(
        "I think fruit is awesome!", k=k, return_as_text=True
    )
    print(f"Closest {k} text(s):", relevant_texts)
