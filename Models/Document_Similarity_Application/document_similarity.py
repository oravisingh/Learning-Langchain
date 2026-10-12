from dotenv import dotenv_values
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

api_key = dotenv_values().get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Set OPENROUTER_API_KEY in your .env file.")

embeddings = OpenAIEmbeddings(
    model="nvidia/llama-nemotron-embed-vl-1b-v2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    check_embedding_ctx_length=False,
    dimensions = 32
)

document = [
  "Mahatma Gandhi led India to independence through non-violent civil disobedience and inspired civil rights movements globally.",
  "Albert Einstein revolutionized physics by developing the theory of relativity, forever changing our understanding of space, time, and gravity.",
  "Nelson Mandela dedicated his life to dismantling apartheid in South Africa and served as the nation's first Black president.",
  "Martin Luther King Jr. championed civil rights in the United States using peaceful protest to fight racial inequality.",
  "Abraham Lincoln preserved the American Union during the Civil War and signed the Emancipation Proclamation to abolish slavery.",
  "Leonardo da Vinci mastered both science and art, leaving behind timeless masterpieces and visionary engineering designs."
]


query1 = "Who was the first Black president of South Africa?"
query2 = "BlackWhole is no way possible without the theory of relativity."

document_vector = embeddings.embed_documents(document)
query_vector = np.array([embeddings.embed_query(query2)])

cosine_similarities = cosine_similarity(query_vector, document_vector)
print("Cosine Similarities:", cosine_similarities)

ranked_scores = sorted(
    enumerate(cosine_similarities[0]),
    key=lambda x: x[1],
    reverse=True,
)

best_index, best_score = ranked_scores[0]

print("Best match:", document[best_index])
print("Similarity:", float(best_score))


######################JabarDast########################