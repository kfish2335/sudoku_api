# Step 1: Build the React app
FROM node:18-alpine as build_react

# Set working directory
WORKDIR /app

# Copy the React app's package.json and package-lock.json
COPY client/package*.json ./client/

# Install dependencies for the React app
RUN cd client && npm install

# Copy the rest of the React app
COPY client/ ./client/

# Build the React app
RUN cd client && npm run build

# Step 2: Set up the Flask server
FROM python:3.10-slim

# Set working directory for Flask
WORKDIR /app

# Install Flask
COPY server/requirements.txt .

RUN pip install -r requirements.txt

# Copy the Flask server code
COPY server/ ./server/

# Copy the built React app from the previous step
COPY --from=build_react /app/client/build ./server/build

# Set environment variables for Flask
ENV FLASK_APP=server/application.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask will run on
EXPOSE 5000

# Run Flask server
CMD ["flask", "run"]