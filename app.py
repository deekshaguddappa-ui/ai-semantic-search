from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 1: Read documents
dataset_path = "dataset"
documents = []

for file in os.listdir(dataset_path):
    with open(os.path.join(dataset_path, file), 'r', encoding='utf-8') as f:
        documents.append(f.read())

# Step 2: Convert documents to vectors
doc_vectors = model.encode(documents)


# Step 3: Take user query
query = input("Enter your search query: ")

# Step 4: Convert query to vector
query_vector = model.encode([query])

# Step 5: Calculate similarity
similarity = np.dot(doc_vectors, query_vector.T)

# Step 6: Get best match
best_match_index = np.argmax(similarity)

# Step 7: Show result
print("\nBest matching document:")
print(documents[best_match_index])