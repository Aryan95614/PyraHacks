import random, sys

list = [
    "If you have 3 quarters, 4 dimes, and 4 pennies, you have $1.19. You also have the largest amount of money in coins without being able to make change for a dollar.",
    "The numbers '172' can be found on the back of the U.S. $5 dollar bill in the bushes at the base of the Lincoln Memorial.",
    "President Kennedy was the fastest random speaker in the world with upwards of 350 words per minute.",
    "In the average lifetime, a person will walk the equivalent of 5 times around the equator.",
    "Odontophobia is the fear of teeth.",
    "The 57 on Heinz ketchup bottles represents the number of varieties of pickles the company once had.",
    "The surface area of an average-sized brick is 79 cm squared.",
    "According to suicide statistics, Monday is the favored day for self-destruction.",
    "Cats sleep 16 to 18 hours per day.",
    "The most common name in the world is Mohammed.",
    "It is believed that Shakespeare was 46 around the time that the King James Version of the Bible was written. In Psalms 46, the 46th word from the first word is shake and the 46th word from the last word is spear.",
    "The Eisenhower interstate system requires that one mile in every five must be straight. These straight sections are usable as airstrips in times of war or other emergencies.",
    "The first known contraceptive was crocodile dung, used by Egyptians in 2000 B.C.",
    "When you die your hair still grows for a couple of months.",
    "There are two credit cards for every person in the United States.",
    "Isaac Asimov is the only author to have a book in every Dewey-decimal category.",
    "The newspaper serving Frostbite Falls, Minnesota, the home of Rocky and Bullwinkle, is the Picayune Intellegence.",
    "It would take 11 Empire State Buildings, stacked one on top of the other, to measure the Gulf of Mexico at its deepest point.",
    "The first person selected as the Time Magazine Man of the Year - Charles Lindbergh in 1927.",
    "The most money ever paid for a cow in an auction was $1.3 million.",
    "The Neanderthal's brain was bigger than yours is.",
    "On the new hundred dollar bill the time on the clock tower of Independence Hall is 4:10.",
    "Each of the suits on a deck of cards represents the four major pillars of the economy in the middle ages: heart represented the Church, spades represented the military, clubs represented agriculture, and diamonds represented the merchant class.",
    "The names of the two stone lions in front of the New York Public Library are Patience and Fortitude. They were named by then-mayor Fiorello LaGuardia.",
    "The Main Library at Indiana University sinks over an inch every year because when it was built, engineers failed to take into account the weight of all the books that would occupy the building.",
    "The sound of E.T. walking was made by someone squishing her hands in jelly.",
    "The pancreas produces Insulin.",
    "1 in 5,000 north Atlantic lobsters are born bright blue.",
    "There are 10 human body parts that are only 3 letters long (eye hip arm leg ear toe jaw rib lip gum).",
    "The king of hearts is the only king without a moustache.",
    "Henry Ford produced the model T only in black because the black paint available at the time was the fastest to dry.",
    "Mario, of Super Mario Bros. fame, appeared in the 1981 arcade game, Donkey Kong. His original name was Jumpman, but was changed to Mario to honor the Nintendo of America's landlord, Mario Segali.",
    "The three best-known western names in China: Jesus Christ, Richard Nixon, and Elvis Presley.",
    "Every year about 98% of the atoms in your body are replaced.",
    "Elephants are the only mammals that can't jump.",
    "The international telephone dialing code for Antarctica is 672."]


while True:
    choice = input('Would you like a random fact?[y][quit]')
    if choice == 'y':
        thing = random.choice(list)
        print(thing)
        list.remove(thing)

    if choice == 'quit':
        sys.exit()