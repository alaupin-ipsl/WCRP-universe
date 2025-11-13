import json
import os


def extract_unique_variable_ids(json_file_path):
    """Extract unique variable_id values from JSON database."""
    with open(json_file_path, "r") as f:
        data = json.load(f)

    variable_ids = set()
    for entry in data:
        if "variable_id" in entry:
            if entry["variable_id"] is not None:
                variable_ids.add(entry["variable_id"])

    return sorted(list(variable_ids))


def create_variable_json_files(variable_ids, output_dir):
    """Create individual JSON files for each variable_id."""
    os.makedirs(output_dir, exist_ok=True)

    for validatation_key in variable_ids:
        var_id = validatation_key.lower()
        json_content = {
            "@context": "000_context.jsonld",
            "id": var_id,
            "cmip_acronym": validatation_key,
            "long_name": "",
            "standard_name": "",
            "type": "variable",
            "units": "",
            "drs_name": validatation_key,
        }

        filename = f"{var_id}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            json.dump(json_content, f, indent=4)

        print(f"Created: {filepath}")


def remove_file(file_path):
    """Removes the file at the given file_path if it exists."""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been removed.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")


if __name__ == "__main__":
    json_file = "_src/wcrp_universe/scripts/input4MIPs/original_CVs/input4MIPs_db_file_entries.json"
    output_directory = "variable"

    unique_ids = extract_unique_variable_ids(json_file)

    print(f"Found {len(unique_ids)} unique variable_id values:")
    for var_id in unique_ids:  # here it is not ids, it is validation-key
        print(var_id)
        remove_file(f"variable/{var_id}.json")
    print(f"\nCreating JSON files in {output_directory}/ directory...")
    create_variable_json_files(unique_ids, output_directory)
