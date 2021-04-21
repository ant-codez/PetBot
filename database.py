import psycopg2
import yaml
from player import Player


class Database:
    
    def __init__(self):
        credentials = yaml.load(open(".config/database_login.yml"))
        # connect to the mathbot database
        self.session = psycopg2.connect(
            host = credentials['login']['host'],
            database = credentials['login']['database'],
            user = credentials['login']['user'],
            port = credentials['login']['port'],
            password = credentials['login']['password'],
        )

    def __del__(self):
        self.session.close()
    
    def test(self):
        self.cursor = self.session.cursor()
        
        self.cursor.execute(
                    psycopg2.SQL("INSERT INTO {} VALUES (%i, %s, $s)")
                    .format(psycopg2.Identifier('UserInfo'.users)),
                    [42, 'test', 1])
        
        try:
            rows = self.cursor.fetchall()
        
            for r in rows:
                print(f"id {r[0]} name {r[1]}")
        except:
            print("db fetch error")
            
        
        self.cursor.close()
   
    def commit_query(self, query: str):
        # bind cursor
        self.cursor = self.session.cursor()

        # execute query
        self.cursor.execute(query)

        # commit and unbind cursor
        self.session.commit()
        self.cursor.close()     
    
    def record_from_user_id(self, user_id: int):
        # bind the cursor
        self.cursor = self.session.cursor()

        print("checking if user exists...")

        # find user_id that we are looking for
        self.cursor.execute(f"""
            select *
            from "UserInfo".users
            where "id" = {user_id};
        """)
        
        user_record = self.cursor.fetchone()

        # fetch the record from our execution
        try:
            p = Player(user_record[0], user_record[2])
            print(f"name = {user_record[0]} userID={user_record[2]}")
            print("user exists!")
            print("player class:",p)
        except:
            print("user does not exist!")
            p = None
            
            

        # close the cursor
        self.cursor.close()

        # return it, it's either going to be None or a tuple
        return p
        
    def create_user(self, user_id: int, username: str):
        # find user_id that we are looking for
        self.commit_query(f"""
            insert into "UserInfo".users ("id", "username", "eggs") values ({user_id}, '{username}', 1);
        """)

        print(f"created user: {username}!")

        return self.record_from_user_id(user_id)
    
    #Save pet data into the PETS DB. | DB FORMAT: ID , SPECIES , COLOR, CLOSENESS, NAME, SIZE, ABILITYTYPE, RARITY
    def savePetToDB(self, user_id, username, pet):
        self.cursor = self.session.cursor()
        
        self.cursor.execute("INSERT INTO \"UserInfo\".pets (id, pet_name, species, color, closeness, size, ability_type, rarity, owner) VALUES (%s,%s, %s,%s,%s, %s, %s,%s,%s)",
        (user_id, pet.name, pet.species.name, pet.color.name, 0, pet.size.name, pet.ability_type.name, pet.rarity.name, username))
        
         # commit and unbind cursor
        self.session.commit()
        self.cursor.close()  
        
        print(f"logged pet info successfully")
        print(pet)
    
    #check if Pet name is found in the database, is so return pet object. Else return False
    def checkForPet(self, user_id, petName):
        self.cursor = self.session.cursor()

        try:
            self.cursor.execute(f"SELECT * FROM \"UserInfo\".pets WHERE pet_name = '{petName}' AND id = {user_id}")
            # fetch the record from our execution
            user_record = self.cursor.fetchone()
            print(user_record)
            print("pet name: ", user_record[0])
            return user_record
        except:
            print("No pet found, hatching egg...")
            return False
            
        # commit and unbind cursor
        self.session.commit()
        self.cursor.close()
    
    #check how many eggs the player has
    def checkTotalEggs(self, user_id):
        self.cursor = self.session.cursor()
        
        try:
            self.cursor.execute(f"SELECT * FROM \"UserInfo\".users WHERE id = {user_id}")
            # fetch the record from our execution
            user_record = self.cursor.fetchone()
            print(user_record)
        except:
            print("idk")