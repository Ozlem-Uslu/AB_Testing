##############################################################
# AB-Test(Unabhängiger Zwei-Stichproben-T-Test)
##############################################################
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# AUFGABE 1: Aufbereitung und Analyse von Daten

# Lesen Sie den Datensatz ab_testing_data.xlsx, der aus Kontroll- und Testgruppendaten besteht.
# Weisen Sie die Kontroll- und Testgruppendaten separaten Variablen zu.

control_group = pd.read_excel("/Users/Ozlem/Desktop/ab_testing.xlsx", sheet_name="Control Group")
test_group = pd.read_excel("/Users/Ozlem/Desktop/ab_testing.xlsx", sheet_name="Test Group")

#Analysieren Sie die Kontroll- und Testgruppendaten.

test_group.info()
control_group.info()

control_group.describe().T
test_group.describe().T

#Kombinieren Sie nach der Analyse die Kontroll- und Testgruppendaten mithilfe der Concat-Methode.

control_group["Bidding"] = "Maximum_Bidding"
test_group["Bidding"] = "Average_Bidding"
df = pd.concat([control_group, test_group], ignore_index = True)

# AUFGABE 2: Festlegen der Hypothese für den A/B-Test

#Definieren Sie die Hypothese.

#H0 : M1 = M2 (Es gibt keinen statistisch signifikanten Unterschied zwischen
# den „Purchase“ Mittelwerte von „Average Bidding“ und „Maximum Bidding“.)
#H1 : M1 != M2 (Es gibt einen statistisch signifikanten Unterschied.......)

#Analysieren Sie die Mittelwerte von purchase(Gewinn) für die Kontroll- und die Testgruppe.

df.groupby("Bidding").agg({"Purchase": "mean"})

# AUFGABE 3: Durchführen von Hypothesentests (parametrische und nichtparametrische Tests)

# Überprüfen Sie die Annahmen vor der Hypothesenprüfung.
# Dies sind die Normalitätsannahme und die Homogenität der Varianz.

#Prüfung, ob die Kontroll- und die Testgruppe die Normalitätsannahme für die Purchase-Variable getrennt erfüllen!

# Normalitätsannahme (Shapiro-Test):
# H0: Die Annahme einer Normalverteilung ist erfüllt.
# H1:...nicht erfüllt.

#Wenn der p-Wert < 0,05 ist, wird H0 ABGELEHNT.
#Wenn der p-Wert < 0,05 ist, wird H0 nicht abgelehnt.

test_stat, pvalue = shapiro(df.loc[df["Bidding"] == "Average_Bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["Bidding"] == "Maximum_Bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


#Kommentar:
#Da der p-Wert(p-value = 0.1541 für Average_Bidding und p-value = 0.5891 für Maximum_Bidding ) der Purchase-Variablen
#in beiden Gruppen größer als 0,05 ist, kann H0 nicht abgelehnt,
#d. h. akzeptiert werden. Damit ist die Normalitätsannahme gewährleistet.

# Annahme der Homogenität der Varianz: (Levene-Test)
# H0: Die Varianzen sind homogen
# H1: Die Varianzen sind nicht homogen

test_stat, pvalue = levene(df.loc[df["Bidding"] == "Average_Bidding", "Purchase"],
                           df.loc[df["Bidding"] == "Maximum_Bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Kommentar:
#Da der p-Wert(0.1083) größer als 0,05 ist, wird H0 nicht abgelehnt. Dies bedeutet, dass die Varianzen homogen sind,
#d.h. die Varianzen ähnlich sind.

# Wählen Sie den geeigneten Test entsprechend den Ergebnissen der Normalitätsannahme und der Varianzhomogenität aus.

# Da beide Annahmen erfüllt sind, wenden wir den parametrischen Test an (unabhängiger T-Test mit zwei Stichproben).

test_stat, pvalue = ttest_ind(df.loc[df["Bidding"] == "Average_Bidding", "Purchase"],
                              df.loc[df["Bidding"] == "Maximum_Bidding", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Interpretieren Sie unter Berücksichtigung des aus dem Test resultierenden p_Wertes,
#ob ein statistisch signifikanter Unterschied zwischen den Purchase-Durchschnitten
#der Kontroll- und der Testgruppe besteht.

# das Ergebnis:

#Da der p-Wert(0.3493) größer als 0,05 ist, kann H0 zu Beginn unserer Studie nicht abgelehnt werden.
#Das bedeutet, es gibt keinen statistisch signifikanten Unterschied zwischen den Purchase-Durchschnitten
#der beiden Gruppen, also zwischen der Anzahl der gekauften Produkte.

# AUFGABE 4: Analyse der Ergebnisse!

#Beraten Sie den Kunden anhand der Testergebnisse, die Sie erhalten haben.

# Der neu erstellte Gebotstyp „Average_Bidding“ ist nicht vorteilhafter als der alte „Maximum Bidding“,
# sodass der Kunde den für ihn passenden auswählen kann.
# Weitere Variablen (Click (Anzahl der Klicks auf die Anzeige), Earning (Einnahmen aus gekauften Produkten))
# können getestet werden und eine bessere Entscheidung getroffen werden.
# Die Daten können vergrößert und dann erneut getestet werden.
# Der Test kann über einen längeren Zeitraum statt für einen Monat durchgeführt werden,
# d. h. der Testzeitraum kann verlängert werden.