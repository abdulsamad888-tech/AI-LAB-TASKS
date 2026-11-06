import re
from sentence_transformers import SentenceTransformer

test_inputs = [
    "I can't submit CS4944 late!",
    "Contact us at support@university.edu.pk for help.",
    "",
    "کیا آپ پائتھن (Python) سیکھ رہے ہیں؟",
    "Version 2.0.1 released with 100% bug fixes.",
    "Data-driven AI pipelines don't fail easily."
]

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
print("--- Tokenization & Normalization Comparison ---\n")

for i, text in enumerate(test_inputs, 1):
    print(f"Test Case {i}:")
    print(f"Original Text: {repr(text)}")
    
    if not text.strip():
        print("Whitespace: [] (0)")
        print("Word-like: [] (0)")
        print("Model Subwords: [] (0)")
        print("-" * 40)
        continue


    whitespace_tokens = text.split()
    word_like_tokens = re.findall(r"\b\w+\b", text)

    encoded = model.tokenizer(text, truncation=False)
    subword_tokens = model.tokenizer.convert_ids_to_tokens(encoded["input_ids"])
    
    print(f"Whitespace ({len(whitespace_tokens)}): {whitespace_tokens}")
    print(f"Word-like ({len(word_like_tokens)}): {word_like_tokens}")
    print(f"Model Subwords ({len(subword_tokens)}): {subword_tokens}")
    print("-" * 40)