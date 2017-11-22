xenoCanto is a webscraper that scrapes xenoCanto after information from birds for learning a machine learning model identify birds.

It's run from a master python script from the terminal with the firstname of the bird and the surname of the bird in latin.
It then takes these into a bash script that scrapes xenoCanto for download links for audio files and saves these as a txt file. The bash script then runs a separate python script which gathers the corresponding data like the country etc. After this, the master python script runs a bash script that downloads the mp3 files from the download links txt-file created.  


What we want to do next:

  - Fix database query to send link to audiofile in the correct id table
  - Vulnerable for sql injection (for example: can put script in remarks)
