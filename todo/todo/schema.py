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
    all_notes = graphene.List(NotesType)
    
    def resolve_all_notes(root, info):
        return Notes.objects.all()
    
    all_users = graphene.List(UserType)
    
    def resolve_all_users(root, info):
        return User.objects.all()
        

schema = graphene.Schema(query=Query)
