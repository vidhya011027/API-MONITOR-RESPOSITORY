import requests
import time

url = input("Enter API URL: ")

print("\n========== API PERFORMANCE MONITOR ==========")

try:
    start_time = time.time()

    response = requests.get(url, timeout=10)

    end_time = time.time()

    response_time = (end_time - start_time) * 1000

    print("API URL       :", url)
    print("Status Code   :", response.status_code)
    print("Response Time :", round(response_time, 2), "ms")

    if response.status_code == 200:
        print("Status        : API is Working")
    else:
        print("Status        : API Error")

    if response_time < 500:
        print("Performance   : Excellent")
    elif response_time < 1000:
        print("Performance   : Good")
    elif response_time < 2000:
        print("Performance   : Average")
    else:
        print("Performance   : Slow")

except requests.exceptions.Timeout:
    print("Error         : API request timed out")

except requests.exceptions.ConnectionError:
    print("Error         : Unable to connect to API")

except Exception as e:
    print("Error         :", e)

print("============================================")