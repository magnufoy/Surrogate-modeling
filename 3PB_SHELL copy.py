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
HEIGHT_INSIDE_WALL_SIDE = 13.45 # BRUKES IKKE
HEIGHT_INSIDE_WALL_MIDDLE = 43.6
HEIGHT = 75.9
WIDTH = 127.9
OUTER_WALL_TICKNESS = 2.7
HALF_HEIGHT_INNER = HEIGHT/2-OUTER_WALL_TICKNESS
HALF_WIDTH_INNER = WIDTH/2-OUTER_WALL_TICKNESS
LENGTH = 480.0
R = 10.0
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
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='3PB')
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
CROSS_SECTION = model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
CROSS_SECTION.Line(point1=(0.0, 0.0), point2=(0.0, HEIGHT_INSIDE_WALL_MIDDLE/2))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[2])
CROSS_SECTION.Line(point1=(0.0, HEIGHT_INSIDE_WALL_MIDDLE/2), point2=(0.0, HALF_HEIGHT_INNER))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[3])
CROSS_SECTION.ParallelConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[2], entity2=CROSS_SECTION.geometry[3])
CROSS_SECTION.Line(point1=(0.0, HALF_HEIGHT_INNER), point2=(HALF_WIDTH_INNER-R, HALF_HEIGHT_INNER))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[4])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[3], entity2=CROSS_SECTION.geometry[4])
CROSS_SECTION.Line(point1=(HALF_WIDTH_INNER, 0.0), point2=(HALF_WIDTH_INNER, HALF_HEIGHT_INNER-R))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[5])
CROSS_SECTION.FilletByRadius(curve1=CROSS_SECTION.geometry[4], curve2=CROSS_SECTION.geometry[5], nearPoint1=(45.4165077209473, 37.7963790893555), nearPoint2=(64.2001495361328, 18.3933868408203), radius=10.0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Cross-section', type=DEFORMABLE_BODY)
model.parts['Cross-section'].BaseShellExtrude(depth=LENGTH, sketch=CROSS_SECTION)
del CROSS_SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PLANES FOR MIRRORING
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=YZPLANE)
model.parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=XZPLANE)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MIRROR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=model.parts['Cross-section'].datums[2])
model.parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=model.parts['Cross-section'].datums[3])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LINE TO DEVIDE INSIDE-WALL-MIDDLE AND INSIDE-WALL-SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
LINE = model.ConstrainedSketch(gridSpacing=21.83, name='__profile__', sheetSize=873.29, transform=model.parts['Cross-section'].MakeSketchTransform(sketchPlane=model.parts['Cross-section'].faces[10], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[5], sketchOrientation=RIGHT, origin=(0.0, 0.0, LENGTH/2)))
model.parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=LINE)
LINE.Line(point1=(-HEIGHT_INSIDE_WALL_MIDDLE/2, LENGTH/2), point2=(-HEIGHT_INSIDE_WALL_MIDDLE/2, -LENGTH/2))
LINE.VerticalConstraint(addUndoState=False, entity=LINE.geometry[16])
LINE.PerpendicularConstraint(addUndoState=False, entity1=LINE.geometry[12], entity2=LINE.geometry[16])
LINE.Line(point1=(HEIGHT_INSIDE_WALL_MIDDLE/2, LENGTH/2), point2=(HEIGHT_INSIDE_WALL_MIDDLE/2, -LENGTH/2))
LINE.VerticalConstraint(addUndoState=False, entity=LINE.geometry[17])
LINE.PerpendicularConstraint(addUndoState=False, entity1=LINE.geometry[10], entity2=LINE.geometry[17])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR LINE TO DEVIDE INSIDE-WALL-MIDDLE AND INSIDE-WALL-SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].PartitionFaceBySketch(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#400 ]', ), ), sketch=LINE, sketchUpEdge=model.parts['Cross-section'].edges[5])
del LINE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
mdb.models['3PB'].parts['Cross-section'].Set(faces= mdb.models['3PB'].parts['Cross-section'].faces.getSequenceFromMask(('[#1000 ]', ), ), name='Middle_inner_wall')
mdb.models['3PB'].parts['Cross-section'].Set(faces= mdb.models['3PB'].parts['Cross-section'].faces.getSequenceFromMask(( '[#3 ]', ), ), name='Side_inner_wall')
mdb.models['3PB'].parts['Cross-section'].Set(faces= mdb.models['3PB'].parts['Cross-section'].faces.getSequenceFromMask(( '[#ffc ]', ), ), name='Thick_wall')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
mdb.models['3PB'].ConstrainedSketch(gridSpacing=24.37, name='__profile__', sheetSize=974.91, transform= mdb.models['3PB'].parts['Cross-section'].MakeSketchTransform( sketchPlane=mdb.models['3PB'].parts['Cross-section'].faces[6], sketchPlaneSide=SIDE1,  sketchUpEdge=mdb.models['3PB'].parts['Cross-section'].edges[24], sketchOrientation=RIGHT, origin=(-63.95, 0.0, 240.0)))
mdb.models['3PB'].parts['Cross-section'].projectReferencesOntoSketch(filter= COPLANAR_EDGES, sketch=mdb.models['3PB'].sketches['__profile__'])
mdb.models['3PB'].sketches['__profile__'].CircleByCenterPerimeter(center=( 37.95, -40.0), point1=(19.95, -40.0))
mdb.models['3PB'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON,  sketch=mdb.models['3PB'].sketches['__profile__'], sketchOrientation=RIGHT,  sketchPlane=mdb.models['3PB'].parts['Cross-section'].faces[6],   sketchPlaneSide=SIDE1, sketchUpEdge= mdb.models['3PB'].parts['Cross-section'].edges[24])
del mdb.models['3PB'].sketches['__profile__']
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Middle_inner_wall'], sectionName='Middle_inner', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Side_inner_wall'], sectionName='Side_inner', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Thick_wall'], sectionName='Outer', thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
assembly.Instance(dependent=ON, name='Cross-section-1', part=model.parts['Cross-section'])
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
model.parts['Cross-section'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=ELEMENT_SIZE)
model.parts['Cross-section'].generateMesh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#job = mdb.Job(model='BENDING', name=input_name)
#job.writeInput(consistencyChecking=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN INPUT FILE AND INCLUDE THE MATERIAL CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#fp = open(input_name+'.inp','r')
#lines = fp.read()
#fp.close()
#lines=lines.replace('*Material, name={}'.format(mat_name),'*include,input={}'.format(mat_card_file))
#fp = open(input_name+'.inp','w')
#fp.write(lines)
#fp.close()