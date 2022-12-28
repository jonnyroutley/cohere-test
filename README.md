# Cohere API Test
A quick test of the Co:here API.

The main file in this repo takes a prompt of some descriptions of exhibitions currently on at the British Library (where I'm writing this) and their titles, and seeks a response to fill out a missing title. Very basic but just wanted to have a quick play around !

Example input: 
> **A free exhibition exploring British Chinese communities and culture.**
> 
> Chinese communities have been calling the UK home for much longer than many realise. Many are able to trace their heritage to regions across East and Southeast Asia, which has led to a rich and diverse culture across the UK.
> 
> In this new free display at the British Library we reflect on this long history through photographs, manuscripts and interviews with those who have lived through it. 
> 
> Meet remarkable individuals from British Chinese communities across the UK. Listen to personal accounts of merchant seamen. Get to know the local business owners who set up Europe’s first Chinatowns. Be inspired by the scientists, artists and writers breaking new ground. And uncover the challenges that British Chinese people have encountered through the centuries, and continue to face today.
> 
> Join us to celebrate the history and impact of this vibrant community, and to understand what it really means to be Chinese and British.

Real exhibition title from BL website:
> British and Chinese

Output title from script:
> Voices of British Chinese communities: from Chinatown to the world

*This seems like a better title to me!*

-----------------

### Run: 
Clone this repository and make sure you have a .env file in the repository with the line API_KEY=[your cohere api key excluding these brackets]

```
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt

python main.py
```

