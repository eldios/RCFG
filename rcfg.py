#!/usr/bin/env python
# coding: utf-8

version = '0.0.4'
author = """
Emanuele 'Lele' Calo'
Email:<lele [at] quasinormale [dot] it>
Github/Twitter: eldios
"""

from pycodicefiscale import codicefiscale as cf
import datetime
from random import choice as randchoice
from random import randint

import argparse

# script description
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description = '''
Random CodiceFiscale Generator - Generates a list of random fake Italian people along with their CF (Codice Fiscale, italian birth data ID) and output the result as a CSV
''',
    allow_abbrev = False)

# arguments
parser.add_argument('-V','--version', action='version', version="%(prog)s {}\n{}".format(version,author))
parser.add_argument('-d','--debug', action='store_true',
                   help='Enable debugging info')
parser.add_argument('-n','--firstnames', action='append',
                   help='*TODO* File containing a newline separated list of first names. If not specified a list of 50 common Italian first (male/female) names will be used')
parser.add_argument('-l','--lastnames', action='append',
                   help='*TODO* File containing a newline separated list of last names. If not specified a list of 50 common Italian last names will be used')
parser.add_argument('-p','--cities', action='append',
                   help='*TODO* File containing a CSV list of cities (ID,Name,ProvinceCode). If not specified a list of random Italian cities will be used')
parser.add_argument('-o','--output', action='store',
                    help='Output file used to store the resulting list of random CFs')
parser.add_argument('-y','--years', action='store', type=int , default=120,
                   help='Max past number of years to be used during birth date randomization starting from today and going back.')
parser.add_argument('-c','--count', action='store', type=int , default=1,
                   help='How many CF should be generated')
parser.add_argument('-q','--quiet', action='store_true',
                   help='Only output CF without the related Person data')

# argparse magic
args = parser.parse_args()
debug = args.debug

if ( debug ):
    print(args)

class City():
    """City entity used to define Place of Birth"""
    def __init__(self,id,name,province):
        self.id = id
        self.name = name
        self.province = province

    def __str__(self):
        return "{} ({})".format(self.name,self.province)

    def __repr__(self):
        return str(self)

