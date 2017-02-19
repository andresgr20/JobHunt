#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An example Kik bot implemented in Python.

It's designed to greet the user, send a suggested response and replies to them with their profile picture.
Remember to replace the BOT_USERNAME_HERE, BOT_API_KEY_HERE and WEBHOOK_HERE fields with your own.

See https://github.com/kikinteractive/kik-python for Kik's Python API documentation.

Apache 2.0 License

(c) 2016 Kik Interactive Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.

"""
import urllib2

from flask import Flask, request, Response
from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage, PictureMessage, \
    SuggestedResponseKeyboard, TextResponse, StartChattingMessage


class KikBot(Flask):
    """ Flask kik bot application class"""

    def __init__(self, kik_api, import_name, static_path=None, static_url_path=None, static_folder="static",
                 template_folder="templates", instance_path=None, instance_relative_config=False,
                 root_path=None):

        self.kik_api = kik_api

        super(KikBot, self).__init__(import_name, static_path, static_url_path, static_folder, template_folder,
                                     instance_path, instance_relative_config, root_path)

        self.route("/incoming", methods=["POST"])(self.incoming)

    def incoming(self):
        """Handle incoming messages to the bot. All requests are authenticated using the signature in
        the 'X-Kik-Signature' header, which is built using the bot's api key (set in main() below).
        :return: Response
        """
        # verify that this is a valid request
        if not self.kik_api.verify_signature(
                request.headers.get("X-Kik-Signature"), request.get_data()):
            return Response(status=403)

        messages = messages_from_json(request.json["messages"])

        response_messages = []
        job=""
        location=""
        
        for message in messages:
            user = self.kik_api.get_user(message.from_user)
            # Check if its the user's first message. Start Chatting messages are sent only once.
            if isinstance(message, StartChattingMessage):
                print("body is " + message_body)
                response_messages.append(TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body="Hey {}, Welcome to Job Hunt! You can search for technical internships here! What type of intership are you looking for?".format(user.first_name),
                    # keyboards are a great way to provide a menu of options for a user to respond with!
                    keyboards=[SuggestedResponseKeyboard(responses=[TextResponse("Web Developer"), TextResponse("iOS Developer"),
                                                                        TextResponse("Android Developer"),TextResponse("Full Stack Developer"), TextResponse("BackEnd Developer"),
                                                                        TextResponse("FrontEnd Developer")])]))

            # Check if the user has sent a text message.
            elif isinstance(message, TextMessage):
                user = self.kik_api.get_user(message.from_user)
                message_body = message.body.lower()
                
                if message_body.split()[0] in ["hi","hello","hey" ]:
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Hey {}, what type of internship are you looking for?".format(user.first_name),
                        keyboards=[SuggestedResponseKeyboard(responses=[TextResponse("Web Developer"), TextResponse("iOS Developer"),
                                                                        TextResponse("Android Developer"),TextResponse("Full Stack Developer"), TextResponse("BackEnd Developer"),
                                                                        TextResponse("FrontEnd Developer")])]))
                    
                elif message_body == "web developer":
                    job="web developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"),TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])]))
                    
                elif message_body == "ios developer":
                    job="ios developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"),TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])]))   
                    
                elif message_body == "full stack developer":
                    job="full stack developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"),TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])]))
                    
                elif message_body == "android developer":
                    job="android developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"),TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])]))                         
                    
                elif message_body == "backend developer":
                    job="backend developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"),TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])]))     
                    
                elif message_body == "frontend developer":
                    job="frontend developer"
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Where would you like to work?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Toronto,ON"), TextResponse("Waterloo,ON"), TextResponse("California"), TextResponse("Ottawa,ON"),TextResponse("Austin,TX"), TextResponse("Vancouver,BC"),TextResponse("London,UK"), TextResponse("Himalayas"),TextResponse("Mars"),TextResponse("Atlantis")])])) 


                elif message_body == "toronto,on":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "waterloo,on":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "california":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + " . Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])]))
                    
                elif message_body == "ottawa,on":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "austin,tx":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "vancouver,on":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "london,uk":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Here is the link for the website: " + jobSearch(job,location) + ". Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])]))
                    
                elif message_body == "himalayas":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body= "It is super cold there! " +jobSearch(job,location) + " Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])]))
                elif message_body == "mars":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body= "There is no oxygen there! " + jobSearch(job,location) + " Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])])) 
                    
                elif message_body == "atlantis":
                    location=message_body
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body= "Under the sea, under the sea. Ok, Ariel "+ jobSearch(job,location) + " Can I help you with something else?",
                        keyboards=[SuggestedResponseKeyboard(
                            responses=[TextResponse("Yes"),TextResponse("No")])]))  
                    
                elif message_body == "yes":
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Perfect! {}, what type of internship are you looking for?".format(user.first_name),
                        keyboards=[SuggestedResponseKeyboard(responses=[TextResponse("Web Developer"), TextResponse("iOS Developer"),
                                                                        TextResponse("Android Developer"),TextResponse("Full Stack Developer"), TextResponse("BackEnd Developer"),
                                                                        TextResponse("FrontEnd Developer")])]))                    
                    
                elif message_body in ["WN", "sure! i'd love to!"]:

                    # Send the user a response along with their profile picture (function definition is below)
                    response_messages += self.profile_pic_check_messages(user, message)

                elif message_body in ["no", "no thank you", "nope","cancel","bye"]:
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Ok, {}. Chat with me again if you change your mind.".format(user.first_name)))
                else:
                    response_messages.append(TextMessage(
                        to=message.from_user,
                        chat_id=message.chat_id,
                        body="Sorry {}, I didn't quite understand that.".format(user.first_name),
                        keyboards=[SuggestedResponseKeyboard(responses=[TextResponse("Web Developer"), TextResponse("iOS Developer"),
                                                                        TextResponse("Android Developer"),TextResponse("Full Stack Developer"), TextResponse("BackEnd Developer"),
                                                                        TextResponse("FrontEnd Developer")])]))

            # If its not a text message, give them another chance to use the suggested responses
            else:

                response_messages.append(TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body="Sorry, I didn't quite understand that. What are you looking for, {}?".format(user.first_name),
                    keyboards=[SuggestedResponseKeyboard(responses=[TextResponse("Web Developer"), TextResponse("iOS Developer"),
                                                                        TextResponse("Android Developer"),TextResponse("Full Stack Developer"), TextResponse("BackEnd Developer"),
                                                                        TextResponse("FrontEnd Developer")])]))

            # We're sending a batch of messages. We can send up to 25 messages at a time (with a limit of
            # 5 messages per user).

            self.kik_api.send_messages(response_messages)

        return Response(status=200)

response = urllib2.urlopen("https://ca.indeed.com/")
response.read();

def jobSearch(job,location):
    print(job)  
    site=""
    if(location == "london,uk"):
        site=" https://www.indeed.co.uk/jobs?q=computer+science&l=London%2C+Greater+London "
        return site
    elif(location == "california"):
        site=" https://www.looksharp.com/c/california "
        return site
    elif(location == "waterloo,on"):
        site="https://ca.indeed.com/Computer-Science-Science-jobs-in-Waterloo,-ON "
        return site
    elif (location == "toronto,on"):
        site=" https://ca.indeed.com/jobs?q=Computer+Science+Internship&l=Toronto%2C+ON "
        return site        
    elif(location =="vancouver,bc"):
        site=" https://ca.indeed.com/jobs?q=Computer+Science+Internship&l=Vancouver%2C+BC "
        return site        
    elif(location =="austin,tx"):
        site=" https://www.looksharp.com/c/austin-tx "
        return site        
    elif(location == "ottawa,tx"):
        site=" https://ca.indeed.com/jobs?q=Computer+Science+Internship&l=Ottawa%2C+ON "
        return site        
    return "Sorry, I coulnd't find a job for that location. " 

if __name__ == "__main__":
    """ Main program """
    kik = KikApi('jobhuntbot','529399e3-4780-431f-9881-03089a6554f1')
    # For simplicity, we're going to set_configuration on startup. However, this really only needs to happen once
    # or if the configuration changes. In a production setting, you would only issue this call if you need to change
    # the configuration, and not every time the bot starts.
    kik.set_configuration(Configuration(webhook='https://965cb5ef.ngrok.io/incoming'))
    app = KikBot(kik, __name__)
    app.run(port=8080, host='127.0.0.1', debug=True)
