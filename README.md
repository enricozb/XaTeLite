# XaTeLite 🛰️

LaTeX over SSH and HTTP. Lets you remotely compile LaTeX and immediately see
your compiled pdf all remotely.

## Requirements
You need
 - Flask
 - pdflatex

## Installation
Just install by
```
python3 -m pip install flask
python3 -m pip install xatelite
```

## Usage
The most common use case is ssh-ing into your remote server,
starting xatelite, and opening up a web browser to your xatelite latex server.

Here's an example: after ssh-ing into your server, run
```
$ xatelite -f ~/math/pset4/pset4.tex -q -p 5010
```

This starts an HTTP server on port `5010` and uses `-q` to silence Flask's
output. Now if you visit your server on port `5010` through a web browser,
you'll be presented with your pdf. **Refreshing recompiles the LaTeX file**.

If there's a bug in your .tex file (if pdflatex returns a non-zero error code),
a log file will be presented instead. Use the log file to debug.

## Options
The current options can be accessed by `xatelite -h` and are:

    usage: xatelite.py [-h] [-f LATEX_FILE] [-p PORT] [-q] [-qq]

    optional arguments:
      -h, --help            show this help message and exit
      -f LATEX_FILE, --latex_file LATEX_FILE
                            the latex file to be compiled and served. If this is
                            not passed in, the single *.tex file in the working
                            directory will be used.
      -p PORT, --port PORT  specify which port the webserver will run on
      -q, --quiet           suppress any Flask output
      -qq, --qquiet         suppress all output including running message

## TODO
 - [ ] Better debugging options
   - [ ] Maybe have a relaxed mode that allows errors if a pdf is generated?
 - [ ] Have a config file with specific pdflatex commands.
 - [ ] Recommend `xatelite [file] -qq & disown` for non-screen/tmux users.
   - [ ] Have a `-k/--kill` option to kill servers that can take PID/filename
   - [ ] Have a `-s/--sessions` option to see PID/filename/ports

