
# Blocklist Retriever 📃 (GSOC selection test)
This is a Python script that helps you retrieve the latest blocklists from a source of your choice and store them in a folder. The script is designed to run every day, without overwriting the files from the previous day.

Requirements
To use this script, you need the following:
```
Python 3.x: If you don't have it, you can download it from the official Python website.
```
requests library: This is a Python library that allows you to send HTTP requests easily. You can install it by running pip install requests in your terminal or command prompt.

## Configuration
Before you can use the script, you need to configure it. The script has four variables that you need to set:

- blocklist_urls: This is a list of URLs from where the blocklists will be retrieved. You can add or remove URLs as needed.

- output_folder: This is the folder where the blocklists will be stored. If the folder does not exist, the script will create it.

- date_format: This is the format for the date used in the filenames of the blocklists. You can change this if you prefer a different date format.

- output_filename_template: This is the template for the filename of the blocklists. It contains a placeholder for the date. If a file with the same name already exists, the script will append a number to the filename to avoid overwriting it.

## how to Use 
To use the script, follow these steps:
```
Install Python 3.x and the requests library (if you haven't already).
Download the blocklist_retriever.py file from this repository.
Open the file and set the variables in the Configuration section to your preferred values.
Save the file and close it.
Open a terminal or command prompt and navigate to the directory where the blocklist_retriever.py file is located.
Run the command python blocklist_retriever.py to execute the script.
The script will retrieve the latest blocklists from the URLs specified in blocklist_urls and save them in the output_folder. The filenames of the saved files will be constructed using the output_filename_template and the date of the previous day. If a file with that name already exists, a number will be appended to the filename to avoid overwriting it.
```



