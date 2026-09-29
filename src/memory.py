import chromadb
from config import CHROMA_DB_DIR

class TeamMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
        self.collection = self.client.get_or_create_collection(name="code_review_memory")

    def retrieve_past_context(self, current_diff: str, n_results: int = 3) -> str:
        results = self.collection.query(
            query_texts=[current_diff],
            n_results=n_results
        )
        
        if not results['documents'] or not results['documents'][0]:
            return "No relevant past team feedback found."
            
        context = "\n---\n".join(results['documents'][0])
        return context

    def save_feedback(self, diff: str, agent_review: str, developer_feedback: str, pr_number: str):
        # Stores the interaction so the agent learns preferences over time
        document = f"PR: {pr_number}\nDiff:\n{diff}\nReview:\n{agent_review}\nTeam Correction/Feedback:\n{developer_feedback}"
        self.collection.add(
            documents=[document],
            metadatas=[{"pr_number": pr_number}],
            ids=[f"pr_{pr_number}"]
        )