from model.model import Model

m=Model()

# m.create_zip('36700','Salamanca','Guanajuato')
# m.create_zip('36783','Salamanca','Guanajuato')
# m.create_zip('76001','Queretaro','Queretaro')

# m.create_client('Ana','Hernandez','Lopez','Hidalgo','34',None,'Centro','76001','ana.hernandez@gmail.com','1364825972')
# m.create_client('Pedro','Matadamas',None,'Liatris','121',None,'Floresta','36783','pedro_matadamas@hotmail.com','4641661118')
# m.create_client('Sofia','Matadamas',None,'Revolcion','201',None,'Centro','36700','sofia.matadamas@gmail.com','4646473350')
# m.create_client('Pedro','Matadamas',None,'Liatris','121',None,'Floresta','36783','pedro_matadamas@hotmail.com','4641661118')

# data = m.read__all__zips()
# print(data)

# fields = ('ciudad = %s',)
# vals =('Celaya',36783)
# m.update_zip(fields,vals)


# data = m.read_zips_city('Salamanca')
# print(data)

# data = m.read__all__zips()
# print(data)
# m.delete_zip('36783')
# data = m.read__all__zips()
# print(data)

# m.create_product('Jabon','La corona','Jabron de 1 Kg',35)
# m.create_product('Leche','Lala','Presentacion tetrapack',22.5)
# m.create_product('Clorox 1Lt','Clorox','Limpiador liquido',37.5)


#data = m.read__all__products()
#print(data)

# products = m.read_a_products_price_range(30,40)
# print(products)

# data = m.read_a_products(3)
# print(data)

# fields = ('p_price = %s',)
# vals =(20.5,3)
# products = m.update_product(fields,vals)

# data = m.read__all__products()
# print(data)

# m.delete_product(2)
# data = m.read__all__products()
# print(data)

# data = m.read_a_client_zip('36783')
# print(data)


# fields = ('c_zip = %s',)
# vals =(36783,3)
# m.update_client(fields,vals)
# client = m.read__all__clients()
# print(client)

# m.create_contact('Ana','Hernandez','Lopez','ana.hernandez@gmail.com','4641659885')
# m.create_contact('Juan','Martinez','Lopez','Juan.Lopez@gmail.com','4641657855')
# m.create_contact('Pablo','Paramo','Rodriguez','paparo@gmail.com','4645897539')

# fields = ('nombre = %s',)
# vals =('Andrea',1)
# products = m.update_contact(fields,vals)

# data = m.read__all__contacts()
# print(data)

# m.create_lugar('120',None,'Revolucion','Centro','36700')
# m.create_lugar('562',None,'Virreyes','Guanajuato','36783')
# m.create_lugar('624','12','Carretera Cel-Ira','Carretera','76001')

# data=m.read__all__lugar()
# print(data)

# fields = ('num_int = %s',)
# vals =('12',1)
# products = m.update_lugar(fields,vals)

data=m.read__all__lugar()
print(data)

# m.create_cita('2020/02/05','18:00','Pistear',1)
# m.create_cita('2020/04/16','19:30','Cine',6)
# m.create_cita('2020/01/31','14:20','Dentista',5)
# data=m.read__all__cita()
# print(data)

# data = m.read_a_cita_fecha('2020/01/31')
# print(data)
# m.close_db()

