from github import Github
from config import GITHUB_TOKEN

class GitHubClient:
    def __init__(self, repo_name: str):
        self.client = Github(GITHUB_TOKEN)
        self.repo = self.client.get_repo(repo_name)

    def get_pr_diff(self, pr_number: int) -> str:
        pr = self.repo.get_pull(pr_number)
        # Using the requests library to fetch the raw diff URL or PyGithub's internal methods
        # PyGithub returns file objects, we can extract patch data
        diffs = []
        for file in pr.get_files():
            if file.patch:
                diffs.append(f"File: {file.filename}\n{file.patch}")
        return "\n\n".join(diffs)

    def post_review_comment(self, pr_number: int, review_body: str):
        pr = self.repo.get_pull(pr_number)
        pr.create_issue_comment(review_body)