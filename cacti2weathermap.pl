#!/usr/bin/perl

# you might need to uncomment this line, or one like it
# use lib qw(/usr/local/rrdtool-1.0.49/lib/perl);
use RRDs;

#Path to rrd files, or take a command-line option if it exists
$my_dir = $ARGV[0] || "/Users/howie/Sites/weathermap/cacti/rra/";

#Path to store weathermap compatible files
$my_htmldir = "data/";

die("RRA directory specified ($my_dir) doesn't exist.") if ! -d $my_dir;
die("Output directory ($my_html_dir) doesn't exist.") if ! -d $my_htmldir;

opendir RRDDIR, $my_dir or die "Impossible to open file: $!";
@rrd_files = grep /rrd/, readdir RRDDIR;

foreach my $router (@rrd_files){
	print $router,"\n";
        #Get the last cuin/cuout values
        my ($start,$step,$names,$data) = RRDs::fetch $my_dir.$router,"AVERAGE","--start","now";
        foreach my $line (@$data) {
            if( defined(@$line[0]) ) {
                (my $name, my $ext)  = split /rrd/,$router;
                $weatherfile = $my_htmldir."wea_".$name."html";
				print $weatherfile,"\n";
                #Open special html weathermap file
                open OUT,">$weatherfile" or die "bad luck: $!";
                print OUT "<html>\n<body>\n$router\n";
                $nice = sprintf "<!-- cuin d %d -->\n<!-- cuout d %d -->\n", @$line[0], @$line[1];
                print OUT $nice;
                print OUT "</body>\n</html>";
                close OUT;
                }
        }
} 
