import datetime
import math
import json

tiempo = datetime.datetime.now()
print(tiempo.strftime('%Y-%m-%d'))


#Math Module
print(pow(2,5))
print(max(3,4,1,34,5))
print(min(32,3,1.2,0.1))
raiz = math.sqrt(100)
print(raiz)


#Using JSON 
dato= '{"nombre":"Pepito", "edad":34 , "ciudad":"Amsterdam"}'
ajson=json.loads(dato)
print(ajson['nombre'])