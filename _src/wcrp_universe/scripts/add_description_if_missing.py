import json
from pathlib import Path

# Directory containing the JSON files
directory = Path("source")  # Replace with your actual path

# Iterate over all JSON files in the directory
for json_file in directory.glob("*.json"):
    try:
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Add the "description" key if it doesn't exist
        if "description" not in data:
            data["description"] = ""

            # Save the modified data back to the file
            with json_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✅ Updated: {json_file.name}")
        else:
            print(f"ℹ️ Already has description: {json_file.name}")

    except Exception as e:
        print(f"❌ Error with {json_file.name}: {e}")
