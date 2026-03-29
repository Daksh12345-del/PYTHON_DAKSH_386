import re
pattern="Die" 
text='''
Wikibooks – Die freie Bibliothek“ für Lehr-, Fach- und Sachbücher wurde 2003 als Lehrbuchabteilung der Wikipedia eingerichtet. Seither haben viele Freiwillige 33.876 Buchkapitel in 844 Büchern geschrieben. Die 98 bereits fertigen Bücher sind im Buchkatalog zu finden. Auch viele Bücher, die nicht fertig sind und deshalb nicht im Buchkatalog stehen, können lesbar und informativ sein. Aber Wikibooks ist eine Bibliothek nur für Lehr-, Sach- und Fachbücher.

Was bedeutet „frei“? Jeder darf alle diese Bücher frei nutzen – auch kommerziell, solange die Lizenzbestimmungen der CC-BY-SA-4.0 und ggf. der GFDL eingehalten werden.

Unsere Lehrbücher sollen gesichertes Wissen widerspiegeln. Das heißt, das hier dargestellte Wissen soll die gleichen Fähigkeiten und Kenntnisse vermitteln, wie andere Werke des jeweiligen Fachs. Wir können jedoch nicht für Fehlerfreiheit unserer Bücher garantieren: Menschen machen Fehler und wenn einer auffällt, ist er von jeder Person leicht zu ändern.
'''

match=re.search(pattern,text) 
print(match)  #prints the first occurrence of the pattern in the text and provides us output as: