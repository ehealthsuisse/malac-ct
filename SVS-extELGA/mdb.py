
import pyodbc

#python 64 bit
#python environment and Acces ODBC need the same bit rate either 64 - 64 or 32 - 32
#usefull links for adjusting your Microsoft Access Driver:
#find bit rate of your python https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox
#How to connect to Microsoft Access with ODBC from Windows 10 https://help.interfaceware.com/v6/connect-to-microsoft-access-odbc
#How to install 64bit Microsoft Access https://knowledge.autodesk.com/de/support/autocad/learn-explore/caas/sfdcarticles/sfdcarticles/DEU/How-to-install-64-bit-Microsoft-Database-Drivers-alongside-32-bit-Microsoft-Office.html
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\gralf\OneDrive\Desktop\FH Technikum\Bachelor\SYSTEMDATEN2022.mdb;')
cursor = conn.cursor()
#cursor.execute('select * from DIAGLIST')
#cursor.execute("select * from DIAGLIST where [Diagnose] like 'N80%'")
#cursor.execute('select * from DIAGLIST where Kapitel = A1')
#cursor.execute('select * from "DIAGLIST - UNTERKAPITEL"') #for row in cursor.execute('select kapitel from DIAGLIST'):

# cursor.execute('select "DIAGLIST - 3 STELLER".Bezeichnung,"DIAGLIST - UNTERKAPITEL".Beschreibung,"DIAGLIST - UNTERKAPITEL".Diagnose_von,"DIAGLIST - UNTERKAPITEL".Diagnose_bis '
#                'from "DIAGLIST - 3 STELLER" '
#                'left outer join "DIAGLIST - UNTERKAPITEL" '
#                'where "DIAGLIST - 3 STELLER".Diagnose between "DIAGLIST - UNTERKAPITEL".Diagnose_von and "DIAGLIST - UNTERKAPITEL".Diagnose_bis')
               #'on "DIAGLIST - 3 STELLER".Diagnose = temp.Diagnose and temp.Diagnose '
               #'between "DIAGLIST - UNTERKAPITEL".Diagnose_von and "DIAGLIST - UNTERKAPITEL".Diagnose_bis')
               #'on "DIAGLIST - 3 STELLER".Diagnose >= "DIAGLIST - UNTERKAPITEL".Diagnose_von AND "DIAGLIST - 3 STELLER".Diagnose <=UNTERKAPITEL".Diagnose_bis ')
               #alias geben

#jointable between "DIAGLIST - 3 STELLER" and "DIAGLIST - UNTERKAPITEL"
# cursor.execute('SELECT [DIAGLIST - 3 STELLER].*, [DIAGLIST - UNTERKAPITEL].* '
#                 'FROM [DIAGLIST - 3 STELLER], [DIAGLIST - UNTERKAPITEL] '
#                 'WHERE [DIAGLIST - 3 STELLER].Diagnose '
#                 'BETWEEN [DIAGLIST - UNTERKAPITEL].Diagnose_von AND [DIAGLIST - UNTERKAPITEL].Diagnose_bis')

cursor.execute('SELECT [D3S].*, [DUK].* '
               'FROM [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK] '
               'WHERE [D3S].Diagnose '
               'BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis')
print()

# #jointable between "DIAGLIST - UNTERKAPITEL" and "DIAGLIST-KAPITEL"
# cursor.execute('SELECT [DIAGLIST - UNTERKAPITEL].*, [DIAGLIST - KAPITEL].* '
#                 'FROM [DIAGLIST - UNTERKAPITEL], [DIAGLIST - KAPITEL]'
#                 'WHERE [DIAGLIST - UNTERKAPITEL].Diagnose_von AND [DIAGLIST - UNTERKAPITEL].Diagnose_bis '
#                 'BETWEEN [DIAGLIST - KAPITEL].Diagnose_von AND [DIAGLIST - KAPITEL].Diagnose_bis')

cursor.execute('SELECT [DUK].*, [DK].* '
               'FROM [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]'
               'WHERE [DUK].Diagnose_von AND [DUK].Diagnose_bis '
               'BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis')

print()
# #jointable between "DIAGLIST - 3 STELLER" and "DIAGLIST"
# cursor.execute("SELECT [DIAGLIST - 3 STELLER].*, [DIAGLIST].* "
#                "FROM [DIAGLIST - 3 STELLER], [DIAGLIST]"
#                "WHERE [DIAGLIST].Diagnose LIKE [DIAGLIST - 3 STELLER].Diagnose + '%'")

cursor.execute("SELECT [D3S].*, [D].* "
               "FROM [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST] AS [D]"
               "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%'")

#jointable between "DIAGLIST -
#cursor.execute('select "DIAGLIST - UNTERKAPITEL".Diagnose_bis from "DIAGLIST - UNTERKAPITEL"')
#cursor.execute(
#    'SELECT "DIAGLIST - 3 STELLER".Bezecihnung  WHERE "DIAGLIST - UNTERKAPITEL".Diagnose_von  >= ? AND "DIAGLIST - UNTERKAPITEL".Diagnose_bis <= ?'
#)
#cursor.execute('select * froom "DIAGLIST - 3 STELLER" join
#cursor.execute('SELECT "DIAGLIST - 3 STELLER".Diagnose from "DIAGLIST - 3 STELLER"')
for row in cursor.fetchall():
     print(row)




