On the interview.py file there are siz methods among them four method headers were already given
on the reference.py file.

On the generate_password method, basically I just created passwords based on the given complexity
and length parameters and at the end I just return the newly created password.

On the check_password_level method, first I tried using regex in order to find the complexity of
every password. However, later on I changed that implementation to 'any' and 'all' functionalities
of python and used string's islower, isupper, isdigit functions in order to determine the complexity
level of every password.

Then I created new method called step_4() which is for the forth step of the instruction under
the Challenge paragraph that we have provided with. Refer to that method, the script generates
passwords manually and later on we can print those passwords.

On the create_user method, first I get access to the randomuser api and pull the random data from api.
Afterwards, I parsed json formatted data and achieved name, last name and email. Subsequently, I
created a database and inserted name, last name and email to that database.

Then I created another method called step_6 for the sixth step of instruction under Challenge
paragraph. Based on that instruction, I first read data which was previously inserted to the table.
Then I created 10 passwords and added that to the database as well.