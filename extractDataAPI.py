import requests
import boto3
# import json
import pandas as pd


# Set up s3 client
s3 = boto3.client('s3', aws_access_key_id='REDACTED', aws_secret_access_key='REDACTED')

# Set endpoint URL to fetch data on NBA players 
url = "https://free-nba.p.rapidapi.com/players"

# Declare query parameters. Pull data from page 1-3, 25 results per page
querystring = {"page":["0", "1", "2"],"per_page":"25"}

# Declare headers to include in API request.
headers = {
    # specify RapidAPI key needed to authenticate request
	"X-RapidAPI-Key": "ddb2a038a0msh54bdd237ef3a945p17b068jsnf504609f8b52",
    # specify API host to connect to 
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

# Make request to API and pull data
response = requests.request("GET", url, headers=headers, params=querystring)

# convert JSON response to pandas dataframe
data = pd.json_normalize(response.json()['data'])

# Convert DataFrame to CSV
csv_data = data.to_csv(index=False)

# set bucket name to upload to
bucket = "nba-database"

# set key/object name for the data file that will be uploaded to S3 bucket
key = "nbaPlayersStats.csv"

# upload JSON to s3 bucket
# args: name of s3 bucket to upload to, filename to use for object in bucket, data to upload  
s3.put_object(Bucket=bucket, Key=key, Body=csv_data)

print("Data stored in S3 bucket: " + bucket + ", with key: " + key)

# Response JSON output
# {
#   "data": [
#     {
#       "id": 498,
#       "first_name": "John",
#       "height_feet": null,
#       "height_inches": null,
#       "last_name": "Salley",
#       "position": "",
#       "team": {
#         "id": 9,
#         "abbreviation": "DET",
#         "city": "Detroit",
#         "conference": "East",
#         "division": "Central",
#         "full_name": "Detroit Pistons",
#         "name": "Pistons"
#       },
#       "weight_pounds": null
#     },
#     {
#       "id": 499,
#       "first_name": "Dan",
#       "height_feet": null,
#       "height_inches": null,
# ...
#     "per_page": 25,
#     "total_count": 3838
#   }
# }

 