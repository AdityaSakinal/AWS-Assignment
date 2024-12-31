# AWS-Assignment

Resource Used:
1. VS Code - for coding purpose (Python 3.13)
2. AWS free tire account - S3, IAM
3. Postman and Chrome - for testing purpose
4. PowerShell - to configure IAM user

Steps:
1. Gathered all reqired resources
2. Write our python code in VS code and saved as "app.py"
   Libraries used:
   a) Flask: To create the HTTP service
   b) Boto3: To interact with AWS
3. Created S3 bucket (without allowing public access)
   Objects:- (total 6)
   dir1 - empty folder
   dir2 - contains 2 text files in it (named: file1.txt & file2.txt)
   file1.txt (on root page)
   file2.txt (on root page)
4. Created IAM > user (with programmatic access) to access the S3 bucket credentials | also saved access key and secret key for login
   Policies attahed:
   a) AmazonS3ReadOnlyAccess (Ready to use)
   b) s3-new-fresh-policy (self-generated)
5. Used PowerShell for logging in IAM user and starting HTTP service
6. Testd the Service locally (on chrome) and also on Postman
7. After the complition, carefully cleaned up the services used

Challenges faced:
1. Got correct output for Response 1, but Response 2 and 3 were redirecting me to the same directory 
2. Couldnt complete Part2 - as am still learning Terraform
