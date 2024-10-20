from flask import Flask, render_template

app = Flask(__name__)

# Sample data for projects and blog posts
projects = [
    {
        "title": "Weather Forecast",
        "description": "A Java-based program that displays the weather in searched locations.",
        "live_demo": "https://example.com/weather-forecast",
        "github": "https://github.com/yourusername/weather-forecast"
    },
    {
        "title": "Road Lane Detection",
        "description": "This detects lane lines on the road using Python code.",
        "live_demo": "https://example.com/road-lane-detection",
        "github": "https://github.com/yourusername/road-lane-detection"
    },
    # Add more projects as needed
        {
        "title": "Road Lane Detection",
        "description": "This detects lane lines on the road using Python code.",
        "live_demo": "https://example.com/road-lane-detection",
        "github": "https://github.com/yourusername/road-lane-detection"
    },

]

blog_posts = [
    {
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "date": "2024-10-20"
    },
    {
        "title": "Learning Flask",
        "content": "In this post, I share my experiences while learning Flask.",
        "date": "2024-10-19"
    },
        {
        "title": "Learning Flask",
        "content": "In this post, I share my experiences while learning Flask.",
        "date": "2024-10-19"
    },

    # Add more blog posts as needed
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
