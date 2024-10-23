import argparse
import os
import sys
import tempfile

import requests
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5111,
                        help="Port to run the UI on. Defaults to 5111.")
    parser.add_argument("--host", type=str, default="127.0.0.1",
                        help="Host to run the UI on. Defaults to 127.0.0.1. "
                             "Set to 0.0.0.0 to make the UI externally "
                             "accessible from other devices.")
    args = parser.parse_args()
    app.run(debug=False, host=args.host, port=args.port)