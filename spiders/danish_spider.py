import scrapy

# execute: scrapy crawl danish -O danish.json

class QuotesSpider(scrapy.Spider):
  name = "danish"
  start_urls = [
    'http://duolingo.fandom.com/wiki/Danish_Skill:Basics_1'
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Basics_2"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Phrases"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Food"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Animals"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Definites"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Plurals"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Genitive_Case"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Possessive_Pronouns"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Objective_Pronouns"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Clothing"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Present_1"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Colors"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Questions"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Prepositions_1"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Conjunctions"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Time"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Family"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Occupation"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Adjectives_1"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Present_2"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Adverbs"
  ]
  '''
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Places?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Objects?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Animals_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:People?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Determiners?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Prepositions_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Travel?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Numbers?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Past_1?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Infinitive_1?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Education?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Present_3?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Abstract_Objects_1?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Past_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Adjectives_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Present_Perfect?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Danish_Food?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Relative_Pronouns?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Indefinite_Pronouns?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Infinitive_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Medical?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Modality?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Past_Perfect?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Abstract_Objects_2?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Nature?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Progress.?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Reflexive_Pronouns?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Sports?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Common_Nouns?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Passive_Present?action=edit&amp;redlink=1"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Arts?action=edit&amp;redlink=1"
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Communication?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Politeness?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Present_Participle?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Imperative?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Politics?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Future?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Passive_Past?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Business?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Kitchen?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Attributes?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Future_Perfect?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Science?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Events?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Verbs:Conditional_Perfect?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Spiritual?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Danish_Culture?action=edit&amp;redlink=1
    ,"https://duolingo.fandom.com/wiki/Danish_Skill:Once_Upon_a_Time?action=edit&amp;redlink=1
  '''
  def parse(self, response):
    for quote in response.css('div.mw-parser-output'):
      yield {
        'dk': quote.css('ul li i::text').getall(),
        'en': quote.css('ul li::text').getall()
      }