

## Testing


## Credits

### [Django/documentation](https://docs.djangoproject.com/en/4.2/) 

Been reading the documents pages up and down scanning for usefull bits and pieces and found som interesting stuff.
For a large section of the forms, found under the posts, i found alot about the ImageField/FileField that was helpful.


### Leftovers/problems

The problem terminal indicates that some of my lines are to long, 2 in the env.py and 5 in the settings.py:

**env.py:** The lines are my DATABASE_URL key/value pair and my CLOUDINARY_URL key/value pair
I won't change this because of safety reasons while deploying.

**settings.py:** The lines are the password authentication provided by django while installing.
I won't change these because of safety reasons while deploying.