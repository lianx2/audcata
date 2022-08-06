#!usr/bin/perl -w

# Creation: 20220523
# Modified: 20220803 - Further automation; see ~/mit/course-audit/main.py
# This code parses MIT's course catalog by course crn, title, level, and instructor.
# INPUT: website HTTP request (main.py can generate an input file)
# OUTPUT: Excel spreadsheet with parsed catalog data.

use Excel::Writer::XLSX;

printf "[Success] Retrieved $ARGV[0] to parse and $ARGV[1] to write.\n";
my $f2o = $ARGV[0];
my $f2w = $ARGV[1];
print "$f2w\n";

printf "[Initializing] Data structures for parsing...\n";
my $num_of_attributes = 4; # starting from 0
my @crn = ();
my @title = ();
my @units = ();
my @total = ();
my @instructor = ();

# extract out course attributes
print "[Progress] Parsing input catalog...\n";
open (F2O, "<", "$f2o") || die "Cannot open $f2o: $!";
while (<F2O>) {
    chomp;
    my $line = $_;
    if (/<p><h3>/) {
        while (/(?<=<p><h3>).+/g) {
            my ($name, $title) = split / /, $&, 2;
            push(@crn, $name);
            push(@title, $title);
        }
        # Validate if data was extracted for each desired attribute.
        # If not, append 'n/a' (only @instructor has this issue)
        if (@crn-1 > @instructor) {
            push(@instructor, 'n/a');
        }
    } elsif (/<br>Units:/) {
        while (/(?<=<br>Units: )[0-9\-]+/g) {
            push(@units, $&);
            my ($one, $two, $thr) = split /-/, $&;
            push(@total, ($one+$two+$thr));
        }
    } elsif (/<br><I>/) {
        while (/(?<=<br><I>)[\w\.\s\,]+/g) {
            push(@instructor, $&);
        }
    }
}
close(F2O) || die "Cannot close $f2o: $!";
print("[Success] Parsed the HTTP request for relevant attributes.\n");

# Print a warning if the length of each data attribute is not equal.
# This check does not catch all errors... must compare each attribute length directly to do so.
if ((@crn+@title+@units+@total+@instructor) % ($num_of_attributes+1) != 0) {
    print ">>>>>>> WARNING: Length of data attributes do not match! <<<<<<<\n";
}

# Debug statements...
#foreach $a (@units) {
#    print("$a\n");
#}
#foreach $a (@total) {
#    print("$a\n");
#}
#foreach $a (@crn) {
#    print("$a\n");
#}
#foreach $a (@title) {
#     print("$a\n");
#}
#foreach $a (@instructor) {
#    print("$a\n");
#}

# Align indices of data for writing to file
my @coursebook = (\@crn, \@title, \@units, \@total, \@instructor);
my $Excelbook = Excel::Writer::XLSX->new( $f2w );
my $Excelsheet = $Excelbook->add_worksheet();
print ("[Success] New .xlsx workbook created: $f2w\n");
# General cell formating
my %font1 = (
    font => 'Arial',
    size => 11,
);
my $genformat = $Excelbook->add_format( %font1 );
# Header formatting
my %font2 = (
    font => 'Arial',
    size => 11,
    color => 'white',
    bold => 1,
    align => 'center',
);
my %shading = (
    bg_color => 'black'
);
my $headerformat = $Excelbook->add_format( %font2, %shading );
# Apply headerformat to header row
$Excelsheet->write( 0, 0, "num", $headerformat );
$Excelsheet->write( 0, 1, "title", $headerformat );
$Excelsheet->write( 0, 2, "units", $headerformat );
$Excelsheet->write( 0, 3, "total", $headerformat );
$Excelsheet->write( 0, 4, "instructor", $headerformat );
print("[Progress] Writing to spreadsheet...\n");
# Write data...
for ($row=0; $row<=$#crn; $row++) {
    for ($col=0; $col<=$num_of_attributes; $col++) {
        $Excelsheet->write( $row+1, $col, ${$coursebook[$col]}[$row], $genformat)
        # First row is reserved for a header
    }
}
$Excelbook->close;
print("[Success] Finished writing to spreadsheet $f2w\n");
