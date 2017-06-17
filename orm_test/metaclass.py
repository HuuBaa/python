# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add']=lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)
# class MyList(list,metaclass=ListMetaclass):
#     pass
# l=MyList()
# l.add(1)
# print(l)


class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):       
        if name == 'Model': 
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s'%name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mappings %s ==> %s'%(k,v))
                mappings[k]=v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):    
    def __init__(self,**kw):       
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError: 
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,value):
        self[key]=value

    def save(self):
        fields=[]
        params=  []
        args=[]
        for k,v in self.__mappings__.item():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))

        sql='insert into %s(%s) values (%s)'%(self.__table__,','.join(fields),','.join(args))
        print('SQL:%s'%sql)
        print('ARGS:%s'%str(args))

class Field(object):
    def __init__(self,name,columns_type):
        self.name=name
        self.columns_type=columns_type
    def __str__(self):
        return '<%s:%s>'%(self.name,self.columns_type)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        Field.__init__(self,name,'bigint')


class User(Model):
    id=IntegerField('id')
    name=StringField('name')
    email=StringField('email')
    password=StringField('password')

u=User(id='1',name='huu',email='742790905@qq.com',password='huabng1994')

