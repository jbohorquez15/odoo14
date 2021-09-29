from xmlrpc import client
url='https://jbohorquez15-odoo14-desarrollo-3299590.dev.odoo.com'
db='jbohorquez15-odoo14-desarrollo-3299590'
username='admin'
password='admin'

common =client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_acces = models.execute_kw(db, uid, password, 
                               'biblioteca.libros_lecturas','check_access_rights',
                                ['write'],{'raise_exception':False}
                               )
print(model_acces)

libros= models.execute_kw(db, uid, password, 
                                 'biblioteca.libros','search',
                                [[['categoria','in',['ciencias']]]])
print(libros)

lecturas= models.execute_kw(db, uid, password, 
                                 'biblioteca.libros_lecturas','search',
                                [[['name','=',['Prestamos fin']]]])

print(libros)

lecturas2= models.execute_kw(db, uid, password, 
                                 'biblioteca.libros_lecturas','fields_get',
                                [],{'attributes':['string','type','required']})

print(lecturas2)

nuew_lectura= models.execute_kw(db, uid, password, 
                                 'biblioteca.libros_lecturas','create',
                                [
                                    {
                                        'libros_ids':libros[0],
                                        'name':'pruebas2',
                                    }
                                ])

print(nuew_lectura)