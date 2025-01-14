import random
animal_card={
    'Fox':0,
    'Bear':0,
    'Bird':0,
    'Elk':0,
    'Salmon':0
}
for i in animal_card:
    animal_card[i]=random.randint(1,4)
    print(i,'Card is ',animal_card[i])