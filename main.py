import os
import cohere
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


if __name__ == '__main__':
    co = cohere.Client(api_key)

    prompt = f""" Description: A display of photographs taken between 1857 and 1970, capturing the archaeological site of Hampi. The Hindu kingdom Vijayanagara (meaning ‘City of Victory’) established its capital at Hampi in southern India in about 1336. Located along the banks of the Tungabhadra River, temple complexes, palaces and administrative buildings were built amongst the rugged landscape of granite boulders. After flourishing for over 200 years, in 1565, Vijayanagara fell to a rival kingdom and Hampi was abandoned. Hampi’s ongoing religious significance and its designation as a UNESCO World Heritage site in 1987 mean it continues to attract worshippers and tourists to this day. This display provides a lens on the archaeological legacy of Hampi through our archives and the research activities that have played a role in preserving the city’s cultural heritage. 
    
    Title: Hampi: Photography and Archaeology in southern India
    --
    Description: He built an empire that stretched across the world. Rode across the sky on a flying chariot. And descended to the bottom of the sea in a glass bell.Or did he? Piece together an epic tale 2,000 years in the telling. From astrological clay tablets, ancient papyri, and medieval manuscripts, to Hollywood and Bollywood movies and cutting-edge videogames, our major exhibition crosses continents to explore the fantastical stories that turned legacy into legend. Pharaoh, prophet, philosopher. European, Middle Eastern and Asian cultures have all moulded Alexander into the fictional hero they want him to be. And today artists and storytellers alike are still trying to reimagine the man and his myth. Who was he really? You’ll have to decide for yourself.
    
    Title: Alexander the Great: The Making of a Myth
    --
    Description: A free exhibition exploring British Chinese communities and culture. Chinese communities have been calling the UK home for much longer than many realise. Many are able to trace their heritage to regions across East and Southeast Asia, which has led to a rich and diverse culture across the UK. In this new free display at the British Library we reflect on this long history through photographs, manuscripts and interviews with those who have lived through it. Meet remarkable individuals from British Chinese communities across the UK. Listen to personal accounts of merchant seamen. Get to know the local business owners who set up Europe’s first Chinatowns. Be inspired by the scientists, artists and writers breaking new ground. And uncover the challenges that British Chinese people have encountered through the centuries, and continue to face today. Join us to celebrate the history and impact of this vibrant community, and to understand what it really means to be Chinese and British.
    
    Title:"""

    response = co.generate(
        model='xlarge', 
        prompt = prompt,
        max_tokens=40, 
        temperature=0.6,
        stop_sequences=["--"]
    )

    print(response[0])
