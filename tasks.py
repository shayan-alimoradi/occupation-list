from celery import Celery
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from occupation.spiders.occupation_spider import OccupationSpider
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Celery("tasks", broker="redis://localhost:6379/0")
app.config_from_object("celeryconfig")


@app.task
def run_spider():
    logger.info("Starting spider task")
    try:
        process = CrawlerProcess(get_project_settings())
        logger.info("Stage 1")
        process.crawl(OccupationSpider)
        process.start()
        logger.info("Spider task finished successfully")
    except Exception as e:
        logger.error(f"Error running spider: {e}")
