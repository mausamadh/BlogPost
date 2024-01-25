
from fastapi import HTTPException
from src.entrypoint.database import blog

class InMemoryRep:
    def __init__(self):
        self.repo=blog

   
    
    def get(self,index):
        return self.repo[index]
    def getall(self):
        return self.repo
    def add(self,item):
        self.repo.append(item)
        return "added successfully"
    
    

blogRepo=InMemoryRep