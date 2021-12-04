f = open('3_input.txt').read().splitlines()

def life_support_rating(o2, co2):
    return o2 * co2

def filter(list, i=0, co2=False): # where `i` is the bit position
    if len(list) == 1:
        return list[0]
    count = 0
    for item in list:
        count += int(item[i])
    dom_num = 1 if count >= len(list) / 2 else 0 # prefers 1 in case of ties by default
    pref_num = dom_num if co2 == False else abs(dom_num - 1) # pref_num is opposite if co2 reading sought
    list = [x for x in list if int(x[i]) == pref_num]
    return filter(list, i + 1, co2)

o2_rating = filter(f) # oxygen generator rating
co2_rating = filter(f, co2 = True) # co2 scrubber rating

answer = life_support_rating(int(o2_rating, 2), int(co2_rating, 2))
