import os
import subprocess
import threading
from datetime import datetime
from flask import Flask
from flask_restx import Api
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from sentimentControllers.schedule_task_controller import scheduled_task
from sentimentControllers.sentimentController import api as sentiment_api
from tickerListService.tickerController import api as ticker_api
from stockPriceControllers.stockPriceController import api as stock_price_api

app = Flask(__name__)
api = Api(app, version='1.0', title='NexoSphere API', description='A simple NexoSphere API')

# Register namespaces
api.add_namespace(sentiment_api)
api.add_namespace(ticker_api)
api.add_namespace(stock_price_api)

# Scheduler setup
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=scheduled_task, trigger="interval", hours=1, next_run_time=datetime.now()
)

# Function to run the Streamlit app
def run_streamlit():
    subprocess.run(['streamlit', 'run', './nexosphere/frontEnd/streamlit_app.py', '--server.port=8501'])

if __name__ == "__main__":
    load_dotenv()
    # Start the Streamlit app in a separate thread
    threading.Thread(target=run_streamlit).start()

    app.run(debug=True, host="0.0.0.0", port=os.getenv("FLASK_PORT"))  # Start the server