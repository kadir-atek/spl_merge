import os
import re

errCnt=0
wrnCnt=0
infoCnt=0

def loge(str):
    print('\u001b[31m[ERROR] '+str+'\u001b[0m')
    global errCnt
    errCnt+=1

def logw(str):
    print('\u001b[33m[WARNING] '+str+'\u001b[0m')
    global wrnCnt
    wrnCnt+=1

def logi(str):
    print('\u001b[32m[INFO] '+str+'\u001b[0m')
    global infoCnt
    infoCnt+=1
    
fileDir=os.getcwd()
files=os.listdir(fileDir)

mergedFile=open(fileDir+'\\merged.txt', 'w')
mergedFile.write('fileName valid gamma_src1 gamma_ld1 Freq Pin_avail_dBm Pin_deliv_dBm Refl_coef Refl_dB Pout_dBm Gt_dB Gp_dB Vout_v Iout_mA Vin_v Iin_mA Eff_% DrainEfficiency_percent GainCpLin_db PAE_percent PDC_dBm\n')
    
for file in files:
    match=re.search('\\.spl$', file)
    if match:
        fileName=file[:match.start()]
        
        f=open(fileDir+'\\'+file, 'r')
        
        found=False
        for line in f:
            #logi('line: '+line)
            if (not found) and (line.rstrip()=='valid gamma_src1 gamma_ld1 Freq Pin_avail_dBm Pin_deliv_dBm Refl_coef Refl_dB Pout_dBm Gt_dB Gp_dB Vout_v Iout_mA Vin_v Iin_mA Eff_% DrainEfficiency_percent GainCpLin_db PAE_percent PDC_dBm'):
                found=True
                continue
            if found:
                mergedFile.write(fileName+' '+line)
                
        if not found:
            loge('header could not found in the file: '+file)
                
        f.close()
    else:
        loge('unknown file: '+file)

mergedFile.close()

print('Process completed, Info(s): '+str(infoCnt)+', Warning(s): '+str(wrnCnt)+', Error(s): '+str(errCnt))