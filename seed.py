import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcrm.settings')
django.setup()

from leads.models import User, UserProfile, Agent, Lead, Category

# Create organizer
org_user = User.objects.create_user(
    username='admin_org', password='demo1234',
    first_name='Sarah', last_name='Connor',
    is_organizer=True, is_agent=False
)
profile = UserProfile.objects.get(user=org_user)

# Create agents
agent_users = [
    ('james_a', 'James', 'Wilson'),
    ('lisa_b', 'Lisa', 'Park'),
    ('mike_c', 'Mike', 'Torres'),
]
agents = []
for username, first, last in agent_users:
    u = User.objects.create_user(
        username=username, password='demo1234',
        first_name=first, last_name=last,
        is_organizer=False, is_agent=True
    )
    agent = Agent.objects.create(user=u, organization=profile)
    agents.append(agent)

# Create categories
cat_names = ['New', 'Unresponsive']
categories = [Category.objects.create(name=n, organization=profile) for n in cat_names]

# Create leads
leads_data = [
    ('John', 'Smith', 34),
    ('Emma', 'Davis', 28),
    ('Carlos', 'Rivera', 45),
    ('Nina', 'Patel', 31),
    ('Tom', 'Baker', 52),
    ('Zara', 'Ahmed', 27),
    ('Luke', 'Chen', 39),
    ('Maya', 'Jones', 33),
]
import random
for first, last, age in leads_data:
    Lead.objects.create(
        first_name=first, last_name=last, age=age,
        agent=random.choice(agents),
        organization=profile,
        category=random.choice(categories)
    )

print("Done! Seeded organizer, 3 agents, 4 categories, 8 leads.")
print("Login: admin_org / demo1234")