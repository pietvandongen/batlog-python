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

### Viewing the log file

Go to the directory you set above and open the file. In the above case, it's located at `/path/to/your/log/file/batlog.csv`. 

[1]: https://github.com/jradavenport/batlog
[2]: http://en.wikipedia.org/wiki/Cron