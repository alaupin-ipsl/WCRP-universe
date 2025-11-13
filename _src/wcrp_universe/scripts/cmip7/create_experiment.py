
import requests
import json
import os
from datetime import datetime

# URLs of the JSON files on GitHub
json_url = 'https://raw.githubusercontent.com/WCRP-CMIP/CMIP7-CVs/refs/heads/main/CMIP7-CVs_experiment.json'

# Directory where the JSON files will be saved
save_dir = 'experiment/'

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

# Fetch the JSON data from both URLs
data = fetch_json(json_url)

# Extract the experiment_id dictionaries from both JSON files
experiment_ids = data.get('experiment', {})


def get_parent_activity_id(value: str, experiment_dir: str = "experiment"):
    if value == "none":
        return ["no parent"]

    parent_file = os.path.join(experiment_dir, f"{value}.json")

    if not os.path.exists(parent_file):
        print(f"Parent file for {value} not found : {parent_file}")
        return ["no parent"]

    with open(parent_file, "r", encoding="utf-8") as f:
        parent_data = json.load(f)

    return parent_data.get("activity_id")


# Normalize and merge data
def normalize_experiment_data(experiment_data):
    start_year = experiment_data.get('start-date', experiment_data.get('start_year', ''))
    end_year = experiment_data.get('end', experiment_data.get('end_year', ''))

    if not isinstance(start_year, int):
        try:
            if start_year.lower() != "none":
                start_year = datetime.fromisoformat(start_year).year
        except ValueError:
            start_year = None
    try:
        end_year = int(end_year)
    except ValueError:
        end_year = None  # or handle as needed if conversion fails
    
    model_realms = experiment_data.get('model-realms', [])
    if isinstance(model_realms, dict):
        model_realms = [model_realms]

    return {
        'activity_id': experiment_data.get('activity', []),
        'additional_allowed_model_components': model_realms,
        'description': experiment_data.get('description', ''),
        'end_year':end_year,
        'experiment': experiment_data.get('ui-label', ''),
        'experiment_id': experiment_data.get('validation-key', ''),
        'min_number_yrs_per_sim': experiment_data.get('minimum-number-of-years') if (experiment_data.get('minimum-number-of-years') != "none" and experiment_data.get('minimum-number-of-years') != "") else None,
        'parent_experiment_id': experiment_data.get('parent-experiment', []),
        'start_year': start_year,
        'sub_experiment_id': experiment_data.get('sub_experiment_id', []),
        'tier': experiment_data.get('tier', '')
    }

# Merge both datasets into a single dictionary
experiment_dict = {}
for key, value in experiment_ids.items():
    experiment_dict[key] = normalize_experiment_data(value)

# Save each experiment as an individual JSON file
for key, value in experiment_dict.items():
    experiment_data = {
        '@context':'000_context.jsonld',
        'id': value['experiment_id'].lower(),
        'type':'experiment',
        'experiment_id': value['experiment_id'],
        'activity_id': [value['activity_id'].split('/')[-1].lower()],
        'additional_allowed_model_components': [v.get('id').split('/')[-1].lower() for v in value['additional_allowed_model_components']],
        'description': value['description'],
        'end_year': int(value['start_year']) + int(value['min_number_yrs_per_sim']) - 1 if (value['start_year'] and value['min_number_yrs_per_sim'] and value['start_year'] != "none") else value['end_year'],
        'experiment': value['experiment'],
        'min_number_yrs_per_sim': value['min_number_yrs_per_sim'] if (value['min_number_yrs_per_sim'] != "none" and value['min_number_yrs_per_sim']!="" ) else None,
        'parent_activity_id': get_parent_activity_id(value['parent_experiment_id'].split('/')[-1].lower()),
        'parent_experiment_id': [value['parent_experiment_id'].split('/')[-1].lower() if value['parent_experiment_id'].split('/')[-1].lower() != "none" else None],
        'required_model_components': [v.get('id').split('/')[-1].lower() for v in value['additional_allowed_model_components'] if v.get("is-required")],
        'start_year': value['start_year'] if value['start_year'] != "none" else None,
        'tier': value['tier'],
        'drs_name': value['experiment_id']
    }

    file_path = os.path.join(save_dir, f"{key.lower()}.json")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump(experiment_data, f, indent=4)

print("Experiment files saved to", save_dir)
