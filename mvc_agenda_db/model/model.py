from mysql import connector

class Model:
    """
    *****************************************
    * a data model with MySQL for a store DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file ) as f_r:
            for line in f_r: 
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
        
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **************
    * Cps methods*
    *************
    """
    def create_zip(self,cp,ciudad,estado):
        try:
            sql = 'INSERT INTO cps (`cp`,`ciudad`,`estado`) VALUES (%s,%s,%s)'
            vals = (cp,ciudad,estado)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_zip(self,cp):
        try:
            sql = 'SELECT * FROM cps WHERE cp = %s'
            vals = (cp,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read__all__zips(self):
        try:
            sql = 'SELECT * FROM cps'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_zips_city(self, ciudad):
        try:
            sql = 'SELECT * FROM cps WHERE ciudad = %s'
            vals = (ciudad,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            print(err)
            return err

    def update_zip(self,fields,vals):
        try:
            sql = 'UPDATE cps SET '+','.join(fields)+'WHERE cp = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_zip(self, zip):
        try:
            sql = 'DELETE FROM cps WHERE cp = %s'
            vals = (zip,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    *contacto methods*
    ******************
    """
    def create_contact(self, nombre, apellidopat, apellidomat, correo,ntelefono):
        try:
            sql = 'INSERT INTO contacto (`nombre`, `apellidopat`, `apellidomat`, `correo`,`ntelefono`) VALUES (%s,%s,%s,%s,%s)'
            vals = (nombre, apellidopat, apellidomat, correo,ntelefono)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_contacts(self,id_contacto):
        try:
            sql = 'SELECT * FROM contacto WHERE id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read__all__contacts(self):
        try:
            sql = 'SELECT * FROM contacto'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_contact(self,fields,vals):
        try:
            sql = 'UPDATE contacto SET '+','.join(fields)+' WHERE id_contacto = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_product(self, id_product):
        try:
            sql = 'DELETE FROM contacto WHERE id_contacto = %s'
            vals = (id_product,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * lugar methods*
    ****************
    """
    
    def create_lugar(self, num_ext, num_int,colonia,calle,l_cp):
        try:
            sql = 'INSERT INTO lugar (`num_ext`, `num_int`,`colonia`,`calle`,`l_cp`) VALUES (%s,%s,%s,%s,%s)'
            vals = (num_ext, num_int,colonia,calle,l_cp)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_a_lugar(self,id_lugar ):
        try:
            sql = 'SELECT * FROM lugar WHERE id_lugar = %s'
            vals = (id_lugar,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read__all__lugar (self):
        try:
            sql = 'SELECT * FROM lugar'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_lugar(self,fields,vals):
        try:
            sql = 'UPDATE lugar SET '+','.join(fields)+' WHERE id_lugar = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_lugar(self, id_lugar):
        try:
            sql = 'DELETE FROM lugar WHERE id_lugar = %s'
            vals = (id_lugar,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    ****************
    * citas methods*
    ****************
    """
    
    def create_cita(self, fecha,hora,asunto,cp):
        try:
            sql = 'INSERT INTO cita (`fecha`,`hora`,`asunto`,`c_id_lugar`) VALUES (%s,%s,%s,%s)'
            vals = (fecha,hora,asunto,cp)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_a_cita(self,id_cita ):
        try:
            sql = 'SELECT * FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_cita_fecha(self,fecha ):
        try:
            sql = 'SELECT * FROM cita WHERE fecha = %s'
            vals = (fecha,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read__all__cita (self):
        try:
            sql = 'SELECT * FROM cita'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_cita(self,fields,vals):
        try:
            sql = 'UPDATE cita SET '+','.join(fields)+' WHERE id_cita = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_cita(self, id_lugar):
        try:
            sql = 'DELETE FROM cita WHERE id_cita = %s'
            vals = (id_lugar,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


