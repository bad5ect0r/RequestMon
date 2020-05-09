# RequestMon

This is a simple monitoring tool that I developed in a day.
It's very modular since you have to write part of the code yourself.
Credit for @wagoodman for his [diff2HtmlCompare](https://github.com/wagoodman/diff2HtmlCompare) repo.

### Usage

Make sure to follow the install steps for [diff2HtmlCompare](https://github.com/wagoodman/diff2HtmlCompare) by going into that dir and running

```
pip3 install -r requirements.txt
```

Then just write up a python class that inherits from RequestObj. See selftest.py for an example.
Then in checker.py, add it to the list `REQUEST_OBJS`.

Next fill in your pushover details in pushover.py.
Finally, you can edit and use run.sh to automate the execution of the monitoring in a cronjob.

Page versions are maintained in the pages directory.
Diffs are found in the Results directory.

