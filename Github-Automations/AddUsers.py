import requests

# Your GitHub access token
# Make sure you have the required access to perform this activity
GITHUB_TOKEN = 'your_github_token'

# GitHub API URL
GITHUB_API_URL = 'https://api.github.com'

# Your GitHub organization
ORGANIZATION = 'your_organization'

# Source and destination team slugs
SOURCE_TEAM_NAME = 'source_team_name'
DEST_TEAM_NAME = 'dest_team_name'

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

def get_team_members(team_id):
    """Get the list of members in the team."""
    url = f'https://api.github.com/teams/{team_id}/members'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return [member['login'] for member in response.json()]

def add_member_to_team(member, team_id):
    """Add a member to the team."""
    url = f'https://api.github.com/teams/{team_id}/memberships/{member}'
    response = requests.put(url, headers=HEADERS)
    response.raise_for_status()

def copy_members(SOURCE_TEAM_NAME, DEST_TEAM_NAME):
    """Copy members from one team to another."""
    source_team_id = get_team_id(source_team_team)
    dest_team_id = get_team_id(dest_team_name)
    
    members = get_team_members(source_team_id)
    
    for member in members:
        print(f'Copying {member} from {source_team_team} to {dest_team_name}')
        add_member_to_team(member, dest_team_id)
        print(f'Copied {member} successfully')

if __name__ == '__main__':
    copy_members(SOURCE_TEAM_NAME, DEST_TEAM_NAME)
