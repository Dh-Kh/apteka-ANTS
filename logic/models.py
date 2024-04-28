from django.db import models
from django.db.models import CheckConstraint, Q, F
from treebeard.mp_tree import MP_Node

class EmployeeModel(MP_Node):
    
    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(parent__position__gte=F("position")),
                name="parent_position_check"
                )
            ]
    
    HIERARCHY = (
        (8, "Owner"),
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
    
    node_order_by = ["-position"]