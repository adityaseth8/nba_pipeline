import requests
import boto3
import json


# Set up s3 client
s3 = boto3.client('s3', aws_access_key_id='redacted', aws_secret_access_key='redacted')

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

# load response.text from HTTP request into python dictionary
data = json.loads(response.text)

bucket = "nba-data-de"
# set key/object name for the data file that will be uploaded to S3 bucket
key = "nbaPlayersStats.json"

# encode python dictionary as a JSON-formatted string
json_data = json.dumps(data)

# upload JSON to s3 bucket
# args: name of s3 bucket to upload to, filename to use for object in bucket, data to upload  
s3.put_object(Bucket=bucket, Key=key, Body=json_data)

print("Data stored in S3 bucket: " + bucket + ", with key: " + key)
