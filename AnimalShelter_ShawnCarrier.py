from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://localhost:46914')
        #self.client = MongoClient('mongodb://%s:%s@localhost:46914/?authMechanism=DEFAULT&authSource=AAC'%(username,password)
        self.database = self.client['AAC']

    # Create new animal entry in database
    def create(self, data):
        if data is not None:
            # data should be dictionary
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Failed to Create Data")
            
    # Search database for one animal
    def read(self, data):
        return self.database.animals.find_one(data)
            
    # Search database for all animals based on search criteria
    def readAll(self, data):
        if data is not None:
            cursor = self.database.animals.find(data, {'_id':False})
            return cursor
        else:
            raise Exception("No data to read; search criteria empty.")
                        
    # Delete animal from database
    def delete(self, data):
        if data is not None:
            data = self.read(data) # Find animal within database
            if data is None:
                print("Animal not in database.")
                return
            self.database.animals.delete_many(data)  # data should be dictionary 
        else:
            raise Exception("No data to delete, animal data is empty.")
            
    # Update animal information within database
    def update(self, criteria, data):
        if criteria is not None and data is not None:
            self.database.animals.update_many(criteria,{"$set":data}) 
            self.read(data)           
        else:
            raise Exception("No data to update.")