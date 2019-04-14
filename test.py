'''import pandas as pd
import numpy as np
import re

data = ["Hi(2000)","Hi(2000)","Hi(2000)","Hi(2000)","Hi(2000)","0000:(hi)"]
print("Sample one: Hi(2000)\n")
df = pd.DataFrame(data = data)
print(df[0].str.extract('([a-zA-Z ]+)', expand=False).str.strip())
print(df[0].str.replace(r'([a-zA-Z ]+)', '').str.strip())

print("Sample two: 0000:(hi hi)")
data1 = ["0000:(hi hi)","0000:(hi hi)","0000:(hi hi)","0000:(hi hi)"]
df1 = pd.DataFrame(data = data1)
print(df1[0].str.extract('([a-zA-Z ]+)', expand=False).str.strip())
print(df1[0].str.replace(r'([a-zA-Z ]+)', '').str.strip())
a=df1[0].str.replace(r'([a-zA-Z ]+)', '').str.strip()
print(a.str.strip(":()"))

data2 = ['-','taxid:7227(Drosophila melanogaster)','taxid:9606(Homo sapiens)',
 'taxid:10090(Mus musculus)','taxid:10116(Rattus norvegicus)',
 'taxid:6239(Caenorhabditis elegans)',
 'taxid:10377(Human herpesvirus 4 strain B95-8)',
 'taxid:82830(Epstein-barr virus strain ag876)',
 'taxid:559292(Saccharomyces cerevisiae S288C)',
 'taxid:10678(Escherichia virus P1)',
 'taxid:85962(Helicobacter pylori 26695)',
 'taxid:882(Desulfovibrio vulgaris str. Hildenborough)',
 'taxid:9823(Sus scrofa)','taxid:224324(Aquifex aeolicus VF5)',
 'taxid:4102(Petunia x hybrida)',
 'taxid:39947(Oryza sativa Japonica Group)','taxid:562(Escherichia coli)',
 'taxid:284812(Schizosaccharomyces pombe 972h-)',
 'taxid:3702(Arabidopsis thaliana)','taxid:7955(Danio rerio)',
 'taxid:83333(Escherichia coli K-12)',
 'taxid:1196325(Pseudomonas putida DOT-T1E)',
 'taxid:44689(Dictyostelium discoideum)','taxid:3120(Ulva pertusa)',
 'taxid:192222(Campylobacter jejuni subsp. jejuni NCTC 11168 = ATCC 700819)',
 'taxid:1111708(Synechocystis sp. PCC 6803 substr. Kazusa)',
 'taxid:243276(Treponema pallidum subsp. pallidum str. Nichols)',
 'taxid:518(Bordetella bronchiseptica)',
 'taxid:170187(Streptococcus pneumoniae TIGR4)','taxid:9913(Bos taurus)',
 'taxid:5147(Sordaria macrospora)','taxid:9031(Gallus gallus)',
 'taxid:302272(Sendai virus (strain Ohita))'
 'taxid:10366(Murid betaherpesvirus 1)','taxid:632(Yersinia pestis)',
 'taxid:4577(Zea mays)',
 'taxid:187420(Methanothermobacter thermautotrophicus str. Delta H)',
 'taxid:32630(synthetic construct)','taxid:6523(Lymnaea stagnalis)',
 'taxid:1085(Rhodospirillum rubrum)',
 'taxid:1833(Rhodococcus erythropolis)','taxid:210(Helicobacter pylori)',
 'taxid:10298(Human alphaherpesvirus 1)',
 'taxid:10335(Human alphaherpesvirus 3)',
 'taxid:177416(Francisella tularensis subsp. tularensis SCHU S4)',
 'taxid:62715(Golovinomyces orontii)',
 'taxid:11142(Murine hepatitis virus strain A59)',
 'taxid:83332(Mycobacterium tuberculosis H37Rv)',
 'taxid:8355(Xenopus laevis)','taxid:11138(Murine hepatitis virus)',
 'taxid:90370(Salmonella enterica subsp. enterica serovar Typhi)',
 'taxid:11103(Hepatitis C virus)','taxid:1773(Mycobacterium tuberculosis)',
 'taxid:271(Thermus aquaticus)',
 'taxid:11705(Human immunodeficiency virus type 1 (WMJ2 ISOLATE))',
 'taxid:1079(Blastochloris viridis)','taxid:9675(Paguma larvata)',
 'taxid:90371(Salmonella enterica subsp. enterica serovar Typhimurium)',
 'taxid:4932(Saccharomyces cerevisiae)','taxid:8022(Oncorhynchus mykiss)',
 'taxid:36329(Plasmodium falciparum 3D7)',
 'taxid:1434(Bacillus thuringiensis serovar berliner)',
 'taxid:224308(Bacillus subtilis subsp. subtilis str. 168)',
 'taxid:246197(Myxococcus xanthus DK 1622)',
 'taxid:100226(Streptomyces coelicolor A3(2))',
 'taxid:1392(Bacillus anthracis)','taxid:9615(Canis lupus familiaris)',
 'taxid:337052(Deltapapillomavirus 4)',
 'taxid:511145(Escherichia coli str. K-12 substr. MG1655)',
 'taxid:630(Yersinia enterocolitica)',
 'taxid:146786(Thermosynechococcus elongatus)',
 'taxid:485(Neisseria gonorrhoeae)','taxid:63363(Aquifex aeolicus)',
 'taxid:3649(Carica papaya)','taxid:9825(Sus scrofa domesticus)',
 'taxid:312017(Tetrahymena thermophila SB210)',
 'taxid:272563(Clostridioides difficile 630)',
 'taxid:573(Klebsiella pneumoniae)',
 'taxid:155864(Escherichia coli O157:H7 str. EDL933)',
 'taxid:220668(Lactobacillus plantarum WCFS1)',
 'taxid:2771(Cyanidium caldarium)',
 'taxid:211586(Shewanella oneidensis MR-1)',
 'taxid:11676(Human immunodeficiency virus 1)',
 'taxid:227321(Aspergillus nidulans FGSC A4)',
 'taxid:1422(Geobacillus stearothermophilus)',
 'taxid:408871(Dengue virus 4 Dominica/814669/1981)',
 'taxid:11246(Bovine orthopneumovirus)',
 'taxid:83334(Escherichia coli O157:H7)','taxid:274(Thermus thermophilus)',
 'taxid:12110(Foot-and-mouth disease virus)',
 'taxid:623(Shigella flexneri)',
 'taxid:243232(Methanocaldococcus jannaschii DSM 2661)',
 'taxid:10360(Human herpesvirus 5 strain AD169)',
 'taxid:1083(Phaeospirillum molischianum)',
 'taxid:381518(Influenza A virus (A/Wilson-Smith/1933(H1N1)))',
 'taxid:10376(Human gammaherpesvirus 4)','taxid:2336(Thermotoga maritima)',
 'taxid:10141(Cavia porcellus)','taxid:9986(Oryctolagus cuniculus)',
 'taxid:28282(Human adenovirus 12)',
 'taxid:272634(Mycoplasma pneumoniae M129)',
 'taxid:341980(Human herpesvirus 3 strain Oka vaccine)',
 'taxid:11927(Human T-cell lymphotrophic virus type 1 (Caribbean isolate))',
 'taxid:10600(Human papillomavirus type 6b)',
 'taxid:10515(Human adenovirus 2)',
 'taxid:10367(Murine cytomegalovirus (strain Smith))',
 'taxid:129875(Human mastadenovirus A)',
 'taxid:70601(Pyrococcus horikoshii OT3)',
 'taxid:119602(Streptococcus dysgalactiae subsp. equisimilis)',
 'taxid:10754(Salmonella virus P22)','taxid:40690(Trematomus bernacchii)',
 'taxid:11033(Semliki Forest virus)','taxid:1525(Moorella thermoacetica)',
 'taxid:186497(Pyrococcus furiosus DSM 3638)',
 'taxid:223283(Pseudomonas syringae pv. tomato str. DC3000)',
 'taxid:868565(Human herpesvirus 8 strain GK18)',
 'taxid:3888(Pisum sativum)',
 'taxid:381513(Influenza A virus (A/Panama/2007/1999(H3N2)))',
 'taxid:10254(Vaccinia virus WR)','taxid:44130(Human rhinovirus B3)',
 'taxid:301447(Streptococcus pyogenes serotype M1)',
 'taxid:2261(Pyrococcus furiosus)','taxid:12131(Rhinovirus B14)',
 'taxid:46015(Autographa californica nucleopolyhedrovirus)',
 'taxid:33708(Murid gammaherpesvirus 4)',
 'taxid:10665(Enterobacteria phage T4)',
 'taxid:169066(Human rhinovirus sp.)',
 'taxid:192952(Methanosarcina mazei Go1)','taxid:11053(Dengue virus 1)',
 'taxid:10359(Human betaherpesvirus 5)',
 'taxid:224325(Archaeoglobus fulgidus DSM 4304)',
 'taxid:1423(Bacillus subtilis)','taxid:8724(Bothrops jararaca)',
 'taxid:5911(Tetrahymena thermophila)',
 'taxid:10579(Human papillomavirus type 8)',
 'taxid:211044(Influenza A virus (A/Puerto Rico/8/1934(H1N1)))',
 'taxid:714(Aggregatibacter actinomycetemcomitans)',
 'taxid:103690(Nostoc sp. PCC 7120)','taxid:8844(Anser anser anser)',
 'taxid:435895(Human herpesvirus 8 type M)',
 'taxid:493803(Merkel cell polyomavirus)','taxid:615(Serratia marcescens)',
 'taxid:266(Paracoccus denitrificans)',
 'taxid:283166(Bartonella henselae str. Houston-1)',
 'taxid:11191(Murine respirovirus)','taxid:5507(Fusarium oxysporum)',
 'taxid:4097(Nicotiana tabacum)',
 'taxid:243365(Chromobacterium violaceum ATCC 12472)',
 'taxid:84600(Sulfolobus sp. NOB8H2)',
 'taxid:11678(Human immunodeficiency virus type 1 BH10)',
 'taxid:295027(Human herpesvirus 5 strain Merlin)',
 'taxid:384509(Influenza A virus (A/tern/Australia/G70C/1975(H11N9)))',
 'taxid:3858(Lathyrus ochrus)','taxid:294(Pseudomonas fluorescens)',
 'taxid:1901(Streptomyces clavuligerus)',
 'taxid:273063(Sulfolobus tokodaii str. 7)',
 'taxid:37296(Human gammaherpesvirus 8)',
 'taxid:235443(Cryptococcus neoformans var. grubii H99)','taxid:10635(-)',
 'taxid:11707(Human immunodeficiency virus type 1 (HXB3 ISOLATE))',
 'taxid:11214(Human parainfluenza virus 2 (strain Toshiba))',
 'taxid:523850(Thermococcus onnurineus NA1)',
 'taxid:284813(Encephalitozoon cuniculi GB-M1)',
 'taxid:10923(Simian rotavirus A/SA11)',
 'taxid:1354920(Xerocomellus chrysenteron)',
 'taxid:300852(Thermus thermophilus HB8)',
 'taxid:10559(Bovine papillomavirus type 1)'
 'taxid:12083(Human poliovirus 2)','taxid:12215(Potato virus A)',
 'taxid:4530(Oryza sativa)','taxid:8631(Laticauda semifasciata)',
 'taxid:11855(Mason-Pfizer monkey virus)',
 'taxid:99287(Salmonella enterica subsp. enterica serovar Typhimurium str. LT2)',
 'taxid:47664(Populus tremula x Populus tremuloides)',
 'taxid:10299(Herpes simplex virus (type 1 / strain 17))',
 'taxid:176299(Agrobacterium fabrum str. C58)',
 'taxid:636(Edwardsiella tarda)','taxid:45219(Guanarito mammarenavirus)',
 'taxid:352472(Dictyostelium discoideum AX4)',
 'taxid:238(Elizabethkingia meningoseptica)',
 'taxid:9103(Meleagris gallopavo)',
 'taxid:1348078(Poecilobdella manillensis)',
 'taxid:1280(Staphylococcus aureus)',
 'taxid:1823(Nocardia otitidiscaviarum)','taxid:6253(Ascaris suum)',
 'taxid:11908(Human T-lymphotropic virus 1)',
 'taxid:472390(Prunus dulcis x Prunus persica)',
 'taxid:227859(SARS coronavirus)','taxid:32046(Synechococcus elongatus)',
 'taxid:3847(Glycine max)','taxid:40674(Mammalia)',
 'taxid:243274(Thermotoga maritima MSB8)',
 'taxid:190486(Xanthomonas axonopodis pv. citri str. 306)',
 'taxid:73044(Streptomyces seoulensis)','taxid:40353(Echis carinatus)',
 'taxid:5811(Toxoplasma gondii)','taxid:6396(Eisenia fetida)',
 'taxid:1168(Nostoc sp. PCC 7119)','taxid:243243(Mycobacterium avium 104)',
 'taxid:7091(Bombyx mori)','taxid:652939(Tobacco rattle virus PpK20)',
 'taxid:337042(Alphapapillomavirus 7)',
 'taxid:12305(Cucumber mosaic virus)',
 'taxid:31944(Corynebacterium sp. U-96)','taxid:11886(Rous sarcoma virus)',
 'taxid:0(-)','taxid:272558(Bacillus halodurans C-125)',
 'taxid:237561(Candida albicans SC5314)','taxid:10407(Hepatitis B virus)',
 'taxid:273057(Sulfolobus solfataricus P2)',
 'taxid:11283(Vesicular stomatitis virus (serotype New Jersey / strain Ogden))',
 'taxid:10029(Cricetulus griseus)',
 'taxid:266834(Sinorhizobium meliloti 1021)',
 'taxid:511(Alcaligenes faecalis)','taxid:11089(Yellow fever virus)',
 'taxid:11060(Dengue virus 2)','taxid:1765(Mycobacterium bovis)',
 'taxid:3562(Spinacia oleracea)','taxid:272951(Rickettsia sibirica 246)',
 'taxid:240269(Paramecium bursaria Chlorella virus AN69C)',
 'taxid:4513(Hordeum vulgare)',
 'taxid:185431(Trypanosoma brucei brucei TREU927)',
 'taxid:145262(Methanothermobacter thermautotrophicus)',
 'taxid:11741(Visna/maedi virus)',
 'taxid:387344(Lactobacillus brevis ATCC 367)',
 'taxid:11636(Reticuloendotheliosis virus)',
 'taxid:47421(Hydrogenophaga pseudoflava)',
 'taxid:5482(Candida tropicalis)','taxid:12069(Coxsackievirus A21)',
 'taxid:45596([Candida] tenuis)',
 'taxid:488537(Clostridium perfringens D str. JGS1721)',
 'taxid:94232(Epinephelus coioides)',
 'taxid:10345(Suid alphaherpesvirus 1)',
 'taxid:382835(Influenza A virus (A/WSN/1933(H1N1)))',
 'taxid:9940(Ovis aries)',
 'taxid:648242(Adeno-associated virus 2 Srivastava/1982)',
 'taxid:208964(Pseudomonas aeruginosa PAO1)',
 'taxid:8618(Dendroaspis angusticeps)','taxid:303(Pseudomonas putida)',
 'taxid:208963(Pseudomonas aeruginosa UCBPP-PA14)',
 'taxid:10036(Mesocricetus auratus)','taxid:12222(Soybean mosaic virus)',
 'taxid:10280(Molluscum contagiosum virus subtype 1)',
 'taxid:29760(Vitis vinifera)']

df2 = pd.DataFrame(data = data2)
a = df2[0].str.extract('([a-zA-Z]+:[^a-zA-Z]+)', expand=False).str.strip() # tax id and code
b = df2[0].str.replace('([a-zA-Z]+:[^a-zA-Z]+)', '').str.strip() # description
s_b = pd.DataFrame(data=b.unique())
print(a.head())
print(b.head())
print(s_b[0].str.strip(")"))'''

'''
from Bio import Entrez

def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='20',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    results = search('fever')
    id_list = results['IdList']
    papers = fetch_details(id_list)
    #print(papers["PubmedArticle"][0]["AuthorList"])
    #for i, paper in enumerate(papers['PubmedArticle']): 
        #print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
    # Pretty print the first paper in full
    import json
    a=json.dumps(papers["PubmedArticle"][0], indent=2, separators=(',', ':'))
    json1_data = json.loads(a)
    
    for i in range(len(json1_data["MedlineCitation"]["Article"]["AuthorList"])):
        print(json1_data["MedlineCitation"]["Article"]["AuthorList"][i]["LastName"]+", "+
            json1_data["MedlineCitation"]["Article"]["AuthorList"][i]["ForeName"]+
            "("+str(json1_data["MedlineCitation"]["DateRevised"]["Year"])+")")'''

a = [True, False, True, True, False]

print(False*True)