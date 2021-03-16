# vaccine-notifier
Receive a notification when vaccines are available in your area

## Setup
#### Configuration
Ensure that the following parameters are setup to your liking.
- minutes - scheduled interval to check for available vaccines
- center - the origin from which to compare distances to nearby pharmacies
- max_distance - the search radius in miles

#### Run
Simply run `python notifier.py` as a background job or within a `tmux` session.

#### Extend
Update `sound` to include additional actions you might want to take when a vaccine is
located within your search radius. Send an email, a native notification, or sound a buzzer!

![Raspberry PI Vaccine Buzzer](https://github.com/gkumar7/model/blob/main/rpi-buzzer.jpg)