---

# Frontend and Backend Deployment on Kubernetes

## Overview

This repository contains the solution for deploying frontend and backend services on a local Kubernetes cluster using Minikube. The frontend communicates with the backend to display the message **"Hello from backend!"**. The repository also includes a Python test script to verify the communication between the frontend and backend services.

## Steps to Deploy and Test

### Step 1: Start Minikube

1. Open your terminal or command prompt.
2. Start Minikube to set up your local Kubernetes cluster with the following command:

   ```
   minikube start
   ```

   This command initializes the Kubernetes cluster on your local machine.

### Step 2: Clone the Repository

Clone the repository from GitHub using the following commands:

```
git clone https://github.com/Vengatesh-m/qa-test.git
cd qa-test
```

This downloads the project to your local machine.

### Step 3: Deploy Backend Service

1. Apply the backend deployment configuration using `kubectl`:

   ```
   kubectl apply -f backend-deployment.yaml
   ```

2. Check the status of the backend service to ensure that the backend pod is running:

   ```
   kubectl get pods
   ```

### Step 4: Deploy Frontend Service

Apply the frontend deployment configuration with the following command:

```
kubectl apply -f frontend-deployment.yaml
```

### Step 5: Expose Frontend Service

To access the frontend service outside the Kubernetes cluster, expose it using Minikube:

```
minikube service frontend-service
```

### Step 6: Verify Frontend-Backend Communication

Open the frontend URL obtained from the previous step in your web browser. The frontend should display the message:

**Hello from backend!**

## Running the Automated Test

### Step 7: Install Python Dependencies

Make sure you have Python installed. To install the required `requests` library, run:

```
pip install requests
```

### Step 8: Run the Test Script

1. Navigate to the directory where `test_frontend.py` is located.
2. Run the Python script with the following command:

   ```
   python test_frontend.py
   ```

The script will check if the frontend is successfully displaying the message from the backend. If the message is correct, the script will output:

```
Test Passed: Backend message displayed correctly.
```

If the test fails, it will output:

```
Test Failed: Backend message not found.
```

## Conclusion

By following these steps, you should be able to deploy and test the frontend and backend services successfully on your local Kubernetes cluster.
