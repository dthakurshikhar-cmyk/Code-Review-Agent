import argparse
from src.github_client import GitHubClient
from src.agent import CodeReviewAgent
from src.memory import TeamMemory

def process_pr(repo_name: str, pr_number: int):
    print(f"Starting review for {repo_name} PR #{pr_number}...")
    
    github_client = GitHubClient(repo_name)
    agent = CodeReviewAgent()
    
    diff = github_client.get_pr_diff(pr_number)
    
    if not diff:
        print("No readable code changes found. Exiting.")
        return

    print("Analyzing code and checking team memory...")
    review_comment = agent.generate_review(diff, pr_number)
    
    print("Posting review to GitHub...")
    github_client.post_review_comment(pr_number, review_comment)
    print("Review posted successfully.")

def ingest_feedback(repo_name: str, pr_number: int, feedback: str):
    """
    Called manually or via webhook when a developer replies to the bot's comment.
    This enables the RAG memory to avoid repeating rejected suggestions.
    """
    github_client = GitHubClient(repo_name)
    diff = github_client.get_pr_diff(pr_number)
    
    memory = TeamMemory()
    # In a production app, you would fetch the specific agent review text from GitHub as well.
    memory.save_feedback(
        diff=diff, 
        agent_review="[Retrieved from GitHub history]", 
        developer_feedback=feedback, 
        pr_number=str(pr_number)
    )
    print(f"Feedback ingested for PR #{pr_number}. The agent has updated its preferences.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Code Review Agent")
    parser.add_argument("--repo", type=str, required=True, help="GitHub repository (e.g., octocat/Hello-World)")
    parser.add_argument("--pr", type=int, required=True, help="Pull Request number")
    parser.add_argument("--feedback", type=str, help="Developer feedback to correct the agent for future PRs")
    
    args = parser.parse_args()
    
    if args.feedback:
        ingest_feedback(args.repo, args.pr, args.feedback)
    else:
        process_pr(args.repo, args.pr)