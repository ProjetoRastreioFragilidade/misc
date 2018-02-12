# coding: utf-8

# com o banco essa célula não será mais necessária

#-----------------------#
# carregando a planilha #
#-----------------------#

import pandas as pd

df_sh = pd.read_excel("collected_data.xlsx", sheet_name=0)

col_list = list(df_sh)


#-----------#
# variáveis #
#-----------#

df_feat = pd.DataFrame()

df_feat['meem'] = df_sh['RESULTADO MEEM']

cols = col_list[293 : 297]
df_feat['ativ_fis'] = df_sh[cols].sum(axis=1)

df_feat['temp_sent'] = df_sh['MINUTOS AF/TEMPO SENTADO']

df_feat['gds'] = df_sh['GDS TOTAL']

df_feat['fes'] = df_sh['FES TOTAL']

df_feat['man'] = df_sh[' MAN_TOTAL']

cols = col_list[200 : 203]
df_feat['fraq_musc_media'] = df_sh[cols].mean(axis=1)

df_feat['fraq_musc_max'] = df_sh['MAIOR FORÇA_PREENSÃO']

df_feat['lawton'] = df_sh['LAWTON_TOTAL']

df_feat['katz'] = df_sh['KATZ_TOTAL']

df_feat['ativ_ava'] = df_sh['CONTAGEM AINDA FAZ']

df_feat['tug'] = df_sh['TUG']

df_feat['caminhada'] = df_sh['MENOR_VELOCIDADE_CAT']

df_feat['mos'] = df_sh['MOS TOTAL']

df_feat['circ_cint'] = df_sh['CIRCUNF.CINTURA']
df_feat['circ_quad'] = df_sh['CINCUNF.QUADRIL']
df_feat['circ_pant'] = df_sh['CINCUNF.PANTURILHA']

df_feat['berg'] = df_sh['BERG TOTAL']

df_feat['idade'] = df_sh['IDADE'] 

df_feat['relogio'] = df_sh['ITEM 1 RELÓGIO']

df_feat['quedas'] = df_sh[col_list[126]]

# Exames de sangue [443 : 468] + Biomarcadores inflamatórios [468 : 475]
cols = col_list[443 : 475]
df_feat = pd.concat([df_feat, df_sh[cols]], axis=1)


#---------------#
# classificação #
#---------------#

def cat_class(cat):
    if (cat == 1):
        return('N')
    if (cat == 2):
        return('P')
    if (cat == 3):
        return('F')

df_feat.insert(0, 'subjetiva', df_sh['SUBJETIVA_CAT'].apply(cat_class))
df_feat.insert(1, 'fried',     df_sh['FRIED_CAT'].apply(cat_class))
df_feat.insert(2, 'edmonton',  df_sh['EDMONTON_CAT2'].apply(cat_class))

# remove as categóricas, para deixar todas agrupadas no fim
df_coleta = df_feat.drop({'PROTEINA TOTAL_CAT','ALBUMINA_CAT','GLOBULINAS_CAT','HEMOGLOBINA_CAT ','HEMATÓCRITO_CAT '}, axis=1)

# concatena com as categóricas
df_coleta = pd.concat([df_coleta, df_sh[['INTERNAÇÃO_CAT', 'MEEM_CAT', 'DOENÇA RENAL_CAT', 'FUMO_CAT', 'GDS_CAT2', 'INDEPEN_CAT', 'ITEM 4 VELOCIDADE_CAT',        'ITEM 5 (IPAQ_CAT (GASTO CALÓRICO)', 'ITEM 5 e 6 FADIGA_CAT', 'IPAQ_TOTAL_CAT1 (TRABALHO/TRANSPORTE/DOMÉSTICA/LAZER)', 'IPAQ_CAT2 (TRANSPORTE/LAZER)', 'AAVD_CAT', 'KATZ_CAT 2', 'TUG_CAT', 'BERG_CAT2', 'PROTEINA TOTAL_CAT', 'ALBUMINA_CAT', 'GLOBULINAS_CAT', 'HEMOGLOBINA_CAT ', 'HEMATÓCRITO_CAT ']]], axis=1)

# respostas da subjetiva
df_coleta.insert(3, 'subjetiva_q1',    df_sh[col_list[222]])
df_coleta.insert(4, 'subjetiva_q1_kg', df_sh[col_list[221]]) 
df_coleta.insert(5, 'subjetiva_q2',    df_sh[col_list[224]]) 
df_coleta.insert(6, 'subjetiva_q3',    df_sh[col_list[226]]) 
df_coleta.insert(7, 'subjetiva_q4',    df_sh[col_list[228]]) 
df_coleta.insert(8, 'subjetiva_q5',    df_sh[col_list[229]].apply(lambda x: 1 if x!=0 else 0)) 
df_coleta.insert(9, 'subjetiva_q6',    df_sh[col_list[230]].apply(lambda x: 1 if x!=0 else 0))

# respostas da fried
df_coleta.insert(10, 'fried_q1', df_sh[col_list[195]])
df_coleta.insert(11, 'fried_q2', df_sh[col_list[199]])
df_coleta.insert(12, 'fried_q3', df_sh[col_list[208]])
df_coleta.insert(13, 'fried_q4', df_sh[col_list[214]])
df_coleta.insert(14, 'fried_q5', df_sh[col_list[216]])
# respostas da edmonton
df_coleta.insert(15, 'edmonton_q1',   df_sh[col_list[169]])
df_coleta.insert(16, 'edmonton_q2_b', df_sh[col_list[171]])
df_coleta.insert(17, 'edmonton_q2_a', df_sh[col_list[173]])
df_coleta.insert(18, 'edmonton_q3',   df_sh[col_list[175]])
df_coleta.insert(19, 'edmonton_q4',   df_sh[col_list[177]])
df_coleta.insert(20, 'edmonton_q5_a', df_sh[col_list[179]])
df_coleta.insert(21, 'edmonton_q5_b', df_sh[col_list[181]])
df_coleta.insert(22, 'edmonton_q6',   df_sh[col_list[184]])
df_coleta.insert(23, 'edmonton_q7',   df_sh[col_list[186]])
df_coleta.insert(24, 'edmonton_q8',   df_sh[col_list[188]])
df_coleta.insert(25, 'edmonton_q9',   df_sh[col_list[190]])

