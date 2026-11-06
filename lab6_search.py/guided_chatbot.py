import argparse
from lab6 import Retriever

FAQ = [
    {
        "id": "faq:password",
        "question": "How do I reset my password?",
        "answer": "Use the recovery link on the login page.",
        "source": "it_help.txt",
    },
    {
        "id": "faq:submit",
        "question": "Where do I submit my assignment?",
        "answer": "Use the assignment upload page in the learning portal.",
        "source": "assessment.txt",
    },
    {
        "id": "faq:late",
        "question": "Can illness justify a late submission?",
        "answer": "Request an extension with medical evidence before the deadline.",
        "source": "handbook.txt",
    },
]


def build_bot(backend="tfidf"):
    records = [dict(r, text=r["question"] + " " + r["answer"]) for r in FAQ]
    return Retriever(records, backend)

def reply(engine, query, threshold=0.2):
    if not query.strip():
        return "Please enter a question."

    # 1. Exact match check
    for r in FAQ:
        if query.strip().casefold() == r["question"].casefold():
            return r["answer"]

    # 2. Vector search
    hits = engine.search(query)

    # 3. Filter hits using similarity threshold
    valid_hits = [hit for hit in hits if hit[1] >= threshold]

    if not valid_hits:
        return "No matching FAQ. Please contact the help desk."

    lines = ["Possible matches; choose or rephrase your question:"]
    for r, score in valid_hits:
        lines.append(f"{r['question']} (similarity {score:.3f})")
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--backend", choices=["tfidf", "embedding"], default="tfidf"
    )
    args = parser.parse_args()
    engine = build_bot(args.backend)
    print("FAQ assistant. Type exit to stop.")
    while True:
        try:
            query = input("You: ")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() == "exit":
            break
        print("Bot:", reply(engine, query))