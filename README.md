# Kelompok 2 - Tugas Besar Teori Bahasa Automata
##
**M. ALIF GIBRAN A BOSSA - 1301213125\
RESKY ADHYAKSA         - 1301202259\
TIO ADJI HIDAYAT       – 1301213084**
##


Penggalan kata atau huruf atau simbol yang dapat diperiksa[^1] :\
**if, else, true, false, x, y, : , >=, <=, =**


Grammar yang diterima[^2] :\
 *If "KONDISI" :*\
      ‎ ‎ ‎ *"AKSI"*\
*else :*\
  ‎ ‎ ‎ *"AKSI"*
 
 Contoh :\
 *if x <= y :\
 ‎ ‎ ‎x = y\
 else :\
 ‎ ‎ ‎y = x*
  
**KONDISI : "VARIABLE" "OPERATOR" "VARIABLE" | "TRUE" | "FALSE"\
AKSI : "VARIABLE" = "VARIABLE"\
OPERATOR : <= | >=\
VARIABLE : x | y**
####
[^1]: Apabila user menginputkan diluar penggalan kata yang tidak berada dalam list, program akan error
[^2]: Program Akan Error bila inputan tidak sesuai dengan grammar yang telah ditentukan

    
