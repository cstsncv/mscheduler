from .agent import Agent
import datetime
import uuid
from .task import Task
from .state import *

class Storage:
    def __init__(self):
        self.agents = {}
        self.tasks = {}

    def reg_hb(self, **payload):
        id = payload['id']
        agent = self.agents.get(id)
        if not agent:
            agent = {}
        #self.agents[id] = Agent(**payload)
        agent['timestamp'] = datetime.datetime.now()
        agent['busy'] = False
        agent['info'] = payload
        self.agents[id] = agent

    def get_agents(self):
        return list(self.agents.keys())

    def add_task(self,msg:dict):
        msg['task_id'] = uuid.uuid4().hex
        task = Task(**msg)
        self.tasks[task.id] = task
        return task.id

    def iter_tasks(self, state={WAITING, RUNNING}):
        # for task in self.tasks.values():
        #     if task.state in {WAITING, RUNNING}:
        #         yield task
        yield from (task for task in self.tasks.values() if task.state in state)

    def get_task(self, agent_id):
        for task in self.iter_tasks():
            if agent_id in task.targets:
                if task.state == WAITING:
                    task.state = RUNNING
                task.targets[agent_id]['state'] = RUNNING
                return [task.id, task.script, task.timeout]

    def result(self, msg: dict):
        task = self.tasks[msg['id']]
        agent = task.targets[msg['agent_id']]
        if msg['code'] == 0:
            agent['state'] = SUCCEED
        else:
            agent['state'] = FAILED








