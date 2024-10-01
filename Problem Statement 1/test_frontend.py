import requests

def test_frontend():
    frontend_url = 'http://127.0.0.1:60465/'
    response = requests.get(frontend_url)

    # This Checks if the frontend is displaying the correct message
    assert 'Hello from the Backend!' in response.text, "Test Failed: Backend message not found"
    print("Test Passed: Backend message displayed correctly.")

if __name__ == '__main__':
    test_frontend()