class Person():
    """Person entity used to generate the Codice Fiscale id"""
    def __init__(self):
        self.gender = randchoice(('m','f'))
        self.firstname = self._random_firstname()
        self.lastname = self._random_lastname()
        self.birthdate = self._random_birthdate()
        self.placeofbirth = self._random_placeofbirth()
        self.codfis = self._gen_cf()

    def _random_firstname(self):
        """Pick a random firstname from 50 of the most common Italian male/female firstnames"""
        firstname_list = {
            'f' : (
                'alessandra','alessia','alice','angela','anna','arianna','beatrice','camilla','caterina','chiara','claudia','cristina','debora','elena','eleonora','elisa','erica','erika','federica','francesca','gaia','giada','giorgia','giulia','greta','ilaria','irene','jessica','laura','lisa','lucia','maria','marta','martina','michela','monica','nicole','noemi','paola','roberta','sara','serena','silvia','simona','sofia','stefania','valentina','valeria','vanessa','veronica' ) ,
            'm' : (
                'alberto','alessandro','alessio','alex','andrea','angelo','antonio','christian','claudio','daniele','dario','davide','domenico','edoardo','emanuele','enrico','fabio','federico','fernando','filippo','francesco','gabriele','giacomo','gianluca','giorgio','giovanni','giulio','giuseppe','jacopo','leonardo','lorenzo','luca','luigi','manuel','marco','matteo','mattia','michele','mirko','nicola','nicolò','paolo','pietro','riccardo','roberto','salvatore','simone','stefano','tommaso','valerio','vincenzo' )
        }
        return randchoice(firstname_list[self.gender]).title()

    def _random_lastname(self):
        """Pick a random lastname from 50 of the most common Italian lastnames"""
        lastname_list = (
            'rossi','russo','ferrari','esposito','bianchi','romano','colombo','ricci','marino','greco','bruno','gallo','conti','de luca','mancini','costa','giordano','rizzo','lombardi','moretti','barbieri','fontana','santoro','mariani','rinaldi','caruso','ferrara','galli','martini','leone','longo','gentile','martinelli','vitale','lombardo','serra','coppola','de santis','d\'angelo','marchetti','parisi','villa','conte','ferraro','ferri','fabbri','bianco','calò','marini','grasso','valentini'
        )
        return randchoice(lastname_list).title()

    def _random_placeofbirth(self):
        """Pick a random city from a bunch of random italian cities"""
        cities = [
            City('H333','Rivalba','TO'),
            City('H511','Romano Canavese','TO'),
            City('A130','Albano Vercellese','VC'),
            City('A752','Bellinzago Novarese','NO'),
            City('A953','Bolzano Novarese','NO'),
            City('B176','Briga Novarese','NO'),
            City('C149','Castellazzo Novarese','NO'),
            City('D492','Fara Novarese','NO'),
            City('D911','Garbagna Novarese','NO'),
            City('G703','Pisano','NO'),
            City('H502','Romagnano Sesia','NO'),
            City('A124','Alba','CN'),
            City('A139','Albaretto della Torre','CN'),
            City('A589','Baldissero d\'Alba','CN'),
            City('C173','Castellinaldo d\'Alba','CN'),
            City('C504','Ceresole Alba','CN'),
            City('D022','Corneliano d\'Alba','CN'),
            City('D291','Diano d\'Alba','CN'),
            City('F358','Monforte d\'Alba','CN'),
            City('F669','Monticello d\'Alba','CN'),
            City('G683','Piobesi d\'Alba','CN'),
            City('I210','Sant\'Albano Stura','CN'),
            City('I316','Santa Vittoria d\'Alba','CN'),
            City('I646','Serralunga d\'Alba','CN'),
            City('L817','Vezza d\'Alba','CN'),
            City('M009','Villaromagnano','AL'),
            City('D551','Ferrera di Varese','VA'),
            City('L682','Varese','VA'),
            City('A143','Albavilla','CO'),
            City('E951','Mariano Comense','CO'),
            City('A135','Albaredo per San Marco','SO'),
            City('A127','Albairate','MI'),
            City('A389','Arese','MI'),
            City('F205','Milano','MI'),
            City('A129','Albano Sant\'Alessandro','BG'),
            City('A383','Ardesio','BG'),
            City('E006','Ghisalba','BG'),
            City('H509','Romano di Lombardia','BG'),
            City('D016','Cornalba','BG'),
            City('I433','Sarezzo','BS'),
            City('A134','Albaredo Arnaboldi','PV'),
            City('H505','Romagnese','PV'),
            City('L256','Torre d\'Arese','PV'),
            City('B686','Capralba','CR'),
            City('E356','Isola Dovarese','CR'),
            City('H508','Romanengo','CR'),
            City('B911','Casalromano','MN'),
            City('D286','Desio','MB'),
            City('E063','Giussano','MB'),
            City('H506','Romallo','TN'),
            City('A137','Albaredo d\'Adige','VR'),
            City('H512','Romano d\'Ezzelino','VI'),
            City('A906','Boara Pisani','PD'),
            City('C544','Cervarese Santa Croce','PD'),
            City('C885','Colloredo di Monte Albano','UD'),
            City('H514','Romans d\'Isonzo','GO'),
            City('C302','Castiglione Chiavarese','GE'),
            City('L681','Varese Ligure','SP'),
            City('A138','Albareto','PR'),
            City('A551','Bagnara di Romagna','RA'),
            City('A565','Bagno di Romagna','FC'),
            City('C777','Civitella di Romagna','FC'),
            City('F715','Morciano di Romagna','RN'),
            City('I304','Santarcangelo di Romagna','RN'),
            City('A560','Bagni di Lucca','LU'),
            City('E715','Lucca','LU'),
            City('I142','San Romano in Garfagnana','LU'),
            City('D612','Firenze','FI'),
            City('G090','Orciano Pisano','PI'),
            City('G702','Pisa','PI'),
            City('L850','Vicopisano','PI'),
            City('A390','Arezzo','AR'),
            City('E202','Grosseto','GR'),
            City('F745','Morro d\'Alba','AN'),
            City('A628','Barbarano Romano','VT'),
            City('A704','Bassano Romano','VT'),
            City('D452','Fabrica di Roma','VT'),
            City('F603','Monte Romano','VT'),
            City('G111','Oriolo Romano','VT'),
            City('A132','Albano Laziale','RM'),
            City('A370','Arcinazzo Romano','RM'),
            City('B496','Campagnano di Roma','RM'),
            City('B828','Carpineto Romano','RM'),
            City('C266','Castel San Pietro Romano','RM'),
            City('C543','Cervara di Roma','RM'),
            City('C702','Cineto Romano','RM'),
            City('D561','Fiano Romano','RM'),
            City('D972','Genzano di Roma','RM'),
            City('E813','Magliano Romano','RM'),
            City('F064','Mazzano Romano','RM'),
            City('F692','Montorio Romano','RM'),
            City('G022','Olevano Romano','RM'),
            City('G874','Ponzano Romano','RM'),
            City('H501','Roma','RM'),
            City('I284','Sant\'Angelo Romano','RM'),
            City('I400','San Vito Romano','RM'),
            City('L401','Trevignano Romano','RM'),
            City('M095','Vivaro Romano','RM'),
            City('E057','Giuliano di Roma','FR'),
            City('A125','Alba Adriatica','TE'),
            City('E058','Giulianova','TE'),
            City('H436','Roccaromana','CE'),
            City('A128','Albanella','SA'),
            City('H503','Romagnano al Monte','SA'),
            City('A131','Albano di Lucania','PZ'),
            City('B906','San Paolo Albanese','PZ'),
            City('H808','San Costantino Albanese','PZ'),
            City('F399','Montalbano Jonico','MT'),
            City('D473','Falconara Albanese','CS'),
            City('H806','San Cosmo Albanese','CS'),
            City('H881','San Giorgio Albanese','CS'),
            City('I171','Santa Caterina Albanese','CS'),
            City('I895','Spezzano Albanese','CS'),
            City('L524','Vaccarizzo Albanese','CS'),
            City('G543','Piana degli Albanesi','PA'),
            City('F400','Montalbano Elicona','ME'),
            City('E714','Lucca Sicula','AG'),
            City('L959','Villalba','CL'),
            City('H507','Romana','SS'),
            City('L235','Torralba','SS'),
            City('M259','Viddalba','SS'),
            City('A126','Albagiara','OR'),
            City('L122','Terralba','OR'),
        ]
        return randchoice(cities)

    def _random_birthdate(self):
        """Generate a random though plausible birth date"""
        today = datetime.date.today()
        maxlifespan = args.years # I know, I'm optimist, but there it goes :)
        stime = datetime.date(year = (today.year - maxlifespan), month=1, day=1)
        birthdatetimestamp = randint(stime.toordinal() , today.toordinal())
        return datetime.date.fromordinal(birthdatetimestamp)

    def _gen_cf(self):
        """Generate the Codice Fiscale ID using a 3rd party library"""
        codfis = cf.build(self.lastname, self.firstname, self.birthdate, self.gender, self.placeofbirth.id)
        return codfis

    def __str__(self):
        """Convert to string"""
        if(not args.quiet):
            return "{},{},{},{},{},{},{}".format(self.codfis,self.firstname,self.lastname,self.birthdate,self.gender,self.placeofbirth.name,self.placeofbirth.province)
        else:
            return "{}".format(self.codfis)

    def __repr__(self):
        """Convert to string"""
        return str(self)

def output_to_stdout():
    """Output result to STDOUT"""
    if(not args.quiet):
        print("CF,firstname,lastname,birthdate,gender,placeofbirthname,placeofbirthprovince")
    else:
        print("CF")

    for i in range (args.count):
        print("{}".format(Person()))

def output_to_file(output_file):
    """Output result to FILE"""
    with open(output_file,'w',encoding='UTF8') as f:
        if(not args.quiet):
            f.write("CF,firstname,lastname,birthdate,gender,placeofbirthname,placeofbirthprovince\n")
        else:
            f.write("CF\n")
    
        for i in range (args.count):
            f.write("{}\n".format(Person()))

def __main__():
    """main function"""
    if(not args.output):
        output_to_stdout()
    else:
        output_to_file(args.output)

if __name__ == '__main__':
    __main__()
