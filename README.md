# estudo-acloudguru
Estudo sobre Cloud na plataforma  A cloud Guru

## AWS Certified Developer - Associate (DVA-C01)

### 5.5 - Introduction to Serverless Computing

#### Building a Serverless Website - Demo
Arquivos: [https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Serverless_Webite_Demo](https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Serverless_Webite_Demo)

### 5.6 - Version Control With Lambda - Demo
Arquivos: [https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Version_Control_With_Lambda](https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/tree/main/Version_Control_With_Lambda)

- `$LATEST` is always the lastversion of code you uploaded to lambda
- `Versionong and Aliases`: Use Lambda versioning and aliases to point your applications to specific version if you don't want to use $LATEST
- `Examples ARNs`: 
  - arn:aws:lambda:us-east-1:123456789012: function:mylambda:Prod
  - arn:aws:lambda:us-east-1:123456789012: function:mylambda:$LATEST
- `Update your Aliases`: If your application uses an alias instead of $LATEST, remember that it will not automatically use the new code when you upload it.

### 5.7 Lambda Concurrent Executions Limit
Know that a limit exits - 1,000 concurrent executions per second
- If you are running a serverless website like ACG, it’s likely you will hit the limit at some point
- If you hit the limit you will start to see invocations being rejected - 429 HTTP status code
- The remedy is to get the limit raised by AWS support
- Reserved concurrency guarantees a set number of concurrent executions are always available to a critical
function

### 5.8 Lambda and VPC Access

Enabling Lambda to Access VPC Resources
• To enable this, you need to allow the function to connect to the private subnet.
• Lambda needs the following VPC Configuration information so that it can connect to the VPC:
• Private subnet ID
• Security group ID (with required access)
• Lambda uses this information to set up ENIs using an available IP address from your private
subnet

Enabling Lambda to Access VPC Resources
• You add VPC information to your Lambda function config using the vpc-config parameter.
```bash
aws lambda update-function-configuration \
--function-name my-function \
--vpcconfig SubnetIds=subnet-1122aabb,SecurityGroupIds=sg-51530134
```

Lambda and VPCs
• It is possible to enable Lambda to access resources which are inside a private VPC.
• Provide VPC config to the function – private subnet ID, security group ID.
• Lambda uses the VPC information to set up ENIs using an IP from the private subnet CIDR range.
• The security group then allows your function to access resources in VPC.

### 5.9 Step Functions - Demo
Step Functions allows you to visualize and test your serverless
applications. Step Functions provides a graphical console to
arrange and visualize the components of your application as a
series of steps. This makes it simple to build and run multistep
applications. Step Functions automatically triggers and tracks
each step, and retries when there are errors, so your application
executes in order and as expected. Step Functions logs the state
of each step, so when things do go wrong, you can diagnose and
debug problems quickly

• Great way to visualize your serverless application.
• Step Functions automatically triggers and tracks each step.
• Step Functions logs the state of each step so if something
goes wrong you can track what went wrong and where

- [Perguntas frequentes sobre o AWS Step Functions](https://aws.amazon.com/pt/step-functions/faqs/)

### Hand-on Lab: Building a Serverless Application Using Step Functions, API Gateway, Lambda, and S3 in AWS
- [GitHub repository](https://github.com/JulieElkinsAWS/LALabs)

Anotações:
- criar email no SES
-  criar lambda email (email_reminder.py) e atualizar email gerado no SES
- criar lambda sms (sms_reminder.py)
- criar Step Function
- criar API GAteway (api_handler.py) e atualizar ARN da Step Function

Exemplo de request
```json
{
  "waitSeconds":"1",
  "preference": "email",
  "message": "mensagem um",
  "phone": "+5511999999999",
  "email": "seuemail@dominio.com"
}
``` 

### Hands-on Lab: Building and Troubleshooting a Serverless Web Application
- [GitHub repository](https://github.com/ACloudGuru/hands-on-aws-troubleshooting/tree/main/Building_and_Troubleshooting_a_Serverless_Web_Application)

```bash
git clone https://github.com/ACloudGuru/hands-on-aws-troubleshooting/

cd hands-on-aws-troubleshooting/Building_and_Troubleshooting_a_Serverless_Web_Application/

aws dynamodb create-table --table-name fortunes --attribute-definitions \
AttributeName=fort_id,AttributeType=N --key-schema \
AttributeName=fort_id,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

aws dynamodb batch-write-item --request-items file://items.json
```
S3 Bucket with Public Access Enabled
```json
{
    "Version": "2012-10-17",
    "Id": "Policy1650555565088",
    "Statement": [
        {
            "Sid": "Stmt1650555563210",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mywebsitefiles6754376825/*"
        }
    ]
}
```

### 5.12 Comparing Step Functions Workflows
- [Standard vs. Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
- Standard Workflow
  - Long running
  - At most once Model: tasks are never executed more than once, unless you explicity specify retry actions.
  - No-Idempotent Actions: When processing payments, you only want a payment to be processed once, not multiple times.
- Express Workflow
  - Short Lived: up to 5 minutes
  - At leat once model: ideal if there is a possibility that an execution might be run more than once or you require multiple concurrent executions.
  - Idempotent: for example, transforming input data and storing the result in DynamoDB

In Express Workflow we have two types: syncronous ans asynchronous

Express
Syncrono
Assyncrono

### 5.13 Understanding X-Ray
`AWS X-Ray` is a service that collects data about requests that
your application serves, and provides tools you can use to view,
filter, and gain insights into that data to identify issues and
opportunities for optimization. For any traced request to your
application, you can see detailed information not only about the
request and response, but also about calls that your application
makes to downstream AWS resources, microservices, databases
and HTTP web APIs.

- [Perguntas frequentes sobre o AWS X-Ray](https://aws.amazon.com/pt/xray/faqs/)
- [Integrating AWS X-Ray with other AWS services](https://docs.aws.amazon.com/xray/latest/devguide/xray-services.html)

### 5.15 X-Ray Configuration
High-Level Configuration Steps

X-Ray integrates with many AWS services like DynamoDB, Lambda, API Gateway, etc.
- You can also instrument your own applications to send data to X-Ray.
- Applications can be running on EC2, Elastic Beanstalk environments, on-premises systems and
ECS.
- For ECS, run the X-Ray daemon in it’s own Docker image, running alongside your application
- You’ll need three things:
  1. X-Ray SDK.
  2. X-Ray daemon.
  3. Instrument your application using the SDK to send the required data to X-Ray, e.g. data about
incoming HTTP requests to your application.
- If you want to also record application specific information in the form of key-value pairs, use
annotations to add user defined key-value pairs to your X-Ray data – allows you to filter, index and
search within X-Ray, e.g. game_name=TicTacToe, game_id=2645445842

### 5.16 Advanced API Gateway
Import API’s using Swagger 2.0 definition files
- API Gateway can be throttled
- Default limits are 10,000 RPS or 5000 concurrently
- You can configure API Gateway as a SOAP Webservice
passthrough or you can transform XML to JSON
