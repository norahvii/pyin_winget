import subprocess
import re
import os

# Run "winget upgrade" command and extract the list of package IDs
upgrade_output = subprocess.check_output(['winget', 'upgrade']).decode('utf-8')
lines = upgrade_output.split('\n')


package_ids = []

pattern = r'\b(?![0-9]+\.[0-9]+\b)\w+\.\w+\b'
matches = re.findall(pattern, str(lines))

print("---------------------------------------")

print("The following packages can be upgraded:")

for match in matches:
    print(match)
    package_ids.append(match)

print("---------------------------------------")

# Read the exclusions from the "exclusions.txt" file
exclusions = set()
exclusions_file = "exclusions.txt"
if os.path.exists(exclusions_file):
    with open(exclusions_file, 'r') as file:
        for line in file:
            exclusion = line.strip()
            if exclusion:
                exclusions.add(exclusion)
                print(f"Added {exclusion} to list of exclusions.")

# Filter out excluded package IDs
remaining_ids = [package_id for package_id in package_ids if package_id not in exclusions]

# Perform "winget upgrade" for each remaining package ID
for package_id in remaining_ids:
    try:
        print(f"Attempting update on {package_id}...")
        subprocess.call(['winget', 'upgrade', package_id])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while upgrading package {package_id}: {str(e)}")
