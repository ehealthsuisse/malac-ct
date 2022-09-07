
import pyodbc
# #python 64 bit
# #python environment and Acces ODBC need the same bit rate either 64 - 64 or 32 - 32
# #usefull links for adjusting your Microsoft Access Driver:
# #find bit rate of your python https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox
# #How to connect to Microsoft Access with ODBC from Windows 10 https://help.interfaceware.com/v6/connect-to-microsoft-access-odbc
# #How to install 64bit Microsoft Access https://knowledge.autodesk.com/de/support/autocad/learn-explore/caas/sfdcarticles/sfdcarticles/DEU/How-to-install-64-bit-Microsoft-Database-Drivers-alongside-32-bit-Microsoft-Office.html
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\gralf\OneDrive\Desktop\FH Technikum\Bachelor\SYSTEMDATEN2022.mdb;')
# cursor = conn.cursor()
# #infile wäre path
# #jointabelle between "DIAGLIST", "DIAGLIST- 3 STELLER", "DIAGLIST - UNTERKAPITEL", "DIAGLIST-KAPITEL"
# cursor.execute("SELECT [D].*, [D3S].*, [DUK].*, [DK].* "
#                "FROM [DIAGLIST] AS [D], [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
#                "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
#                "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
#                "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")
# #tabellennamenändern indem bestimmte spalten geholt werden und dann nur mit dem AS umegändert werden
# #getter von pcam verwenden
# #VS=ICD
#
# #odbc doku hinzufügen als kommentar
# #odbc andere namen als hier
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()
#self.resource=row.Diagnose

#temp =rows.DIAGLIST+Diagnose
#print(temp)
#
# for row in cursor.columns():
#      print(row.column_name)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row.Diagnose)
#     print(row[0])

#     tempk =row.Kennzeichen
#     print(tempk)
#     break
#     #1min 23sec
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\gralf\OneDrive\Desktop\FH Technikum\Bachelor\SYSTEMDATEN2022.mdb;')
cursor = conn.cursor()
cursor.execute("SELECT [D].*, [D3S].*, [DUK].*, [DK].* "
               "FROM [DIAGLIST] AS [D], [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
               "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
               "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
               "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")
dict = {}
#hi="hi"
#hi2="hi2"
#dict[hi] = "string"
#dict[hi2] = "string"
dict[1]="hewo"
num =[1,2,3,4,5,6,7,8,9]
for row in num:
    if row != list(dict)[-1]:
        dict[row] = "hello"



print(dict)
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()


