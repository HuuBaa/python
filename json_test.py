#import json
# d= dict(name='huu',age=24)
# f=open('HUU.txt','w')
# json.dump(d,f)
# f.close()
# print(json.dumps(d))

# f=open('HUU.txt','r')
# print(json.load(f))

# f.close()


# import json

# class Student(object):
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score

# def stu2dict(std):
#     return {
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }

# s=Student('Huu',24,100)
# print(json.dumps(s,default=lambda obj:obj.__dict__))

# json_str=json.dumps(s,default=stu2dict)

# def dict2stu(d):
#     return Student(d['name'],d['age'],d['score'])
# print(json.loads(json_str,object_hook=dict2stu))


import json
class Person(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
def per2json(per):
    return {
        'name':per.name,
        'age':per.age,
        'score':per.score
    }
huu = Person('Huu',24,100)
huujson=json.dumps(huu,default=per2json)
print(huujson)
print(json.dumps(huu, default=lambda obj: obj.__dict__))


jsonstr='{"name": "Huu", "age": 24, "score": 100}'
def json2per(d):
    return Person(d['name'],d['age'],d['score'])
huuobj=json.loads(jsonstr,object_hook=json2per)
print(huuobj)
print(type(huuobj))