# py-illiad
Demo scripts for using ILLiad Web Services APIs with Python.

These scripts can be used as a starting point to incorporate ILLiad API functions into your Python programs. More information about the ILLiad Web Platform is available at https://support.atlas-sys.com/hc/en-us/articles/360011809394-The-ILLiad-Web-Platform-API.

This repo was created as part of a project at NC State University Libraries and is not affiliated with Atlas Systems.

## Prerequisites
### Install the Python requests library
```python
python -m pip install requests
```
### Configure ILLiad API
To connect to the ILLiad API, ask your ILLiad administrator to create an API key for this project. You will also need the base URL for your ILLiad system. It will look like `https://your.illiad.edu/ILLiadWebPlatform`.
### Config
Use `config.py.template` to create `config.py`. Fill in the values for your ILLiad API base URL and key.

## Usage
Open each script in your text editor of choice. Replace the sample data with real data where indiciated by the comments. Run the script from the command line. User and transaction data will be returned as JSON.
