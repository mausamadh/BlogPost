from src.blog.repository.repository import blogRepo


class BlogService:
    def __init__(self):
        self.repo = blogRepo()

    def get(self, index):
        blog = self.repo.get(index=index)
        return blog

    def getall(self):
        blog = self.repo.getall()
        return blog

    def add(self, data):
        return self.repo.add(item=data)

    def delete(self, index):
        return self.repo.delete(index=index)

    def update(self, index, data):
        return self.repo.update(index=index, change=data)


service = BlogService
