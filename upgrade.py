import subprocess
import re
import os

# Run "winget upgrade" command and extract the list of package IDs
upgrade_output = subprocess.check_output(['winget', 'upgrade']).decode('utf-8')
lines = upgrade_output.split('\n')

for i in lines:
	header = lines[0]

prefix_char = "I"
prefix_count = 0

suffix_char = "V"
suffix_count = 0

for i in header:
    prefix_count += 1
    print(str(i))
    if prefix_char in i:
        break

print(prefix_count)


for i in header:
    suffix_count += 1
    print(str(i))
    if suffix_char in i:
        break

print(suffix_count)



for line in lines[2:-1]:
	print(line[prefix_count:])


# for i in package_ids:
#     print(i)

#
# # Read the exclusions from the "exclusions.txt" file
# exclusions = set()
# exclusions_file = "exclusions.txt"
# if os.path.exists(exclusions_file):
#     with open(exclusions_file, 'r') as file:
#         for line in file:
#             exclusion = line.strip()
#             if exclusion:
#                 exclusions.add(exclusion)
#                 print(f"Added {exclusion} to list of exclusions.")
#
# # Filter out excluded package IDs
# remaining_ids = [package_id for package_id in package_ids if package_id not in exclusions]
#
# # Perform "winget upgrade" for each remaining package ID
# for package_id in remaining_ids:
#     try:
#         print(f"Attempting update on {package_id}...")
#         subprocess.call(['winget', 'upgrade', package_id])
#     except subprocess.CalledProcessError as e:
#         print(f"Error occurred while upgrading package {package_id}: {str(e)}")
