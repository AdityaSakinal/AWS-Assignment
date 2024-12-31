from flask import Flask, jsonify
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize Flask app
app = Flask(__name__)

# AWS S3 Configuration
s3 = boto3.client('s3')
BUCKET_NAME = 'mybucket1q2w' 

# Helper function to list content in the S3 bucket
def list_s3_content(path=''):
    try:
        # List the objects in the bucket at the specified path (if any)
        result = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path, Delimiter='/')

        # Print out the raw response for debugging
        print("S3 Response:", result)

        # Collect the directory names (CommonPrefixes) and files (Contents) from the response
        dirs = [content['Prefix'].split('/')[-2] for content in result.get('CommonPrefixes', [])]
        files = [content['Key'].split('/')[-1] for content in result.get('Contents', [])]

        # Debugging logs
        print("Dirs:", dirs)
        print("Files:", files)

        # If the request path is a directory and has no files, return an empty list
        if path and not dirs and not files:
            return []

        # Return the combined content (directories + files)
        return dirs + files
    except NoCredentialsError:
        return {"error": "Credentials not available"}

# Define the route for listing bucket content
@app.route('/list-bucket-content', defaults={'path': ''}, methods=['GET'])
@app.route('/list-bucket-content/<path>', methods=['GET'])
def list_bucket_content(path):
    # Get the list of content at the specified path (or root if no path)
    content = list_s3_content(path)
    
    # Return the content as a JSON response
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
