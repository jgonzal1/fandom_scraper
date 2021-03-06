import pandas as pd

def arrs_to_cols(i):
  '''
  i = {
    "l_a":{"d":["b","c"],"e":["f","g"]},
    "l_h":{"d":["i","j","k"],"e":["l","m","n"]},
    "l_o":{"d":["p","q","r"],"e":["s","t"]}
  }  
  '''
  i_df_ut = pd.DataFrame(data=i)
  i_df = i_df_ut.T
  f_df = pd.DataFrame(columns=["les","dk","en"])
  for les in i_df.index:
    dk = i_df.loc[les].loc['dk']
    en = i_df.loc[les].loc['en']
    l_d = len(dk)
    l_e = len(en)
    if(l_d > l_e):
      en += [""]*(l_d - l_e)
    elif(l_d < l_e):
      dk += [""]*(l_e - l_d)
    l = max(l_d, l_e)
    d={"les":[les]*l,"dk":dk,"en":en}
    df_a = pd.DataFrame(data=d)
    f_df = f_df.append(df_a)
  return f_df

i = {
  "1_Basics_1": {
    "dk": [
      "drenge",
      "drengen",
      "piger",
      "pigen",
      "mælk",
      "læser",
      "avis",
      "vi",
      "ris",
      "mænd",
      "kvinder",
      "pigerne",
      "drengene",
      "avisen",
      "sandwich",
      "menu",
      "menuen =",
      "bog",
      "har",
      "barn",
      "I",
      "det",
      "kvinderen",
      "mændene"
    ],
    "en": [
      " = boys (en- word)",
      " = the boy",
      " = girls (en- word)",
      " = the girl",
      " = milk",
      " = read, reads, am/is/are reading",
      " = newspaper (en- word)",
      " = we",
      " = rice",
      " = the man",
      " = the woman",
      " = the girls",
      " = the boys",
      " = the newspaper",
      " = sandwich",
      " = menu (en- word)",
      " the menu",
      " = book",
      " = have/has",
      " = child (et- word)",
      " = you (pl.)",
      " = it, that, the",
      " = the women",
      " = the men"
    ]
  },"2_Basics_2": {
    "dk": [
      "kaffe",
      "vin",
      "appelsin",
      "kylling",
      "æg ",
      "tallerken ",
      "fisk",
      "kartoffel",
      "sukker ",
      "pasta",
      "is",
      "frokost",
      "saft",
      "morgenmad",
      "frugt",
      "ost",
      "kage",
      "jordbær",
      "bøf",
      "mad",
      "citron",
      "suppe",
      "tomat",
      "øl",
      "svinekød",
      "kød",
      "aftensmad",
      "te",
      "olie",
      "salt",
      "vegetar",
      "måltid"
    ],
    "en": [
      " = coffee",
      " = wine",
      " = orange (the fruit) (en- word)",
      " = chicken",
      "= egg",
      "= plate (en- word)",
      " = fish",
      " = potato",
      "= sugar",
      " = pasta",
      " = ice cream, ice",
      " = lunch",
      " = juice",
      " = breakfast",
      " = fruit",
      " = cheese",
      " = cake",
      " = strawberry",
      " = steak",
      " = food",
      " = lemon",
      " = soup",
      " = tomato (en- word)",
      " - beer (en- word)",
      " = pork",
      " = meat",
      " = dinner",
      " = tea",
      " = oil",
      " = salt",
      " = vegetarian",
      " = meal (et- word)"
    ]
  },"3_Phrases": {
    "dk": [
      "hej",
      "ja",
      "farvel",
      "nej",
      "tak",
      "godmorgen",
      "godaften",
      "glad",
      "velkommen",
      "undskyld",
      "siger",
      "siger undskyld",
      "ikke",
      "goddag",
      "godnat",
      "engelsk",
      "snakker",
      "måske"
    ],
    "en": [
      " = hello, bye",
      " = yes",
      " = goodbye/bye, farewell",
      " = no",
      " = thank you/thanks, please",
      " = good morning",
      " = good evening",
      " = happy/fond",
      " = welcome (as in \"Welcome to Denmark\")",
      " = sorry/excuse me",
      " = say/says, am/is/are saying",
      " = (I/you/he/she/it/we/they) apologise/apologises",
      " = not, do/does not",
      " = good day/hello",
      " = good night",
      " = English",
      "talk/talks, am/is/are talking",
      " = maybe"
    ]
  },"4_Food": {
    "dk": [
      "mælken",
      "sandwichen",
      "appelsinen",
      "tallerkenen",
      "kaffen",
      "bogen",
      "kyllingen",
      "barnet",
      "ægget",
      "frugten = ",
      "saften",
      "morgenmaden",
      "frokosten",
      "osten",
      "pastaen",
      "vinen",
      "fisken",
      "sukkeret",
      "aviserne",
      "dyrene",
      "bøgerne",
      "kattene",
      "frugterne",
      "æblerne = ",
      "hestene",
      "hundene",
      "bjørnene",
      "maden",
      "øllen",
      "jordbæret",
      "risene",
      "tomaten",
      "skildpadderne",
      "bøffen = ",
      "suppen",
      "saltet",
      "vegetarene",
      "svinekødet = ",
      "olien",
      "citronen",
      "måltidet",
      "teen",
      "kødet =",
      "børnene ",
      "appelsinerne ",
      "aftensmaden",
      "dyret",
      "kagen",
      "vegetaren",
      "elefanterne",
      "tellerknerne",
      "sandwichene",
      "anden",
      "skildpadden",
      "elefanten",
      "hesten",
      "krabben",
      "kartoflen",
      "musen",
      "øllene = ",
      "edderkoppen",
      "bjørnen = "
    ],
    "en": [
      " = the milk (en- word)",
      " = the sandwich (en- word)",
      " = the apple (en- word)",
      " = the plate (en- word)",
      " = the coffee (en- word)",
      " = the book (en- word)",
      " = the chicken (en- word)",
      " = the child (et- word)",
      " = the egg (et- word)",
      "the fruit (en- word)",
      " = the juice (en- word)",
      " = the breakfast (en- word)",
      " = the lunch (en- word)",
      " = the cheese (en- word)",
      " = the pasta (en- word)",
      " = the wine (en- word)",
      " = the fish (en- word)",
      " = the sugar (et- word)",
      " = the newspapers",
      " = the animals",
      " = the books",
      " = the cats",
      " = the fruits",
      "the apples",
      " = the horses",
      " = the dogs",
      " = the bears",
      " = the food (en- word)",
      " = the beer (en- word)",
      " = the strawberry (et- word)",
      " = the rice",
      " = the tomato (en- word)",
      " = the turtles",
      "the steak (en- word)",
      " = the soup (en- word)",
      " = the salt (et- word)",
      " = the vegetarians",
      "the pork (et- word)",
      " = the oil (en- word)",
      " = the lemon (en- word)",
      " = the meal (et- word)",
      " = the tea (en- word)",
      " the meat (et- word)",
      "= the children",
      "= the oranges",
      " = the dinner (en- word)",
      "fluglene = the birds",
      " = the animal (et- word)",
      " = the cake (en- word)",
      " = the vegetarian (en- word)",
      " = the elephants",
      " = the plates",
      " = the sandwiches",
      " = the duck (en- word)",
      " = the turtle (en- word)",
      " = the elephant (en- word)",
      " = the horse (en- word)",
      " = the crab (en- word)",
      " = the potato (en- word)",
      " = the mouse (en- word)",
      "the beers (en- word)",
      " = the spider (en- word)",
      "the bear (en- word)"
    ]
  },"5_Animals": {
    "dk": [
      "skildpadde ",
      "fugl",
      "hest",
      "elefant",
      "and",
      "kat",
      "mus",
      "bjørn",
      "krabbe",
      "katten ",
      "dyr",
      "hund",
      "hunden",
      "edderkop",
      "løve",
      "ugle",
      "fuglen"
    ],
    "en": [
      "= turtle (en- word)",
      " = bird (en- word)",
      " = horse (en- word)",
      " = elephant (en- word)",
      " = duck (en- word)",
      " = cat (en- word)",
      " = mouse (en- word)",
      " = bear",
      " = crab",
      "= the cat",
      " = animal (et- word)",
      " = dog (en- word)",
      " = the dog",
      " = spider",
      " = lion (en- word)",
      " = owl (en- word)",
      " = the bird"
    ]
  },"6_Definites": {
    "dk": [
      "mælken"
      ,"sandwichen"
      ,"appelsinen"
      ,"tallerkenen"
      ,"kaffen"
      ,"bogen"
      ,"kyllingen"
      ,"barnet"
      ,"ægget"
      ,"frugten"
      ,"saften"
      ,"morgenmaden"
      ,"frokosten"
      ,"osten"
      ,"pastaen"
      ,"vinen"
      ,"fisken"
      ,"sukkeret"
      ,"aviserne"
      ,"dyrene"
      ,"bøgerne"
      ,"kattene"
      ,"frugterne"
      ,"æblerne"
      ,"hestene"
      ,"hundene"
      ,"bjørnene"
      ,"maden"
      ,"øllen"
      ,"jordbæret"
      ,"risene"
      ,"tomaten"
      ,"skildpadderne"
      ,"bøffen"
      ,"suppen"
      ,"saltet"
      ,"vegetarene"
      ,"svinekødet"
      ,"olien"
      ,"citronen"
      ,"måltidet"
      ,"teen"
      ,"kødet"
      ,"børnene"
      ,"appelsinerne"
      ,"aftensmaden"
      ,"fluglene"
      ,"dyret"
      ,"kagen"
      ,"vegetaren"
      ,"elefanterne"
      ,"tellerknerne"
      ,"sandwichene"
      ,"anden"
      ,"skildpadden"
      ,"elefanten"
      ,"hesten"
      ,"krabben"
      ,"kartoflen"
      ,"musen"
      ,"øllene"
      ,"edderkoppen"
      ,"bjørnen"
    ],
    "en": [
      "the milk (en- word)"
      ,"the sandwich (en- word)"
      ,"the apple (en- word)"
      ,"the plate (en- word)"
      ,"the coffee (en- word)"
      ,"the book (en- word)"
      ,"the chicken (en- word)"
      ,"the child (et- word)"
      ,"the egg (et- word)"
      ,"the fruit (en- word)"
      ,"the juice (en- word)"
      ,"the breakfast (en- word)"
      ,"the lunch (en- word)"
      ,"the cheese (en- word)"
      ,"the pasta (en- word)"
      ,"the wine (en- word)"
      ,"the fish (en- word)"
      ,"the sugar (et- word)"
      ,"the newspapers"
      ,"the animals"
      ,"the books"
      ,"the cats"
      ,"the fruits"
      ,"the apples"
      ,"the horses"
      ,"the dogs"
      ,"the bears"
      ,"the food (en- word)"
      ,"the beer (en- word)"
      ,"the strawberry (et- word)"
      ,"the rice"
      ,"the tomato (en- word)"
      ,"the turtles"
      ,"the steak (en- word)"
      ,"the soup (en- word)"
      ,"the salt (et- word)"
      ,"the vegetarians"
      ,"the pork (et- word)"
      ,"the oil (en- word)"
      ,"the lemon (en- word)"
      ,"the meal (et- word)"
      ,"the tea (en- word)"
      ,"the meat (et- word)"
      ,"the children"
      ,"the oranges"
      ,"the dinner (en- word)"
      ,"the birds"
      ,"the animal (et- word)"
      ,"the cake (en- word)"
      ,"the vegetarian (en- word)"
      ,"the elephants"
      ,"the plates"
      ,"the sandwiches"
      ,"the duck (en- word)"
      ,"the turtle (en- word)"
      ,"the elephant (en- word)"
      ,"the horse (en- word)"
      ,"the crab (en- word)"
      ,"the potato (en- word)"
      ,"the mouse (en- word)"
      ,"the beers (en- word)"
      ,"the spider (en- word)"
      ,"the bear (en- word)"
    ]
  },"7_Plurals": {
    "dk": [
      "mig",
      "dig",
      "ham",
      "hende",
      "dem"
    ],
    "en": [
      " = me",
      " = you",
      " = him",
      " = her",
      " = them"
    ]
  },"8_Genitive_Case": {
    "dk": [],
    "en": [
      "\n",
      "\n"
    ]
  },"9_Possessive_Pronouns": {
    "dk": [
      "heste",
      "hunde",
      "katte",
      "ænder",
      "bøger",
      "aviser"
    ],
    "en": [
      " = horses",
      " = dogs",
      " = cats",
      " = ducks",
      " = books",
      " = newspapers"
    ]
  },"10_Objective_Pronouns": {
    "dk": [
      "a man",
      "the man",
      "water",
      "an apple",
      "the apple",
      "pige",
      "mand",
      "dreng",
      "kvinde",
      "en",
      "jeg",
      "er = ",
      "du ",
      "æble",
      "hun",
      "han",
      "spiser",
      "et",
      "manden",
      "kvinden",
      "og",
      "vand ",
      "vandet",
      "brød",
      "brødet",
      "æblet "
    ],
    "en": [
      " (",
      ", common gender) adds -en and becomes ",
      " (",
      ")",
      " (",
      ", neuter gender) adds -et and becomes ",
      ".",
      " (",
      ", neuter gender) becomes ",
      " (",
      ").",
      " = girl (en- word)",
      " = man (en-word)",
      " = boy (en- word)",
      " = woman (en- word)",
      " = a/an/one",
      " = I",
      "am/is/are",
      "= you (sg.)",
      " = apple (et- word)",
      " = she",
      " = he",
      " = eat, eats, am/is/are eating",
      " = a/an/one",
      " = the man",
      " = the woman",
      " = and",
      "= water (et- word)",
      " = the water",
      " = bread (et- word)",
      " = the bread",
      "= the apple",
      "drikker = drink, drinks, am/is/are drinking"
    ]
  },"11_Clothing": {
    "dk": [
      "går",
      "løber",
      "ser",
      "skriver",
      "sover",
      "svømmer",
      "rører",
      "koger",
      "laver",
      "synger",
      "gerne have",
      "betaler",
      "kan godt lide",
      "leger",
      "spiller",
      "tager",
      "tager afsted",
      "bruger",
      "elsker",
      "regner",
      "fortæller",
      "om",
      "arbejder",
      "finder",
      "hører",
      "lytter",
      "ved",
      "til",
      "behøver",
      "får",
      "kender",
      "designer",
      "viser",
      "tøtter"
    ],
    "en": [
      " = walk/walks, am/is/are walking",
      " = run/runs, am/is/are running",
      " = see/sees, am/is/are seeing",
      " = write/writes, am/is/are writing",
      " = sleep/sleeps, am/is/are sleeping",
      " = swim/swims, am/is/are swimming",
      " = touch/touches, am/is/are touching",
      " = boil/boils",
      " = make/makes",
      " = sing/sings",
      " = like/want/wants to have",
      " = pay/pays",
      " = like/likes",
      " = play/plays (playing e.g. children playing together)",
      " = play/plays (a game with rules e.g football/cars)",
      " = take/takes",
      " = leave/leaves, am/is/are leaving",
      " = use/uses",
      " = love/loves",
      " = rain/rains, raining",
      " = tell/tells, telling",
      " = about",
      " = work/words, working",
      " = find/finds",
      " = hear/hears",
      " = listen/listens, listening",
      " = know/knows (a fact)",
      " = to",
      " = need/needs",
      " = get/gets",
      " = know/knows (someone/someplace)",
      " = design/designs",
      " = show/shows",
      "s",
      " = support/supports"
    ]
  },"12_VerbsPresent_1": {
    "dk": [
      "har",
      "på = on",
      "har på",
      "frakke",
      "nederdel",
      "nederdelen",
      "nederdele",
      "kjole",
      "kjoler",
      "sko",
      "en jakke",
      "jakken",
      "skjorten",
      "kjorterne",
      "bukser",
      "bukserne",
      "strømpe",
      "strømper",
      "hat",
      "hattene",
      "jakkesæt",
      "jakkesættet",
      "tøj",
      "tøjet"
    ],
    "en": [
      " = have/has",
      " = wear/wears, am/is/are wearing",
      " = coat",
      " = skirt",
      " = the skirt",
      " = skirts",
      " = dress",
      " = dresses",
      " = shoe",
      " = a jacket",
      " = the jacket",
      " = the shirt",
      "s",
      " = the shirts",
      " = pants/trousers",
      " = the pants/trousers",
      " = sock",
      " = socks",
      " = hat",
      " = the hats",
      " = suit",
      " = the suit",
      " = clothes",
      " = the clothes"
    ]
  },"13_Colors": {
    "dk": [
      "blå",
      "grønt",
      "gult",
      "gule",
      "hvid",
      "hvide",
      "rød",
      "røde",
      "sort"
    ],
    "en": [
      " = blue",
      " = green",
      " = yellow",
      " = yellow (definite noun, or plural)",
      " = white",
      " = white (plural)",
      " = red",
      " = red (plural)",
      " = black"
    ]
  },"14_Questions": {
    "dk": [
      "at",
      "fordi",
      "eller",
      "om",
      "hvis",
      "men",
      "når",
      "mens"
    ],
    "en": [
      " = that",
      " = because",
      " = or",
      " = if",
      " = if",
      " = but",
      " = when",
      " = while/when"
    ]
  },"15_Prepositions_1": {
    "dk": [
      "fra",
      "i",
      "ved = ",
      "rører ved",
      "med",
      "uden",
      "til",
      "om",
      "af",
      "bag",
      "efter",
      "under",
      "omkring",
      "som",
      "tilbage",
      "nær ved",
      "før",
      "for",
      "mellem",
      "på"
    ],
    "en": [
      " = from",
      " = in",
      "next to",
      " = touch/touches",
      " = with",
      " = without",
      " = to",
      " = about",
      " = off",
      " = behind",
      " = after",
      " = under",
      " = around",
      " = like/what",
      " = back",
      " = close/near to",
      " = until",
      " = for",
      " = between",
      " = on"
    ]
  },"16_Conjunctions": {
    "dk": [
      "hvad ",
      "hvor",
      "hvordan",
      "hvem",
      "hvis",
      "hvorfor",
      "hvilke",
      "hvornår",
      "et spørgsmål",
      "spørgsmålene",
      "et",
      "svar",
      "svaret",
      "svarene"
    ],
    "en": [
      "= what",
      " = where",
      " = how",
      " = who",
      " = whose",
      " = why",
      " = which",
      " = when",
      " = a question",
      " = the questions",
      " ",
      " = an answer",
      " = the answer",
      " = the answers"
    ]
  },"17_Time": {
    "dk": [
      "morgen",
      "formiddagen",
      "formiddagene",
      "eftermiddag",
      "eftermiddagen",
      "i dag",
      "i aften",
      "i morgen",
      "tid",
      "nat",
      "mandag",
      "tirsdage",
      "fredag",
      "fredagen",
      "hverdag",
      "hverdage",
      "hverdagene",
      "kalender",
      "lørdag",
      "søndag",
      "om søndagen",
      "weekend",
      "weekenden",
      "alder",
      "lderen",
      "aldrene",
      "en time",
      "en uge",
      "ugen",
      "en måned",
      "et år",
      "året",
      "dato",
      "datoen",
      "januar",
      "februar",
      "marts",
      "april",
      "maj",
      "juni",
      "en sæson",
      "sæsonen",
      "sæsonerne",
      "juli",
      "august",
      "september",
      "oktober",
      "november",
      "december",
      "et minut",
      "et århundred",
      "en periode",
      "perioden",
      "perioderne",
      "vinter",
      "vinteren",
      "forår",
      "foråret",
      "sommer",
      "sommeren",
      "efteråret",
      "fødsel",
      "fødslen",
      "fødslerne",
      "generation",
      "generationen",
      "et marked",
      "markedet",
      "fest",
      "festen",
      "en scene",
      "scenen",
      "et øjeblik",
      "øjeblikket",
      "i øjeblikket",
      "midnat",
      "et sekund",
      "sekunder",
      "et årti",
      "årtier",
      "en smule",
      "middag",
      "indtil"
    ],
    "en": [
      " = morning",
      " = the morning",
      " = the mornings",
      " = afternoon",
      " = the afternoon",
      " = today",
      " = tonight",
      " = tomorrow",
      " = time",
      " = night",
      " = Monday",
      "tirsdag = Tuesday",
      " = Tuesdays",
      "onsdag = Wednesday",
      "torsdag = Thursday",
      "torsdage = Thursdays",
      " = Friday",
      " = the Friday",
      " = weekday",
      " = weekdays",
      " = the weekdays",
      " = calendar",
      " = Saturday",
      " = Sunday",
      " = on Sundays",
      " = weekend",
      " = the weekend",
      " = age",
      "a",
      " = the age",
      " = the ages",
      " = an hour",
      " = a week",
      " = the week",
      " = a month",
      " = a year",
      " = the year",
      " = date",
      " = the date",
      " = January",
      " = February",
      " = March",
      " = April",
      " = May",
      " = June",
      " = a season",
      " = the season",
      " = the seasons",
      " = July",
      " = August",
      " = September",
      " = October",
      " = November",
      " = December",
      " = a minute",
      " = a century",
      " = a period",
      " = the period",
      " = the periods",
      " = Winter",
      " = the Winter",
      " = Spring",
      " = the Spring",
      " = Summer",
      " = the Summer",
      " = the Fall/Autumn",
      " = birth",
      " = the birth",
      " = the births",
      " = generation",
      " = the generation",
      " = a market",
      " = the market/fair",
      " = party",
      " = the party",
      " = a stage/scene",
      " = the stage",
      " = a moment",
      " = the moment",
      " = currently",
      " = midnight",
      " = a second",
      " = seconds",
      " = a decade",
      " = decades",
      " = a bit",
      " = noon",
      " = until"
    ]
  },"18_Family": {
    "dk": [
      "forældre",
      "forældrene",
      "far",
      "faren",
      "mor",
      "moren",
      "bror",
      "søster",
      "søn",
      "sønner",
      "sønnerne",
      "datteren",
      "døtre",
      "døtrene",
      "familie",
      "familien",
      "mand",
      "kone",
      "koner",
      "onkel",
      "onkler",
      "tante",
      "tanter",
      "søskende",
      "et ægteskab",
      "ægteskaberne",
      "bedstefar",
      "bedstefædre",
      "bedstefaren",
      "bedstemor",
      "bedstemødre",
      "gæst",
      "gæsten",
      "bamse",
      "bamsen",
      "legetøj",
      "en leg",
      "et navn"
    ],
    "en": [
      " = parents",
      " = the parents",
      " = father",
      " = the father",
      " = mother",
      " = the mother",
      " = brother",
      " = sister",
      " = son",
      " = sons",
      " = the sons",
      " = the daughter",
      " = daughters",
      " = the daughters",
      " = family",
      " = the family",
      " = husband",
      " = wife",
      " = wives",
      " = uncle",
      " = uncles",
      " = aunt",
      " = aunts",
      " = siblings",
      " = a marriage",
      " = the marriages",
      " = grandfather",
      " = grandfathers",
      " = the grandfather",
      " = grandmother",
      " = grandmothers",
      " = guest",
      " = the guest",
      " = the guests",
      " = teddy bear",
      " = the teddy bear",
      " = toy",
      " = a game",
      " = a name"
    ]
  },"19_Occupation": {
    "dk": [
      "der",
      "for",
      "hen til",
      "meget",
      "mere",
      "nu",
      "så",
      "aldrig",
      "altid",
      "derefter",
      "henne",
      "her",
      "også",
      "ret",
      "bare",
      "endda",
      "engang",
      "ikke engang",
      "godt",
      "imidlertid",
      "kun",
      "selv",
      "stadig",
      "allerede",
      "endnu",
      "endnu ikke",
      "igen",
      "lidt",
      "for lidt",
      "nogensinde",
      "mindst",
      "i det mindste",
      "væk",
      "virkelig",
      "ellers",
      "i øjeblikket",
      "langt",
      "længe",
      "time",
      "sædvanligvis",
      "senere",
      "snart",
      "tilstrækkeligt",
      "endelig",
      "for",
      "generelt",
      "især",
      "mens",
      "næsten",
      "nemt",
      "om",
      "sent",
      "sommetider",
      "tidligt",
      "fuldstændigt",
      "inde",
      "muligvis",
      "omtrent",
      "præcis",
      "præcist",
      "tydeligt",
      "ude",
      "lige meget = ",
      "lige så meget som",
      "bestemt",
      "nødvendigvis",
      "hverken",
      "normalt",
      "perfekt",
      "personligt",
      "langsomt",
      "sammen"
    ],
    "en": [
      " = there",
      " = too",
      " = to",
      " = very",
      " = more",
      " = now",
      " = so",
      " = never",
      " = always",
      " = then",
      " = at",
      " = here",
      " = too/also",
      " = pretty, very",
      " = just",
      " = even",
      " = even/once",
      " = not even",
      " = well",
      " = however",
      " = only",
      " = even",
      " = still",
      " = already",
      " = yet/even",
      " = not yet",
      " = again",
      " = a bit",
      " = too little?",
      " = ever",
      " = least",
      " = at least",
      " = away",
      " = really",
      " = else",
      " = currently/at the moment",
      " = far",
      " = long (",
      "), long a time",
      " = usually",
      " = later",
      " = soon",
      " = enough",
      " = finally",
      " = too",
      " = generally",
      " = especially",
      " = while",
      " = almost",
      " = easily",
      " = during/in",
      " = late",
      " = sometimes",
      " = early/soon",
      " = completely",
      " = inside",
      " = possibly",
      " = approximately",
      " = exactly",
      " = exactly",
      " = clearly",
      " = out/outside",
      "it does not matter",
      " = as much as",
      " = definitely",
      " = necessarily",
      " = neither",
      " = normally",
      " = perfect/perfectly",
      " = personal",
      " = slowly",
      " = together"
    ]
  },"20_Adjectives_1": {
    "dk": [
      "studerende",
      "doktor",
      "doktorer",
      "en forfatter",
      "forfattere",
      "en model",
      "modellen",
      "modeller",
      "personalet",
      "et job",
      "arbejde",
      "arbejdet",
      "en advokat",
      "advokaten",
      "advokaterne",
      "direktør",
      "direktøren",
      "kunstner",
      "kunstneren",
      "ninjaer",
      "ninjaen",
      "ninjaerne",
      "politi",
      "en sekretær",
      "sekretæren",
      "arbejder",
      "arbejderne",
      "karriere",
      "betjent",
      "en betjent",
      "en borgmester",
      "dommer",
      "en dommer",
      "dommere",
      "professionel",
      "professionelle",
      "skuespillere",
      "soldat",
      "soldater",
      "soldaterne",
      "vagt",
      "en vagt",
      "arkitekt",
      "chef",
      "chefen",
      "chefer",
      "erhverv",
      "erhvervet",
      "en ingeniør",
      "ingeniøren",
      "kok",
      "kokke",
      "landmand",
      "landmænd",
      "servitrice",
      "tjener",
      "tjeneren"
    ],
    "en": [
      " = student",
      " = doctor",
      " = doctors",
      " = an author",
      " = authors",
      " = a model",
      " = the model",
      " = models",
      " = the staff",
      " = a job",
      " = work/job",
      " = the work/job",
      " = a lawyer",
      " = the lawyer",
      " = the lawyers",
      " = manager/director",
      " = the manager/director",
      " = artist",
      " = the artist",
      " = ninjas",
      " = the ninja",
      " = the ninjas",
      " = police",
      " = a secretary",
      " = the secretary",
      " = worker",
      " = the workers",
      " = career",
      " = police officer",
      " = a police officer",
      " = a mayor",
      " = judge/referee",
      " = a judge/referee",
      " = judges/referees",
      " = professional",
      " = professionals",
      " = actors/actresses",
      "skuespilleren = the actor/actress",
      " = soldier",
      " = soldiers",
      " = the soldiers",
      " = guard",
      " = a guard",
      " = architect",
      " = boss",
      " = the boss/manager",
      " = bosses",
      " = profession",
      " = the profession",
      " = an engineer",
      " = the engineer",
      " = cook/chef",
      " = cooks/chefs",
      " = farmer",
      " = farmers",
      " = waitress",
      " = waiter/servant",
      " = the waiter/servant"
    ]
  },"21_VerbsPresent_2": {
    "dk": [
      "generel",
      "common singular",
      "generelle",
      "plural or definite",
      "lille",
      "common singular",
      "næste",
      "common singular",
      "rigtig",
      "common singular",
      "rigtigt",
      "neuter singular",
      "rigtige",
      "plural or definite",
      "samme",
      "plural or definite",
      "små",
      "plural or definite",
      "tosproget",
      "common singular",
      "tosprogede",
      "plural or definite",
      "træt",
      "neuter singular",
      "trætte",
      "plural or definite",
      "åben",
      "common singular",
      "eget",
      "neuter singular",
      "plural or definite",
      "fantastiske",
      "lokal",
      "common singular",
      "lokalt",
      "neuter singular",
      "plural or definite",
      "personlig",
      "common singular",
      "plural or definite",
      "private",
      "specielt",
      "neuter singular",
      "plural or definite",
      "stor",
      "stort",
      "store",
      "plural or definite",
      "anderledes",
      "beskidt",
      "neuter singular",
      "beskidte",
      "plural or definite",
      "dansk",
      "common singular",
      "danske",
      "plural or definite",
      "lovlig",
      "common singular",
      "lovligt",
      "neuter singular",
      "plural or definite",
      "menneskelig",
      "common",
      "singular",
      "neuter singular",
      "menneskelige",
      "plural",
      "common singular",
      "nylige",
      "plural or definite",
      "ren",
      "common singular",
      "rent",
      "plural or definite",
      "venstre",
      "fremtidige",
      "levende",
      "mulig",
      "common singular",
      "muligt",
      "neuter singular",
      "mulige",
      "plural or definite",
      "populært",
      "neuter singular",
      "plural or definite",
      "common singular",
      "neuter singular",
      "tilgængelige",
      "plural or definite",
      "common singular",
      "vigtigt",
      "neuter singular",
      "vigtige",
      "plural or definite",
      "ansvarlig",
      "singular common",
      "ansvarligt",
      "singular neuter",
      "singular neuter",
      "hel",
      "singular common",
      "helt",
      "neuter singular",
      "hele",
      "plural or definite",
      "militær",
      "singular common",
      "plural or definite",
      "nødvendig",
      "common singular",
      "nødvendigt",
      "neuter singular",
      "plural or definite",
      "officiel",
      "common singular",
      "officielt",
      "neuter singular",
      "officielle",
      "plural or definite",
      "uafhængigt",
      "neuter singular",
      "uafhængige",
      "plural or definite",
      "moderne",
      "plural or definite",
      "normal",
      "common singular",
      "normalt",
      "neuter singular",
      "normale",
      "plural or definite",
      "common singular",
      "onde",
      "plural or definite",
      "perfekt",
      "neuter singular",
      "perfekte",
      "plural or definite",
      "positiv",
      "common singular",
      "neuter singular",
      "positive",
      "plural or definite",
      "smuk",
      "common singular",
      "neuter singular",
      "smukke",
      "plural or definite",
      "forkert",
      "neuter singular",
      "forkerte",
      "plural or definite",
      "historisk",
      "common singular",
      "historiske",
      "plural or definite",
      "interessant",
      "neuter singular",
      "interessante",
      "plural or definite",
      "kulturel",
      "common singular",
      "kulturelt",
      "neuter singular",
      "kulturelle",
      "plural or definite",
      "religiøs",
      "common singular",
      "religiøst",
      "neuter singular",
      "seriøs",
      "common singular",
      "seriøst",
      "neuter singular",
      "seriøse",
      "plural or definite",
      "traditionel",
      "common singular",
      "traditionelle",
      "plural or definite",
      "i live",
      "berømt",
      "neuter singular",
      "berømte",
      "plural or definite",
      "dyr",
      "common singular",
      "dyrt",
      "neuter singular",
      "effektiv",
      "common singular",
      "effektive",
      "plural or definite",
      "negativ",
      "common singular",
      "negativt",
      "neuter singular",
      "negative",
      "plural or definite",
      "umulig",
      "common singular",
      "umuligt",
      "neuter singular",
      "umulige",
      "plural or definite",
      "underligt",
      "neuter singular",
      "underlige",
      "plural or definite",
      "velkendt",
      "neuter singular",
      "bange",
      "common singular",
      "bekvem",
      "common singular",
      "bekvemt",
      "neuter singular",
      "bekvemme",
      "plural or definite",
      "hyppigt",
      "neuter singular",
      "hyppige",
      "plural or definite",
      "modsatte",
      "praktisk",
      "common singular",
      "praktiske",
      "plural or definite",
      "sjov",
      "common singular",
      "sjovt",
      "neuter singular",
      "sjove",
      "plural or definite",
      "trist",
      "neuter singular",
      "triste",
      "plural or definite",
      "ked af det",
      "common singular",
      "kede af det",
      "plural or definite"
    ],
    "en": [
      " = general (",
      ")",
      " = general (",
      ")",
      " = little (",
      ")",
      " = next (",
      ")",
      " = real (",
      ")",
      " = real (",
      ")",
      " = real (",
      ")",
      " = same (",
      ")",
      " = little (",
      ")",
      " = bilingual (",
      ")",
      " = bilingual (",
      ")",
      " = tired (",
      ")",
      " = tired (",
      ")",
      " = open",
      "egen = own (",
      ")",
      " = own (",
      ")",
      "egne = own (",
      ")",
      " = amazing/fantastic",
      " = local (",
      ")",
      " = local (",
      ")",
      "lokale = local (",
      ")",
      " = personal (",
      ")",
      "personlige = personal (",
      ")",
      " = private",
      " = special (",
      ")",
      "specielle = special (",
      ")",
      " = big (common singular)",
      " = big (neuter singular)",
      " = big (",
      ")",
      " = different",
      " = dirty (",
      ")",
      " = dirty (",
      ")",
      " = Danish (",
      ")",
      " = Danish (",
      ")",
      " = legal (",
      ")",
      " = legal (",
      ")",
      "lovlige = legal (",
      ")",
      " = human (",
      " ",
      ")",
      "menneskeligt = human (",
      ")",
      " = human (",
      ")",
      "nylig = recent (",
      ")",
      " = recent (",
      ")",
      " = clean (",
      ")",
      " = clean (",
      ")",
      " = left",
      " = future",
      " = living",
      " = possible (",
      ")",
      " = possible (",
      ")",
      " = possible (",
      ")",
      " = popular (",
      ")",
      "populære = popular (",
      ")",
      "tilgængelig = available (",
      ")",
      "tilgængeligt = available (",
      ")",
      " = available (",
      ")",
      "vigtig = important (",
      ")",
      " = important (",
      ")",
      " = important (",
      ")",
      " = responsible (",
      ")",
      " = responsible (",
      ")",
      "endeligt = final (",
      ")",
      " = whole (",
      ")",
      " = whole/all (",
      ")",
      " = whole/all (",
      ")",
      " = military (",
      ")",
      "militære = military (",
      ")",
      " = necessary (",
      ")",
      " = necessary (",
      ")",
      "nødvendige = necessary (",
      ")",
      " = official (",
      ")",
      " = official (",
      ")",
      " = official (",
      ")",
      " = independent (",
      ")",
      " = independent (",
      ")",
      "fremragende = excellent/fantastic",
      " = modern (",
      ")",
      " = normal (",
      ")",
      " = normal (",
      ")",
      " = normal (",
      ")",
      "ond = evil (",
      ")",
      " = evil/evil ones (",
      ")",
      " = perfect (",
      ")",
      " = perfect (",
      ")",
      " = positive (",
      ")",
      "positivt = positive (",
      ")",
      " = positive (",
      ")",
      " = beautiful (",
      ")",
      "smukt = beautiful (",
      ")",
      " = beautiful (",
      ")",
      " = wrong (",
      ")",
      " = wrong (",
      ")",
      " = historical (",
      ")",
      " = historical (",
      ")",
      " = interesting (",
      ")",
      " = interesting (",
      ")",
      " = cultural (",
      ")",
      " = cultural (",
      ")",
      " = cultural (",
      ")",
      " = religious (",
      ")",
      " = religious (",
      ")",
      " = serious (",
      ")",
      " = serious (",
      ")",
      " = serious (",
      ")",
      " = traditional (",
      ")",
      " = traditional (",
      ")",
      " = alive",
      " = famous (",
      ")",
      " = famous (",
      ")",
      " = expensive (",
      ")",
      " = expensive (",
      ")",
      " = effective (",
      ")",
      " = effective (",
      ")",
      " = negative (",
      ")",
      " = negative (",
      ")",
      " = negative (",
      ")",
      " = impossible (",
      ")",
      " = impossible (",
      ")",
      " = impossible (",
      ")",
      " = strange (",
      ")",
      " = strange (",
      ")",
      " = familiar (",
      ")",
      " = afraid/scared (",
      ")",
      " = convenient (",
      ")",
      " = convenient (",
      ")",
      " = convenient/confartable (",
      ")",
      " = frequent (",
      ")",
      " = frequent (",
      ")",
      " = opposite",
      " = convenient/practical (",
      ")",
      " = convenient/practical (",
      ")",
      " = fun/funny (",
      ")",
      " = fun/funny (",
      ")",
      " = fun/funny (",
      ")",
      " = sad (",
      ")",
      " = sad (",
      ")",
      " = sorry/sad (",
      ")",
      " = sorry/sad (",
      ")"
    ]
  },"22_Adverbs": {
    "dk": [
      "åbner",
      "ændrer",
      "ændrer på",
      "gemmer sig",
      "kalder på",
      "redder",
      "ringer",
      "ringer",
      "til",
      "tænker",
      "bor",
      "giver",
      "kigger",
      "kommer",
      "lever",
      "studerer",
      "tilbyder",
      "inkluderer",
      "præsenterer",
      "prøver",
      "spørger",
      "taler",
      "underskriver",
      "afmærker",
      "føler ",
      "husker",
      "ønsker",
      "står",
      "stopper",
      "synes",
      "håber",
      "håber på det",
      "opdrager",
      "rækker",
      "søger",
      "svigter",
      "tror",
      "danser",
      "følger",
      "overvejer",
      "returnerer",
      "takker",
      "vender tilbage",
      "begynder",
      "hviler",
      "slutter",
      "stoler på",
      "svarer"
    ],
    "en": [
      " = open/opens",
      " = change/changes/changing",
      " = alter/alters/altering",
      " = hide/hides/hiding",
      " = call/calls/calling for",
      " = save/saves/saving, rescue/rescues/rescuing",
      " = call/calls/rings",
      " ",
      " = call/calls to",
      " = think/thinks/thinking",
      " = live/lives/living (in a house)",
      " = give/gives/giving",
      " = look/looks/looking",
      " = come/comes/coming",
      " = live/lives, am/is/are alive",
      " = study/studies/studying",
      " = offer/offers/offering",
      " = include/includes/including",
      " = present/presents/presenting, introduce/introduces/introducing",
      " = try/tries/trying",
      " = ask/asks/asking",
      " = speak/speaks/speaking",
      " = sign/signs/signing",
      " = mark/marks/marking",
      "= touch/touches, feel/feels",
      " = remember/remembers",
      " = wish/wishes, want/wants",
      " = stand/stands/standing, written (on the page)",
      " = stop/stops/stopping",
      " = think/thinks/thinking (an opinion), like/likes",
      " = hope/hopes",
      " = hope/hopes so",
      " = raise/raises/raising",
      " = hand/hands/handing",
      " = look/looks/looking, search/searches/searching",
      " = fail, let down",
      " = believe/believes, do/does think, think/thinks",
      " = dance/dances/dancing",
      " = follow/follows/folllowing",
      " = consider/considers/considering",
      " = return/returns",
      " = thank/thanks",
      " = returning",
      " = start/starts, begin/begins/beginning",
      " = rest/rests/resting",
      " = end/ends/ending",
      " = trust/trusts",
      " = answer/answers/answering"
    ]
  }
}
df = arrs_to_cols(i)
df.to_csv("../data/danish_parsed.csv")
