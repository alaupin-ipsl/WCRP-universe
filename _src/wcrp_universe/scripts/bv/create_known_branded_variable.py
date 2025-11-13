import json
import os
import time
from pathlib import Path

import requests

# GitHub repository information
repo_owner = "znichollscr"
repo_name = "CMIP7_DReq_Content"
branch = "extract-branded-variables"
path = "branded-variables"

# store directory
input_dir = Path(__file__).parent / "origin_data"
print(input_dir)
# Local directory where the modified JSON files will be saved
local_dir = "known_branded_variable/"

# Create the local directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)


def get_github_directory_contents(owner, repo, branch, path):
    """Fetch the contents of a directory in a GitHub repository with pagination support."""
    all_contents = []
    page = 1
    per_page = 100  # Maximum allowed by GitHub API

    while True:
        print(page)
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}&per_page={per_page}&page={page}"
        response = requests.get(url)
        response.raise_for_status()

        contents = response.json()

        # If we get an empty list or not a list at all, we've reached the end of pagination
        if not contents or not isinstance(contents, list) or len(contents) == 0:
            break

        all_contents.extend(contents)

        # If we got fewer items than the per_page limit, we've reached the end
        if len(contents) < per_page:
            break

        print(all_contents)
        break
        page += 1
    print(f"Total items found: {len(all_contents)}")
    return all_contents


def download_json_files():
    """Download all JSON files from the GitHub repository to the input directory."""
    try:
        # Get the directory contents
        print("Retrieving directory contents from GitHub...")
        contents = get_github_directory_contents(repo_owner, repo_name, branch, path)

        # Download each JSON file
        json_count = 0
        for item in contents:
            if item["type"] == "file" and item["name"].endswith(".json"):
                filename = item["name"]
                download_url = item["download_url"]

                # Skip if already downloaded
                output_path = os.path.join(input_dir, filename)
                if os.path.exists(output_path):
                    print(f"Skipping {filename} (already downloaded)")
                    json_count += 1
                    continue

                # Download the file
                print(f"Downloading {filename}...")
                response = requests.get(download_url)
                response.raise_for_status()

                # Save the raw file
                with open(output_path, "wb") as f:
                    f.write(response.content)

                json_count += 1

                # Add a small delay between downloads to avoid rate limiting
                time.sleep(0.1)

        print(f"Downloaded {json_count} JSON files to {input_dir}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub: {e}")
    except Exception as e:
        print(f"An error occurred during download: {e}")


def transform_json_files():
    """Transform the downloaded JSON files and save them to the output directory."""
    try:
        # Get all JSON files in the input directory
        input_files = list(Path(input_dir).glob("*.json"))

        print(f"Found {len(input_files)} JSON files to transform")

        for file_path in input_files:
            filename = file_path.name

            # Load the original JSON
            with open(file_path, "r") as f:
                try:
                    original_json = json.load(f)
                except json.JSONDecodeError:
                    print(f"Error: Could not parse {filename} as JSON. Skipping.")
                    continue
            # Modify the JSON according to requirements
            modified_json = {
                "@context": "000_context.jsonld",
                "id": original_json.get(
                    "branded_variable", ""
                ).lower(),  # Use branded_variable as id, lower ?
                "description": ""
                if original_json.get("description") is None
                or (isinstance(original_json.get("description"), float))
                else original_json.get("description", ""),
                "dimensions": original_json.get("dimensions", []),
                "type": "known_branded_variable",
                "cell_methods": original_json.get("cell_methods", ""),
                "variable": original_json.get("variableRootDD", ""),
                "label": original_json.get("branded_variable"),
                "drs_name": original_json.get("branded_variable"),
            }

            # Save the modified JSON
            save_path = os.path.join(local_dir, filename.lower())  # lower ?
            with open(save_path, "w") as f:
                json.dump(modified_json, f, indent=2)

    except Exception as e:
        print(f"An error occurred during transformation: {e}")


# Main execution
if __name__ == "__main__":
    # print("=== Phase 1: Downloading JSON files ===")
    # download_json_files()
    # TOO MUCH issues (too much number of files, rate imit on github)
    # so Manually copied for now (April 28th 2025)

    print("\n=== Phase 2: Transforming JSON files ===")
    transform_json_files()

    print("\nProcess completed successfully!")
