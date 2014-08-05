# batlog-python

An OS X battery data logger based on [batlog][1], written in Python.

## Usage

### Installing the script

Download the `batlog.py` file and put it somewhere on your file system. For example, I've put it under `/Users/pietvandongen/batlog.py`.

### Automatically running the script

Then, set up a [Cron][2] job that runs the script every minute by going to your terminal and running:

```bash
crontab -e
```

Then, enter this line and save:

```bash
* * * * * python /path/to/the/script/batlog.py /path/to/your/log/file/batlog.csv
```

This will run the `batlog.py` script every minute and write the results to `/path/to/your/log/file/batlog.csv`.

You can check your Cron configuration by typing:

```bash
crontab -l
```

## Viewing the log file

### On your system

Go to the directory you set above and open the file. In the above case, it's located at `/path/to/your/log/file/batlog.csv`.

### Visualizing data
 
You can generate a graph of your log by dropping the CSV in the [batlog chart generator][3]. This will generate a chart that looks like this:

![example graph](http://pietvandongen.github.io/batlog-d3-chart/images/example.png)

## Example

The script generates logs that look like this:

```csv
Date,DesignCapacity,CurrentCapacity,MaxCapacity,CycleCount
2014-08-04 14:42:01,8440,870,8199,153
2014-08-04 14:43:00,8440,851,8206,153
2014-08-04 14:44:00,8440,828,8207,153
2014-08-04 14:45:01,8440,788,8195,153
2014-08-04 14:46:00,8440,764,8199,153
2014-08-04 14:47:01,8440,718,8183,153
2014-08-04 14:48:00,8440,707,8198,153
```
 
## License

Apache License, Version 2.0, see `LICENSE.md`.

[1]: https://github.com/jradavenport/batlog
[2]: http://en.wikipedia.org/wiki/Cron
[3]: http://pietvandongen.github.io/batlog-d3-chart/