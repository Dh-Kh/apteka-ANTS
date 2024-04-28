import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel

class Command(BaseCommand):
    help = 'Database seeding command'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        get = lambda node_id: EmployeeModel.objects.get(pk=node_id)
        root = EmployeeModel.add_root(
            full_name=seeder.faker.name(),
            position=8,
            joined=seeder.faker.date_this_decade(),
            email = seeder.faker.email()
        )
        position_level = 7
        level = 50000//7
        
        
        self.stdout.write(self.style.SUCCESS('Completed!'))