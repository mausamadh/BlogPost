from src.crud.repository.blog_repository import blogRepo

class BlogService:
    def __init__(self):
        self.repo=blogRepo()

    def get(self,index):
        blog=self.repo.get(index=index)
        return blog
    def getall(self):
        blog=self.repo.getall()
        return blog
    def add(self,data):
        return self.repo.add(item=data)
    
    


service=BlogService