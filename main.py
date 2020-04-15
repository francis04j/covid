from flask import Flask, Response
from aggregator import Collector, IndiaCollector
from prometheus_client.exposition import generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)

@app.route('/')
def home():
    return "It works!"

@app.route("/uk", methods=["GET"])
def uk_metrics():
    collector_obj = Collector()
    return Response(collector_obj.get_uk_metrics(),
                    mimetype=CONTENT_TYPE_LATEST)

@app.route("/metrics", methods=["GET"])
def metrics():
    collector_obj = Collector()
    return Response(generate_latest(collector_obj),
                    mimetype=CONTENT_TYPE_LATEST)

@app.route("/india", methods=["GET"])
def india_metrics():
    collector_obj = IndiaCollector()
    return Response(generate_latest(collector_obj),
                    mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run()