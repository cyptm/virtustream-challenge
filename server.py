#!virtustream_env/bin/python
from flask import Flask
import json
import logging

app = Flask(__name__)

@app.route('/fib/<int:num>')
def fib(num):
    logging.debug("Handled request for number: %s" % num)
    return calc_fib(num)


def calc_fib(num):

    try:
        n = int(num)
        if n < 0:
            return json.dumps("Please provide a positive number")

        if n <=1 and n >= 0: 
            return json.dumps([n])
        else:
            fibSeq = [0, 1]
            for i in range(2, n):
                fibSeq.append(fibSeq[i - 1] + fibSeq[i - 2])
            return json.dumps(fibSeq)
    except Exception as e: 
        logging.error("An exception has occured while processing: " + str(e))
        return json.dumps("Something is up on our end. Please try again later")

if __name__ == '__main__':
    logging.basicConfig(filename='fib_server.log', filemode='w', level=logging.DEBUG)
    app.run(debug=True)
