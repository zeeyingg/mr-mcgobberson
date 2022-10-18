# Blue Haired Gals (Talia, Ziying, Jasmine)
# Softdev Period 2
# K12
# 2022-10-17
# time spent: 0.5 hr

IN CLASS:

- we figured out the difference between GET and POST methods
- we figured out how to use the POST method to return the username and display it on the website
- we linked the html render template to the flask app

AT HOME:
* We couldn’t really get POST to work, and we weren’t really understanding what the problem was
* When submitting form data through the POST method, the data is not appended to the web address anymore, so the user can’t change the data after submitting
* GET puts the form data into the URL and can be changed by the user after submitting. We found that this was the case when we changed the data in the address bar and saw it being overwritten in the terminal output

- We returned the POST method and displayed the submitted username
by setting the form action of the login page to be "/auth"
(the route of the response.html) and updating the method to "post"
