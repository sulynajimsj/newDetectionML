import requests

# Define the URL of your API
url = "http://sully-enviroment-first.eba-3tf9ihwj.us-east-2.elasticbeanstalk.com/predict"

# Define your test cases with expected results
test_cases = [
    {"text": "This is a fake news example.", "expected": "FAKE"},
    {"text": "This is another fake news example.", "expected": "FAKE"},
    {"text": "This is a real news example.", "expected": "REAL"},
    {"text": "This is another real news example.", "expected": "REAL"}
]

# Function to test the API
def test_api():
    for i, case in enumerate(test_cases):
        response = requests.post(url, json={"text": case["text"]})
        if response.status_code == 200:
            result = response.json()
            assert result['is_fake_news'] == case['expected'], f"Test case {i+1} failed: expected {case['expected']}, got {result['is_fake_news']}"
            print(f"Test case {i+1} passed: {result}")
        else:
            print(f"Test case {i+1} failed with status code: {response.status_code}")

# Run the tests
if __name__ == "__main__":
    test_api()