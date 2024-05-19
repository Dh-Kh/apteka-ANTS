from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel
from random import randint

class Command(BaseCommand):
    
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        
        def insert(root, levels):
            value = randint(1, 6)
            children_per_node = randint(1, 10)
            if levels == 0:
                return
        
            for i in range(children_per_node):
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
        
    
        insert(root, levels=3)
        
        self.stdout.write(self.style.SUCCESS('Completed!'))