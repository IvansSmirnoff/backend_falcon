# backend_falcon

Simple api that returns the drawn plot with parameters fiven in get request. The way it works is shown [here](https://www.youtube.com/watch?v=Xw7dQXJUSqw) (careful, Russian comments.;) As the foundation of the api this [tutorial](https://falcon.readthedocs.io/en/0.3.0.1/user/tutorial.html) was used
# Stack

__Language:__ Python

__Libraries:__ falcon, os, matplotlib, pandas(optional, may be needed to ease the work with the input values on the axis of the plot)

For the server I used gunicorn

# Tutorial

From the scratch, let's create some folder to store our files

```bash
$mkdir project_directory
```
