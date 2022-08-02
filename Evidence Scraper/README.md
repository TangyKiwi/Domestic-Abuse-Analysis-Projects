# Evidence Scraper

## Audio
Contains audio files pertaining to Harvey Weinstein in `mp3` and `wav` fomat

## Data
### Depp & Heard
Scraped files from Fairfax County, Virginia site, link [here](https://ffxtrail.azurewebsites.net/). One table respective to Heard and one to Depp. Each table contains all the evidence files used on X date and the related link, as well as file format. `depp_times.csv` and `heard_times.csv` contain extracted time data values from all of the pdfs. 
### FLOWS
Manually scraped stories on domestic abuse from [FLOWS](https://www.flows.org.uk/support-for-women/am-i-being-abused/case-studies).
### UQ Case Studies
Scraped domestic violence cases from the University of Queensland Law site, link [here](https://law.uq.edu.au/research/dv/using-law-leaving-domestic-violence/case-studies).
### Weinstein
Speech to text conversion of the audio files found in `Audio`. `otterai` denotes speech to text from [OtterAI](https://otter.ai/home), `sr` using the python library [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), and  `w2v` denotes speech to text using the python library [Wav2vec 2.0](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/).

## Code
`audio_scraper.py`: python script used to convert `wav` audio files to `txt`. Used for `Weinstein` project.  
`ffxtrail_scraper.py`: python script to scrape the Fairfax county site into readable evidence tables for `Depp & Heard`.  
`uq_scraper.py`: python script to scrape the cases found in `UQ Case Studies` into a readable csv.  