from model.model import Model

m = Model()

#m.create_zip('36000','Salamanca','Guanajuato')
#m.create_zip('76000','Queretaro','Queretaro')

#READ ALL ZIPS
#data = m.read_all_zips()
#print(data)

#READ A ZIP
#data = m.read_zip('36000')
#print(data)

#Read a zip by city
#data = m.read_zips_city('salamanca')
#print(data)

#update a zip
#fields = ('ciudad = %s',)
#vals = ('Irapuato',36000)
#m.update_zip(fields, vals)
#data = m.read_all_zips()
#print(data)

#Delete a zip
#m.delete_zip('76000')
#data = m.read_all_zips()
#print(data)

#m.create_dir('Jose','Soto','146',None,'36000',)
#m.create_dir('Rinconada','Rinconada','111',None,'36000',)
#print(data)


#Read a direccion
#data = m.read_dir(1)
#print(data)

#Read all dir
#data = m.read_all_dir()
#print(data)

#Read a dir by cp
#data = m.read_dir_cps('36000')
#print(data)

#UPDATE a dir
#fields = ('u_id_dir = %s',)
#vals = (3,2)
#m.update_dir(fields, vals)
#data = m.read_all_dir()
#print(data)

#m.delete_dir(1)
#data = m.read_all_dir()
#sprint(data)

#m.create_user('Cesar', 'Padron', 'García', '1234567897', 'cp@gmail.com',3)

#Read a user
#data = m.read_user(1)
#print(data)

#Read all users
#data = m.read_all_users()
#print(data)

#Read a user by last name
#data = m.read_user_ap('Padron')
#print(data)

#Update a user
""" fields = ('u_nombre = %s',)
vals = ('Manuel',2)
m.update_user(fields, vals)
data = m.read_all_users()
print(data)
"""

#Delete a user
#m.delete_user(2)
#data = m.read_all_users()
#print(data)

#m.create_autor('Joanne','J.K','Rowling')
#m.create_autor('Cesar','Padron','García')

#Read an autor
#data = m.read_autor(1)
#print(data)

#Read all autor
#data = m.read_all_autors()
#print(data)

#Update an autor
""" fields = ('a_nombre = %s',)
vals = ('Manuel',2)
m.update_autor(fields, vals)
data = m.read_all_autors()
print(data) """

#Delete an autor
#m.delete_autor(2)
#data = m.read_all_autors()
#print(data)

#data = m.create_libro('hp',100,'2da edicion',1)
#print(data)
#m.create_libro('hp2',100, '2da edicion',1)

#READ A BOOK
#data = m.read_book(2)
#print(data)

#READ ALL BOOKS
#data = m.read_all_books()
#print(data)

#Read a book by name
#data = m.read_book_name('hp')
#print(data)

#Update a book
""" fields = ('l_nombre = %s',)
vals = ('Harry Potter y la piedra filosofal',1)
m.update_book(fields, vals)
data = m.read_all_books()
print(data) """

#Delete a book
""" m.delte_book(2)
data = m.read_all_books()
print(data) """

#Create a prestamo
#data = m.create_prestamo('2020-03-02','2020-03-03',0,3)
#print(data)

#Read a prestamo
#data = m.read_prestamo(1)
#print(data)

#Read all prestamos
#data = m.read_all_prestamos()
#print(data)

#Read a prestamo by user
#data = m.read_prestamo_user(3)
#print(data)

#Update a prestamo
""" fields = ('p_adeudo = %s',)
vals = (10.0,1)
data = m.update_prestamo(fields, vals)
data = m.read_all_prestamos()
print(data) """

#Delete a prestamo
""" m.delete_prestamo(1)
data = m.read_all_prestamos()
print(data)
 """

#data = m.create_details_prestamo(2,1,100,0)
#print(data)

#Read a detalle prestamo
#data = m.read_detallesprestamo(2)
#print(data)

#Read all detalles prestamo
#data = m.read_all_detallesprestamo()
#print(data)

#Read a detalle prestamo by libro
#data = m.read_detalleprestamo_book(1)
#print(data)

#Update a detalle prestamo
""" fields = ('d_cantidad = %s',)
vals = (1000.0,2)
data = m.update_detalleprestamo(fields, vals)          EL D_CANTIDAD ES INT PERO NOS PIDE PONER EL VALOR EN FLOTANTE
data = m.read_all_detallesprestamo()
print(data) """


#BORRAR UN DETALLE DE PRESTAMO
""" m.delete_detalleprestamo(2)
data = m.read_all_detallesprestamo()
print(data) """

m.close_db() 