# RESTwebservice
This is a simple REST webservice implemented in python, using the Flask Framework

# Runtime information
In order to run locally, you require the following software and packages
- Python 3.7.3
- Flask
- Flask-Restful

# API End-Points Details
The API consist of the following different end-points

### 1- closestToZero (GET): /close/
    Implements an API method that returns the closest to zero value, when supplied by an array parameter. If two of the numbers are equally close to zero, consider the positive number to be closer to zero.
    
    ![Alt text](/relative/path/to/images/endpoint1_test_result.jpg?raw=true "Optional Title")

### 2- sumOfNumbersFor (GET): /sumof-for/
    Computes the sum of the numbers in a given list using for loop

### 3- sumOfNumbersWhile (GET): /sumof-while/
    Computes the sum of the numbers in a given list using While loop

### 4- sumOfNumbersRecursion (GET): /sumof-recursion/
    Computes the sum of the numbers in a given list using recursion

### 5- getFibonacciAt (GET): /FibonacciAt/
    Returns the nth value from the list of the first 100 Fibonacci numbers given n as input

### 6- transformPerson (POST): /transformperson/
    Will fulfil the following transformation with the respective input and output message samples provided.

    Inputs Sample (json):-
    Customers =[{ "id": 1, 
            "first_name": "Jeanette", 
            "last_name": "Penddreth", 
            "email": "jpenddreth0@census.gov", 
            "gender": "Female", 
            "ip_address": "26.58.193.2" 
            }, 
            { "id": 2, 
            "first_name": "Giavani", 
            "last_name": "Frediani", 
            "email": "gfrediani1@senate.gov", 
            "gender": "Male", 
            "ip_address": "229.179.4.212" 
            }, 
            { "id": 3, 
            "first_name": "Noell", 
            "last_name": "Bea", 
            "email": "nbea2@imageshack.us", 
            "gender": "Female", 
            "ip_address": "180.66.162.255" 
            }, 
            { "id": 4, 
            "first_name": "Willard", 
            "last_name": "Valek", 
            "email": "wvalek3@vk.com", 
            "gender": "Male", 
            "ip_address": "67.76.188.26" 
            }]

            
    Output Sample (xml):- 
        <?xml version="1.0" ?>
            <response>
                <Gender>
                    <Type>Female</Type>
                    <PersonList>
                        <id>1</id>
                        <first_name>Jeanette</first_name>
                        <last_name>Penddreth</last_name>
                        <email>jpenddreth0@census.gov</email>
                        <gender>Female</gender>
                        <ip_address>26.58.193.2</ip_address>
                        <id>3</id>
                        <first_name>Noell</first_name>
                        <last_name>Bea</last_name>
                        <email>nbea2@imageshack.us</email>
                        <gender>Female</gender>
                        <ip_address>180.66.162.255</ip_address>
                    </PersonList>
                </Gender>
                <Gender>
                    <Type>Male</Type>
                    <PersonList>
                        <id>2</id>
                        <first_name>Giavani</first_name>
                        <last_name>Frediani</last_name>
                        <email>gfrediani1@senate.gov</email>
                        <gender>Male</gender>
                        <ip_address>229.179.4.212</ip_address>
                        <id>4</id>
                        <first_name>Willard</first_name>
                        <last_name>Valek</last_name>
                        <email>wvalek3@vk.com</email>
                        <gender>Male</gender>
                        <ip_address>67.76.188.26</ip_address>
                    </PersonList>
                </Gender>
            </response>
