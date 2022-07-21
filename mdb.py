
import pyodbc
#python 64 bit
#python environment and Acces ODBC need the same bit rate either 64 - 64 or 32 - 32
#usefull links for adjusting your Microsoft Access Driver:
#find bit rate of your python https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox
#How to connect to Microsoft Access with ODBC from Windows 10 https://help.interfaceware.com/v6/connect-to-microsoft-access-odbc
#How to install 64bit Microsoft Access https://knowledge.autodesk.com/de/support/autocad/learn-explore/caas/sfdcarticles/sfdcarticles/DEU/How-to-install-64-bit-Microsoft-Database-Drivers-alongside-32-bit-Microsoft-Office.html
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\gralf\OneDrive\Desktop\FH Technikum\Bachelor\SYSTEMDATEN2022.mdb;')
cursor = conn.cursor()

#jointabelle between "DIAGLIST", "DIAGLIST- 3 STELLER", "DIAGLIST - UNTERKAPITEL", "DIAGLIST-KAPITEL"
cursor.execute("SELECT [D].*, [D3S].*, [DUK].*, [DK].* "
               "FROM [DIAGLIST] AS [D], [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
               "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
               "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
               "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")

for row in cursor.fetchall():
     print(row)




