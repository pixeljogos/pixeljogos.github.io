#!/usr/bin/perl
##################################################################
# By BumbleBeeWare.com 2007
# Very Simple search program to search a specified web directory
# easysearrch.cgi
##################################################################
# configure

# the directory with files you want to search
$searchdir = "./";

# the file types you want to allow to be searched
@filetypes = ('*.html','*.htm','*.txt');

# end configuration
######################

# print search form
if($ENV{"REQUEST_METHOD"} ne "POST") {
	&print_form;
	exit;}


# parse incoming form data
read(STDIN,$buffer,$ENV{'CONTENT_LENGTH'});
@pairs = split(/&/,$buffer);

foreach $pair (@pairs){
	($name,$value) = split(/=/,$pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
}


# get the files to search
chdir($searchdir);

# find all the files that match your file types only
foreach $file (@filetypes){
	
	$listedfiles = `ls $file`;
	@listedfiles = split(/\s+/,$listedfiles);
	
	# build an array of correct file types
	foreach $okfile (@listedfiles){ push(@OKFILES,$okfile); }
	}

# read each file that matches your file type array
foreach $file (@OKFILES){&search;}


# print files with matching text
$count = 0;
print "Content-type: text/html\n\n";
print "<p align=left>Search Results</p>";

foreach $file (keys %FILEOK) {
	
	# modify this html for your actual display output
	print "<p align=left><a href=\"$file\">$TITLE{$file} ($file)</a> - $FILEOK{$file}</p>\n";
	$count++;
}

# show how many matches were found
print "<p align=left>$count Matches Found</p>";
exit;

######################
# subroutines
######################

# search directory for matches
sub search {

$summary = "";
$filetext = "";

open (FILE, "$searchdir/$file");
@filetext=<FILE>;
close(FILE);

$filetext = join(' ',@filetext);
$filetext =~ s/\n//g;

# if there is a title save it for display
if ($filetext =~ /<title>(.*)<\/title>/i){$TITLE{$file} = "$1";}

# remove any html leave only text to match
$filetext =~ s/<([^>]|\n)*>//g;

if ($FORM{'keywords'} =~ / /){@keywords = split (/ /,$FORM{'keywords'});}
else {$keywords[0] = $FORM{'keywords'};}
	  
foreach $word (@keywords){
	
	 if ($filetext =~ /$word/i){
		
		# get a text summary for the result 100 characters
		$summary = substr($filetext,0,100);
		$FILEOK{$file} = "$summary";
		
		}

	}
}	


# print the search form
sub print_form {

print "Content-type: text/html\n\n";
print "<form action=\"easysearch.cgi\" method=\"POST\">
    <div align=\"center\"><center><table border=\"0\" cellpadding=\"3\">
        <tr>
            <td align=\"center\"><input type=\"text\" size=\"25\"
            name=\"keywords\"> </td>
            <td align=\"center\"><input type=\"submit\"
            value=\"Search\"></td>
        </tr>
    </table>
    </center></div>
</form>";

}
