import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from logic.models import EmployeeModel

class Command(BaseCommand):
    help = 'Seed the database with fake data for EmployeeModel'
    
    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(EmployeeModel, 50000, {
            'full_name': lambda x: seeder.faker.name(),
            'position': lambda x: random.choice([level[0] for level in EmployeeModel.HIERARCHY]),
            'joined': lambda x: seeder.faker.date_this_decade(),
            'email': lambda x: seeder.faker.email(),
        })
        inserted_pks = seeder.execute()
        for boss_pk in inserted_pks[EmployeeModel]:
            boss = EmployeeModel.objects.get(pk=boss_pk)
            num_subordinates = random.randint(0, 10)  
            subordinate_pks = random.sample(inserted_pks[EmployeeModel], num_subordinates)
            for subordinate_pk in subordinate_pks:
                subordinate = EmployeeModel.objects.get(pk=subordinate_pk)
                subordinate.boss = boss
                subordinate.save()

        self.stdout.write(self.style.SUCCESS('Database successfully seeded with fake data.'))
        