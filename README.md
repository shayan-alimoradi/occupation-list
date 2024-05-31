# Occupation Spider

## Introduction
This project implements a web scraper using Scrapy to extract information from the Australian Department of Home Affairs website regarding the Skill Occupation List for various visa programs.

## Setup and Running

### Prerequisites
- Python 3.x
- Docker

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shayan-alimoradi/occupation-list
   cd occupation-list

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Running the Spider:
    ```bash
    To run the spider without Celery:

        cd occupation
        scrapy crawl occupation_spider


### Using Splash with Docker
#### Splash

Splash is used for rendering JavaScript-heavy pages. To set up Splash with Docker:

#### Pull the Splash image from Docker Hub:

```bash
docker pull scrapinghub/splash
docker run -p 8050:8050 scrapinghub/splash

```
