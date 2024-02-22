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

mdb.ModelFromInputFile(
    inputFileName='3_point_bending_notched1.inp',
    name='/home/magnufoy/Simulering_1/3_point_bending_notched1.inp')

model_name = '3_point_bending_notched1'
impactor = 'Impactor'
support = 'Support'

sheet_size = 200.0

model = mdb.models[model_name]
assembly = model.rootAssembly

# Creating sketch
model.ConstrainedSketch(name='__profile__', sheetSize=sheet_size)
model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
model.sketches['__profile__'].FixedConstraint(entity=model.sketches['__profile__'].geometry[2])
model.sketches['__profile__'].Line(point1=(30.0, 0.0), point2=(30.0, 15.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].VerticalDimension(
    textPoint=(37.7902183532715, 11.455696105957), value=200.0, vertex1=
    model.sketches['__profile__'].vertices[0], 
    vertex2=
    model.sketches['__profile__'].vertices[1])

# Creating parts
model.Part(dimensionality=THREE_D, name=
    impactor, type=ANALYTIC_RIGID_SURFACE)
model.parts[impactor].AnalyticRigidSurfRevolve(
    sketch=model.sketches['__profile__'])
del model.sketches['__profile__']

# Creating sketch
model.ConstrainedSketch(name='__profile__', sheetSize=sheet_size)
model.sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
model.sketches['__profile__'].FixedConstraint(entity=model.sketches['__profile__'].geometry[2])
model.sketches['__profile__'].Line(point1=(30.0, 0.0), point2=(30.0, 25.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].VerticalDimension(
    textPoint=(41.9750480651855, 4.7468376159668), value=200.0, vertex1=
    model.sketches['__profile__'].vertices[1], 
    vertex2=
    model.sketches['__profile__'].vertices[0])

# Creating parts
model.Part(dimensionality=THREE_D, name=support, type=ANALYTIC_RIGID_SURFACE)
model.parts[support].AnalyticRigidSurfRevolve(sketch=model.sketches['__profile__'])
del model.sketches['__profile__']


model.Material(name='C28')

model.parts[impactor].ReferencePoint(point=
    model.parts[impactor].InterestingPoint(
    model.parts[impactor].edges[1], CENTER))
model.parts[support].ReferencePoint(point=
    model.parts[support].InterestingPoint(
    model.parts[support].edges[1], CENTER))

model.parts[impactor].Set(name='Imp_rp', referencePoints=(model.parts[impactor].referencePoints[2], ))
model.parts[support].Set(name='Support_rp', referencePoints=(model.parts[support].referencePoints[2], ))

model.parts[impactor].Surface(name=
    impactor, side2Faces=
    model.parts[impactor].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
model.parts[support].Surface(name=support, 
    side2Faces=
    model.parts[support].faces.getSequenceFromMask(
    ('[#1 ]', ), ))

# Matialparameters SLETT?
model.keywordBlock.synchVersions(
    storeNodesAndElements=False)
model.keywordBlock.setValues(edited=0)

# Assigning material properties to sections
model.sections['Section-1-P2;OUTER_WALL'].setValues(
    idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', 
    nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=2.7, 
    thicknessField='', thicknessType=UNIFORM)
model.sections['Section-2-P4;INNER_WALL_TRANSITION'].setValues(
    idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', 
    nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=2.0, 
    thicknessField='', thicknessType=UNIFORM)
model.sections['Section-3-P5;INNER_WALL'].setValues(
    idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', 
    nodalThicknessField='', numIntPts=5, preIntegrate=OFF, thickness=1.5, 
    thicknessField='', thicknessType=UNIFORM)

# Creating instances
assembly.Instance(dependent=ON, 
    name='Impactor-1', part=
    model.parts[impactor])
assembly.translate(instanceList=(
    'Impactor-1', ), vector=(0.0, 80.0, 104.0))
assembly.Instance(dependent=ON, 
    name='Support-1', part=
    model.parts[support])
assembly.translate(instanceList=(
    'Support-1', ), vector=(-187.5, -100.0, -32.001))
assembly.Instance(dependent=ON, 
    name='Support-2', part=
    model.parts[support])
assembly.translate(instanceList=(
    'Support-2', ), vector=(187.5, -100.0, -32.001))

# Creating steps
model.ExplicitDynamicsStep(improvedDtMethod=ON
    , name='Load', previous='Initial', timePeriod=0.05)

# Modify field output requests
model.fieldOutputRequests['F-Output-1'].setValues(
    numIntervals=100, variables=('MISES', 'PEEQ', 'U', 'SDV', 'STATUS'))

# Material properties
model.keywordBlock.synchVersions(
    storeNodesAndElements=False)
model.keywordBlock.replace(53, 
    '\n*Material, name=C28\n\n\t*density\n\t2.7e-9\n\n\t*Elastic\n\t70000.0, 0.3\n\n\t*Plastic, hardening=USER, properties=8\n\t** SIGMA0,  THETA1,    Q1,    THETA2,      Q2,   THETA3,       Q3,   BLANK\n   \t  267.1, 32.602, 1.832,   1425.7,   48.633,   129300,   10.675,     0.0\n\n\t*Depvar, delete=6\n\t6,\n\t1,PEEQ,"equivalent plastic strain"\n\t2,DAMAGE,"Damage Cockcroft-Latham"\n\t3,leote,"Element aspect ratio"\n\t4,omega,"Element deformation mode"\n\t5,N,"Element normal"\n\t6,FAIL,"Failure status"\n\n*User Defined Field, properties=8\n** dcrit,     WcB,    WcS,   WcL,      c, phi, gamma, THICK\n     1.0,  390.47,  83.46, 33.00, 0.950, 1.0,   1.0,   2.0')

# Boundary conditions
model.DisplacementBC(amplitude=UNSET, 
    createStepName='Initial', distributionType=UNIFORM, fieldName='', 
    localCsys=None, name='Imp_fixed', region=
    assembly.instances['Impactor-1'].sets['Imp_rp']
    , u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, 
    createStepName='Initial', distributionType=UNIFORM, fieldName='', 
    localCsys=None, name='Supp1_fixed', region=
    assembly.instances['Support-1'].sets['Support_rp']
    , u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, 
    createStepName='Initial', distributionType=UNIFORM, fieldName='', 
    localCsys=None, name='Supp2_fixed', region=
    assembly.instances['Support-2'].sets['Support_rp']
    , u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.SmoothStepAmplitude(data=((0.0, 0.0), (
    0.01, 1.0)), name='Load_amp', timeSpan=STEP)
model.VelocityBC(amplitude='Load_amp', 
    createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=
    None, name='Load', region=
    assembly.instances['Impactor-1'].sets['Imp_rp']
    , v1=UNSET, v2=UNSET, v3=-1000.0, vr1=UNSET, vr2=UNSET, vr3=UNSET)

# Interaction properties
model.ContactProperty('Intprop')
model.interactionProperties['Intprop'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.05, ), ), temperatureDependency=OFF)
model.interactionProperties['Intprop'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
model.ContactExp(createStepName='Load', name='Interaction')
model.interactions['Interaction'].includedPairs.setValuesInStep(
    stepName='Load', useAllstar=ON)
model.interactions['Interaction'].contactPropertyAssignments.appendInStep(
    assignments=((GLOBAL, SELF, 'Intprop'), ), stepName='Load')

# History output
model.HistoryOutputRequest(createStepName=
    'Load', name='F-D', rebar=EXCLUDE, region=
    assembly.allInstances['Impactor-1'].sets['Imp_rp']
    , sectionPoints=DEFAULT, variables=('U3', 'RF3'))

# Material properties
model.keywordBlock.synchVersions(
    storeNodesAndElements=False)
model.keywordBlock.replace(54, 
    '\n*Material, name=C28\n\n\t*density\n\t\t2.7e-9\n\n\t*Elastic\n\t\t70000.0, 0.3\n\n\t*Plastic, hardening=USER, properties=8\n\t** SIGMA0,  THETA1,    Q1,    THETA2,      Q2,   THETA3,       Q3,   BLANK\n   \t \t 267.1, 32.602, 1.832,   1425.7,   48.633,   129300,   10.675,     0.0\n\n\t*Depvar, delete=6\n\t6,\n\t1,PEEQ,"equivalent plastic strain"\n\t2,DAMAGE,"Damage Cockcroft-Latham"\n\t3,leote,"Element aspect ratio"\n\t4,omega,"Element deformation mode"\n\t5,N,"Element normal"\n\t6,FAIL,"Failure status"\n\n*User Defined Field, properties=8\n** dcrit,     WcB,    WcS,   WcL,      c, phi, gamma, THICK\n     1.0,  390.47,  83.46, 33.00, 0.950, 1.0,   1.0,   2.')

model.keywordBlock.replace(55, '\n')
model.keywordBlock.replace(66, '\n')
model.keywordBlock.replace(67, '\n')
model.keywordBlock.replace(68, '\n')
model.keywordBlock.replace(69, '\n')
model.keywordBlock.replace(70, '\n')
model.keywordBlock.replace(71, '\n')
model.keywordBlock.replace(72, '\n')
model.keywordBlock.replace(73, 
    '\n** \n** STEP: Load\n**')
model.keywordBlock.synchVersions(
    storeNodesAndElements=False)
job = mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
    description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='3_point_bending_notched1', 
    modelPrint=OFF, multiprocessingMode=DEFAULT, name='3PB', 
    nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, 
    numThreadsPerMpiProcess=1, parallelizationMethodExplicit=DOMAIN, queue=None
    , resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', 
    waitHours=0, waitMinutes=0)
job.submit(consistencyChecking=OFF)
model.keywordBlock.synchVersions(
    storeNodesAndElements=False)
