from models import *


def connect_database():
    db.connect()
    db.drop_tables([UserStory], safe=True)
    db.create_tables([UserStory], safe=True)


def example_user_story(userstory_db):
    userstory_db.create(
        story_title="System / Handle new application", user_story="As an Administrator,I want to automate the process of incoming applications So that I can save some time (of manual work).", accept_criteria="Given that there is a new applicant in the applicants db tablev And it has no application code and school yet When the system detects this new entry Then ensure the program assigns a generated application code for the applicant.", business_value=1000, estimation=10, status="done")
    userstory_db.create(
        story_title="System / Find possible interview date", user_story="As an Administrator, I want to automate the process of scheduling interviews So that I can save some time (of manual work).", accept_criteria="When the system detects this entry Then ensure the program finds a possible interview date based on the availability of mentors", business_value=1000, estimation=8, status="done")
    userstory_db.create(
        story_title="Applicant view / Application", user_story="As an Applicant, I want to see the details of my application So that I can be informed about my evaluation.", accept_criteria="When the user chooses the Application Details menu Then ensure the program displays the status of the application", business_value=800, estimation=5, status="done")
