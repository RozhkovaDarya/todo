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
    
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    
    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
        
    notes_by_user_name = graphene.List(NotesType, 
                                       name=graphene.String(required=False))
    
    def resolve_notes_by_user_name(self, info, name=None):
        notes = Notes.objects.all()
        if name:
            notes = notes.filter(user__name=name)
        return notes

schema = graphene.Schema(query=Query)
