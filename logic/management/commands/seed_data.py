from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel

class Command(BaseCommand):
    
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        positions = [7, 6, 5, 4, 3, 2, 1] 
        total_employee = 500
        total_positions = len(positions)
        employee_per_position = [total_employee // total_positions] * total_positions
        
        #need to update
        #random assign subordinates to each node from range that affect 
        #on their position
        def children(parent, position_index):
            if position_index == 0:
                return
            position = positions[position_index]
            for i in range(employee_per_position[position_index]):
                child = parent.add_child(
                    full_name=seeder.faker.name(),
                    position=position,
                    joined=seeder.faker.date_this_decade(),
                    email=seeder.faker.email()
                )
            children(child, position_index-1)
        
        root = EmployeeModel.add_root(
            full_name=seeder.faker.name(),
            position=7,
            joined=seeder.faker.date_this_decade(),
            email = seeder.faker.email()
        )
        children(root, total_positions-2)
        
        
        self.stdout.write(self.style.SUCCESS('Completed!'))