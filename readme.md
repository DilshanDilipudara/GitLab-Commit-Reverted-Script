# GitLab Commit Reverted Script

This script is designed to facilitate the management of repositories in GitLab groups. It provides functionality for both downloading repositories from a specified group and uploading changes back to the respective repositories.

## Requirements

- Python 3.x
- `gitlab` Python package (`pip install python-gitlab`)

## Setup

1. Install the required Python packages using pip:
    ```
    pip install python-gitlab
    ```

2. Set up a GitLab private token with the appropriate permissions. Replace `private_token` parameter in the script with your generated private token.

3. Define the `group_id` variable in the script with the ID of the GitLab group containing the repositories you want to manage.

## Usage

1. Clone repositories from the specified GitLab group:
    ```
    python main.py
    ```

2. Make changes to the downloaded repositories as needed.

3. Upload changes back to their respective repositories:
    ```
    python main.py
    ```

## Configuration

- `url`: The URL of your GitLab instance.
- `group_id`: The ID of the GitLab group containing the repositories you want to manage.
- `rootdir`: The directory where repositories will be cloned/downloaded.
- `depth`: The depth of subdirectories to search for repositories within `rootdir`.

## Notes

- This script assumes that you have appropriate permissions to clone and push to the repositories within the specified GitLab group.
- Be cautious when using the upload functionality, as it automatically reverts the latest commit (`git revert HEAD~0`) and pushes changes back to the repository.

