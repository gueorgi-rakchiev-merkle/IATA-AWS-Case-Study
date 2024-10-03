# AWS-Case-Study
The solution was created using a step function as the main orchestrator of the ETL. In the step function there are two Lambda functions. The extraction Lambda function gets the sales records zip file from the provided URL and uploads it to S3 landing zone. The transformation Lambda function takes the zipped file from the S3 landing zone location, uncompresses the file, and transforms it per the requirements. After the transformation, the Glue crawler "george-iata-glue-crawler" is triggered and creates a table in the Glue catalog database named "george-iata-glue-database". 

Required resources are managed in the CloudFormation template iata-deployment.yaml, including the necessary roles and policies. Also included are the neccessary resources needed to properly query the data in Athena.
# Repo Structure
In the deployment folder you will find the zipped Lambda Functions, the CloudFormation deployment yaml, and an example of the input needed for the step function. The code folder has the python code used for the Lambda functions. 
# Lambda Deployment
In the repository you will find two zip files for the respective Lambda functions. These files must be uploaded to a seperate S3 bucket. The bucket name of where the Lambda function zip files are stored is taken as a parameter in the CloudFormation template. Be sure to leave the files in the base of the bucket.
# Running the Step Function
The step function must be executed with a proper input in order to succesfully process the data. The file example_input.json can be used for the input. Take note that if the bucket name or crawler name are changed, then the input must be updated accordingly.
