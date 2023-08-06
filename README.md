# Devops_assignment_network


1.1st question steps.
 1.1download and install wamp in windows
 1.2follow the steps as says to install on installation window
 1.3run wamp server as it says do want to make changes to this app, proceed by clicking on yes on next it will start the server and then you    can test its installation by opening browser        and hitting localhost it will be default directing to wamp page on this stage it will indicate
 that wamp and apache has been installed perfectly in the machine.
 1.4we can download any html template from web,copy those template files in to one folder and copy that template folder and paste it inside inside windows(c)->wamp64->www  folder.
 1.5next we need to modify httpd-vhosts.conf Documentroot,directory inside C:\wamp64\bin\apache\apache2.4.54.2\conf\extra to point that html page to localhost call instead of     localhost/awesomeweb
 1.6next to make a call to our own dns like awesomeweb instead of localhost,we need to change the host file by directing to C:\Windows\System32\drivers\etc\hosts and opening that host file as run as administrator in notepad and make changes as #127.0.0.1 awesomeweb.local
 from default localhost call like #
 127.0.0.1 localhost
 ::1 localhost
 1.7next hit on the browser with awesomeweb.local it should open the page which previously was directing to localhost,at this point if you hit localhost the page says page not found as    currently it directing to awesomeweb.local.


3.3rd question steps.

3.1.install Nginx
   Start Nginx using sudo systemctl start nginx
 3.2enable Nginx
   sudo systemctl enable nginx
 3.3Check the status of Nginx
   sudo systemctl status nginx
 3.4create basic html file or paste any other html template inside
   
     sudo nano /var/www/html/index.html
 3.5next go to below path and configure ip address and save
    sudo nano /etc/nginx/sites-available/default
 3.6check nginx by below command in terminal
    sudo systemctl reload nginx

 3.7reload nginx by below command
    sudo systemctl reload nginx

 3.8open browser and hit the page configured
