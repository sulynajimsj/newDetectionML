import requests
import time
import csv

url = "http://sully-enviroment-first.eba-3tf9ihwj.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    {"text": "This is a fake news example.", "expected": "FAKE"},
    {"text": "This is another fake news example.", "expected": "FAKE"},
    {"text": "This is a real news example.", "expected": "REAL"},
    {"text": "This is another real news example.", "expected": "REAL"}
]

def test_performance():
    with open('performance_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['test_case', 'call_number', 'latency', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, case in enumerate(test_cases):
            for j in range(100):
                start_time = time.time()
                response = requests.post(url, json={"text": case["text"]})
                end_time = time.time()
                latency = end_time - start_time
                if response.status_code == 200:
                    result = response.json()
                    assert result['is_fake_news'] == case['expected'], f"Test case {i+1}, call {j+1} failed: expected {case['expected']}, got {result['is_fake_news']}"
                    writer.writerow({'test_case': i+1, 'call_number': j+1, 'latency': latency, 'result': result['is_fake_news']})
                    print(f"Test case {i+1}, call {j+1}: {latency:.4f} seconds, result: {result['is_fake_news']}")
                else:
                    print(f"Test case {i+1}, call {j+1} failed with status code: {response.status_code}")

if __name__ == "__main__":
    test_performance()