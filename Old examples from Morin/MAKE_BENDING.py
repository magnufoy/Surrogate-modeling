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
# DEFINE INPUT FILE NAMES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
input_name    = 'BENDING_MODEL' # input file name
mat_name      = 'AA6060'        # material name
mat_card_file = 'mat.inc'       # input file with material card
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE SIZE OF THE EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
WIDTH    = 80.0
THICK    = 3.0
DIAMETER = 60.0
OFFSET   = THICK/2.0+0.05
LENGTH   = 500.0
DISTANCE = 350.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE MESH SIZE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Le = 5.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE FRICTION COEFFICIENT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
FC = 0.05
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
VELOCITY  = 700.0
TIME      = 0.12
TIME_RAMP = TIME/10.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MODEL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='BENDING')
try:
   del mdb.models['Model-1']
except:
   pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Material(name='AA6060')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='AA6060', name='AA6060', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=3.0, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
sketch = model.ConstrainedSketch(name='PROFILE_SKETCH', sheetSize=200.0)
sketch.rectangle(point1=(-(WIDTH-THICK)/2.0, -(WIDTH-THICK)/2.0), point2=((WIDTH-THICK)/2.0, (WIDTH-THICK)/2.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part = model.Part(dimensionality=THREE_D, name='PROFILE', type=DEFORMABLE_BODY)
model.parts['PROFILE'].BaseShellExtrude(depth=LENGTH, sketch=sketch)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
faces = part.faces.findAt((( (WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),),
                  ((-(WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),),
                  ((               0.0,  (WIDTH-THICK)/2.0, LENGTH/2.0),),
                  ((               0.0, -(WIDTH-THICK)/2.0, LENGTH/2.0),))
part.Set(faces=faces, name='elements')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=part.sets['elements'], sectionName='AA6060', thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part.seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=Le)
part.generateMesh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
sketch = model.ConstrainedSketch(name='IMPACTOR_SKETCH', sheetSize=200.0)
sketch.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
sketch.FixedConstraint(entity=sketch.geometry[2])
sketch.Line(point1=(DIAMETER/2.0, 100.0), point2=(DIAMETER/2.0, -100.0))
sketch.VerticalConstraint(addUndoState=False, entity=sketch.geometry[3])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='IMPACTOR', type=ANALYTIC_RIGID_SURFACE)
model.parts['IMPACTOR'].AnalyticRigidSurfRevolve(sketch=sketch)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['IMPACTOR'].ReferencePoint(point=model.parts['IMPACTOR'].InterestingPoint(model.parts['IMPACTOR'].edges[2], CENTER))
model.parts['IMPACTOR'].Set(name='REFPT', referencePoints=(model.parts['IMPACTOR'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACE FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
faces = model.parts['IMPACTOR'].faces.findAt(((DIAMETER/2.0, 0,    0),),)
model.parts['IMPACTOR'].Surface(name='IMPACTOR', side1Faces=faces)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR SUPPORT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
sketch = model.ConstrainedSketch(name='SUPPORT_SKETCH', sheetSize=200.0)
sketch.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
sketch.FixedConstraint(entity=sketch.geometry[2])
sketch.Line(point1=(DIAMETER/2.0, 100.0), point2=(DIAMETER/2.0, -100.0))
sketch.VerticalConstraint(addUndoState=False, entity=sketch.geometry[3])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR SUPPORT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='SUPPORT', type=ANALYTIC_RIGID_SURFACE)
model.parts['SUPPORT'].AnalyticRigidSurfRevolve(sketch=sketch)
model.parts['SUPPORT'].ReferencePoint(point=model.parts['SUPPORT'].InterestingPoint(model.parts['SUPPORT'].edges[2], CENTER))
model.parts['SUPPORT'].Set(name='REFPT_SUPPORT', referencePoints=(model.parts['SUPPORT'].referencePoints[2], ))
faces = model.parts['SUPPORT'].faces.findAt(((DIAMETER/2.0, 0,    0),),)
model.parts['SUPPORT'].Surface(name='SUPPORT', side1Faces=faces)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE ASSEMBLY
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
assembly = model.rootAssembly
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='PROFILE-1', part=part)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR IMPACTOR + ROTATION AND TRANSLATION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='IMPACTOR-1', part=model.parts['IMPACTOR'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('IMPACTOR-1', ))
assembly.translate(instanceList=('IMPACTOR-1', ), vector=(0.0, (WIDTH-THICK)/2.0+DIAMETER/2.0+OFFSET, LENGTH/2.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR 1ST SUPPORT + ROTATION AND TRANSLATION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='SUPPORT-1', part=model.parts['SUPPORT'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('SUPPORT-1', ))
assembly.translate(instanceList=('SUPPORT-1', ), vector=(0.0, -((WIDTH-THICK)/2.0+DIAMETER/2.0+OFFSET), LENGTH/2.0+DISTANCE/2.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR 2ND SUPPORT + ROTATION AND TRANSLATION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='SUPPORT-2', part=model.parts['SUPPORT'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('SUPPORT-2', ))
assembly.translate(instanceList=('SUPPORT-2', ), vector=(0.0, -((WIDTH-THICK)/2.0+DIAMETER/2.0+OFFSET), LENGTH/2.0-DISTANCE/2.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SMOOTH AMPLITUDE CURVE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='loading_curve', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE STEP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='loading', previous='Initial', timePeriod=TIME)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='CLAMP_1', region=assembly.instances['SUPPORT-1'].sets['REFPT_SUPPORT'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='CLAMP_2', region=assembly.instances['SUPPORT-2'].sets['REFPT_SUPPORT'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BCload', region=assembly.instances['IMPACTOR-1'].sets['REFPT'], u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='loading_curve', createStepName='loading', distributionType=UNIFORM, fieldName='', localCsys=None, name='load', region=assembly.instances['IMPACTOR-1'].sets['REFPT'], v1=UNSET, v2=-VELOCITY, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE FIELD AND HISTORY OUTPUTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=100, variables=('S', 'PEEQ', 'U', 'SDV', 'STATUS'))
model.HistoryOutputRequest(createStepName='loading', name='force_displacement', numIntervals=1000, rebar=EXCLUDE, region=assembly.allInstances['IMPACTOR-1'].sets['REFPT'], sectionPoints=DEFAULT, variables=('U2', 'RF2'))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE CONTACT PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact_properties = model.ContactProperty('CONTACT_PROPERTIES')
contact_properties.TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((FC, ), ), temperatureDependency=OFF)
contact_properties.NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE GENERAL CONTACT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact = model.ContactExp(createStepName='loading', name='GENERAL_CONTACT')
contact.includedPairs.setValuesInStep(stepName='loading', useAllstar=ON)
contact.contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'CONTACT_PROPERTIES'), ), stepName='loading')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Job = mdb.Job(model='BENDING', name=input_name)
Job.writeInput(consistencyChecking=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN INPUT FILE AND INCLUDE THE MATERIAL CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
fp = open(input_name+'.inp','r')
lines = fp.read()
fp.close()
lines=lines.replace('*Material, name={}'.format(mat_name),'*include,input={}'.format(mat_card_file))
fp = open(input_name+'.inp','w')
fp.write(lines)
fp.close()