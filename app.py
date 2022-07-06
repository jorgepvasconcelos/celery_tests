from celery import Celery
from celery.app.registry import TaskRegistry

from tasks.hello import TaskHello
from envs import REDIS_URL

task_registry = TaskRegistry()
task_registry.register(TaskHello)

app = Celery(
    main='celery_main',
    backend=REDIS_URL,
    tasks=task_registry,
    broker=REDIS_URL,
    namespace='celery_namespace'
)
