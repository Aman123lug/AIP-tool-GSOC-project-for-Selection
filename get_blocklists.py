import os
import requests
import datetime

# Config
blocklist_urls = ["https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv","https://example.com/blocklist1.csv", "https://example.com/blocklist2.csv"]
output_folder = "blocklist"
date_format = "%Y-%m-%d"
yesterday = datetime.date.today() - datetime.timedelta(days=1)
output_filename_template = "blocklist_{}.csv"

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Retrieve and save blocklists
for url in blocklist_urls:
    response = requests.get(url)
    if response.status_code == 200:
        output_filename = os.path.join(output_folder, output_filename_template.format(yesterday.strftime(date_format)))
        i = 0
        while os.path.exists(output_filename):
            i += 1
            output_filename = os.path.join(output_folder, output_filename_template.format(yesterday.strftime(date_format) + "_" + str(i)))
        with open(output_filename, "wb") as f:
            f.write(response.content)
        print("Retrieved and saved {} to {}".format(url, output_filename))
    else:
        print("Failed to retrieve {} (status code: {})".format(url, response.status_code))
