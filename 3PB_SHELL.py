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
input_name = '3PB_BENDING_NOTCHED'
mat_name = 'C28'
mat_card_file = 'C28.inp'
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
WIDTH = 127.9
HEIGHT = 75.9
HEIGHT_SIDE_INNER = 13.45
HEIGHT_MIDDLE_INNER = 43.6
R = 10.0
L = 480.0
T_OUTER = 2.7
T_SIDE_INNER = 2.0
T_MIDDLE_INNER = 1.5
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE MESH SIZE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
ELEMENT_SIZE = 5.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE FRICTION COEFFICIENT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
FRICTION_COEFFICIENT = 0.05
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
VELOCITY  = 700.0
TIME      = 0.05
TIME_RAMP = TIME/10.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MODEL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='3PB_BENDING_NOTCHED')
try:
   del mdb.models['Model-1']
except:
   pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Material(name='C28')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Middle_inner', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=T_MIDDLE_INNER, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Side_inner', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=T_SIDE_INNER, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Outer', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF,temperature=GRADIENT, thickness=T_OUTER, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CROSS_SECTION = model.ConstrainedSketch(name='CROSS_SECTION', sheetSize=200.0)
CROSS_SECTION.Line(point1=(0.0, 0.0), point2=(0.0, HEIGHT_MIDDLE_INNER/2))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[2])
CROSS_SECTION.Line(point1=(0.0, HEIGHT_MIDDLE_INNER/2), point2=(0.0, HEIGHT/2))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[3])
CROSS_SECTION.ParallelConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[2], entity2=CROSS_SECTION.geometry[3])
CROSS_SECTION.Line(point1=(0.0, 0.0), point2=(0.0, -HEIGHT_MIDDLE_INNER/2))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[4])
CROSS_SECTION.ParallelConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[2], entity2=CROSS_SECTION.geometry[4])
CROSS_SECTION.Line(point1=(0.0, -HEIGHT_MIDDLE_INNER/2), point2=(0.0, -HEIGHT/2))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[5])
CROSS_SECTION.ParallelConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[4], entity2=CROSS_SECTION.geometry[5])
CROSS_SECTION.Line(point1=(0.0, HEIGHT/2), point2=(53.95, HEIGHT/2))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[6])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[3], entity2=CROSS_SECTION.geometry[6])
CROSS_SECTION.Line(point1=(0.0, HEIGHT/2), point2=(-53.95, HEIGHT/2))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[7])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[3], entity2=CROSS_SECTION.geometry[7])
CROSS_SECTION.Line(point1=(0.0, -HEIGHT/2), point2=(53.95, -HEIGHT/2))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[8])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[5], entity2=CROSS_SECTION.geometry[8])
CROSS_SECTION.Line(point1=(0.0, -HEIGHT/2), point2=(-53.95, -HEIGHT/2))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[9])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[5], entity2=CROSS_SECTION.geometry[9])
CROSS_SECTION.CircleByCenterPerimeter(center=(-53.95, -34.95), point1=(-53.95, -HEIGHT/2))
CROSS_SECTION.Line(point1=(-53.95, -34.95), point2=(-56.95, -34.95))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[11])
CROSS_SECTION.CoincidentConstraint(addUndoState=False, entity1=CROSS_SECTION.vertices[10], entity2= CROSS_SECTION.geometry[10])
CROSS_SECTION.breakCurve(curve1=CROSS_SECTION.geometry[10], curve2=CROSS_SECTION.geometry[11], point1=(-52.8506393432617, -32.0841178894043), point2=(-55.0026931762695, -34.9176025390625))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[12], ))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.constraints[37], ))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[11], ))
CROSS_SECTION.CircleByCenterPerimeter(center=(-53.95, 34.95), point1=(-53.95, HEIGHT/2))
CROSS_SECTION.Line(point1=(-53.95, 34.95), point2=(-56.95, 34.95))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[15])
CROSS_SECTION.CoincidentConstraint(addUndoState=False, entity1=CROSS_SECTION.vertices[12], entity2=CROSS_SECTION.geometry[14])
CROSS_SECTION.breakCurve(curve1=CROSS_SECTION.geometry[14], curve2= CROSS_SECTION.geometry[15], point1=(-55.7310485839844, 33.0573425292969), point2=(-55.4055557250977, 34.6818466186523))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[17], ))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[15], ))
CROSS_SECTION.CircleByCenterPerimeter(center=(53.95, 34.95), point1=(53.95, HEIGHT/2))
CROSS_SECTION.Line(point1=(53.95, 34.95), point2=(56.95, 34.95))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[19])
CROSS_SECTION.CoincidentConstraint(addUndoState=False, entity1=CROSS_SECTION.vertices[14], entity2=CROSS_SECTION.geometry[18])
CROSS_SECTION.breakCurve(curve1=CROSS_SECTION.geometry[18], curve2=CROSS_SECTION.geometry[19], point1=(55.1857604980469, 32.6559982299805), point2=(55.2821464538574, 34.9650039672852))
CROSS_SECTION.delete(objectList=( CROSS_SECTION.geometry[20], ))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[19], ))
CROSS_SECTION.CircleByCenterPerimeter(center=(53.95, -34.95), point1=(53.95, -HEIGHT/2))
CROSS_SECTION.Line(point1=(53.95, -34.95), point2=(56.95, -34.95))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[23])
CROSS_SECTION.CoincidentConstraint(addUndoState=False, entity1=CROSS_SECTION.vertices[16], entity2=CROSS_SECTION.geometry[22])
CROSS_SECTION.breakCurve(curve1=CROSS_SECTION.geometry[22], curve2=CROSS_SECTION.geometry[23], point1=(56.3024559020996, -36.884765625), point2=(55.1151924133301, -35.2687149047852))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[25], ))
CROSS_SECTION.delete(objectList=(CROSS_SECTION.geometry[23], ))
CROSS_SECTION.Line(point1=(56.95, 34.95), point2=(56.95, -34.95))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[26])
CROSS_SECTION.TangentConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[21], entity2=CROSS_SECTION.geometry[26])
CROSS_SECTION.Line(point1=(-56.95, 34.95), point2=(-56.95, -34.95))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[27])
CROSS_SECTION.TangentConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[16], entity2=CROSS_SECTION.geometry[27])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Profile_shell', type=DEFORMABLE_BODY)
model.parts['Profile_shell'].BaseShellExtrude(depth=L, sketch=CROSS_SECTION)
del CROSS_SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
EXTRUSION = model.ConstrainedSketch(gridSpacing=24.29, name='__profile__', sheetSize=971.92, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[0], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[6], sketchOrientation=RIGHT, origin=(0.0, 0.0, 240.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=EXTRUSION)
EXTRUSION.Line(point1=(-HEIGHT_MIDDLE_INNER/2, -240.0), point2=(-HEIGHT_MIDDLE_INNER/2, 240.0))
EXTRUSION.VerticalConstraint(addUndoState=False, entity=EXTRUSION.geometry[16])
EXTRUSION.PerpendicularConstraint(addUndoState=False, entity1=EXTRUSION.geometry[4], entity2=EXTRUSION.geometry[16])
EXTRUSION.Line(point1=(HEIGHT_MIDDLE_INNER/2, -240.0), point2=(HEIGHT_MIDDLE_INNER/2, -47.8779907226562))
EXTRUSION.VerticalConstraint(addUndoState=False, entity=EXTRUSION.geometry[17])
EXTRUSION.Line(point1=(HEIGHT_MIDDLE_INNER/2, -240.0), point2=(HEIGHT_MIDDLE_INNER/2, 240.0))
EXTRUSION.VerticalConstraint(addUndoState=False, entity=EXTRUSION.geometry[17])
EXTRUSION.PerpendicularConstraint(addUndoState=False, entity1=EXTRUSION.geometry[6], entity2=EXTRUSION.geometry[17])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Profile_shell'].PartitionFaceBySketch(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#1 ]', ), ), sketch=EXTRUSION, sketchUpEdge=model.parts['Profile_shell'].edges[6])
del EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#2 ]', ), ), name='Middle_inner_wall')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#5 ]', ), ), name='Side_inner_wall')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#1fe8 ]', ), ), name='Thick_wall')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CUT = model.ConstrainedSketch(gridSpacing=24.46, name='__profile__', sheetSize=978.57, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[16], sketchOrientation=RIGHT, origin=(-56.95, 0.0, 240.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=CUT)
CUT.CircleByCenterPerimeter(center=(HEIGHT/2, -40.0), point1=(19.95, -20.05))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=ON, sketch=CUT, sketchOrientation=RIGHT, sketchPlane=model.parts['Profile_shell'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[16])
del CUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Middle_inner_wall'], sectionName='Middle_inner', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Side_inner_wall'], sectionName='Side_inner', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Thick_wall'], sectionName='Outer', thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#3fa67 ]', ), ), name='Thick_wall')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#3fe67 ]', ), ), name='Thick_wall')
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
IMPACTOR_PROFILE = model.ConstrainedSketch(name='IMPACTOR_PROFILE', sheetSize=200.0)
IMPACTOR_PROFILE.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
IMPACTOR_PROFILE.FixedConstraint(entity=IMPACTOR_PROFILE.geometry[2])
IMPACTOR_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0))
IMPACTOR_PROFILE.VerticalConstraint(addUndoState=False, entity=IMPACTOR_PROFILE.geometry[3])
#--------------------------------------------------------------------------------------------------------
# CREATE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
impactor_part = model.Part(dimensionality=THREE_D, name='Impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Impactor'].AnalyticRigidSurfRevolve(sketch=IMPACTOR_PROFILE)
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
SUPPORT_PROFILE = model.ConstrainedSketch(name='SUPPORT_PROFILE', sheetSize=200.0)
SUPPORT_PROFILE.ConstructionLine(point1=(0.0,  -100.0), point2=(0.0, 100.0))
SUPPORT_PROFILE.FixedConstraint(entity=SUPPORT_PROFILE.geometry[2])
SUPPORT_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0))
SUPPORT_PROFILE.VerticalConstraint(addUndoState=False, entity=SUPPORT_PROFILE.geometry[3])
#--------------------------------------------------------------------------------------------------------
# CREATE PART FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
support_part = model.Part(dimensionality=THREE_D, name='Support', type=ANALYTIC_RIGID_SURFACE)
model.parts['Support'].AnalyticRigidSurfRevolve(sketch=SUPPORT_PROFILE)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Impactor'].ReferencePoint(point=model.parts['Impactor'].InterestingPoint(model.parts['Impactor'].edges[1], CENTER))
model.parts['Impactor'].Set(name='Impactor_RP', referencePoints=(model.parts['Impactor'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - SUPPORT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Support'].ReferencePoint(point=model.parts['Support'].InterestingPoint(model.parts['Support'].edges[1], CENTER))
model.parts['Support'].Set(name='Support_RP', referencePoints=(model.parts['Support'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Impactor'].Surface(name='Impactor', side2Faces=model.parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
model.parts['Support'].Surface(name='Support', side2Faces=model.parts['Support'].faces.getSequenceFromMask(('[#1 ]', ), ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE ASSEMBLY
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
assembly = model.rootAssembly
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR PROFILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Profile_shell-1', part=model.parts['Profile_shell'])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR SUPPORT 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Support-1', part=model.parts['Support'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-1', ))
assembly.translate(instanceList=('Support-1', ), vector=(0.0, 69.5, 52.5))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR SUPPORT 2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Support-2', part=model.parts['Support'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-2', ))
assembly.translate(instanceList=('Support-2', ), vector=(0.0, 69.5, 427.5))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Impactor-1', part=model.parts['Impactor'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Impactor-1', ))
assembly.translate(instanceList=('Impactor-1', ), vector=(0.0, -69.5, 240.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE STEP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='Load', previous='Initial', timePeriod=TIME)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SMOOTH AMPLITUDE CURVE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='Amp-1', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_support1', region=assembly.instances['Support-1'].sets['Support_RP'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_support_2', region=assembly.instances['Support-2'].sets['Support_RP'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_impactor', region=assembly.instances['Impactor-1'].sets['Impactor_RP'], u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='Amp-1', createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=None, name='Load', region=assembly.instances['Impactor-1'].sets['Impactor_RP'], v1=UNSET, v2=VELOCITY, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE CONTACT PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact_properties = model.ContactProperty('Int_prop')
contact_properties.TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((FRICTION_COEFFICIENT, ), ), temperatureDependency=OFF)
contact_properties.NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE GENERAL CONTACT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact = model.ContactExp(createStepName='Load', name='Interaction')
contact.includedPairs.setValuesInStep(stepName='Load', useAllstar=ON)
contact.contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'Int_prop'), ), stepName='Load')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE FIELD AND HISTORY OUTPUTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.HistoryOutputRequest(createStepName='Load', name='F-D', numIntervals=100, rebar=EXCLUDE, region=assembly.allInstances['Impactor-1'].sets['Impactor_RP'], sectionPoints=DEFAULT, variables=('U2', 'RF2'))
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=100, variables=('MISES', 'PEEQ', 'U', 'SDV', 'STATUS'))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Profile_shell'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=ELEMENT_SIZE)
model.parts['Profile_shell'].generateMesh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
job = mdb.Job(model='BENDING', name=input_name)
job.writeInput(consistencyChecking=OFF)
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