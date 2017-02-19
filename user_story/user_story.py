import os
from peewee import *
from build import *
from models import UserStory
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app


app = Flask(__name__)


@app.route('/list', methods=["GET", "POST"])
def list_user_stories():
    user_stories = UserStory.select()
    return render_template("list.html", user_stories=user_stories)


@app.route('/')
def index():
    return list_user_stories()


@app.route('/story', methods=["GET", "POST"])
def story():
    if request.method == "GET":
        title = "- Add Story"
        button = "Create"
        return render_template('form.html', title=title, button=button)
    else:
        cols = ['story_title', 'user_story', 'acceptance_criteria',
                'business_value', 'estimation', 'status']
        inputs = [request.form[i] for i in cols]
        new_story = UserStory(
            story_title=inputs[0], user_story=inputs[1], accept_criteria=inputs[2], business_value=inputs[
                3], estimation=inputs[4], status=inputs[5])
        new_story.save()
        return redirect(url_for('list_user_stories'))


@app.route('/story/<story_id>', methods=["GET", "POST"])
def update_story(story_id):
    user_story = UserStory.select().where(UserStory.id == story_id).get()
    if request.method == 'GET':
        title = "- Edit Story"
        button = "Update"
        return render_template("form.html", user_story=user_story, title=title, button=button)
    else:
        cols = ['story_title', 'user_story', 'acceptance_criteria',
                'business_value', 'estimation', 'status']
        inputs = [request.form[i] for i in cols]
        update = UserStory.update(story_title=inputs[0], user_story=inputs[1], accept_criteria=inputs[
            2], business_value=inputs[3], estimation=inputs[4], status=inputs[5]).where(UserStory.id == story_id).execute()
        return redirect(url_for('list_user_stories'))


@app.route('/story/<story_id>/delete')
def delete_user_story(story_id):
    UserStory.delete().where(UserStory.id == story_id).execute()
    return redirect(url_for('list_user_stories'))

if __name__ == "__main__":
    connect_database()
    example_user_story(UserStory)
    app.run(debug=True)
