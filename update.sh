#!/bin/sh

CACTIBASE="/usr/local/www/data/cacti"
WMAPBASE="$CACTIBASE/weathermap"

# do the normal cacti data update
/usr/local/bin/php $CACTIBASE/poller.php 

cd $WMAPBASE

# make the HTML files that weathermap needs
$WMAPBASE/cacti2weathermap.pl $CACTIBASE/rra/

# make the weathermaps
$WMAPBASE/weathermap --htmloutput $WMAPBASE/weathermap.html --config $WMAPBASE/weathermap.conf --output weathermap.png

# repeat line above for additional maps/customers
