broker_url = "redis://localhost:6379/0"
result_backend = "rpc://"
accept_content = ["json"]
result_serializer = "json"
task_serializer = "json"
timezone = "UTC"
enable_utc = True

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Celery specific logging
from kombu import Exchange, Queue

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

task_routes = {
    'tasks.run_spider': {'queue': 'default'},
}

task_annotations = {
    'tasks.run_spider': {'rate_limit': '10/m'}
}

worker_redirect_stdouts_level = 'INFO'
