import scrapy
from scrapy_splash import SplashRequest


class OccupationSpider(scrapy.Spider):
    name = "occupation_spider"

    def start_requests(self):
        yield SplashRequest(
            "https://immi.homeaffairs.gov.au/visas/working-in-australia/skill-occupation-list",
            self.parse,
        )

    def parse(self, response):
        print("Celery start")
        rows = response.css("table tbody tr")

        visa_programs = {
            "186": [],
            "189": [],
            "190": [],
            "494": [],
            "485": [],
            "407": [],
            "187": [],
            "491 state or territory nominated": [],
            "482 Medium term stream": [],
            "482 Short term stream": [],
            "489 state or territory nominated": [],
        }

        def matches_visa(visa_string, visa_code):
            print("*" * 90, visa_string)
            if visa_code in visa_string:
                return True
            if (
                visa_code == "491 state or territory nominated"
                and "491 - Skilled Work Regional (provisional) visa (subclass 491) State or Territory nominated"
                in visa_string
            ):
                return True
            if (
                visa_code == "482 Medium term stream"
                and "482 - Temporary Skill Shortage (subclass 482) – Medium Term Stream"
                in visa_string
            ):
                return True
            if (
                visa_code == "482 Short term stream"
                and "482 - Temporary Skill Shortage visa (subclass 482) - Short Term Stream"
                in visa_string
            ):
                return True
            if (
                visa_code == "489 state or territory nominated"
                and "489 - Skilled Regional (Provisional) visa (subclass 489) - State or Territory nominated"
                in visa_string
            ):
                return True
            return False

        for row in rows:
            cols = row.css("td")
            if len(cols) >= 3:
                occupation = cols[0].css("::text").get().strip()
                visa_col = cols[2].css("li::text").getall()
                if not visa_col:
                    visa_col = cols[2].css("::text").getall()
                visas = [v.strip() for v in visa_col if v.strip()]
                # print("*"*90, visas)
                self.logger.info(f"Occupation: {occupation}, Visas: {visas}")
                for visa in visas:
                    for code in visa_programs:
                        if matches_visa(visa, code):
                            visa_programs[code].append(occupation)
                            # self.logger.info(f"Appending {occupation} to {code}")
                            break

        for visa_code, occupations in visa_programs.items():
            filename = f"{visa_code.replace(' ', '_')}.txt"
            with open(filename, "w") as f:
                for occupation in occupations:
                    f.write(f"{occupation}\n")

        yield visa_programs
