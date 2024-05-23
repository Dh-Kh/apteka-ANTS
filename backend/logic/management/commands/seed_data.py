from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel
from random import randint

class Command(BaseCommand):
    
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        
        def insert(root, levels):
            children_per_node = randint(1, 10)
            if levels == 0:
                return
        
        
            for _ in range(children_per_node):
                value = randint(1, 6)
                if value < root.position:
                    child = root.add_child(
                        full_name=seeder.faker.name(), 
                        position=value,
                        joined=seeder.faker.date_this_decade(), 
                        email=seeder.faker.email()
                        )
                    insert(child, levels - 1)
                
                    
            
        root_exists = EmployeeModel.objects.filter(path__isnull=True).exists()
        
        if not root_exists:
            root = EmployeeModel.add_root(
                full_name=seeder.faker.name(),
                position=7,
                joined=seeder.faker.date_this_decade(),
                email = seeder.faker.email()
            )
        else:
            root = EmployeeModel.objects.get(path__isnull=True)
        
    
        insert(root, levels=5)
        
        self.stdout.write(self.style.SUCCESS('Completed!'))
        
#function backtracking(choosen):
#   if valid_solution?(choosen):
#      perform_action_with(choosen) // save, print, etc
#   else:
#      for each option we can take here:
#         choosen = choose_one(option)   // choose
#         backtracking(choosen)          // explore
#         choosen = unchoose(option)     // unchoose