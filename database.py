import psycopg2
import yaml
import sys

sys.path.append('./pet/')

from Player import Player
from pet.abstract_pet_factory import AbstractPetFactory
from pet.abstract_pet import AbstractPet
import init_Pet

class Database:
    
    def __init__(self):
        credentials = yaml.load(open("config/database_login.yaml"))
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
            from user_info.users
            where "discord_id" = {user_id};
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
            insert into user_info.users ("discord_id", "username", "eggs", "coins") values ({user_id}, '{username}', 1, 500);
        """)

        print(f"created user: {username}!")

        return self.record_from_user_id(user_id)
    
    #Save pet data into the PETS DB. | DB FORMAT: ID , SPECIES , COLOR, CLOSENESS, NAME, SIZE, ABILITYTYPE, RARITY, STATS[]
    def savePetToDB(self, user_id, username, pet):
        self.cursor = self.session.cursor()
        petStats = [0,0,0,0,0,7,7]
        
        self.cursor.execute("INSERT INTO user_info.Pets (discord_id, pet_name, species, color, closeness, size, ability_type, rarity, owner, stats) VALUES (%s,%s, %s,%s,%s, %s, %s,%s,%s, %s)",
        (user_id, pet.name, pet.species.name, pet.color.name, 0, pet.size.name, pet.ability_type.name, pet.rarity.name, username, petStats))
        
         # commit and unbind cursor
        self.session.commit()
        self.cursor.close()  
        
        print(f"logged pet info successfully")
        print(pet)
    
    #check if Pet name is found in the database, is so return pet object. Else return False
    def checkForPet(self, user_id, petName):
        self.cursor = self.session.cursor()

        try:
            self.cursor.execute(f"SELECT * FROM User_info.pets WHERE pet_name = '{petName}' AND discord_id = {user_id}")
            # fetch the row from the db contatining pet information
            p = self.cursor.fetchone()
            print(p)
            #print("pet stats: ", p[9])
            
            pet = init_Pet.DBPet(p[0], p[1], p[3], p[4], p[5], p[6], p[7], p[9])
            print(pet.printStats())
            return pet
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
            self.cursor.execute(f"SELECT * FROM user_info.users WHERE discord_id = {user_id}")
            # fetch the record from our execution
            user_record = self.cursor.fetchone()
            print(user_record)
        except:
            print("idk")
    
    #update player coins in DB
    def updateCoins(self, user_id, coins):
        self.cursor = self.session.cursor()
        
        try:
            self.cursor.execute(f"UPDATE user_info.users SET coins = {coins}  WHERE discord_id = '{user_id}'")
            print("DB coins updates successfully")
        except:
            print("DB ERROR")
    
    #update pet stats in DB
    def updatePetStats(self, user_id, petName, petStats):
        self.cursor = self.session.cursor()
        
        try:
            self.cursor.execute(f"UPDATE user_info.pets SET stats = ARRAY{petStats}  WHERE pet_name = '{petName}' AND discord_id = {user_id}")
            print("DB updates successfully")
        except:
            print("DB ERROR")
        # commit and unbind cursor
        self.session.commit()
        self.cursor.close()  
        
        