import time


class PerformanceTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. RECORD START TIME (Before the view runs)
        start_time = time.time()

        # 2. LET THE VIEW PROCESS (The request travels through the factory)
        response = self.get_response(request)

        # 3. CALCULATE TOTAL TIME (After the view finishes)
        duration = time.time() - start_time

        # 4. INJECT INTO RESPONSE HEADERS
        # This makes the data visible in Postman!
        response["X-Process-Time"] = f"{duration:.4f} seconds"

        return response
