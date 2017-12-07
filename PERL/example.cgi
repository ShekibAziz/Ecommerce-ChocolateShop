#!/usr/bin/perl 
#	Sample perl cgi script.  This script prints a list of the 
#	KEY=VALUE parameters received from the client.
#	CS545 Fall 2017
#	Code by Alan Riggins
#
use CGI;

my $q = new CGI;

print "Content-type: text/html\n\n";

print <<END_HTML;

<h1>Example Form and CGI Script</h1>
<h2>You have submitted the following 
<i><b>key=value</b></i> parameter pairs</h2>
<br /><br />
<table>
END_HTML
		
my ($key, $value);
                
foreach $key ($q->param) {
    print "<tr>\n";
    print "<td>$key</td>\n";
    foreach $value ($q->param($key)) {
        print "<td>$value</td>\n";
        }
    print "</tr>\n";
}
print "</table>\n"