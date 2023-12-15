from django.db import models
from django.core.exceptions import ValidationError


class EmployeeModel(models.Model):
    HIERARCHY = (
        (7, "SEO"),
        (6, "Team Lead"),
        (5, "Tech Lead"),
        (4, "Senior"),
        (3, "Middle"),
        (2, "Junior"),
        (1, "Trainee"),
        )
    full_name = models.CharField(max_length=255) 
    position = models.IntegerField(choices=HIERARCHY)
    joined = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey("self", on_delete=models.CASCADE, 
                             null=True, blank=True, related_name="subordinates")
    
    def clean(self):
        if self.boss and self.position > self.boss.position:
            raise ValidationError('Boss position must be higher')
        
    def hierarchy_tree(self):
        return {
            "employee": self,
            'subordinates': [
                subordinates.hierarchy_tree() for subordinates in self.subordinates.all()]
            } if self.subordinates.exists() else {'employee': self, 'subordinates': []}
