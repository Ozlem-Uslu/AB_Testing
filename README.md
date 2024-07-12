# AB_Testing
Vergleich der Konversion von "Bidding"-Methoden durch den AB-Test


PROJEKTÜBERSICHT

##################
Geschäftsproblem
##################

Ein Unternehmen hat vor kurzem eine neue Gebotsart, "averagebidding", als Alternative zur bestehenden Gebotsart "maximumbidding" eingeführt. Einer unserer Kunden hat beschlossen, diese neue Funktion zu testen und möchte einen A/B-Test durchführen, um zu sehen, ob "averagebidding" mehr Conversions bringt als "maximumbidding". Der A/B-Test läuft bereits seit einem Monat und Ihr Kunde bittet Sie nun, die Ergebnisse dieses A/B-Tests zu analysieren. Der ultimative Erfolgsmaßstab für den Kunden ist der Kauf. Daher sollten sich die statistischen Tests auf die Kaufmetrik konzentrieren.

##################
Datensatz Geschichte
##################

In diesem Datensatz, der die Website-Informationen eines Unternehmens enthält, finden sich Informationen wie die Anzahl der von den Nutzern gesehenen und angeklickten Anzeigen sowie Informationen über die Einnahmen aus dieser Website. Es gibt zwei separate Datensätze, die Kontroll- und die Testgruppe. Diese Datensätze befinden sich auf separaten Seiten von ab_testing.xlsxexcel. Auf die Kontrollgruppe wurde "Maximum Bidding" und auf die Testgruppe "Average Bidding" angewendet.

####################
Variablen im Datensatz
####################

Impression: Anzahl der Anzeigenaufrufe
Click: Anzahl der Klicks auf die angezeigte Anzeige
Purchase: Anzahl der gekauften Produkte nach angeklickter Werbung
Earning: Verdienst nach gekauften Produkten

ANWENDUNG DES AB_TESTS

In diesem Projekt wurde ein unabhängiger T-Test mit zwei Stichproben verwendet.

1-die Aufstellung von Hypothesen

2-überprüfung der Annahmen

  -die Normalitätsannahme (Shapiro)
  
  -die Homogenität der Varianz (Levene)
  
3.die Umsetzung der Hypothese

4.Interpretation der Ergebnisse anhand des p-Wertes

Hinweis
- Wenn die Normalität nicht erfüllt ist, wird ein direkter nonparametrischer Mannwhitneyu-Test durchgeführt.  Wenn die Homogenität der Varianz nicht gewährleistet ist, werden die Argumente in den unabhängigen T-Test mit zwei Stichproben eingegeben.
- Es kann sinnvoll sein, vor der Normalitätsprüfung eine Ausreißeranalyse und -korrektur durchzuführen.




