import math

def get_dist(user_lon, user_lat, defib_lon, defib_lat):
    x = (defib_lon - user_lon) * math.cos((user_lat + defib_lat)/2)
    y = defib_lat - user_lat
    d = math.sqrt(pow(x,2) + pow(y,2)) * 6371
    return d

defib_list = ['1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;04 67 02 21 60;3,87952263361082;43,6071285339217', '2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;04 67 34 44 93;3,89652239197876;43,5987299452849', '3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;04 67 54 45 23;3,87388031141133;43,6395872778854', '4;Centre municipal Garosud;34000 Montpellier;04 67 34 74 62;3,85859221929501;43,5725732056683', '14;Service surveillance voie publique (ASVP); 8 Avenue Louis Blanc;04 99 58 80 31-32;3,87964814275905;43,6144971208687', '16;Poste de police Ecusson Centre ville;19 bis Rue durand 34000 Montpellier;04 67 34 70 89;3,87860749270054;43,6050174770208', '17;Unite Service Fourriere;1945 avenue de toulouse;04 67 06 10 51;3,85396082760103;43,5873825371736', '18;Poste de police Hotel de ville;789 chemin de moulares;;3,89399056177745;43,5988579879724', '20;Palais des sports Pierre-de-Coubertin;Avenue de Naples 34000 Montpellier;04 67 03 02 24;3,81388672389191;43,6382964524906']

lon,lat = 3.88995587137398, 43.6260090150577

print(min(defib_list, key=(lambda x: get_dist(lon,
                                              lat,
                                              float(x.split(';')[4].replace(',','.')),
                                              float(x.split(';')[5].replace(',','.')))))
      .split(';')[1])




