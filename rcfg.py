#!/usr/bin/env python
# coding: utf-8

version = '0.0.1'
author = "Emanuele 'Lele' Calo'\nEmail:<lele [at] quasinormale [dot] it>\nGithub/Twitter: eldios"

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
parser.add_argument('-o','--output', action='store',
                    help='Output file used to store the resulting list of random CFs')
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
    def __init__(self,name,id):
        self.name = name
        self.id = id

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
            City('Alba Adriatica','A125'),
            City('Alba','A124'),
            City('Albagiara','A126'),
            City('Albairate','A127'),
            City('Albanella','A128'),
            City('Albano Laziale','A132'),
            City('Albano Sant\'Alessandro','A129'),
            City('Albano Vercellese','A130'),
            City('Albano di Lucania','A131'),
            City('Albaredo Arnaboldi','A134'),
            City('Albaredo d\'Adige','A137'),
            City('Albaredo per San Marco','A135'),
            City('Albareto','A138'),
            City('Albaretto della Torre','A139'),
            City('Albavilla','A143'),
            City('Aulla','A496'),
            City('Baldissero d\'Alba','A589'),
            City('Battipaglia','A717'),
            City('Bellinzago Novarese','A752'),
            City('Boara Pisani','A906'),
            City('Bologna','A944'),
            City('Bolognano','A945'),
            City('Bolzano Novarese','A953'),
            City('Borgo San Giacomo','B035'),
            City('Bressanone','B160'),
            City('Briga Novarese','B176'),
            City('Canicattini Bagni','B603'),
            City('Capralba','B686'),
            City('Caprarica di Lecce','B690'),
            City('Casaleggio Novara','B883'),
            City('Casanova Elvo','B928'),
            City('Castel Guelfo di Bologna','C121'),
            City('Castellazzo Novarese','C149'),
            City('Castellinaldo d\'Alba','C173'),
            City('Castri di Lecce','C334'),
            City('Ceresole Alba','C504'),
            City('Colloredo di Monte Albano','C885'),
            City('Como','C933'),
            City('Cornalba','D016'),
            City('Corneliano d\'Alba','D022'),
            City('Crotone','D122'),
            City('Desio','D286'),
            City('Diano d\'Alba','D291'),
            City('Falconara Albanese','D473'),
            City('Fara Novarese','D492'),
            City('Foggia','D643'),
            City('Garbagna Novarese','D911'),
            City('Genova','D969'),
            City('Ghisalba','E006'),
            City('Giulianova','E058'),
            City('Giussano','E063'),
            City('Gorgonzola','E094'),
            City('Grado','E125'),
            City('Gradoli','E126'),
            City('Grosseto','E202'),
            City('Lecce nei Marsi','E505'),
            City('Lecce','E506'),
            City('Livorno Ferraris','E626'),
            City('Livorno','E625'),
            City('Lucca','E715'),
            City('Mariano Comense','E951'),
            City('Mariano del Friuli','E952'),
            City('Marianopoli','E953'),
            City('Milano','F205'),
            City('Minervino di Lecce','F221'),
            City('Mombello di Torino','F315'),
            City('Monforte d\'Alba','F358'),
            City('Montalbano Elicona','F400'),
            City('Montalbano Jonico','F399'),
            City('Monte San Giacomo','F618'),
            City('Monteroni di Lecce','F604'),
            City('Monticello d\'Alba','F669'),
            City('Morro d\'Alba','F745'),
            City('Muro Leccese','F816'),
            City('Novalesa','F948'),
            City('Novara','F952'),
            City('Orciano Pisano','G090'),
            City('Palermo','G273'),
            City('Pescara','G482'),
            City('Piana degli Albanesi','G543'),
            City('Pieve San Giacomo','G651'),
            City('Piobesi d\'Alba','G683'),
            City('Pisa','G702'),
            City('Pisano','G703'),
            City('Rivalba','H333'),
            City('Rivalta di Torino','H335'),
            City('Roma','H501'),
            City('Roseto Capo Spulico','H572'),
            City('Roseto Valfortore','H568'),
            City('Roseto degli Abruzzi','F585'),
            City('Sagrado','H665'),
            City('San Cesario di Lecce','H793'),
            City('San Cosmo Albanese','H806'),
            City('San Costantino Albanese','H808'),
            City('San Donato di Lecce','H826'),
            City('San Giacomo Filippo','H868'),
            City('San Giacomo Vercellese','B952'),
            City('San Giacomo degli Schiavoni','H867'),
            City('San Giacomo delle Segnate','H870'),
            City('San Giorgio Albanese','H881'),
            City('San Paolo Albanese','B906'),
            City('Sant\'Albano Stura','I210'),
            City('Sant\'Ambrogio di Torino','I258'),
            City('Santa Caterina Albanese','I171'),
            City('Santa Vittoria d\'Alba','I316'),
            City('Sarzana','I449'),
            City('Seregno','I625'),
            City('Serralunga d\'Alba','I646'),
            City('Spezzano Albanese','I895'),
            City('Terralba','L122'),
            City('Torino di Sangro','L218'),
            City('Torino','L219'),
            City('Torralba','L235'),
            City('Tovo San Giacomo','L315'),
            City('Vaccarizzo Albanese','L524'),
            City('Venezia','L736'),
            City('Vezza d\'Alba','L817'),
            City('Vicopisano','L850'),
            City('Viddalba','M259'),
            City('Villalba','L959'),
            City('Villanova Canavese','L982'),
            City('Zibido San Giacomo','M176'),
        ]
        return randchoice(cities)

    def _random_birthdate(self):
        """Generate a random though plausible birth date"""
        today = datetime.date.today()
        maxlifespan = 120 # I know, I'm optimist, but there it goes :)
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
            return "{},{},{},{},{},{}".format(self.codfis,self.firstname,self.lastname,self.birthdate,self.gender,self.placeofbirth.name)
        else:
            return "{}".format(self.codfis)

    def __repr__(self):
        """Convert to string"""
        return str(self)

def output_to_stdout():
    """Output result to STDOUT"""
    if(not args.quiet):
        print("CF,firstname,lastname,birthdate,gender,placeofbirth")
    else:
        print("CF")

    for i in range (args.count):
        print("{}".format(Person()))

def output_to_file(output_file):
    """Output result to FILE"""
    with open(output_file,'w',encoding='UTF8') as f:
        if(not args.quiet):
            f.write("CF,firstname,lastname,birthdate,gender,placeofbirth\n")
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
