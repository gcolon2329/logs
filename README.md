# Udacity Log Analysis Project

### About this project :
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


### How to run the program:

#### Requirements:
  * [Python3] (https://www.python.org/downloads/) - This code uses version 3.7.2
  * [Vagrant] (https://www.vagrantup.com/) - An open-source software product for building and maintaining portable virtual software development environments
  * [VirtualBox] (https://www.virtualbox.org/) - Open-source hosted hypervisor for x86 computers and is under development by Oracle Corporation


### Access project:
1. Make sure your python is up to date.
2. Download and install Vagrant and VirtualBox.
3. Download Udacity [FSND-virtual-machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
4. Clone this repository
5. Download [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
6. The file "newsdata.sql" must be put within your vagrant directory, which is shared with your virtual machine.
7. Launch your virtual machine from your command line with 'vagrant up'
8. After installation use 'vagrant ssh' to connect. (Your commandline will begin with /vagrant/folder)
9. Unpack the database folder.
10. To load the database type 'psql -d news -f newsdata.sql'
11. To run the database type 'psql -d news'
12. Use command 'python3 logs.py' to runt he program and fetch results.
