import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel

class Command(BaseCommand):
    
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        positions = [7, 6, 5, 4, 3, 2, 1] 
        
        root = EmployeeModel.add_root(
            full_name=seeder.faker.name(),
            position=7,
            joined=seeder.faker.date_this_decade(),
            email = seeder.faker.email()
        )
        
        hierarchy = dict()
        for position in positions:
            if position == position[-1]:
                hierarchy[position] = None
            else:
                hierarchy[position] = random.choice(range(1, position))
        
        def children(parent, position, count):
            if count == 0:
                return
            if position in hierarchy:
                child = parent.add_child(
                    full_name=seeder.faker.name(),
                    position=position,
                    joined=seeder.faker.date_this_decade(),
                    email = seeder.faker.email()
                    )
                children(child, hierarchy[position], count-1)
        
        for position in positions[1:]:
            children(root, position, 50000//7)
        
        self.stdout.write(self.style.SUCCESS('Completed!'))