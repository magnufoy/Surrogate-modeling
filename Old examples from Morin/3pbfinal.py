#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPORT MODULES FROM ABAQUS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MODEL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='3PB_BENDING_NOTCHED')
try:
   del mdb.models['Model-1']
except:
   pass
#mdb.ModelFromInputFile(inputFileName='C:/Users/ben00/Downloads/3_point_bending_notched1.inp', name='3_point_bending_notched1')
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
IMPACTOR_PROFILE = model.ConstrainedSketch(name='IMPACTOR_PROFILE', sheetSize=200.0)
IMPACTOR_PROFILE.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
IMPACTOR_PROFILE.FixedConstraint(entity=IMPACTOR_PROFILE.geometry[2])
IMPACTOR_PROFILE.Line(point1=(30.0, 0.0), point2=(30.0, 15.0))
IMPACTOR_PROFILE.VerticalConstraint(addUndoState=False, entity=IMPACTOR_PROFILE.geometry[3])
IMPACTOR_PROFILE.VerticalDimension(textPoint=(37.7902183532715, 11.455696105957), value=200.0, vertex1=IMPACTOR_PROFILE.vertices[0], vertex2=IMPACTOR_PROFILE.vertices[1])
#del model.sketches['IMPACTOR_PROFILE']
#--------------------------------------------------------------------------------------------------------
# MAKE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Impactor'].AnalyticRigidSurfRevolve(sketch=IMPACTOR_PROFILE)
#
model.parts['Impactor'].ReferencePoint(point=model.parts['Impactor'].InterestingPoint(model.parts['Impactor'].edges[1], CENTER))
model.parts['Impactor'].Set(name='Imp_rp', referencePoints=(model.parts['Impactor'].referencePoints[2], ))
model.parts['Impactor'].Surface(name='Impactor', side2Faces=model.parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
SUPPORT_PROFILE = model.ConstrainedSketch(name='SUPPORT_PROFILE', sheetSize=200.0)
SUPPORT_PROFILE.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
SUPPORT_PROFILE.FixedConstraint(entity=SUPPORT_PROFILE.geometry[2])
SUPPORT_PROFILE.Line(point1=(30.0, 0.0), point2=(30.0, 25.0))
SUPPORT_PROFILE.VerticalConstraint(addUndoState=False, entity=SUPPORT_PROFILE.geometry[3])
SUPPORT_PROFILE.VerticalDimension(textPoint=(41.9750480651855, 4.7468376159668), value=200.0, vertex1=SUPPORT_PROFILE.vertices[1], vertex2=SUPPORT_PROFILE.vertices[0])
#del model.sketches['__profile__']
#--------------------------------------------------------------------------------------------------------
# MAKE PART FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Support', type=ANALYTIC_RIGID_SURFACE)
model.parts['Support'].AnalyticRigidSurfRevolve(sketch=SUPPORT_PROFILE)
#
model.parts['Support'].ReferencePoint(point=model.parts['Support'].InterestingPoint(model.parts['Support'].edges[1], CENTER))
model.parts['Support'].Set(name='Support_rp', referencePoints=(model.parts['Support'].referencePoints[2], ))
model.parts['Support'].Surface(name='Support', side2Faces=model.parts['Support'].faces.getSequenceFromMask(('[#1 ]', ), ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Material(name='C28')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='C28', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=3.0, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
model.keywordBlock.synchVersions(storeNodesAndElements=False)
model.keywordBlock.setValues(edited=0)
#--------------------------------------------------------------------------------------------------------
model.sections['Section-1-P2;OUTER_WALL'].setValues(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=2.7, thicknessField='', thicknessType=UNIFORM)
model.sections['Section-2-P4;INNER_WALL_TRANSITION'].setValues(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=2.0, thicknessField='', thicknessType=UNIFORM)
model.sections['Section-3-P5;INNER_WALL'].setValues(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=1.5, thicknessField='', thicknessType=UNIFORM)
#--------------------------------------------------------------------------------------------------------
model.rootAssembly.Instance(dependent=ON, name='Impactor-1', part=model.parts['Impactor'])
model.rootAssembly.translate(instanceList=('Impactor-1', ), vector=(0.0, 80.0, 104.0))
model.rootAssembly.Instance(dependent=ON, name='Support-1', part=model.parts['Support'])
model.rootAssembly.translate(instanceList=('Support-1', ), vector=(-187.5, -100.0, -32.001))
model.rootAssembly.Instance(dependent=ON, name='Support-2', part=model.parts['Support'])
model.rootAssembly.translate(instanceList=('Support-2', ), vector=(187.5, -100.0, -32.001))
#--------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='Load', previous='Initial', timePeriod=0.05)
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=100, variables=('MISES', 'PEEQ', 'U', 'SDV', 'STATUS'))
model.keywordBlock.synchVersions(storeNodesAndElements=False)
model.keywordBlock.replace(53, '\n*Material, name=C28\n\n\t*density\n\t2.7e-9\n\n\t*Elastic\n\t70000.0, 0.3\n\n\t*Plastic, hardening=USER, properties=8\n\t** SIGMA0,  THETA1,    Q1,    THETA2,      Q2,   THETA3,       Q3,   BLANK\n   \t  267.1, 32.602, 1.832,   1425.7,   48.633,   129300,   10.675,     0.0\n\n\t*Depvar, delete=6\n\t6,\n\t1,PEEQ,"equivalent plastic strain"\n\t2,DAMAGE,"Damage Cockcroft-Latham"\n\t3,leote,"Element aspect ratio"\n\t4,omega,"Element deformation mode"\n\t5,N,"Element normal"\n\t6,FAIL,"Failure status"\n\n*User Defined Field, properties=8\n** dcrit,     WcB,    WcS,   WcL,      c, phi, gamma, THICK\n     1.0,  390.47,  83.46, 33.00, 0.950, 1.0,   1.0,   2.0')
#--------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Imp_fixed', region=model.rootAssembly.instances['Impactor-1'].sets['Imp_rp'], u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Supp1_fixed', region=model.rootAssembly.instances['Support-1'].sets['Support_rp'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Supp2_fixed', region=model.rootAssembly.instances['Support-2'].sets['Support_rp'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (0.01, 1.0)), name='Load_amp', timeSpan=STEP)
model.VelocityBC(amplitude='Load_amp', createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=None, name='Load', region=model.rootAssembly.instances['Impactor-1'].sets['Imp_rp'], v1=UNSET, v2=UNSET, v3=-1000.0, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------
model.ContactProperty('Intprop')
model.interactionProperties['Intprop'].TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((0.05, ), ), temperatureDependency=OFF)
model.interactionProperties['Intprop'].NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
model.ContactExp(createStepName='Load', name='Interaction')
model.interactions['Interaction'].includedPairs.setValuesInStep(stepName='Load', useAllstar=ON)
model.interactions['Interaction'].contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'Intprop'), ), stepName='Load')
#--------------------------------------------------------------------------------------------------------
model.HistoryOutputRequest(createStepName='Load', name='F-D', rebar=EXCLUDE, region=model.rootAssembly.allInstances['Impactor-1'].sets['Imp_rp'], sectionPoints=DEFAULT, variables=('U3', 'RF3'))
#--------------------------------------------------------------------------------------------------------
model.keywordBlock.synchVersions(storeNodesAndElements=False)
model.keywordBlock.replace(54, '\n*Material, name=C28\n\n\t*density\n\t\t2.7e-9\n\n\t*Elastic\n\t\t70000.0, 0.3\n\n\t*Plastic, hardening=USER, properties=8\n\t** SIGMA0,  THETA1,    Q1,    THETA2,      Q2,   THETA3,       Q3,   BLANK\n   \t \t 267.1, 32.602, 1.832,   1425.7,   48.633,   129300,   10.675,     0.0\n\n\t*Depvar, delete=6\n\t6,\n\t1,PEEQ,"equivalent plastic strain"\n\t2,DAMAGE,"Damage Cockcroft-Latham"\n\t3,leote,"Element aspect ratio"\n\t4,omega,"Element deformation mode"\n\t5,N,"Element normal"\n\t6,FAIL,"Failure status"\n\n*User Defined Field, properties=8\n** dcrit,     WcB,    WcS,   WcL,      c, phi, gamma, THICK\n     1.0,  390.47,  83.46, 33.00, 0.950, 1.0,   1.0,   2.')
model.keywordBlock.replace(55, '\n')
model.keywordBlock.replace(66, '\n')
model.keywordBlock.replace(67, '\n')
model.keywordBlock.replace(68, '\n')
model.keywordBlock.replace(69, '\n')
model.keywordBlock.replace(70, '\n')
model.keywordBlock.replace(71, '\n')
model.keywordBlock.replace(72, '\n')
model.keywordBlock.replace(73, '\n** \n** STEP: Load\n**')
model.keywordBlock.synchVersions(storeNodesAndElements=False)
#--------------------------------------------------------------------------------------------------------
mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model='3_point_bending_notched1', modelPrint=OFF, multiprocessingMode=DEFAULT, name='3PB', nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, numThreadsPerMpiProcess=1, parallelizationMethodExplicit=DOMAIN, queue=None, resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
model.keywordBlock.synchVersions(storeNodesAndElements=False)
# Save by ben00 on 2024_02_16-12.04.36; build 2022 2021_09_15-19.57.30 176069
