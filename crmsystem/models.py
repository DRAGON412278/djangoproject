from mongoengine import Document, EmbeddedDocument, fields

class Project(EmbeddedDocument):
    ProjectId= fields.StringField(max_length=10, required=True, null= False)
    ProjectName=fields.StringField(max_length=100, required= True)
    StartDate= fields.DateField()
    EndDate= fields.DateField()

class Skills(EmbeddedDocument):
    Technology=fields.StringField(max_length=100, required= True)
    Experience= fields.StringField(max_length=200)
    Level= fields.StringField(max_length=50)

class Employee(Document):
    EmployeeId=fields.StringField(max_length=10, required=True, null=False)
    EmployeeName= fields.StringField(max_length=25, required= True)
    WorkLocation=fields.StringField(max_length=10, required= True)
    project=fields.EmbeddedDocumentListField(Project)
    skills=fields.EmbeddedDocumentListField(Skills)