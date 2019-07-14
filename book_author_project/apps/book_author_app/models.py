from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __repr__(self):
        return f"<Author object: {self.name} ({self.id})"
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name="books")
    
    def __repr__(self):
        return f"<Book object: {self.title} ({self.id})"