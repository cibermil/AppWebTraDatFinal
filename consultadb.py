from conexion_mongodb import ConexionMongoDB
db_client = ConexionMongoDB().client
db = db_client.get_database('tratamientodatos')
col = db.get_collection('work_final')

print("###############################################################################")
#datos=client.get_database('tratamientodatos').get_collection('trabajo_final').find_one({"año":{ "$gt": 2018 }})
#anios=2010
#busqueda = col.find_one({"año": {"$gt": anios}})
#print(busqueda.keys(), "\n")
def BuscarDatos (desvehiculo:str, anio:int, verbose: bool = False)->dict:
    #busqueda=col.find({"año": {"$gt":anio}})
    busqueda = col.find({ "$or":[{"modelo_vehiculo":{"$regex":desvehiculo}} ,{"año": {"$gte": anio} }]})

    #busqueda = col.find({ "$or"[{"modelo_vehiculo":{"$regex":"peugo","$options":"$i"}} ,"año": {"$gt": anio}]})

    if verbose:
        print("ok")
    return busqueda
#datos=BuscarDatos(desvehiculo="Toyota",anio=2010,verbose=True)
#for x in datos:
#   print(x)