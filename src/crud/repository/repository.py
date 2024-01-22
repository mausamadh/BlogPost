
from fastapi import HTTPException
from src.entrypoint.database import user

class InMemoryRep:
    def __init__(self):
        self.repo=user

    def add(self,item):
        self.repo.append(item)
        return "added successfully"

    def update(self,index,change):
        if 0<=index<len(self.repo):
            existing=self.repo[index]
        else:
            raise HTTPException(status_code=404,detail="user not found")
            
        for key,value in change.items():
            setattr(existing,key,value)
        
        
        self.repo[index]=existing
        return "updated successfully"
    
    def get(self,index):
        return self.repo[index]
    
    def getAll(self):
        
        return self.repo
    
    def delete(self,index):
        return self.repo.pop(index)

repo=InMemoryRep