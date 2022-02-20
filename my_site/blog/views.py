from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hiking-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Spencer",
        "date": date(2022, 2, 20),
        "title": "Mountain Hiking",
        "excerpt": "Ad fugiat tempor consequat quis in reprehenderit nulla.",
        "content": """Laborum exercitation enim minim velit culpa incididunt dolore aliquip veniam ad esse qui officia pariatur. Irure mollit ullamco nulla incididunt adipisicing elit est laborum eiusmod exercitation proident sint.
        Consequat minim minim ipsum deserunt enim magna dolor."""
    },
    {
        "slug": "hiking-in-the-mountains",
        "image": "coding.jpg",
        "author": "Spencer",
        "date": date(2022, 2, 21),
        "title": "Mountain Hiking",
        "excerpt": "Ad fugiat tempor consequat quis in reprehenderit nulla.",
        "content": "Laborum exercitation enim minim velit culpa incididunt dolore aliquip veniam ad esse qui officia pariatur. Irure mollit ullamco nulla incididunt adipisicing elit est laborum eiusmod exercitation proident sint. Consequat minim minim ipsum deserunt enim magna dolor."
    },
    {
        "slug": "hiking-in-the-mountains",
        "image": "woods.jpg",
        "author": "Spencer",
        "date": date(2022, 2, 22),
        "title": "Mountain Hiking",
        "excerpt": "Ad fugiat tempor consequat quis in reprehenderit nulla.",
        "content": "Laborum exercitation enim minim velit culpa incididunt dolore aliquip veniam ad esse qui officia pariatur. Irure mollit ullamco nulla incididunt adipisicing elit est laborum eiusmod exercitation proident sint. Consequat minim minim ipsum deserunt enim magna dolor."
    },
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
