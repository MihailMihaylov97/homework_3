from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


students = []
events = []
courses = []


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", 
                        type = str, 
                        required = True, 
                        help = "This field cannot be left blank")


    def get (self, name):
        for student in students:
            if student["name"] == name:
                return student
        return {"item" : None}, 404

    def post (self, name):
        if next(filter(lambda x: x["name"] == name, students), None) is not None:
            return {"message" : "A student with the name "{}" already exists.".format(name)}
        
        data = Student.parser.parse_args()

        student = {"name": name}
        students.append(student)
        return student, 201


    def delete(self, name):
        global students
        students = list(filter(lambda x: x["name"] != name, students))
        return {"message" : "Item delete"}
    
    def put (self, name):
        data=Student.parser.parse_args()
        student = next(filter(lambda x: x ["name"] == name, students), None)
        if student is None:
            student={"name" : name}
            students.append(student)
        else:
            student.update(data)
        return student



class Students(Resource):
    def get (self):
        return {"Students" : students}




class Course(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", 
                        type = str, 
                        required = True, 
                        help = "This field cannot be left blank")



    def get (self, name):
        for course in courses:
            if course["name"] == name:
                return course
        return {"item" : None}, 404

    def post (self, name):
        if next(filter(lambda x: x["name"] == name, courses), None) is not None:
            return {"message" : "A student with the name "{}" already exists.".format(name)}
        
        data = Student.parser.parse_args()

        course = {"name": name}
        courses.append(student)
        return course, 201


    def delete(self, name):
        global courses
        courses = list(filter(lambda x: x["name"] != name, courses))
        return {"message" : "Item delete"}
    
    def put (self, name):
        data=Course.parser.parse_args()
        course = next(filter(lambda x: x ["name"] == name, courses), None)
        if course is None:
            course={"name" : name}
            courses.append(course)
        else:
            course.update(data)
        return course

class Courses(Resource):
    def get (self):
        return {"courses" : courses}




class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", 
                        type = str, 
                        required = True, 
                        help = "This field cannot be left blank")



    def get (self, name):
        for event in events:
            if event["name"] == name:
                return event
        return {"item" : None}, 404

    def post (self, name):
        if next(filter(lambda x: x["name"] == name, events), None) is not None:
            return {"message" : "A student with the name "{}" already exists.".format(name)}
        
        data = Student.parser.parse_args()

        event = {"name": name}
        events.append(event)
        return event, 201


    def delete(self, name):
        global events
        events = list(filter(lambda x: x["name"] != name, events))
        return {"message" : "Item delete"}
    
    def put (self, name):
        data=Event.parser.parse_args()
        event = next(filter(lambda x: x ["name"] == name, events), None)
        if event is None:
            event={"name" : name}
            events.append(event)
        else:
            event.update(data)
        return event

class Events(Resource):
    def get (self):
        return {"events" : events}


api.add_resource(Student, "/student/<string:name>")
api.add_resource(Students, "/students")
api.add_resource(Course, "/course/<course:name>")
api.add_resource(Courses, "/courses")
api.add_resource(Event, "/event/<event:name>")
api.add_resource(Events, "/events")



