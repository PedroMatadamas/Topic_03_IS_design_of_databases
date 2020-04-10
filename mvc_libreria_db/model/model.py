from mysql import connector

class Model:
    """
    ********************************************
    * A data model with MySQL for a library DB *
    ********************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
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
    ***************
    * Zip methods *
    ***************
    """
    def create_zip(self, cp, ciudad, estado):
        try:
            sql = 'INSERT INTO cps (`cp`, `ciudad`, `estado`) VALUES (%s, %s, %s)'
            vals = (cp, ciudad, estado)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback() #Elimina la operación intermedia de SQL y no ejecuta el cambio en la base de datos 
            return err

    def read_zip(self, cp):
        try:
            sql = 'SELECT * FROM cps WHERE cp = %s'
            vals = (cp,) # Se le pone ',' para indicar que es una tupla
            self.cursor.execute(sql, vals) #Toma la instrucción 'sql' y toma los valores de 'vals' para reemplazarlos por los '%s'
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM cps'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def read_zips_city(self, ciudad):
        try:
            sql = 'SELECT * FROM cps WHERE ciudad = %s'
            vals = (ciudad,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_zip(self, fields, vals):
        """
        fields = []
        vals = [] 

        if city != '':
            vals.append(city)
            fields.append('z_city = %s')

        if state != '':
            vals.append(state)
            fields.append('z_state = %s')
        vals.append(zip)
        vals = tuple(vals)
        """
        try:
            sql = 'UPDATE cps SET ' + ','.join(fields) + ' WHERE cp = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
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
    *********************
    * direccion methods *
    *********************
    """
    def create_dir(self, d_calle, d_col, d_numExt, d_numInt, d_cp):
        try:
            sql = 'INSERT INTO direccion (`d_calle`, `d_col`, `d_numExt`, `d_numInt`, `d_cp`) VALUES (%s, %s, %s, %s, %s)'
            vals = (d_calle, d_col, d_numExt, d_numInt, d_cp)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_dir(self, id_dir):
        try:
            sql = 'SELECT * FROM direccion WHERE id_dir = %s'
            vals = (id_dir,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_dir(self):
        try:
            sql = 'SELECT * FROM direccion'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_dir_cps(self, d_cp):
        try:
            sql = 'SELECT * FROM direccion WHERE d_cp = %s'
            vals = (d_cp,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    
    def update_dir(self, fields, vals):
        try:
            sql = 'UPDATE direccion SET ' + ','.join(fields) + 'WHERE id_dir = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_dir(self, id_dir):
        try:
            sql = 'DELETE FROM direccion WHERE id_dir = %s'
            vals = (id_dir,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    *  usuario methods  *
    *********************
    """
    def create_user(self, u_nombre, u_apellidopat, u_apellidomat, u_tel, correo, u_id_dir):
        try:
            sql = 'INSERT INTO usuario (`u_nombre`, `u_apellidopat`, `u_apellidomat`, `u_tel`, `correo`, `u_id_dir`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = ( u_nombre, u_apellidopat, u_apellidomat, u_tel, correo, u_id_dir )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_user(self, id_usuario):
        try:
            sql = 'SELECT * FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_users(self):
        try:
            sql = 'SELECT * FROM usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_user_ap(self, u_apellidopat):
        try:
            sql = 'SELECT * FROM usuario WHERE u_apellidopat = %s'
            vals = (u_apellidopat,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE usuario SET ' + ','.join(fields) + 'WHERE id_usuario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_user(self, id_usuario):
        try:
            sql = 'DELETE FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    *********************
    *  autor methods    *
    *********************
    """
    def create_autor(self, a_nombre, a_apellidoPat,a_apellidoMat):
        try:
            sql = 'INSERT INTO autor (`a_nombre`, `a_apellidoPat`, `a_apellidoMat`) VALUES (%s, %s, %s)'
            vals = ( a_nombre, a_apellidoPat,a_apellidoMat )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_autor(self, id_autor):
        try:
            sql = 'SELECT * FROM autor WHERE id_autor = %s'
            vals = (id_autor,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_autors(self):
        try:
            sql = 'SELECT * FROM autor'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    

    def update_autor(self, fields, vals):
        try:
            sql = 'UPDATE autor SET ' + ','.join(fields) + 'WHERE id_autor = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_autor(self, id_autor):
        try:
            sql = 'DELETE FROM autor WHERE id_autor = %s'
            vals = (id_autor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    """
    *********************
    *  libros methods   *
    *********************
    """

    def create_libro(self, l_nombre, l_cantidad,l_edicion,l_id_autor):
        try:
            sql = 'INSERT INTO libro (`l_nombre`, `l_cantidad`, `l_edicion`, `l_id_autor`) VALUES (%s, %s, %s, %s)'
            vals = ( l_nombre, l_cantidad,l_edicion,l_id_autor )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    def read_book(self, id_libro):
        try:
            sql = 'SELECT * FROM libro WHERE id_libro = %s'
            vals = (id_libro,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_books(self):
        try:
            sql = 'SELECT * FROM libro'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_book_name(self, l_nombre):
        try:
            sql = 'SELECT * FROM libro WHERE l_nombre = %s'
            vals = (l_nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    
    def update_book(self, fields, vals):
        try:
            sql = 'UPDATE libro SET ' + ','.join(fields) + 'WHERE id_libro = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_book(self, id_libro):
        try:
            sql = 'DELETE FROM libro WHERE id_libro = %s'
            vals = (id_libro,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    ***********************
    *  prestamo methods   *
    ***********************
    """

    def create_prestamo(self, pF_prestamo, pF_devolu,p_adeudo,p_id_usuario):
        try:
            sql = 'INSERT INTO prestamo (`pF_prestamo`, `pF_devolu`, `p_adeudo`, `p_id_usuario`) VALUES (%s, %s, %s, %s)'
            vals = ( pF_prestamo, pF_devolu,p_adeudo,p_id_usuario )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    def read_prestamo(self, id_prestamo):
        try:
            sql = 'SELECT * FROM prestamo WHERE id_prestamo = %s'
            vals = (id_prestamo,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_prestamos(self):
        try:
            sql = 'SELECT * FROM prestamo'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_prestamo_user(self, p_id_usuario):
        try:
            sql = 'SELECT * FROM prestamo WHERE p_id_usuario = %s'
            vals = (p_id_usuario,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    
    def update_prestamo(self, fields, vals):
        try:
            sql = 'UPDATE prestamo SET ' + ','.join(fields) + 'WHERE id_prestamo = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_prestamo(self, id_prestamo):
        try:
            sql = 'DELETE FROM prestamo WHERE id_prestamo = %s'
            vals = (id_prestamo,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    *********************************
    *  detalles prestamos methods   *
    *********************************
    """

    def create_details_prestamo(self,d_id_prestamo, d_id_libro, d_cantidad, d_adeudoTotal):
        try:
            sql = 'INSERT INTO detallesprestamo (`d_id_prestamo`, `d_id_libro`, `d_cantidad`, `d_adeudoTotal`) VALUES (%s, %s, %s, %s)'
            vals = ( d_id_prestamo, d_id_libro, d_cantidad, d_adeudoTotal )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    def read_detallesprestamo(self, d_id_prestamo):
        try:
            sql = 'SELECT * FROM detallesprestamo WHERE d_id_prestamo = %s'
            vals = (d_id_prestamo,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_detallesprestamo(self):
        try:
            sql = 'SELECT * FROM detallesprestamo'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_detalleprestamo_book(self, d_id_libro):
        try:
            sql = 'SELECT * FROM detallesprestamo WHERE d_id_libro = %s'
            vals = (d_id_libro,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    
    def update_detalleprestamo(self, fields, vals):
        try:
            sql = 'UPDATE detallesprestamo SET ' + ','.join(fields) + 'WHERE d_id_prestamo = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_detalleprestamo(self, d_id_prestamo):
        try:
            sql = 'DELETE FROM detallesprestamo WHERE d_id_prestamo = %s'
            vals = (d_id_prestamo,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err