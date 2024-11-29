# NexoSphere 👋

NexoSphere is a cutting-edge project designed to revolutionize the way we analyze stock market news. By leveraging advanced sentiment analysis algorithms, NexoSphere provides valuable insights into market trends and investor sentiment.

## Features

- **Real-time Sentiment Analysis:** Analyze news articles in real-time to gauge market sentiment.
- **Comprehensive Dashboard:** Visualize sentiment trends and historical data with an intuitive dashboard.
- **Custom Alerts:** Set up custom alerts for significant sentiment changes in specific stocks or sectors.

## Prerequisites

- Docker
- Docker Compose

## Running the Project

To run the project using Docker, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/NexoSphere.git
    cd NexoSphere
    ```

2. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

3. **Run the Docker container:**

    ```sh
    docker-compose up
    ```

4. **Access the application:**

    Open your web browser and navigate to `http://localhost:your_port`.

    ## Setup Environment Variables

    Before running the project, you need to set up the environment variables. Create a `.env` file in the root directory of the project based on the `.env.example` file provided:

    ```sh
    cp .env.example .env
    ```

    Edit the `.env` file to configure the necessary environment variables.
