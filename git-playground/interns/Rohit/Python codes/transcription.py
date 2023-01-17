def transcription(dna: str) -> str:
    dna.upper()
    result = dna.replace("T", "U")
    print (result)


transcription("GATGGAACTTGACTACGTAAATT")
