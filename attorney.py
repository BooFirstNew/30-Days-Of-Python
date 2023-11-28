# Logster - generate metrics from logfiles [![Build Status](https://secure.travis-ci.org/etsy/logster.svg)](http://travis-ci.org/etsy/logster)
Logster is a utility for reading log files and generating metrics to
configurable outputs. It is ideal for visualizing trends of events that
logster to graph the number of occurrences of HTTP response code that appears in
your web server logs.
each successive execution only inspects new log entries. In other words, a 1
minute crontab entry for logster would allow you to generate near real-time
trends in the configured output for anything you want to measure from your logs.
are written to accommodate your specific log format. Sample parsers are
included in this distribution. The parser classes essentially read a log file
line by line, apply a regular expression to extract useful data from the lines
you are interested in, and then aggregate that data into metrics that will be
submitted to the configured output. The sample parsers should give you some idea
found on the [Parsers](./docs/parsers.md) page.

provided, and Logster also supports the use of third-party output classes.
page.
## History

The logster project was created at Etsy as a fork of ganglia-logtailer
fork ganglia-logtailer because we were removing daemon-mode from the original
daemon-modes makes for more work when creating parsing scripts. We care
strongly about simplicity in writing parsing scripts -- which enables more of
our engineers to write log parsers quickly.

## Installation
Logster supports two methods for gathering data from a logfile:

1. By default, Logster uses the "logtail" utility that can be obtained from the
   RPMs for logcheck can be found here:
   ```


1. By default, Logster uses ```fcntl.flock```.
   (which is not available on Windows). You can install Portalocker using pip,
   similar to Pygtail above.

   Logster commandline.



    $ sudo python setup.py install


## Usage
to your configured output.


You can use the provided parsers, or you can use your own parsers by passing
the complete module and parser name. In this case, the name of the parser does
not have to match the name of the module (you can have a logster.py file with a
a virtualenv, for example.
    $ /env/my_org/bin/logster --dry-run --output=stdout my_org_package.logster.MyCustomParser /var/log/my_custom_log

    $ logster -h
    Usage: logster [options] parser logfile

    Tail a log file and filter each line to generate metrics that can be sent to
    common monitoring packages.
      -t TAILER, --tailer=TAILER
      --logtail=LOGTAIL     Specify location of logtail. Default
                            same host.
                            Add suffix to all published metrics. This is for
                            metrics.
      --parser-help         Print usage and options for the selected parser
                            VALUE --option2 VALUE". These are parser-specific and
      -s STATE_DIR, --state-dir=STATE_DIR
                            Where to store the tailer state file.  Default
                            location /var/run
                            /var/log/logster
      --log-conf=LOG_CONF   Logging configuration file. None by default
                            Where to send metrics (can specify multiple times).
                            ganglia, nsca or a fully qualified Python class name
      -d, --dry-run         Parse the log file but send stats to standard output.

## Contributing
- Add your feature
- If you are adding new functionality, document it in the README
- Send a pull request to the etsy/logster project.
If you have questions, you can find us on IRC in the `#codeascraft` channel on Freenode.
