meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek"
            }
            

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    word = word.upper()
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        soru = input("Sözlüğe bakmaya devam etmek istermisiniz? (y/n)")
        if soru == "n":
            break
    else:
        print("Bu kelime sözlüğe dahil değil.")
        soru = input("Sözlüğe bakmaya devam etmek istermisiniz? (y/n)")
        if soru == "n":
            break
