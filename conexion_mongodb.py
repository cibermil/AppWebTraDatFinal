from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import dotenv

# cargamos las variables de entorno
dotenv.load_dotenv()

# leemos las varaibles de entorno
class ConexionMongoDB:
       def __init__(self):
            usuario = os.getenv('USR_MONGO')
            passwd = os.getenv('PSW_MONGO')
            dbhostname= os.getenv('HOS_MONGO')

            uri = f"mongodb+srv://{usuario}:{passwd}@¨{dbhostname}/?retryWrites=true&w=majority"
            # Create a new client and connect to the server
            self.client = MongoClient(uri, server_api=ServerApi('1'))

       def test_connection(self):
            # Send a ping to confirm a successful connection
            try:
                self.client.admin.command('ping')
                print("Conexión Correcta a MongoDB!")
            except Exception as e:
                print(e)

if __name__=="__main__":
    ConexionMongoDB().test_connection()