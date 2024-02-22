from odbAccess import *
import sys
import numpy as np
#
def write_results(filename,data,keys):
    header = '*'+','.join(keys)+'\n'
    nvars,ntime  = np.shape(data)[1],np.shape(data)[0]
    format_to_write = '{},'*(nvars-1)+'{}\n'
    fp = open(filename+'_data.csv','w')
    fp.write(header)
    for i in range(0,ntime):
        fp.write(format_to_write.format(*[x for x in data[i,:]]))
    fp.close()
    return
#
def post_crushing_curves(filename):
    #-------------------------------------------------------------------------------
    # Open odb file
    #-------------------------------------------------------------------------------
    odb  = openOdb(path=filename+'.odb')
    #-------------------------------------------------------------------------------
    # Load the step
    #-------------------------------------------------------------------------------
    stepname = 'loading'
    step = odb.steps[stepname]
    #-------------------------------------------------------------------------------
    # Load the assembly
    #-------------------------------------------------------------------------------
    myAssem = odb.rootAssembly
    #-----------------------------------------------------------------------
    # Extract force from reference point
    #-----------------------------------------------------------------------
    forceHist = step.historyRegions['Node IMPACTOR-1.1']
    force     = np.array(forceHist.historyOutputs['RF3'].data)[:,1]
    disp      = np.array(forceHist.historyOutputs['U3'].data)[:,1]
    time      = np.array(forceHist.historyOutputs['RF3'].data)[:,0]
    #-------------------------------------------------------------------------------
    # Close odb file
    #-------------------------------------------------------------------------------
    odb.close()
    DMM = np.abs(disp)
    FKN = np.abs(force)/1000.0
    data = np.transpose(np.array([time,DMM,FKN]))
    keys = ['time','DMM','FKN']
    write_results(filename,data,keys)
    return
####################################################################################
####################################################################################
# START OF SCRIPT
####################################################################################
####################################################################################
filename = sys.argv[-1]
post_crushing_curves(filename)
exit()
####################################################################################
####################################################################################
# END OF SCRIPT
####################################################################################
####################################################################################