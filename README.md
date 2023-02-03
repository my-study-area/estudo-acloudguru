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

####  5.7 Distributing and Installing Packages

Distributing and Installing Packages

Packages are invaluable when working in Python because the community has published a plethora of useful packages that can prevent us from needing to write that code ourselves. Additionally, we can share our own code with others by setting up our packages for distribution.

Documentation for This Video
Distributing Packages and Setuptools (https://packaging.python.org/guides/distributing-packages-using-setuptools/)
The Python Package Index (https://pypi.org/)
pip (https://pip.pypa.io/en/stable/quickstart/)
requests PyPi Page (https://pypi.org/project/requests/)


Installing Packages

Before we look at how we can go about making our own packages installable, let's cover installing a package from someone else. The primary place we'll be installing packages from will be from the "Python Package Index" or "PyPi" for short.

To install packages, we'll use pip. Let's install one of the most popular Python packages, the requests package.

$ pip3.7 install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl (57kB)
     |????????????????????????????????| 61kB 2.4MB/s
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/b9/63/df50cac98ea0d5b006c55a399c3bf1db9da7b5a24de7890bc9cfd5dd9e99/certifi-2019.11.28-py2.py3-none-any.whl (156kB)
     |????????????????????????????????| 163kB 8.0MB/s
Collecting idna<2.9,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
     |????????????????????????????????| 61kB 10.8MB/s
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/e8/74/6e4f91745020f967d09332bb2b8b9b10090957334692eb88ea4afe91b77f/urllib3-1.25.8-py2.py3-none-any.whl (125kB)
     |????????????????????????????????| 133kB 10.8MB/s
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
     |????????????????????????????????| 143kB 12.8MB/s
Installing collected packages: certifi, idna, urllib3, chardet, requests
Successfully installed certifi-2019.11.28 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.8
$


The requests package has some dependencies on other packages so pip will go ahead and download those dependencies. For the purposes of the PCAP exam, we just need to know how to install packages, but it is definitely worth viewing the other commands provided by pip by running pip --help.


Making a Package Installable

To make a package installable, it needs to have a file in the root of the package called setup.py. The structure of installable packages can vary, but the presence of a setup.py is constant. Let's make our helpers package installable by adding a setup.py and configuring it using the setup function. The "Python Packaging Authority" is the working group that maintains the core projects use for Python packaging, and they provide an example project. We're going to take the setup.py from that project as a starting point and modify it for our purposes. To begin, we do need to change our helpers directory to be the container for our installable package (different than a "python package"). Let's move things around before creating our setup.py.

$ cd ~/using_modules
$ mkdir -p helpers/src/helpers
$ mv helpers/*.py helpers/src/helpers/


Using tree on our directory structure for helpers will provide us a better way to view our directories. Note that you may have to install tree using sudo yum install tree.

$ tree helpers
helpers/
     |---> src
           |---> helpers
                |---> __init__.py
                |---> strings.py
                |---> variables.py

2 directories, 3 files


The outer helpers directory is there just to hold onto our code and isn't actually a Python package. The inner helpers will provide the package that can be imported after the distribution of this code is installed. For our code to be installable, we still need a setup.py file, which will go in the outer helpers directory. Feel free to download it directly using the curl command or copy and paste the contents below.

$ cd helpers/
$ curl -O https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py


Here's what it will look like:

~/using_modules/helpers/setup.py

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='helpers', # Required
    version='1.0.0', # Required
    description='Our custom collection of helper functions and variables.', # Optional
    # long_description=long_description, # Optional
    # long_description_content_type='text/markdown', # Optional (the README is markdown so we want to set this)
    # url='https://github.com/pypa/sampleproject', # Optional
    author='Keith Thompson',  # Optional
    author_email='keith@linuxacademy.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='helpers',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where='src'),  # Required
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # project_urls={  # Optional
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)


We left a lot of comments in there because they are good to read and understand, but they're for optional fields. Some of the important and potentially confusing lines to look at are the package_dir and packages arguments. We've put our code into the src directory. We've set these two arguments and used the find_packages function from setuptools to automatically find the packages that we're providing when someone installs this.


Building a Distribution

Making code installable in Python means that we need to create a distribution. There are two primary types of distributions: eggs and wheels. Wheels are the modern way to create a distribution and they're a single file that can be installed by pip. They will install any dependencies and place or unpack the source code into the site-packages directory for our Python installation. For us to build a wheel distribution, we need to install the wheel package and run a command using Python and our setup.py file. Let's install wheel first.

$ pip3.7 install --upgrade wheel
...


Setuptools provides us with multiple different subcommands if we process our setup.py through the Python interpreter. Let's take a look at those commands.

$ python3.7 setup.py --help
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/cloud_user/using_modules/helpers/README.md'


Our setup.py specifies that we'll provide documentation in a README.md file, but that file doesn't exist, so we can't read it. We'll cover file IO later in the course, but for now, we just need to make sure that that file exists.

$ touch README.md

Now, let's try again.

$ python3.7 setup.py --help
Common commands: (see '--help-commands' for more)

  setup.py build      will build the package underneath 'build/'
  setup.py install    will install the package

Global options:
  --verbose (-v)      run verbosely (default)
  --quiet (-q)        run quietly (turns verbosity off)
  --dry-run (-n)      don't actually do anything
  --help (-h)         show detailed help message
  --no-user-cfg       ignore pydistutils.cfg in your home directory
  --command-packages  list of packages that provide distutils commands

Information display options (just display information, ignore any commands)
  --help-commands     list all available commands
  --name              print package name
  --version (-V)      print package version
  --fullname          print <package name>-<version>
  --author            print the author's name
  --author-email      print the author's email address
  --maintainer        print the maintainer's name
  --maintainer-email  print the maintainer's email address
  --contact           print the maintainer's name if known, else the author's
  --contact-email     print the maintainer's email address if known, else the
                      author's
  --url               print the URL for this package
  --license           print the license of the package
  --licence           alias for --license
  --description       print the package description
  --long-description  print the long package description
  --platforms         print the list of platforms
  --classifiers       print the list of classifiers
  --keywords          print the list of keywords
  --provides          print the list of packages/modules provided
  --requires          print the list of packages/modules required
  --obsoletes         print the list of packages/modules made obsolete

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help


This gives us a lot of output, but only the common commands are provided to us. Reading the first line of the output, we can see that the rest of the commands can be shown by using --help-commands instead of --help. Let's do that.

$ python3.7 setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  check             perform some checks on the package
  upload            upload binary package to PyPI

Extra commands:
  bdist_wheel       create a wheel distribution
  alias             define a shortcut to invoke one or more commands
  bdist_egg         create an "egg" distribution
  develop           install package in 'development mode'
  dist_info         create a .dist-info directory
  easy_install      Find/get/install Python packages
  egg_info          create a distribution's .egg-info directory
  install_egg_info  Install an .egg-info directory for the package
  rotate            delete older distributions, keeping N newest files
  saveopts          save supplied options to setup.cfg or other config file
  setopt            set an option in setup.cfg or another config file
  test              run unit tests after in-place build
  upload_docs       Upload documentation to PyPI

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help


There are plenty of commands in here to play with, but the one that we care about is the extra command bdist_wheel. This will build a wheel distribution that will work perfectly with pip. Let's run that now.

$ python3.7 setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/helpers
copying src/helpers/__init__.py -> build/lib/helpers
copying src/helpers/strings.py -> build/lib/helpers
copying src/helpers/variables.py -> build/lib/helpers
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/helpers
copying build/lib/helpers/__init__.py -> build/bdist.linux-x86_64/wheel/helpers
copying build/lib/helpers/strings.py -> build/bdist.linux-x86_64/wheel/helpers
copying build/lib/helpers/variables.py -> build/bdist.linux-x86_64/wheel/helpers
running install_egg_info
running egg_info
writing src/helpers.egg-info/PKG-INFO
writing dependency_links to src/helpers.egg-info/dependency_links.txt
writing top-level names to src/helpers.egg-info/top_level.txt
reading manifest file 'src/helpers.egg-info/SOURCES.txt'
writing manifest file 'src/helpers.egg-info/SOURCES.txt'
Copying src/helpers.egg-info to build/bdist.linux-x86_64/wheel/helpers-1.0.0-py3.7.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/helpers-1.0.0.dist-info/WHEEL
creating 'dist/helpers-1.0.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'helpers/__init__.py'
adding 'helpers/strings.py'
adding 'helpers/variables.py'
adding 'helpers-1.0.0.dist-info/METADATA'
adding 'helpers-1.0.0.dist-info/WHEEL'
adding 'helpers-1.0.0.dist-info/top_level.txt'
adding 'helpers-1.0.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel


We now have a build and dist directory inside of the upper helpers directory. The artifact that we created will be within the dist directory and end with a .whl extension.

Going back to ~/using_modules, we'll actually run into issues if we try to run main.py right now because there is no helpers package local to the file anymore. Here's what we'll see when we run that script:

$ cd ~/using_modules
$ python3.7 main.py
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from helpers.strings import extract_lower
ModuleNotFoundError: No module named 'helpers.strings'


To get around this, we'll install our package using pip and the wheel we built.

$ pip3.7 install helpers/dist/helpers-1.0.0-py3-none-any.whl
Processing ./helpers/dist/helpers-1.0.0-py3-none-any.whl
Installing collected packages: helpers
Successfully installed helpers-1.0.0


When we run a script or load the REPL, we can load the helpers package and its internal modules.

$ python3.7 main.py
Lowercase letters (from strings): ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters (from package): ['K', 'T']
Off of helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']


Our package is installed and our script runs again without using a module local to the script. We're not going to cover publishing a package to PyPi in this course, but the PyPA documentation also details how to do that.

- [pip documentation](https://pip.pypa.io/en/stable/getting-started/)
- [Requests(HTTP Library)](https://pypi.org/project/requests/)
- [Class notes](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602891888875-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.7%20Distributing%20and%20Installing%20Packages.txt)

####  5.8 Docstrings, Doctests, and Shebangs
Docstrings, Doctests, and Shebangs

Now that we've created both modules and packages, we should help the potential users of our code by adding some documentation. Additionally, it's a little cumbersome to continually pass our main.py script to the Python executable to run it, so we're going to turn that script into an executable to make using it a little easier.

Documentation for This Video
Python Packages Documentation (https://docs.python.org/3/tutorial/modules.html#packages)
Python doctest Module (https://docs.python.org/3/library/doctest.html)


Documenting Python Code Using Docstrings

In many languages, when we write documentation for our code, it exists in the source code as a comment. Python is a little different because the documentation exists in the code. This official type of documentation is done by adding docstrings to our modules at the top of the file, or within functions, methods, and classes. Docstrings are triple quoted strings (start with """ or ''') used to write multi-line, structured documentation. To add documentation to a package, we can add a docstring to the top of the package's __init__.py file. Let's add some documentation to the helpers package.

~/using_modules/helpers/src/helpers/__init__.py

"""
Helpers is a package that provides easy to use helper functions
and variables.
"""

__all__ = ["extract_upper"]

from .strings import *


One of the most common misconceptions in Python is that we just created a "block comment". That's entirely incorrect. We created a multi-line string and the interpreter has to do some work to read that content. An actual comment starts with an octothorp/hash/pound sign and the interpreter completely ignores it. In the very specific case of a docstring, this string will actually be assigned to a hidden variable on the package, module, function: the __doc__ variable. To demonstrate this, we're going to change how we installed our package so that it will pick up code changes as we write them. First, let's uninstall the existing helpers package.

Note: Since pip matches your Python version, if you are not using pip 3.7 you can use the pip -V command to find its version.

$ pip3.7 uninstall -y helpers
Found existing installation: helpers 1.0.0
Uninstalling helpers-1.0.0:
  Successfully uninstalled helpers-1.0.0


We can install the package's source so that the changes we make will be available without a reinstall. This is handy in development, but not something we would have other users do.

$ cd ~/using_modules/helpers
$ pip3.7 install --editable .
Obtaining file:///home/cloud_user/using_modules/helpers
Installing collected packages: helpers
  Running setup.py develop for helpers
Successfully installed helpers


To see that our documentation is accessible in code, let's start the REPL, import our package, and access the __doc__ variable:

$ python3.7
Python 3.7.6 (default, Jan 30 2020, 15:46:02)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import helpers
>>> helpers.__doc__
'\nHelpers is a package that provides easy to use helper functions\nand variables.\n'


Since modules are just Python files, we can do this same thing to document any module we write. To document a function we will create a triple-quoted string at the top of the function body. Let's write some documentation for extract_upper now.

~/using_modules/helpers/src/helpers/strings.py

def extract_upper(phrase):
    """
    extract_upper takes a string and returns a list containing
    only the uppercase characters from the string

    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', '']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")


We've now created a docstring for a function. One of the downsides with documenting code is that it is pretty easy for the documentation and the code to get out of sync with one another, and bad documentation helps no one. Thankfully, docstrings can be used by another standard library module called doctest that allows us to add what looks like Python REPL lines into our docstrings that will then be evaluated to verify that they produce the expected results. Let's use the doctest module on our file to see if our documentation is accurate.

$ python3.7 -m doctest src/helpers/strings.py
**********************************************************************
File "src/helpers/strings.py", line 6, in strings.extract_upper
Failed example:
    extract_upper("Hello There, BOB")
Expected:
    ['H', 'T', 'B', 'O', '']
Got:
    ['H', 'T', 'B', 'O', 'B']
**********************************************************************
1 items had failures:
   1 of   1 in strings.extract_upper
***Test Failed*** 1 failures.


Our documentation is acting as an automated test and can now help us find regressions in our code and our documentation. In this case, the code works as intended, but there's a typo in the documentation that demonstrates how the code would be used. Let's fix that.

~/using_modules/helpers/src/helpers/strings.py

def extract_upper(phrase):
    """
    extract_upper takes a string and returns a list containing
    only the uppercase characters from the string

    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', 'B']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")


If we run doctest again, we should see no output because the results match the expected outcome.

$ python3.7 -m doctest src/helpers/strings.py
$


Setting a Shebang for a Script

The last thing we want to do is adjust main.py, so that we can run it directly. To do this, we need to do two things:

Explicitly make it executable using chmod.
Add a shebang to the top of the script so that the proper program will run the script.


Shebangs are useful because they allow us to write scripts in languages other than our shell's language (bash, sh, zsh, etc.). For this to work, we need to add a reference to the executable to use at the top of the file in a special comment called a shebang. From the perspective of Python, a shebang starts like any other comment, but then immediately has an exclamation point. Let's set our script to use the default python executable that is currently active in our environment.

~/using_modules/main.py

#!/usr/bin/env python

from helpers.strings import extract_lower
from helpers import variables
from helpers import *
import helpers

print(f"Lowercase letters (from strings): {extract_lower(variables.name)}")
print(f"Uppercase letters (from package): {extract_upper(variables.name)}")
print(f"Off of helpers: {helpers.strings.extract_lower(variables.name)}")


If we make the script exectuable and run it, we should see the usual output without needing to pass it to the Python executable.

$ chmod +x ~/using_modules/main.py
$ ~/using_modules/main.py
Lowercase letters (from strings): ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters (from package): ['K', 'T']
Off of helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']


Using the env command followed by the executable we'd normally use is a good approach to setting a shebang for Python. If we want to be explicit about the version of Python to use, then we can use the absolute path. Using our pyenv-installed Python 3.7.6, we would use this path:

~/using_modules/main.py

#!/home/cloud_user/.pyenv/versions/3.7.6/bin/python

from helpers.strings import extract_lower
from helpers import variables
from helpers import *
import helpers

print(f"Lowercase letters (from strings): {extract_lower(variables.name)}")
print(f"Uppercase letters (from package): {extract_upper(variables.name)}")
print(f"Off of helpers: {helpers.strings.extract_lower(variables.name)}")


If we switch our Python back to the system Python and run main.py, it will still have access to the helpers package which is only installed for version 3.7.6.

$ pyenv shell system
$ python -V
Python 2.7.5
$ ~/using_modules/main.py
Lowercase letters (from strings): ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
Uppercase letters (from package): ['K', 'T']
Off of helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [Other Resources and Code Scripts - CHAPTER 5.8 Docstrings, Doctests, and Shebangs](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602892402480-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%205.8%20Docstrings%2C%20Doctests%2C%20and%20Shebangs.txt)

#### 5.9 Helpful Modules: the math and random Modules

####  5.10 Helpful Modules: the platform Module

### 6 Classes and Object-Oriented Programming
#### 6.1 What is an Object?
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [CHAPTER 6.1 What is an Object?](https://acloudguru-content-attachment-production.s3-accelerate.amazonaws.com/1602892810482-Other%20Resources%20and%20Code%20Scripts%20-%20CHAPTER%206.1%20What%20is%20an%20Object.txt)