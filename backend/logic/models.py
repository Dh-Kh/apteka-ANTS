from django.db import models
#from django.db.models import CheckConstraint, Q, F
from django.core.exceptions import ObjectDoesNotExist
from treebeard.mp_tree import MP_Node
from typing import List

class EmployeeModel(MP_Node):
    
    #maube need to add skug
    
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
    
    node_order_by = ["position"]
    
    def redistribute(self, new_boss: int) -> None:
        to_redistribute = self.get_children()
        
        if not to_redistribute:
            return

        for employee in to_redistribute:
            if new_boss.position > employee.position:
                employee.move(new_boss, pos="sorted-child")
        
        for employee in to_redistribute:
            employee.redistribute(new_boss)
            
    def check_demotion(self) -> None:
        children_list = self.get_children()
        
        if not children_list:
            return
        
        for children in children_list:
            if self.position < children.position:
                children.move(self, pos="sorted-sibling")
                
    def assign_childs(self, children_list: List[int]) -> None:
        for child_id in children_list:
            try:
                child = EmployeeModel.objects.get(id=child_id)
                child.move(self, pos="sorted-child")
            except ObjectDoesNotExist:
                pass