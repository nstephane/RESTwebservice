from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from simplexml import dumps
from itertools import groupby
from operator import itemgetter


app = Flask(__name__)
api = Api(app)

''' function to convert output to an xml format '''
@api.representation('application/xml')
def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response': data}), code)
    resp.headers.extend(headers or {})
    return resp

# Test Data
people = [{"id": 1,
           "first_name": "Jeanette",
           "last_name": "Penddreth",
           "email": "jpenddreth0@census.gov",
           "gender": "Female",
           "ip_address": "26.58.193.2"
           },
          {"id": 2,
           "first_name": "Giavani",
           "last_name": "Frediani",
           "email": "gfrediani1@senate.gov",
           "gender": "Male",
           "ip_address": "229.179.4.212"
           },
          {"id": 3,
           "first_name": "Noell",
           "last_name": "Bea",
           "email": "nbea2@imageshack.us",
           "gender": "Female",
           "ip_address": "180.66.162.255"
           },
          {"id": 4,
           "first_name": "Willard",
           "last_name": "Valek",
           "email": "wvalek3@vk.com",
           "gender": "Male",
           "ip_address": "67.76.188.26"
           }]

''' Function used to group the elements based on a key '''
def group_by_keys(iterable, keys):
    key_func = itemgetter(*keys)

    # For groupby() to do what we want, the iterable needs to be sorted
    # by the same key function that we're grouping by.
    sorted_iterable = sorted(iterable, key=key_func)

    return [list(group) for key, group in groupby(sorted_iterable, key_func)]


''' Test end point to demonstrate the TransformOperation end point '''
@app.route('/api/v1', methods=['GET'])
def api_all():
    genders = []
    result = []
    sorted_people = group_by_keys(people, ('gender',))
    j = 0

    for i in sorted_people:
        genders.append(i[j]['gender'])
        person = []
        person.append(sorted_people[j])

        result.append({"Gender": {"Type": genders[j],
                                  "PersonList": person}
                       })
        j = j+1

    return output_xml(result, 200)


''' First API End Point as per readme '''
class closestToZero(Resource):
    def __init__(self):
        super(closestToZero, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numbers', action='append', type=int)

    def get(self):
        #arr = [-4,5,6,2,6]
        arr = self.parser.parse_args()
        arr = arr['numbers']
        arr.sort()
        target = 0
        near = arr[0]
        for i in range(len(arr)):
            target = arr[i] * arr[i]
            if target <= (near * near):
                near = arr[i]
        return {'Closest value to 0 in': arr, 'Answer': near}


''' Second API End Point as per readme '''
class sumOfNumbersFor(Resource):
    def __init__(self):
        super(sumOfNumbersFor, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numbers', action='append', type=int)

    def get(self):
        def sumFor(n):
            s = 0
            for i in range(len(n)):
                s = s + n[i]
            return s
        array = self.parser.parse_args()
        array = array['numbers']
        return sumFor(array), 201


''' Third API End Point as per readme '''
class sumOfNumbersWhile(Resource):
    def __init__(self):
        super(sumOfNumbersWhile, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numbers', action='append', type=int)

    def get(self):
        def sumWhile(n):
            s = 0
            i = 0
            while i < len(n):
                s = s + n[i]
                i = i+1
            return s
        array = self.parser.parse_args()
        array = array['numbers']
        return sumWhile(array), 201


''' 4th API End Point as per readme '''
class sumOfNumbersRecursion(Resource):
    def __init__(self):
        super(sumOfNumbersRecursion, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numbers', action='append', type=int)

    def get(self):
        def sumRecur(n):
            if len(n) == 0:
                return 0
            else:
                return n[0] + sumRecur(n[1:])
        array = self.parser.parse_args()
        array = array['numbers']
        return sumRecur(array), 201


''' 5th API End Point as per readme '''
class getFibonacciAt(Resource):
    def __init__(self):
        super(getFibonacciAt, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('input', type=int)

    def get(self):
        arg = self.parser.parse_args()
        arg = arg['input']

        def fib(n):
            if n == 0:
                lst = 0
                return lst
            elif n == 1:
                lst = [0, 1]
                return lst
            else:
                lst = fib(n-1)
                lst.append(lst[-1] + lst[-2])
                return lst
        fiblist = fib(arg)
        result = fiblist[-1]
        return {'The result is': result}


''' 6th API End Point as per readme '''
class transformPerson(Resource):
    def __init__(self):
        super(transformPerson, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'id', type=int, required=True, location='json')
        self.parser.add_argument(
            'first_name', type=str, required=True, location='json')
        self.parser.add_argument(
            'last_name', type=str, required=True, location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument(
            'gender', type=str, required=True, location='json')
        self.parser.add_argument('ip_address', type=str, location='json')
        self.parser.add_argument('rnd_value', type=str, location='json')

    def post(self):
        input_list = request.get_json()
        genders = []
        result = []
        sorted_names = group_by_keys(input_list, ('gender',))
        j = 0

        for i in sorted_names:
            genders.append(i[j]['gender'])
            person = []
            person.append(sorted_names[j])

            result.append({"Gender": {"Type": genders[j],
                                      "PersonList": person}
                           })
            j = j+1
        return output_xml(result, 201)


api.add_resource(closestToZero, '/close/')
api.add_resource(getFibonacciAt, '/FibonacciAt/')
api.add_resource(sumOfNumbersFor, '/sumof-for/')
api.add_resource(sumOfNumbersWhile, '/sumof-while/')
api.add_resource(sumOfNumbersRecursion, '/sumof-recursion/')
api.add_resource(transformPerson, '/transformperson/')

if __name__ == '__main__':
    app.run(debug=True)
