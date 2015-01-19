# CourseOpenings

Checks the [LSA Course Guide](http://www.lsa.umich.edu/cg/) for course openings. Written in Python 3, with a cron script for Windows.

*Written during the winter of my junior year at the University of Michigan.*

## Installation

1. Clone the repo
2. Move `class_alert_invisible.bat` to your Windows startup scripts
  * Change `PATH_TO_CLASS_ALERT` to wherever you cloned the repo
3. Update `class_alert.py`
  * Create a Gmail account for sending messages (password will be stored in plain text here)
  * Change `YOUR_SENDER_EMAIL` and `YOUR_SENDER_PASSWORD` accordingly
  * Change `YOUR_PERSONAL_EMAIL` to the address where you'd like to receive alerts
  * Change `params` for the class ID to the class you want to monitor

## Usage

Assuming you installed correctly, upon startup your computer will query for class listings every 2 hours. If there are openings, you'll get an email to your personal account telling you about it.

Note: `invis.vbs` runs a CMD process invisibly in the background. It can be used with any batch script. To end the background process, kill Windows Command Processor with the task manager.

## History

Applying for classes is a huge pain when they're full, since many don't allow waitlists. I created this script to help remove some stress from the process.

Note:
All the code here is in its (mostly) original form, and hasn't been modified since I wrote it in 2013.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Credit to The Internet for the `invis.vbs` script. I can't find any original attribution; it seems to be quite widely used.