df_coleta.rename(index=str, inplace=True, columns={
    'meem' : 'meem',                      
    'ativ_fis' : 'ativ_fis',                  
    'temp_sent' : 'temp_sent',                 
    'gds' : 'gds',                       
    'fes' : 'fes',                       
    'man' : 'man',                       
    'fraq_musc_media' : 'fraq_musc_media',           
    'fraq_musc_max' : 'fraq_musc_max',             
    'lawton' : 'lawton',                    
    'katz' : 'katz',                      
    'ativ_ava' : 'aavd',                      
    'tug' : 'tug',                       
    'caminhada' : 'caminhada',                 
    'mos' : 'mos',                       
    'circ_cint' : 'circ_cint',                 
    'circ_quad' : 'circ_quad',                 
    'circ_pant' : 'circ_pant',                 
    'berg' : 'berg',                      
    'idade' : 'idade',                     
    'relogio' : 'relogio',                   
    'quedas' : 'quedas',                    
    'GLICOSE mg/dL' : 'glicose',                   
    'HDL mg/dL' : 'hdl',                       
    'LDL mg/dL' : 'ldl',                       
    'VLDL mg/dL' : 'vldl',                      
    'URÉIA mg/dL' : 'ureia',                     
    'CREATININA mg/dL' : 'creatina',                  
    'DHEA mg/dL' : 'dhea',                      
    '25-HIDROXIVITAMINA D ng/mL' : 'hidroxivitamina_d',         
    'INSULINA µUI/mL' : 'insulina',                  
    'HGH ng/mL' : 'hgh',                       
    'TRIGLICÉRIDES mg/dL' : 'triglicerides',             
    'PROTEINA TOTAL g/dL' : 'proteina_total',            
    'ALBUMINA g/dL' : 'albumina',                  
    'GLOBULINAS g/dL' : 'globulinas',                
    'COLESTEROL TOTAL mg/dL' : 'colesterol_total',          
    'S-DHEA µg/dL' : 's_dhea',                    
    'SOMATOMEDINA C ng/dL' : 'somatomedina_c',            
    'HEMOGLOBINA g/dL' : 'hemoglobina',               
    'HEMATÓCRITO (%)' : 'hematocrito',               
    'HEMOGLOBINA GLICADA (%)' : 'hemoglobina_glicada',       
    'ADAM10 pg/mL' : 'adam10',                    
    'IL-10 pg/mL' : 'il_10',                     
    'IL-1α pg/mL' : 'il_1alpha',                 
    'IL-1β pg/mL' : 'il_1beta',                  
    'IL-6 pg/mL' : 'il_6',                      
    'TNFα pg/mL' : 'tnf_alpha',                 
    'TNFβ pg/mL' : 'tnf_beta',                  
    'INTERNAÇÃO_CAT' : 'internacao_cat',            
    'MEEM_CAT' : 'meem_cat',                  
    'DOENÇA RENAL_CAT' : 'doenca_renal_cat',          
    'FUMO_CAT' : 'fumo_cat',                  
    'GDS_CAT2' : 'gds_cat2',                   
    'INDEPEN_CAT' : 'indepen_cat',               
    'ITEM 4 VELOCIDADE_CAT' : 'velocidade_cat',            
    'ITEM 5 (IPAQ_CAT (GASTO CALÓRICO)' : 'ipaq_gasto_calorico_cat',   
    'ITEM 5 e 6 FADIGA_CAT' : 'fadiga_cat',     
    'IPAQ_TOTAL_CAT1 (TRABALHO/TRANSPORTE/DOMÉSTICA/LAZER)' : 'ipaq_total_cat',            
    'IPAQ_CAT2 (TRANSPORTE/LAZER)' : 'ipaq_transp_lazer_cat2',                
    'AAVD_CAT' : 'aavd_cat',                  
    'KATZ_CAT 2' : 'katz_cat2',                  
    'TUG_CAT' : 'tug_cat',                   
    'BERG_CAT2' : 'berg_cat2',                  
    'PROTEINA TOTAL_CAT' : 'proteina_total_cat',        
    'ALBUMINA_CAT' : 'albumina_cat',              
    'GLOBULINAS_CAT' : 'globulinas_cat',            
    'HEMOGLOBINA_CAT ' : 'hemoglobina_cat',           
    'HEMATÓCRITO_CAT ' :'hematocrito_cat'      
})

# converto a resposta da questão para pontuação obtida
df_coleta['subjetiva_q5'] = df_coleta['subjetiva_q5'].apply(lambda x: 1 if x!=0 else 0)


print("DataFrame criado.")


from sqlalchemy import create_engine

print("Conectando com a base de dados.")

engine = create_engine('mysql+mysqldb://ppsus:rede243@localhost:3306/ppsus')
connection = engine.connect()

print("Conexao estabelecida com sucesso.")


print("Criando tabela e inserindo dados")

# cria tabela e insere os dados
df_coleta.to_sql('ppsus_app_coleta', engine, if_exists='replace', index=False)


print("Criando chave primaria para ppsus_app_coleta")

# cria chave primária para coleta
connection.execute('ALTER TABLE ppsus_app_coleta ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;')

print("Chave criada com sucesso")

print("Bye =D")