import json
from datetime import datetime, timedelta
import random
import git

# Path to the data file
path = "./data.json"

# Initialize the Git repository
repo = git.Repo(".")

def mark_commit(x, y):
    # Calculate a random date
    date = datetime.now() - timedelta(weeks=52) + timedelta(days=1) + timedelta(weeks=x) + timedelta(days=y)
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")

    # Write the date to the file
    data = {"date": date_str}
    with open(path, "w") as f:
        json.dump(data, f)

    # Stage and commit the file with a specific date
    repo.index.add([path])
    repo.index.commit(date_str, author_date=date_str, commit_date=date_str)
    print(f"Committed on: {date_str}")

def make_commits(n):
    if n == 0:
        repo.git.push()
        return

    # Generate random values for x (weeks) and y (days)
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    mark_commit(x, y)

    # Recursive call to make the next commit
    make_commits(n - 1)

# Start making commits
make_commits(100)
