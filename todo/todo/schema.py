import graphene
from graphene_django import DjangoObjectType
from mainapp.models import User, Notes


class NotesType(DjangoObjectType):
    class Meta:
        model = Notes
        fields = '__all__'
    

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'
        

class Query(graphene.ObjectType):
    all_books = graphene.List(NotesType)
    
    def resolve_all_books(root, info):
        return Notes.objects.all()
        

schema = graphene.Schema(query=Query)
