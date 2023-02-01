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

###  5.17 API Gateway Caching and Throttling
- Default likmits: 10.000 rps and 5.000 concurrent requests
- if you exceed the limit, API Gateway will return an error: 429, too many requests
- API Gateway uses throttling to prevent your API from being overwhelmed by too many requests.
- [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)
- [Actions](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)

### 5.18 Serverless Summary - Part 1

###  5.19 Serverless Summary - Part 2



## Certified Associate in Python Programming Certification (PCAP 31-03)

### 2. Environment Setup
- [Simple Python Version Management: pyenv](https://github.com/pyenv/pyenv)
- [code-server](https://github.com/coder/code-server)
- [annotations](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602795379212-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%202.1%20Installing%20Python%203.7%20on%20a%20Cloud%20Playground.txt)

### 3. Lambdas, Closures, and Collection Functions
#### 3.1 Defining and Using Lambdas
```python
def square(num):
  return num * num

square_lambda = lambda num: num * 1

assert square_lambda(2) == square(2)
```

#### 3.2 Using Collection Functions
```python
from functools import reduce
from xml import dom


domain = [1, 2, 3, 4, 5]

#f(x) = x * 2
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))


the_sum = reduce(lambda num, acc: num + acc, domain, 10)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print('Sorting with a lambda key')
print(sorted(words, key=lambda s: s.lower()))

print('Sorting with a method')
words.sort(key=str.lower, reverse=True)
print(words)
```

#### 3.3 Understanding Closures
```python
def greeter(prefix):
  other_name = prefix + "lala"
  def greet(name):
      print(f"{prefix} {name} {other_name}")
  return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")
goodbye("Kyle")
```

####  3.4 Hands-on Lab: Processing Collections in Python Using Lambdas
```python
# 1) Sort the `people` list of dictionaries alphabetically based on the
# 'name' key from each dictionary using the `sorted` function and store
# the new list as `sorted_by_name`

people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
]

sorted_by_name = sorted(people, key=lambda people: people.get('name').lower())

assert sorted_by_name == [
    {"name": "Ariana Richards", "age": 40},
    {"name": "finn Carter", "age": 59},
    {"name": "Fred Ward", "age": 77},
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Victor Wong", "age": 74},
], f"Expected sorted_by_name to equal '{sorted_by_name}' to equal '{[{'name': 'Ariana Richards', 'age': 40}, {'name': 'finn Carter', 'age': 59}, {'name': 'Fred Ward', 'age': 77}, {'name': 'Kevin Bacon', 'age': 61}, {'name': 'Victor Wong', 'age': 74}]}''"

# 2) Use the `map` function to iterate over `sorted_by_name` to generate a
# new list called `name_declarations` where each value is a string with
# `<NAME> is <AGE> years old.` where the `<NAME>` and `<AGE>` values are from
# the dictionaries.

name_declarations = list(map(lambda p: f"{p.get('name')} is {p.get('age')} years old",sorted_by_name))

assert name_declarations == [
    "Ariana Richards is 40 years old",
    "finn Carter is 59 years old",
    "Fred Ward is 77 years old",
    "Kevin Bacon is 61 years old",
    "Victor Wong is 74 years old",
], f"Expected name_declarations to equal '{name_declarations}' to equal '{['Ariana Richards is 40 years old', 'finn Carter is 59 years old', 'Fred Ward is 77 years old', 'Kevin Bacon is 61 years old', 'Victor Wong is 74 years old']}'"

# 3) Combine the `filter` and `sorted` functions to iterate over `sorted_by_name` to generate a
# new list called `under_seventy` that only contains the dictionaries where the
# 'age' key is less than 70, sorting the list by age.

filtered_values = filter(lambda p: p.get('age') < 70, sorted_by_name)
under_seventy = sorted(filtered_values, key=lambda p: p.get('age')) 

assert under_seventy == [
    {"name": "Ariana Richards", "age": 40},
    {"name": "finn Carter", "age": 59},
    {"name": "Kevin Bacon", "age": 61},
], f"Expected under_seventy to equal '{under_seventy}' to equal '{[{'name': 'Ariana Richards', 'age': 40}, {'name': 'finn Carter', 'age': 59}, {'name': 'Kevin Bacon', 'age': 61}]}'"
```

### 4 The `if` Operator
#### 4.1 The `if` Operator
```python
if CONDITION:
  my_var = 1
else:
  my_var = 1

my_var = 1 if CONDITION else 2

print("A") if CONDITION else print("B")
```

### 5 Modules and Packages

#### 5.1 Creating and Using Python Modules
#### 5.2 Importing Modules
Documentation: [https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html)

####  5.3 Executing Modules as Scripts
- [__main__ — Top-level code environment](https://docs.python.org/3/library/__main__.html)
- [The import statement](https://docs.python.org/3/reference/simple_stmts.html#import)

#### 5.4 Hiding Module Entities
- [Other Resources and Code Scripts - CHAPTER 5.4 Hiding Module Entities](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602805552722-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.4%20Hiding%20Module%20Entities.txt)

CHAPTER 5.4
Hiding Module Entities

Now that we know how to import our modules, we might want to restrict what is exposed. In this lesson, we'll look at how we can hide some of our module's contents from being imported by other modules and scripts.

Documentation for This Video
Python Modules Documentation (https://docs.python.org/3/tutorial/modules.html)


What Are Module Entities?

When we see module entities, we need to see variables, functions, and classes (we'll cover classes in the next section). A module entity is anything we provide with a name in our module. As we've seen, these things are importable by name when we used from <module> import <name>.


Using __all__

If we want to prevent someone from importing an entity from our module, there aren't very many options. There are only two reasonable things we can do to restrict what is imported if someone uses from <module> import *. The first is by setting the __all__ variable in our module. Let's test this out by setting __all__ to a list including only extract_upper to see what happens in main.py.

~/using_modules/helpers.py

__all__ = ["extract_upper"]

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")


In main.py, we had been using both of these functions after loading them with from helpers import *. Here's another look at what main.py currently looks like.

~/using_modules/main.py

from helpers import *
import extras

print(f"Lowercase letters: {extract_lower(extras.name)}")
print(f"Uppercase letters: {extract_upper(extras.name)}")


With __all__ set in helpers, let's run main.py to see what happens.

$ python3.7 main.py
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(f"Lowercase letters: {extract_lower(extras.name)}")
NameError: name 'extract_lower' is not defined


Although name exists within helpers.py, it is not available in other modules via from helpers import *. This does not mean that we can't explicitly import extract_lower though. Let's modify main.py to import extract_lower by name.

~/using_modules/main.py

from helpers import *
from helpers import extract_lower
import extras

print(f"Lowercase letters: {extract_lower(extras.name)}")
print(f"Uppercase letters: {extract_upper(extras.name)}")


Let's run this one more time.

$ python3.7 main.py
Lowercase letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters: ['K', 'T']


While it doesn't allow us to prevent an entity from ever being imported, using __all__ does provide a way of sometimes restricting what is imported by modules and scripts consuming our modules and packages.



Using Underscored Entities

The other way we can prevent an entity from being exported automatically when someone uses from <module> import * is by making the first character an underscore (_). If we removed __all__ from helpers.py and created a variable called _hidden_var = "test", we would not have access to _hidden_var after running from helpers import *.

#### 5.5 The Module Search Path
CHAPTER 5.5
The Module Search Path

We've seen how to create our modules, and we've been able to import them from scripts adjacent to them in the file system, but where else can we import modules from?

Documentation For This Video
Python Modules Documentation (https://docs.python.org/3/tutorial/modules.html)
Python Standard Libary (https://docs.python.org/3/library/)
Sys Module (https://docs.python.org/3/library/sys.html)


Where Do Modules Come From?
Python is a language with a large and powerful standard library (https://docs.python.org/3/library/) of modules. To use these modules, we need to import them the same way that we've been importing our local modules, but how does Python know where to find the code for these modules? To understand this we need to look at the module search path. When Python goes looking for a module it has a path that works very much like the PATH variable used by our shell to find executables. A few different things are combined to make this path:


The directory containing the running script is automatically the first item in the search path. When running the REPL this will be the current directory.

The values set in the PYTHONPATH environment variable (if it is set) will be next in the list.

Finally, a list of directories configured when Python was installed. This list contains paths to directories that have the standard library modules and other packages we've installed.


If we want to see the module search path, we can import the sys module and view the path variable. Let's do this from a REPL.

$ python3.7
Python 3.7.6 (default, Jan 29 2020, 21:20:26)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python37.zip', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7/lib-dynload', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7/site-packages']
>>> exit()


Our Python install is in ~/.pyenv/versions/3.7.6, and the directories within contain the standard library. The site-packages directory contains third-party packages that we might install.

Just to show that we can change this, let's set the PYTHONPATH environment variable when starting the REPL.

$ PYTHONPATH=/home/cloud_user python3.7
Python 3.7.6 (default, Jan 29 2020, 21:20:26)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/home/cloud_user', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python37.zip', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7/lib-dynload', '/home/cloud_user/.pyenv/versions/3.7.6/lib/python3.7/site-packages']
>>> exit()


Now we can see that /home/cloud_user is the second item in the list. If we don't have a package in our current directory (the '' in the list), then it will check items passed in via PYTHONPATH before looking at items provided by our Python installation.

Note: Python will search for a built-in module by name before searching the paths in sys.path. This means you can't accidentally create a module with the same name as a built-in module, which prevents you from overwriting the built-in module.

[source](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602863127097-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.5%20The%20Module%20Search%20Path.txt)

#### 5.6 Creating and Using Python Packages

Python modules are simply Python files, but they are not the only way we can bundle up our code for reuse. Modules are not that easy to share. The primary way we share code is by wrapping our modules into packages. In this lesson, we'll learn what it takes to create a Python package.

Documentation for This Video
Python Packages Documentation (https://docs.python.org/3/tutorial/modules.html#packages)
Implicit Namespace Packages (https://www.python.org/dev/peps/pep-0420/#specification)


What Is a Package in Python?

A package is a namespace that allows us to group modules together. We create a package in Python by creating a directory to hold our modules and adding a special file named __init__.py. To show how a package can allow us to organize our code even more, let's create a helpers directory within using_modules. Let's create an empty __init__.py file within that directory.

$ mkdir ~/using_modules/helpers
$ touch ~/using_modules/helpers/__init__.py


The __init__.py doesn't need to have anything in it, though we can and will use it later. Next, let's move our helpers.py file into the helpers directory and change its name to strings.py since this file holds helper functions completely focused on working with strings. Our extras.py module actually doesn't do anything besides defining variables, so let's move it into helpers as helpers/variables.py.

$ cd ~/using_modules
$ mv helpers.py helpers/strings.py
$ mv extras.py helpers/variables.py


We now have a package that contains two modules, but we also broke main.py. Let's change main.py to use our package, instead of the modules that we had before.

~/using_modules/main.py

from helpers.strings import extract_lower, extract_upper
from helpers import variables
import helpers

print(f"Lowercase letters: {extract_lower(variables.name)}")
print(f"Uppercase letters: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")


The things to note here are that we can access the modules within our packages by importing them directly like with variables and by chaining them off of the package name to import entities directly from the child module. Just like we can with a module, we're able to import the package directly.

Running main.py again we should see:

$ python3.7 main.py
Lowercase letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters: ['K', 'T']
From helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']


What Does __init__.py Do?

The mysterious __init__.py file is used to set up the initialization code for a package, but what does this mean? This means that when the first subpackage or module within the parent package is accessed, then the code within __init__.py gets executed. The primary other thing we can do with our __init__.py is define the __all__ value for when we use from <package> import *. This doesn't immediately make sense because our __init__.py doesn't define anything right now, but we can import parts from our submodules and then make those immediately available if someone imports our package. Let's modify helpers/__init__.py to do just that.

~/using_modules/helpers/__init__.py

__all__ = ['extract_upper']

from .strings import *


The syntax of .strings allows us to specify that we want to load the strings module within our package, regardless of what our package is named. This is just a way to be a little more explicit. Let's change our main.py to use this.

~/using_modules/main.py

from helpers.strings import extract_lower
from helpers import variables
from helpers import *
import helpers

print(f"Lowercase letters (from strings): {extract_lower(variables.name)}")
print(f"Uppercase letters (from package): {extract_upper(variables.name)}")
print(f"Off of helpers: {helpers.strings.extract_lower(variables.name)}")


Once again, let's run our script to see that this code works.

$ python3.7 main.py
Lowercase letters (from strings): ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters (from package): ['K', 'T']
Off of helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']


Implicit Namespace Packages

While the PCAP syllabus doesn't actually mention implicit namespace packages, it is worth noting that they exist. As of Python 3.3, if we're creating a package that doesn't need to do anything with the __init__.py, then we can skip creating the __init__.py entirely and our package will work just fine.

- [https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602891102789-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.6%20Creating%20and%20Using%20Python%20Packages.txt](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602891102789-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.6%20Creating%20and%20Using%20Python%20Packages.txt)
- [6.4. Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Specification](https://peps.python.org/pep-0420/#specification)
