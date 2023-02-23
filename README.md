<h1 style="text-align: center;">Vaccine-tracker</h1>
<br>
<p>
    Just a basic python script to track if a vaccine slot is available.

    written in python3

    requirments : 
    requests (pip install requests) 
    json (already included with python3) 
    datetime (already included with python3)

    The module uses preexisting api's to get data.

    The code uses 'if-none-match' header to prevent overloading of the server and only retriving the data when new data is available.

    Currently the module checks for availability of vaccination centers for next 5 days in Bhopal district (can be changed by changing the value of district ID) for anyone over 18 and less than 45 of age.

    I only wrote this to try and run as a personal module I currently have no intention of making a service out of it. But, I am definitely open to suggestions.
<p>
<p>
</p>