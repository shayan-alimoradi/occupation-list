from tasks import run_spider

if __name__ == "__main__":
    result = run_spider.delay()
    print(f"Task triggered with ID: {result.id}")
