import csv
from random import randint
from review import Review
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

##### User Message Processing #########################################################################################

def swear_words(user_msg):
	"""
	This function checks user_msg for swear words

	:param user_msg: string
	:return: boolean
	"""
        # your code here, delete pass
        pass


def recommendation_request(user_msg):
	"""
	This function checks user_msg for recommendation requests

	:param user_msg: string
	:return: boolean
	"""
	# your code here, delete pass
        pass


##### Replies ##########################################################################################################

def recommendation():
	"""
	This function randomly selects a cafe from the cafes.csv file and uses
	string formatting to put the cafe's information into a response message

	:param None
	:return: str
	"""

	# stores cafes information
	cafes = []

	# your code here

	selected_cafe = "" # your code here

	response_msg = "I think you might enjoy {0}. Located at {1}. Message me back to tell me what you thought of it!".format(
		selected_cafe['cafe_name'], selected_cafe['cafe_address'])

	return response_msg

def review(user_msg):
	"""
	This function analyzes the users review of a cafe and returns a response
	about the sentiment of the review.

	:param user_msg: string
	:return: str
	"""

	# initiate review object
	rvw = Review(user_msg)

	# determine if review is positive or negative
	predicted_sentiment = rvw.predict_sentiment()

	# store review
	rvw.store_review()

	# if positive, respond to positive experience
	if predicted_sentiment == 1:
		response_msg = "Based on your review, it seems that you had a good time. Great! For another recommendation, please write: recommend me"

	# otherwise it was negative, respond to negative experience
	else:
		response_msg = "Based on your review, it seems that you did not have a good time. I'm sorry! For another recommendation, please write: recommend me"
	return response_msg


##### Chatbot Functionality ############################################################################################

@app.route('/', methods=['GET'])
def index():
	return render_template("chatbot.html")


@app.route('/chat', methods=['POST'])
def chat():
        """
        Checks the user_msg for swearing, recommendation requests, or review of the cafe. Responds accordingly with response_msg and animation.
        Check folder static > images > boto for animation options.
        """

	user_msg = request.form.to_dict().get('msg').lower()

        # your code here

	response = jsonify({"animation": animation, "msg": response_msg})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response


@app.route('/static/<path:path>')
def static_file(path):
	return app.send_static_file(path)


if __name__ == "__main__":
	app.run(debug=True)



