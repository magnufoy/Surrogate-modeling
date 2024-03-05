import numpy as np
import os
import sys
import subprocess
from multiprocessing.pool import ThreadPool
from multiprocessing.pool import Pool
################################################################################
################################################################################
# FUNCTIONS
################################################################################
################################################################################
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def run_process(cmdlist,jobname,cleans):
    print('Job {} started'.format(jobname))
    process = subprocess.Popen(cmdlist,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    process.wait()
    print('Job {} finished'.format(jobname))
    for clean in cleans:
        os.remove(clean.format(jobname))
    os.system('{0} python {1} {2}'.format(ABAQUS_PATH,POST_PYTHON,jobname)) # Kjører postprosessering
    return
################################################################################
################################################################################
# BEGINING OF SCRIPT
################################################################################
################################################################################
try:
   filename = sys.argv[1]
except:
   print('Wrong inputs')
   exit()
#-------------------------------------------------------------------------------
# Define model name
#-------------------------------------------------------------------------------   
model_name  = 'BENDING_{}'
MAKE_PYTHON = 'MAKE_BENDING_2024.py'
POST_PYTHON = 'POST_BENDING.py'
#-------------------------------------------------------------------------------
# Read parameters for simulations
#-------------------------------------------------------------------------------
data_alloys = np.loadtxt(filename,delimiter=',',skiprows=1)
nsamples = len(data_alloys[:,0])
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
ABAQUS_PATH = '/opt/abaqus/Commands/abq2022'
nthreads = 8
cleans = ['{}.abq','{}.com','{}.dat','{}.mdl','{}.msg','{}.pac','{}.prt',
          '{}.res','{}.sel','{}.sta','{}.stt']
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
jobs = []
for k in range(0,nsamples):
    k += 1
    print('Generate model for variations {}'.format(k))
    format_string = '{0} cae noGUI={1} -- {2:3d} {3} {4} {5} {6} {7} {8} {9}'
    data2string = [ABAQUS_PATH]+[MAKE_PYTHON]+[k]+[x for x in data_alloys[k-1,1:]]
    os.system(format_string.format(*data2string))
    jobs.append([ABAQUS_PATH,'double','job='+model_name.format(k),'cpus=4','inter','ask=NO'])
#-------------------------------------------------------------------------------
# Run ABAQUS analyses
#-------------------------------------------------------------------------------
tp = ThreadPool(nthreads)
for i,job in enumerate(jobs):
    tp.apply_async(run_process, (job, model_name.format(i+1), cleans))
tp.close() # Close ThreadPool
tp.join() # Run ThreadPool
print('Finish running jobs')
#-------------------------------------------------------------------------------
# Remove unnecessary files
#-------------------------------------------------------------------------------
os.system('zip results_archive.zip *.csv *.odb *.inp')
os.system('rm -f *.odb *.inp abaqus.rpy* *.csv')
print('End of script')
################################################################################
################################################################################
# END OF SCRIPT
################################################################################
################################################################################
