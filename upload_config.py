from flask import Flask

B_Tech_Folder_1 = 'E:/Student_R_us/uploads/B.tech/1_yr'
B_Tech_Folder_2 = 'E:/Student_R_us/uploads/B.tech/2_yr'
B_Tech_Folder_3 = 'E:/Student_R_us/uploads/B.tech/3_yr'
B_Tech_Folder_4 = 'E:/Student_R_us/uploads/B.tech/4_yr'
B_Tech_Folder_5 = 'E:/Student_R_us/uploads/B.tech/alumni'
Bba_Folder_1 = 'E:/Student_R_us/uploads/BBA/1_yr'
Bba_Folder_2 = 'E:/Student_R_us/uploads/BBA/2_yr'
Bba_Folder_3 = 'E:/Student_R_us/uploads/BBA/3_yr'
Bba_Folder_4 = 'E:/Student_R_us/uploads/BBA/alumni'
Bsc_Folder_1 = 'E:/Student_R_us/uploads/B.sc_Agri/1_yr'
Bsc_Folder_2 = 'E:/Student_R_us/uploads/B.sc_Agri/2_yr'
Bsc_Folder_3 = 'E:/Student_R_us/uploads/B.sc_Agri/3_yr'
Bsc_Folder_4 = 'E:/Student_R_us/uploads/B.sc_Agri/4_yr'
Bsc_Folder_5 = 'E:/Student_R_us/uploads/B.sc_Agri/alumni'
Diploma_Folder_1 = 'E:/Student_R_us/uploads/Diploma/1_yr'
Diploma_Folder_2 = 'E:/Student_R_us/uploads/Diploma/2_yr'
Diploma_Folder_3 = 'E:/Student_R_us/uploads/Diploma/3_yr'
Diploma_Folder_4 = 'E:/Student_R_us/uploads/Diploma/alumni'
B_pharma_Folder_1 = 'E:/Student_R_us/uploads/B.pharma/1_yr'
B_pharma_Folder_2 = 'E:/Student_R_us/uploads/B.pharma/2_yr'
B_pharma_Folder_3 = 'E:/Student_R_us/uploads/B.pharma/3_yr'
B_pharma_Folder_4 = 'E:/Student_R_us/uploads/B.pharma/4_yr'
B_pharma_Folder_5 = 'E:/Student_R_us/uploads/B.pharma/alumni'
D_pharma_Folder_1 = 'E:/Student_R_us/uploads/D.pharma/1_yr'
D_pharma_Folder_2 = 'E:/Student_R_us/uploads/D.pharma/2_yr'
D_pharma_Folder_3 = 'E:/Student_R_us/uploads/D.pharma/3_yr'
D_pharma_Folder_4 = 'E:/Student_R_us/uploads/D.pharma/alumni'

app = Flask(__name__)

app.config['B_Tech_Folder_1'] = B_Tech_Folder_1
app.config['B_Tech_Folder_2'] = B_Tech_Folder_2
app.config['B_Tech_Folder_3'] = B_Tech_Folder_3
app.config['B_Tech_Folder_4'] = B_Tech_Folder_4
app.config['B_Tech_Folder_5'] = B_Tech_Folder_5
app.config['Bba_Folder_1'] = Bba_Folder_1
app.config['Bba_Folder_2'] = Bba_Folder_2
app.config['Bba_Folder_3'] = Bba_Folder_3
app.config['Bba_Folder_4'] = Bba_Folder_4
app.config['Bsc_Folder_1'] = Bsc_Folder_1
app.config['Bsc_Folder_2'] = Bsc_Folder_2
app.config['Bsc_Folder_3'] = Bsc_Folder_3
app.config['Bsc_Folder_4'] = Bsc_Folder_4
app.config['Bsc_Folder_5'] = Bsc_Folder_5
app.config['Diploma_Folder_1'] = Diploma_Folder_1
app.config['Diploma_Folder_2'] = Diploma_Folder_2
app.config['Diploma_Folder_3'] = Diploma_Folder_3
app.config['Diploma_Folder_4'] = Diploma_Folder_4
app.config['B_pharma_Folder_1'] = B_pharma_Folder_1
app.config['B_pharma_Folder_2'] = B_pharma_Folder_2
app.config['B_pharma_Folder_3'] = B_pharma_Folder_3
app.config['B_pharma_Folder_4'] = B_pharma_Folder_4
app.config['B_pharma_Folder_5'] = B_pharma_Folder_5
app.config['D_pharma_Folder_1'] = D_pharma_Folder_1
app.config['D_pharma_Folder_2'] = D_pharma_Folder_2
app.config['D_pharma_Folder_3'] = D_pharma_Folder_3
app.config['D_pharma_Folder_4'] = D_pharma_Folder_4


app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024