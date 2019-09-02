from .agent import Agent
import datetime
import uuid
from .task import Task
class Storage:
    def __init__(self):
        self.agents = {}
        self.tasks = {}

    def reg_hb(self, **payload):
        #self.agents[id] = Agent(**payload)
        agent = self.agents[id]
        agent['timestamp'] = datetime.datetime.now()
        agent['busy'] = False
        agent['info'] = payload

    def get_agents(self):
        return list(self.agents.keys())

    def add_tasks(self,msg:dict):
        msg['id'] = uuid.uuid4().hex



