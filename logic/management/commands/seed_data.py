from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel
from random import randint

class Command(BaseCommand):
    
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        
        def insert(root, value):
            
            if value < root.position:
                if root.get_children():
                    left = root.get_children().first()
                    insert(left, value)
                else:
                    left = root.add_child(
                        full_name=seeder.faker.name(), 
                        position=value, 
                        joined=seeder.faker.date_this_decade(), 
                        email=seeder.faker.email()
                        )
                    left.move(target=root, pos="sorted-child")
            elif root.position < value:
                if root.get_children():
                    right = root.get_children().last()
                    insert(right, value)
                else:
                    right = root.add_child(
                        full_name=seeder.faker.name(), 
                        position=value, 
                        joined=seeder.faker.date_this_decade(), 
                        email=seeder.faker.email()
                    )
                    right.move(target=root, pos='sorted-child')
            else:
                sibling = root.add_sibling(
                    "sorted-sibling",
                    full_name=seeder.faker.name(),
                    position=value,
                    joined=seeder.faker.date_this_decade(),
                    email=seeder.faker.email()
                )
                #insert(sibling, value)
                
            
            
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
        
        for i in range(50):
            value = randint(1, 6)
            insert(root, value)
        
        self.stdout.write(self.style.SUCCESS('Completed!'))