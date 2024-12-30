from flask import Flask, render_template, jsonify

apps = Flask(__name__)

JOBS=[
    {"id": 1, "title": "Software Engineer", "location": "New York, NY", "salary": "$120,000/year"},
     {"id": 4, "title": "UX/UI Designer", "location": "Seattle, WA", "salary": "$110,000/year"},
    {"id": 2, "title": "Product Manager", "location": "San Francisco, CA", "salary": "$140,000/year"},
    {"id": 3, "title": "Data Analyst", "location": "Austin, TX", "salary": "$90,000/year"},
    {"id": 4, "title": "UX/UI Designer", "location": "Seattle, WA", "salary": "$110,000/year"},
    {"id": 5, "title": "DevOps Engineer", "location": "Boston, MA", "salary": "$125,000/year"}
]

@apps.route('/')
def home():
    return render_template('home.html', jobs=JOBS,Company='TastinGo')


@apps.route('/api/jobs')
def job_list():
    return jsonify(JOBS)


if __name__=="__main__":
    apps.run(host='0.0.0.0',debug=True)
