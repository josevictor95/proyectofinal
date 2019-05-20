from operator import itemgetter
import csv
import time

n = itemgetter('nombre')
a = itemgetter('apellido')
t = itemgetter('telefono')
i = itemgetter('id')

with open(r'C:\Users\Jose Victor Miron\Documents\proyectofinalprogra\contactos.csv') as csvfile:

    contactos = []

    reader = csv.reader(csvfile)

    for row in reader:

        user = {}

        user["id"] = row[0]
        user["nombre"] = row[1]
        user["apellido"] = row[2]
        user["telefono"] = row[3]

        contactos.append(user)


class C:
    def ListContacts(self):
        contactos.sort(key = a)
        for item in contactos:
            print(item['id'],'.', item['nombre'], item['apellido'], item['telefono'])
c = C()

class B:
    def AddContacts(self):
        d = {}
        for i in range(1):
            keys = 'id'
            keys1 = 'nombre'
            keys2 = 'apellido'
            keys3 = 'telefono'
            values = input('ingrese un id: ')
            values1 = input("ingrese nombre: ")
            values2 = input("ingrese apellido: ")
            values3 = input("ingrese telefono: ") 
            d[keys] = values
            d[keys1] = values1
            d[keys2] = values2
            d[keys3] = values3
        contactos.append(d)
b = B()

class D:
    def DelContacts(self):
        delnombre = input("ingrese el nombre de la persona que desea eliminar: ")
        delapellido = input("ingrese el apellido de la persona que desea eliminar: ")
        for i in range(len(contactos)): 
            if (contactos[i]['nombre'] == delnombre) and (contactos[i]['apellido'] == delapellido): 
                del contactos[i] 
                break
d = D()

class E:
    def CallContact(self):
        seleccion = input("seleccione el id del contacto que desea llamar: ")
        for i in range(len(contactos)): 
            if contactos[i]['id'] == seleccion: 
                print("llamando a: ",contactos[i]['nombre'],contactos[i]['apellido'])
                print("telefono:",contactos[i]['telefono'])
                print("Llamando... ")
                time.sleep(10)
                break
e = E()

class F:
    def MsgContacts(self):
        seleccion = input("seleccione el id del contacto al que desea mandar un mensaje: ")
        for i in range(len(contactos)): 
            if contactos[i]['id'] == seleccion: 
                print("To: ",contactos[i]['nombre'],contactos[i]['apellido'],"(",contactos[i]['telefono'],")")
                print("Msg: Feliz Dia!")
                print("enviando mensaje... ")
                time.sleep(5)
                break
f = F()

class G:
    def AddToFavorites(self):
        
        lst = [] 
        n = int(input("Ingrese el numero de personas que desea agregar a favoritos(maximo 5): ")) 

        for i in range(0, n): 
            ele = input("ingrese el nombre del contacto: ")
  
            lst.append(ele) 
        
        if n == 5:
            var1, var2, var3, var4, var5 = itemgetter(0, 1, 2, 3, 4)(lst)
            a = [d for d in contactos if d['nombre'] == lst[0]]
            b = [d for d in contactos if d['nombre'] == lst[1]]   
            c = [d for d in contactos if d['nombre'] == lst[2]]   
            d = [d for d in contactos if d['nombre'] == lst[3]]   
            e = [d for d in contactos if d['nombre'] == lst[4]]
            nueva_lista = [a,b,c,d,e]
            print("Lista de Favoritos: ")
            print(nueva_lista)               
        elif n == 4:
            var1, var2, var3, var4 = itemgetter(0, 1, 2, 3)(lst)
            a = [d for d in contactos if d['nombre'] == lst[0]]
            b = [d for d in contactos if d['nombre'] == lst[1]]   
            c = [d for d in contactos if d['nombre'] == lst[2]]   
            d = [d for d in contactos if d['nombre'] == lst[3]]   
            nueva_lista = [a,b,c,d]
            print("Lista de Favoritos: ")
            print(nueva_lista) 
        elif n == 3:
            var1, var2, var3 = itemgetter(0, 1, 2)(lst)
            a = [d for d in contactos if d['nombre'] == lst[0]]
            b = [d for d in contactos if d['nombre'] == lst[1]]   
            c = [d for d in contactos if d['nombre'] == lst[2]]     
            nueva_lista = [a,b,c]
            print("Lista de Favoritos: ")
            print(nueva_lista) 
        elif n == 2:
            var1, var2 = itemgetter(0, 1)(lst)
            a = [d for d in contactos if d['nombre'] == lst[0]]
            b = [d for d in contactos if d['nombre'] == lst[1]]    
            nueva_lista = a,b
            print("Lista de Favoritos: ")
            print(nueva_lista) 
        elif n == 1:
            var1 = itemgetter(0)(lst)
            a = [d for d in contactos if d['nombre'] == lst[0]]   
            nueva_lista = [a]
            print("Lista de Favoritos: ")
            print(nueva_lista) 
g = G()

class H:
    def GetFavoriteList(self):
        nueva_lista.sort(key = a)
        for item in nueva_lista:
            print(item['id'],'.', item['nombre'], item['apellido'], item['telefono'])
h = H()

class I:
    def RemoveFromFavorite(self):
        delnombre = input("ingrese el nombre de la persona que desea eliminar: ")
        delapellido = input("ingrese el apellido de la persona que desea eliminar: ")
        for i in range(len(nueva_lista)): 
            if (nueva_lista[i]['nombre'] == delnombre) and (nueva_lista[i]['apellido'] == delapellido): 
                del nueva_lista[i] 
                break
i = I()

class J:
    def loadFromFile(self):
        with open(r'C:\Users\Jose Victor Miron\Documents\proyectofinalprogra\contactos2.csv') as csvfile:

            reader = csv.reader(csvfile)

            for row in reader:

                user2 = {}

                user2["id"] = row[0]
                user2["nombre"] = row[1]
                user2["apellido"] = row[2]
                user2["telefono"] = row[3]

                contactos.append(user2)
j = J()

class K:
    def PostToHTTP(self):
        import requests

        payload = contactos
        r = requests.post('https://demo2452794.mockable.io/finalprograufm_get', json=payload)
        print(r.text)
k = K() 

class Q:
    def GetHTTP(self):
        import requests

        payload = contactos
        r = requests.get('https://demo2452794.mockable.io/finalprograufm_get', json=payload)
q = Q()


hdt = False
while hdt == False:
    print("CONTACT MANAGER")
    print("Que desea hacer? ")
    print("1. Ver lista de contactos.")
    print("2. Agregar contacto.")
    print("3. Eliminar contacto.")
    print("4. Llamar contacto.")
    print("5. Enviar mensaje a contacto.")
    print("6. Agregar a lista de favoritos.")
    print("7. Ver lista favoritos.")
    print("8. Eliminar favoritos.")
    print("9. Agregar archivo externo a lista.")
    print("10. POST to HTTP.")
    print("11. GET HTTP")
    print("12. Salir.")
    seleccion = int(input())
   
    if seleccion == 1:
        c.ListContacts()
    if seleccion == 2:
        b.AddContacts()
    if seleccion == 3:
        d.DelContacts()
    if seleccion == 4:
        e.CallContact()
    if seleccion == 5:
        f.MsgContacts()
    if seleccion == 6:
        g.AddToFavorites()
    if seleccion == 7:
        h.GetFavoriteList()
    if seleccion == 8:
        i.RemoveFromFavorite()
    if seleccion == 9:
        j.loadFromFile()
    if seleccion == 10:
        k.PostToHTTP()
    if seleccion == 11:
        q.GetHTTP()
    if seleccion == 12:
        hdt = True






