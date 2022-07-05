import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks',
             broker='amqp://admin:password@localhost:5672',
             backend='rpc://')

app.conf.task_ignore_result = True
# ignore_result=True
@app.task(ignore_result=True)
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    # time.sleep(4)
    logger.info('Work Finished ')
    return x + y
