# Assignment

# Front End API
This API will be responsible for presenting available investment products to the user and allowing the user to choose one. 
It will communicate with the Backend API to retrieve product details based on the user's selection

# Backend API
This API will provide detailed information about the available investment products. The Frontend API will request product details from this API based on user input, and both APIs will log the operation using an operation ID for traceability.

# Requirements
1. API Communication: The Frontend API will call the Backend API with an operation ID that is generated at the start of a user's request. Both APIs must log the operation ID along with other relevant request details to allow tracing through the system

2. Operation ID: Candidate needs to implement a way to generate and propagate this operation ID between the Frontend and Backend APIs. The operation ID will be logged for each request to trace the flow of a user’s request across the two services.

3. API Security and Error Handling: Implement a authenticated mechanism between the APIs. For instance frontend api can include a token in the request headers. Ensure the error handling when token is invalid or missing and when operation ID is not provided or if a request fails

4. Deployment and Logging: Dockerize both the APIs and deploy the APIs locally or any cloud provider. Please provide the infrastructure deployment code(such as YAML files) for this. Demonstrate how logs can be traced by operation ID.

5. Documentation: 
- Update the Read me with clear instructions on how the frontend and backend APIs communicate with each other
- A brief explanation of Design decisions(e.g. why specific thing is chosen etc)
- how they are deployed and how to trace the API calls using a common identifier in the logs.
- Brief instructions for testing and troubleshooting

# Note: Starter Python files for the APIs provided

# Logging Example:
- FrontEnd API Log: 
INFO:root:Operation ID: 123e4567-e89b-12d3-a456-426614174000 - User selected Stocks. Requesting details from Backend API.
- Backend API Log: 
INFO:root:Operation ID: 123e4567-e89b-12d3-a456-426614174000 - Backend API received request for Stocks.


