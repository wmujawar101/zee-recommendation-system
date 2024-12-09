from app.app import app
import config

if __name__ == "__main__":
    # Run the app (use host='0.0.0.0' for production deployment)
    app.run(debug=config.DEBUG, host=config.API_HOST, port=config.API_PORT)
