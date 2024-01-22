from src.crud.repository.repository import repo

class CrudService:
    def __init__(self):
        self.repo=repo()

    def get(self,index):
        msg=self.repo.get(index=index)
        return msg
    def getAll(self):
        msg=self.repo.getAll()
        return msg

    def add(self,data):
        return self.repo.add(item=data)
    
    def update(self,index,data):
        return self.repo.update(index=index,change=data)
    
    def delete(self,index):
        return self.repo.delete(index=index)

    


service=CrudService