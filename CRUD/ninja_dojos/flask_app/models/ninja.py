from flask_app.config.mysqlconnection import connectToMySQL

db= "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        print(data)
        query = "INSERT INTO ninjas (first_name, last_name,age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def update(cls, form_data, ninja_id):
        query= f"UPDATE ninjas SET first_name= %(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = {ninja_id};"
        return connectToMySQL(db).query_db(query, form_data)
    
    @classmethod
    def get_one(cls, data, ninja_id):
        query= "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {'id':ninja_id}
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def delete(cls,data):
        query  = """DELETE FROM ninjas 
        WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query,data)