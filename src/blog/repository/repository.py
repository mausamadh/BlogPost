from fastapi import HTTPException
from src.entrypoint.database import blog


class InMemoryRep:
    def __init__(self):
        self.repo = blog

    def get(self, index):
        return self.repo[index]

    def getall(self):
        return self.repo

    def add(self, item):
        self.repo.append(item)
        return "added successfully"

    def delete(self, index):
        return self.repo.pop(index)

    def update(self, index, change):
        if 0 <= index < len(self.repo):
            existing = self.repo[index]
        else:
            raise HTTPException(status_code=404, detail="blog not found")

        for key, value in change.items():
            setattr(existing, key, value)

        self.repo[index] = existing
        return "updated successfully"


blogRepo = InMemoryRep
