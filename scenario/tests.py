from django.test import TestCase, Client
from .models import Scenario, Role
from MyUser.models import MyUser
from django.urls import reverse
from .forms import RoleForm

class ScenarioMakeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user(
            username = 'testmain',
            phone = '09121212',
            password = '123456789987654321'
        )
        self.user.is_main = True
        self.user.save()
        self.client.login(username='09121212', password='123456789987654321')
        
        self.scenario = Scenario.objects.create(
            title='test',
            description = 'test',
        )
        # print(self.user)
    
    def test_if_scenario_made(self):
        scenario = Scenario.objects.filter(title = 'test').exists()
        self.assertTrue(scenario)
        
    def test_user_if_is_main(self):
        user = MyUser.objects.filter(phone='09121212').exists()
        self.assertTrue(user)
        
    def test_make_role(self):
        data = {
            'name' : 'doctor',
            'description' : 'this is doctor'
        }
        form = RoleForm(data=data)
        role = form.save(commit=False)
        role.scenario = self.scenario
        role.save()
        
        self.assertTrue(Role.objects.filter(name='doctor').exists())    
        
    def test_login_success(self):
        logged_in = self.client.login(username='09121212', password='123456789987654321')
        self.assertTrue(logged_in)
            