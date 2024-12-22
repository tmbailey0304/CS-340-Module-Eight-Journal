from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password, host, port, db, collection):
        try:
            self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
            self.database = self.client[db]
            self.collection = self.database[collection]
        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def create(self, data):
        """Insert a document into the collection"""
        try:
            if data:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            else:
                raise ValueError("Data is empty")
        except Exception as e:
            print(f"Create error: {e}")
            return False

    def read(self, query):
        """Query documents from the collection"""
        try:
            cursor = self.collection.find(query)
            return [doc for doc in cursor]
        except Exception as e:
            print(f"Read error: {e}")
            return []

    def update(self, query, update_data):
        """Update documents in the collection"""
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        """Delete documents from the collection"""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0

