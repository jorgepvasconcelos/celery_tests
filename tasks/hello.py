from celery import Task


class TaskHello(Task):
    name = "tasks.hello"

    def run(self, *args, **kwargs):
        print('hello')
