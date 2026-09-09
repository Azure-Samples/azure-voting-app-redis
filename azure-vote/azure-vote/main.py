from flask import Flask, request, render_template, Response, jsonify
import os
import redis
import socket

app = Flask(__name__)

# Load configurations from environment or config file
app.config.from_pyfile('config_file.cfg')

if ("VOTE1VALUE" in os.environ and os.environ['VOTE1VALUE']):
    button1 = os.environ['VOTE1VALUE']
else:
    button1 = app.config['VOTE1VALUE']

if ("VOTE2VALUE" in os.environ and os.environ['VOTE2VALUE']):
    button2 = os.environ['VOTE2VALUE']
else:
    button2 = app.config['VOTE2VALUE']

if ("TITLE" in os.environ and os.environ['TITLE']):
    title = os.environ['TITLE']
else:
    title = app.config['TITLE']

# Redis configurations
redis_server = os.environ['REDIS']

# Redis Connection
try:
    if "REDIS_PWD" in os.environ:
        r = redis.StrictRedis(host=redis_server,
                        port=6379,
                        password=os.environ['REDIS_PWD'])
    else:
        r = redis.Redis(redis_server)
    r.ping()
except redis.ConnectionError:
    exit('Failed to connect to Redis, terminating.')

# Change title to host name to demo NLB
if app.config['SHOWHOST'] == "true":
    title = socket.gethostname()

# Init Redis
if not r.get(button1): r.set(button1,0)
if not r.get(button2): r.set(button2,0)


def vote_counts():
    """Read both option totals from Redis as ints."""
    vote1 = int(r.get(button1) or 0)
    vote2 = int(r.get(button2) or 0)
    return vote1, vote2


def render_index():
    vote1, vote2 = vote_counts()
    return render_template(
        "index.html",
        value1=vote1,
        value2=vote2,
        button1=button1,
        button2=button2,
        title=title,
    )


def redis_ok():
    """Return True when Redis answers PING — used by Kubernetes probes."""
    try:
        return bool(r.ping())
    except redis.RedisError:
        return False


@app.route('/healthz', methods=['GET'])
def healthz():
    # Readiness/liveness: the UI is only useful if Redis is reachable.
    if redis_ok():
        return jsonify(status='ok', redis='up'), 200
    return jsonify(status='unhealthy', redis='down'), 503


@app.route('/metrics', methods=['GET'])
def metrics():
    # Prometheus text format (no extra library). Labels let Grafana
    # split Cats vs Dogs; a separate total is easy to chart/alert on.
    if not redis_ok():
        return jsonify(error='redis unavailable'), 503
    vote1, vote2 = vote_counts()
    lines = [
        '# HELP azure_vote_count Votes stored in Redis for one option.',
        '# TYPE azure_vote_count counter',
        'azure_vote_count{{option="{}"}} {}'.format(button1, vote1),
        'azure_vote_count{{option="{}"}} {}'.format(button2, vote2),
        '# HELP azure_vote_total Sum of all votes.',
        '# TYPE azure_vote_total counter',
        'azure_vote_total {}'.format(vote1 + vote2),
        '',
    ]
    return Response('\n'.join(lines), mimetype='text/plain; version=0.0.4')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_index()

    elif request.method == 'POST':

        if request.form['vote'] == 'reset':
            r.set(button1, 0)
            r.set(button2, 0)
            return render_index()

        else:
            vote = request.form['vote']
            r.incr(vote, 1)
            return render_index()

if __name__ == "__main__":
    app.run()
