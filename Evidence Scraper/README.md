# Evidence Scraper

## Audio
Contains audio files pertaining to Harvey Weinstein in `mp3` and `wav` fomat

## Data
### Depp & Heard
Scraped files from Fairfax County, Virginia site, link <a href="https://ffxtrail.azurewebsites.net/" target="_blank">here</a>. One table respective to Heard and one to Depp. Each table contains all the evidence files used on X date and the related link, as well as file format. `depp_times.csv` and `heard_times.csv` contain extracted time data values from all of the pdfs. 
### FLOWS
Manually scraped stories on domestic abuse from <a href="https://www.flows.org.uk/support-for-women/am-i-being-abused/case-studies" target="_blank">FLOWS</a>.
### UQ Case Studies
Scraped domestic violence cases from the University of Queensland Law site, link <a href="https://law.uq.edu.au/research/dv/using-law-leaving-domestic-violence/case-studies" target="_blank">here</a>.
### Weinstein

Speech to text conversion of the audio files found in `Audio`. `otterai` denotes speech to text from <a href="https://otter.ai/home" target="_blank">OtterAI</a>, `sr` using the python library <a href="https://pypi.org/project/SpeechRecognition/" target="_blank">SpeechRecognition</a>, and  `w2v` denotes speech to text using the python library <a href="https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/" target="_blank">Wav2vec 2.0</a>.

## Code
`audio_scraper.py`: python script used to convert `wav` audio files to `txt`. Used for `Weinstein` project.  
`ffxtrail_scraper.py`: python script to scrape the Fairfax county site into readable evidence tables for `Depp & Heard`.  
`uq_scraper.py`: python script to scrape the cases found in `UQ Case Studies` into a readable csv.  