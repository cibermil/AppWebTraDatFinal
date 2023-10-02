from conexion_mongodb import ConexionMongoDB
db_client = ConexionMongoDB().client
db = db_client.get_database('tratamientodatos')
col = db.get_collection('work_final')

print("###############################################################################")

def BuscarDatos (desvehiculo:str, anio:int, verbose: bool = False)->dict:

    busqueda = col.find({ "$or":[{"modelo_vehiculo":{"$regex":desvehiculo}} ,{"año": {"$gte": anio} }]})


    if verbose:
        print("ok")
    return busqueda
