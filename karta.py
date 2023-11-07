# Okay. First, make a card class, then add two things name, qoute start, qoute end.
# Number is included in wiki, use it as well.
import random

class Karta:    
    def __init__(self, name, qoute_1, qoute_2, number):
        self.name = name
        self.qoute1 = qoute_1
        self.qoute2 = qoute_2
        self.number = number

Stahn = Karta('Stahn','Th-The sword spoke!','How in the world can you speak?', 117)
Rutee = Karta('Rutee','Hey Atwight? I have something to ask you...','It\'s about Leon.', 118)
Philia = Karta('Philia',"L-Look out!","Philia Bomb!",119)
Garr = Karta('Garr',"Allow me to disengage my limiter!","I leave the rest...to you...", 120)
Leon = Karta("Leon","I hail from the Kingdom of Seingald...","My name is Leon Magnus.",121)
Chelsea = Karta("Chelsea","No way, I'm not lost!","I was just hanging out with Keyaki and my other friends!",122)
Mary = Karta ("Mary","I'm alive, Dalis.","You saved my life twice.",123)
Karyl = Karta('Karyl', 'People call me "Blue Lightning".', 'You can call me Karyl!', 124)
Bruiser = Karta('Bruiser', 'I am the champion!', 'Hey, kid! I got next! Remember that!', 125)
Lilith = Karta('Lilith', 'A ladle in my right hand, and a frying pan in my left!', 'Arise! Wake the dead!', 126)
Dymlos = Karta('Dymlos', "It's all right, Stahn...", "We've lived too long already.", 127)
Atwight = Karta('Atwight', "I think I've fulfilled my promise to your mother.", 'Never change, okay Rutee?', 128)
Igtenos = Karta('Igtenos', 'Glory to Phandaria!', 'And long live Garr!', 129)
Chaltier = Karta('Chaltier', 'You will always be my young master.', 'I will follow you, no matter what.', 130)
Clemente = Karta('Clemente', "You'll be all right. You're a strong girl.", 'Take care of yourself, Philia.', 131)
Yuri = Karta('Yuri', 'Intend to?', 'I already have.', 132)
Estelle = Karta('Estelle', 'The voices of corpses buried beneath the trees...', 'creep up and lure us to our doom.', 133)
Karol = Karta('Karol', "Until you really think I'm a boss...", "I'll just do my part as a fellow member of Brave Vesperia.", 134)
Rita = Karta('Rita', 'You thought you could win?', 'Too bad!', 135)
Raven = Karta('Raven', 'So this is the end, huh?', 'Farewell, all my dear fans the world over.', 136)
Judith = Karta('Judith', 'This is the path I have chosen.', '...Goodbye.', 137)
Kyle = Karta('Kyle', 'I want to be just like my dad!', 'A great hero, just like him!', 138)
Loni = Karta('Loni', "Don't attack when your spirit is low!", "You'll get knocked back!", 139)
Judas = Karta('Judas', 'Another nightmare...', "They always begin here, don't they, Chal?", 140)
Reala = Karta('Reala', 'Kyle? Kyyyyle!', 'Hey! Over here!', 141)
Nanaly = Karta('Nanaly', 'I understood Lou better than anyone.', "If nothing else, I'm sure of that.", 142)
Harold = Karta('Harold', 'Always keep your rocket launcher ready to fire.', "It's my motto!", 143)
Cress = Karta('Cress', 'We need magic to defeat Dhaos.', 'Would you help us, please?', 144)
Mint = Karta('Mint', "I'm sure I heard my mother's voice!", 'The voice that helped me pull through.', 145)
Arche = Karta('Arche', 'Hmph! Chester...', 'I REALLY, REALLY HATE YOU!', 146)
Claus = Karta('Claus', 'Defeat Dhaos? Are you...serious?', "Hmph, that's quite a tall tale.", 147)
Suzu = Karta('Suzu', "I'm not going to cry.", 'A true ninja steels her heart against such emotions.', 148)
Chester = Karta('Chester', 'Cress...Did you know?', 'Ami, she liked you.', 149)
Lloyd = Karta('Lloyd', 'How can we go on a quest to regenerate the world...', "if we can't even save the people standing right in front of us?!", 150)
Colette = Karta('Colette', '    ...thanks.', "I'm glad I was able to live to this day.", 151)
Genis = Karta('Genis', "You don't have to apologize, Lloyd.", 'I like you, as well as the people of Iselia.', 152)
Raine = Karta('Raine', 'Lloyd Irving, wake up!', 'Lloyd!', 153)
Sheena = Karta('Sheena', 'The people of Mizuho were chased from this land.', 'We all live in hiding.', 154)
Kratos = Karta('Kratos', "Hmph...and I thought I'd finally earned the right to die.", "But you're as softhearted as ever.", 155)
Zelos = Karta('Zelos', 'Now, now, settle down, my darling hunnies!', "Hi there, my little cool beauty, are you hurt?", 156)
Presea = Karta('Presea', "Thank you for assisting me with my daddy's burial.", "...I've been a great burden on you all.", 157)
Regal = Karta('Regal', 'I swear upon my good name and these shackles that bind me...', 'I shall not betray you.', 158)
Luke = Karta('Luke', "I'm the ambassador!", 'What I say goes! Understand?!', 159)
Guy = Karta('Guy', 'My sword cuts all!', 'Enter the amazing Guy!', 160)
Tear = Karta('Tear', "I didn't expect you to be a Seventh Fonist, too.", 'That was careless of me.', 161)
Anise = Karta('Anise', 'Oh, no! Ion!', "The Commandant's in danger!", 162)
Jade = Karta('Jade', "My apologies. I'd forgotten the young master here...", "hasn't a clue about the world around him.", 163)



#This is where the game starts:
#Choose the number of rounds.
#Set all cards as unknown, if a card is known i.e. answered, remove from play.
roundsmax = int(input("How many rounds?\n"))
print(str(roundsmax) + " will be played.\n")
rounds = 0
knownKarta=[]
Kartas= [Stahn, Rutee, Philia, Garr, Leon, Chelsea, Mary, Karyl, Bruiser, Lilith, Dymlos, Atwight, Igtenos, Chaltier, Clemente, Yuri, Estelle, Karol, Rita, Raven, Judith, Kyle, Loni, Judas, Reala, Nanaly, Harold, Cress, Mint, Arche, Claus, Suzu, Chester, Lloyd, Colette, Genis, Raine, Sheena, Kratos, Zelos, Presea, Regal, Luke, Guy, Tear, Anise, Jade]


while roundsmax > rounds: 
    useable_karta=[item for item in Kartas if item not in knownKarta]
    #choose a random karta
    random_karta = random.choice(useable_karta)

    print(random_karta.qoute1)

    Answer = input("Who am I?\n")

    if Answer == random_karta.name:
        print("Correct\n")
        print(random_karta.qoute2)
        #Karta is known, remove from play.
        knownKarta.append(random_karta) 
    else:
        print("Incorrect\n")
    print("round: " + str(rounds)+"\n")
    rounds+=1
    if rounds == roundsmax:
        print("GAME OVER\n")
        print(knownKarta)
        print("Known Karta cards:\n")
        for card in knownKarta:
            print(f"{card.name} - {card.qoute1} - {card.qoute2}")
        break
