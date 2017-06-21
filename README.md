# Log Analysis Project

A large database log table with over a million rows is analized. The project contains a reporting tool for a news site to report what articles the readers are requesting and what is the errror rate for the server.

## Files
* newsdata.sql - Script file which creates the following tables:
    * Authors table
    * Articles table
    * Log table
* logsanalysis.py - Main python program which executes the queries and returns the results
* logsanalysis_output.txt - Sample output of the program


## How to Run
### You will need:

* Python3
* Vagrant
* VirtualBox

### Setup
Install Vagrant And VirtualBox
Clone this repository
Launch Vagrant VM by running 'vagrant up'
Log in using 'vagrant ssh'
Load the data, by using the command 'psql -d news -f newsdata.sql'

### To Run
Run 'python3 logsanalysis.py' from the command line.

## License
----

David Villegas