from pymongo import MongoClient

class MongoConnect():

    def save(self, json):
        try:
            cliente = MongoClient('localhost', 27017)
            banco = cliente.teste 
            novo_cadastro = banco.teste_collection 
            id = novo_cadastro.insert_one(json).inserted_id
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)