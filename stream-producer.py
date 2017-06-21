import tornado.ioloop
import tornado.httpserver
import tornado.web
import json

from pykafka import KafkaClient
from tornado.options import define, options, parse_command_line

# Add command line flags
define("port", default=8000, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

# Connect to Kafka instance
client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics[b'test']
producer = topic.get_producer()

class MainHandler(tornado.web.RequestHandler):

    """Handles post requests by responding with a JSON file."""
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    @tornado.web.asynchronous
    def get(self):
        """Respond to GET requests for debugging purposes."""
        self.write("Success!")
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        """Forward message to Kafka."""
        data = self.request.body
        print(json.loads(self.request.body.decode('utf-8')))
        producer.produce(data)
        self.write(json.dumps('{}'))
        self.finish()

def make_app():
    tornado.options.parse_command_line()
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def main():
    """Runs application on httpserver with handler for '/'."""
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
