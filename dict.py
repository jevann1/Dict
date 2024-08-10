meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "tanggapan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"
            }
print('selamat datang di aplikasi kamus')
print('masukan 5 kata yang ingin kamu ketahui')

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word == 'END':
        print('terimakasih sudah menggunakan kamus')
        break
    if word in meme_dict.keys():
        print(meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    else:
        print('maaf kata tidak ditemukan')
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
