from src.app import app
import os
                                                               
if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)                                             
    app.run(debug=True, host="0.0.0.0", port=port) # Set debug False before deployment