#!/usr/bin/perl 
#	Sample perl cgi script.  This script prints a list of the 
#	products in the opatija proj4.products table.
#
#	Code by Alan Riggins, Fall 2017
# Access the script with the following URL:
# http://jadran.sdsu.edu/perl/jadrn000/proj4/proj4_products.cgi
#
   
use DBI;

print <<END_HTML;
Content-type: text/html

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>Products in the jadran Database</title>
	<meta http-equiv="content-type" 
		content="text/html;charset=utf-8" />
	<meta http-equiv="Content-Style-Type" content="text/css" />

    
<style type="text/css">
table { 
	margin-left: auto; margin-right: auto; clear: both;
	}
h1, h2 { 
    text-align: center; 
    color: #F22;
    background-color: #FCC;
    border: 5px double #C00;
    width: 600px;
    font-size: 300%;
    margin: 20px auto 20px auto;
    padding: 20px 0 20px 0;
    }
td {	
	text-align: center; 
	background-color: #FDD; 
	border: 5px solid pink; 
	width: 600px; 
	}
img { float: left; } 
#stocking {
    position: absolute;
    top: 35px;
    left: 35px;
    width: 100px;
    }  
#rudolph {
    float: right;
    position: relative;
    top: 0;
    right: 45px;
    width: 100px;
    }     
</style>

<link rel="stylesheet" href="http://jadran.sdsu.edu/~jadrn004/proj4/CSS/index.css">
</head>
<bo
<h3 class='brandName'>Bertha&apos;s Deluxe Chocolate</h3>
<h1>  THIS IS ORDER ONLINE PAGE !!!! ! ! ! ! ! !</h1>
        <!--       Nav Bar-->
        <div id='navBar'>

            <ul>
                <li><a href="/~jadrn004/proj4/index.html">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Order Online</a></li>
                <li><a href="/~jadrn004/proj4/HTML/AboutUs.html">About Us</a></li>
                <li><a href="/~jadrn004/proj4/HTML/contact.html">Contact</a></li>
            </ul>
        </div>
        <!--        // Nav Bar-->
        <div id='clear'></div>

<table>
END_HTML

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "proj4";
my $username = "jadrn004";
my $password = "tomato";
my $database_source = "dbi:mysql:$database:$host:$port";

	
my $dbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';

my $sth = $dbh->prepare("SELECT sku, title, short_description, long_description, retail FROM products order by category");
$sth->execute();

while(my @row=$sth->fetchrow_array()) {
    print "\t<tr>\n";
    my $pic = "/~jadrn000/PROJ4_IMAGES/".$row[0].".jpg";
    print "\t\t<td><img src=\"$pic\" alt=\"$row[1]\" />";
    print "<b>$row[1]</b><br /></br />";
    print "$row[2]<br /><br />";
    print "$row[3]<br /><br />";
    print "$row[4]</td>\n";
    print "\t</tr>\n";
    }
 

$sth->finish();
$dbh->disconnect();

    	

print "</table>\n";
print "</div>\n";
print "<footer>
            <p>
                The following content is copyrighted and may only be used by having a signed permissed from the owner's permission. You may contact the owner via the contact form.
            </p>    
        </footer>";
print "</body>\n";
print "</html>\n";