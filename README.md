I want to run a cron job in every midnight. 
<code>
CRONJOBS = [
    ('0 0 * * *', 'app.cron.test_job')
]
</code>
This works perfectly on my pc but not in docker container.<br>
Basically if try to fire up a job at a time everyday, it doesn't work in container.
But if I try to run a function, after a period of time, it works on docker container.
Example, 
<code>
CRONJOBS = [
    ('*/20 * * * *', 'app.cron.test_job')
]
</code>
works fine.

But not this,
<code>
CRONJOBS = [
    ('20 * * * *', 'app.cron.test_job')
]
</code>

I want to know the reason behind it. Any kinds of suggestions are appreciated.<br>
Thanks in advance
