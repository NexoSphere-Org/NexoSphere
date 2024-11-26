from flask import Flask
import os
from dotenv import load_dotenv
import subprocess
import threading
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from sentimentControllers.schedule_task_controller import scheduled_task
from sentimentControllers.sentimentController import stockSentimentRoute
from tickerListService.tickerController import tickerRoutes
from stockPriceControllers.stockPriceController import stockPriceRoutes

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=scheduled_task, trigger="interval", hours=1, next_run_time=datetime.now()
)
# scheduler.add_job(
#     func=scheduled_task, trigger="cron", hour=6, next_run_time=datetime.now()
# )

# expose the ticker list service
stockSentimentRoute(app)
tickerRoutes(app)
stockPriceRoutes(app)

# Function to run the Streamlit app
def run_streamlit():
    subprocess.run(['streamlit', 'run', './nexosphere/frontEnd/streamlit_app.py', '--server.port=8501'])

if __name__ == "__main__":
    load_dotenv()
    # Start the Streamlit app in a separate thread
    threading.Thread(target=run_streamlit).start()

    app.run(debug=True, host="0.0.0.0", port=os.getenv("FLASK_PORT"))  # Start the server
