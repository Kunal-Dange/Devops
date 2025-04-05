import requests

# Your GitHub access token
GITHUB_TOKEN = 'your_github_token'

# GitHub API URL
GITHUB_API_URL = 'https://api.github.com'

# Your GitHub organization
ORGANIZATION = 'your_organization'

# Source and destination team slugs
SOURCE_TEAM_SLUG = 'source_team_slug'
DEST_TEAM_SLUG = 'dest_team_slug'

# Headers for the requests
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_team_id(team_slug):
    """Get the team ID from the team slug."""
    url = f'{GITHUB_API_URL}/orgs/{ORGANIZATION}/teams/{team_slug}'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()['id']

def get_team_repositories(team_id):
    """Get the list of repositories in the team using pagination."""
    repos = []
    page = 1
    while True:
        url = f'{GITHUB_API_URL}/teams/{team_id}/repos?per_page=100&page={page}'
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def add_repository_to_team(repo_name, team_id):
    """Add a repository to the team."""
    url = f'{GITHUB_API_URL}/teams/{team_id}/repos/{ORGANIZATION}/{repo_name}'
    response = requests.put(url, headers=HEADERS, json={'permission': 'admin'})
    response.raise_for_status()

def move_repositories(source_team_slug, dest_team_slug):
    """Move all repositories from one team to another."""
    source_team_id = get_team_id(source_team_slug)
    dest_team_id = get_team_id(dest_team_slug)
    
    repos = get_team_repositories(source_team_id)
    
    for repo in repos:
        repo_name = repo['name']
        print(f'Moving {repo_name} from {source_team_slug} to {dest_team_slug}')
        add_repository_to_team(repo_name, dest_team_id)
        print(f'Moved {repo_name} successfully')

if __name__ == '__main__':
    move_repositories(SOURCE_TEAM_SLUG, DEST_TEAM_SLUG)
