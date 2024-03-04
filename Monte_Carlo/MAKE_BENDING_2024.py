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
import sys
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE INPUT FILE NAMES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
input_name    = 'BENDING_{}'
mat_name      = 'C28'
mat_card_file = 'C28_{}.inp'

try:
   E0                          = float(sys.argv[-1])
   SIGMA0                      = float(sys.argv[-2])
 
   WIDTH                       = float(sys.argv[-3])
   HEIGHT                      = float(sys.argv[-4])
   
   INSIDE_WALL_MIDDLE_TICKNESS = float(sys.argv[-5])
   INSIDE_WALL_SIDE_TICKNESS   = float(sys.argv[-6])
   OUTER_WALL_TICKNESS         = float(sys.argv[-7])
 
   MODEL                       = int(sys.argv[-8])

except:
  exit() 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#WIDTH = 127.9
#HEIGHT= 75.9
#INSIDE_WALL_MIDDLE_TICKNESS =1.5
#INSIDE_WALL_SIDE_TICKNESS   = 2
#OUTER_WALL_TICKNESS         = 2.7

HEIGHT_DIFFERENCE = 0.5

LENGTH = 480.0

HALF_HEIGHT               = (HEIGHT - OUTER_WALL_TICKNESS)/2
HALF_HEIGHT_CENTER        = HALF_HEIGHT + HEIGHT_DIFFERENCE
HALF_WIDTH                = (WIDTH - OUTER_WALL_TICKNESS)/2

HEIGHT_INSIDE_WALL_SIDE = 13.45
HEIGHT_INSIDE_WALL_MIDDLE = HALF_HEIGHT_CENTER - HEIGHT_INSIDE_WALL_SIDE

RADIUS = 10.0
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
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='BENDING')
try:
   del mdb.models['Model-1']
except:
   pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Material(name='C28_OUTER_WALL')
model.Material(name='C28_INSIDE_WALL_SIDE')
model.Material(name='C28_INSIDE_WALL_MIDDLE')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_OUTER_WALL'        , name='OUTER_WALL'        , nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=OUTER_WALL_TICKNESS        , thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_INSIDE_WALL_SIDE'  , name='INSIDE_WALL_SIDE'  , nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=INSIDE_WALL_SIDE_TICKNESS  , thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_INSIDE_WALL_MIDDLE', name='INSIDE_WALL_MIDDLE', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=INSIDE_WALL_MIDDLE_TICKNESS, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CROSS_SECTION = model.ConstrainedSketch(name='cross-section', sheetSize=200.0)
CROSS_SECTION.Line(point1=(       0.0,                       0.0), point2=(                0.0, HEIGHT_INSIDE_WALL_MIDDLE))
CROSS_SECTION.Line(point1=(       0.0, HEIGHT_INSIDE_WALL_MIDDLE), point2=(                0.0,        HALF_HEIGHT_CENTER))
CROSS_SECTION.Line(point1=(       0.0,        HALF_HEIGHT_CENTER), point2=(HALF_WIDTH - RADIUS,               HALF_HEIGHT))
CROSS_SECTION.Line(point1=(HALF_WIDTH,                       0.0), point2=(         HALF_WIDTH,      HALF_HEIGHT - RADIUS))
CROSS_SECTION.FilletByRadius(curve1=CROSS_SECTION.geometry[4], curve2=CROSS_SECTION.geometry[5], nearPoint1=(45.4165077209473, 37.7963790893555), nearPoint2=(64.2001495361328, 18.3933868408203), radius=10.0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Cross-section', type=DEFORMABLE_BODY)
model.parts['Cross-section'].BaseShellExtrude(depth=LENGTH, sketch=CROSS_SECTION)
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
LINE = model.ConstrainedSketch(gridSpacing=21.83, name='line', sheetSize=873.29, transform=model.parts['Cross-section'].MakeSketchTransform(sketchPlane=model.parts['Cross-section'].faces[10], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[5], sketchOrientation=RIGHT, origin=(0.0, 0.0, LENGTH/2)))
model.parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=LINE)
LINE.Line(point1=(-HEIGHT_INSIDE_WALL_MIDDLE, LENGTH/2), point2=(-HEIGHT_INSIDE_WALL_MIDDLE, -LENGTH/2))
LINE.Line(point1=( HEIGHT_INSIDE_WALL_MIDDLE, LENGTH/2), point2=( HEIGHT_INSIDE_WALL_MIDDLE, -LENGTH/2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR LINE TO DEVIDE INSIDE-WALL-MIDDLE AND INSIDE-WALL-SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].PartitionFaceBySketch(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#400 ]', ), ), sketch=LINE, sketchUpEdge=model.parts['Cross-section'].edges[5])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CUT = model.ConstrainedSketch(gridSpacing=24.37, name='cut', sheetSize=974.91, transform= model.parts['Cross-section'].MakeSketchTransform( sketchPlane=model.parts['Cross-section'].faces[6], sketchPlaneSide=SIDE1,  sketchUpEdge=model.parts['Cross-section'].edges[24], sketchOrientation=RIGHT, origin=(-63.95, 0.0, 240.0)))
model.parts['Cross-section'].projectReferencesOntoSketch(filter= COPLANAR_EDGES, sketch=model.sketches['cut'])
CUT.CircleByCenterPerimeter(center=( 37.95, -40.0), point1=(19.95, -40.0)) # TODO Parameterize
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXTRUDE CUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON,  sketch=CUT, sketchOrientation=RIGHT,  sketchPlane=model.parts['Cross-section'].faces[6],   sketchPlaneSide=SIDE1, sketchUpEdge= model.parts['Cross-section'].edges[24])
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
IMPACTOR_PROFILE = model.ConstrainedSketch(name='IMPACTOR_PROFILE', sheetSize=200.0)
IMPACTOR_PROFILE.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0)) # TODO Parameterize
IMPACTOR_PROFILE.FixedConstraint(entity=IMPACTOR_PROFILE.geometry[2])
IMPACTOR_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0)) # TODO Parameterize
IMPACTOR_PROFILE.VerticalConstraint(addUndoState=False, entity=IMPACTOR_PROFILE.geometry[3])
#--------------------------------------------------------------------------------------------------------
# CREATE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
impactor_part = model.Part(dimensionality=THREE_D, name='Impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Impactor'].AnalyticRigidSurfRevolve(sketch=IMPACTOR_PROFILE)
model.rootAssembly.regenerate()  
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
SUPPORT_PROFILE = model.ConstrainedSketch(name='SUPPORT_PROFILE', sheetSize=200.0)
SUPPORT_PROFILE.ConstructionLine(point1=(0.0,  -100.0), point2=(0.0, 100.0)) # TODO Parameterize
SUPPORT_PROFILE.FixedConstraint(entity=SUPPORT_PROFILE.geometry[2])
SUPPORT_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0)) # TODO Parameterize
SUPPORT_PROFILE.VerticalConstraint(addUndoState=False, entity=SUPPORT_PROFILE.geometry[3])
#--------------------------------------------------------------------------------------------------------
# CREATE PART FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
support_part = model.Part(dimensionality=THREE_D, name='Support', type=ANALYTIC_RIGID_SURFACE)
model.parts['Support'].AnalyticRigidSurfRevolve(sketch=SUPPORT_PROFILE)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].Set(faces= model.parts['Cross-section'].faces.getSequenceFromMask(( '[#3fe6b ]', ), ), name='OUTER_WALL'        )
model.parts['Cross-section'].Set(faces= model.parts['Cross-section'].faces.getSequenceFromMask(( '[#190 ]'  , ), ), name='INSIDE_WALL_SIDE'  )
model.parts['Cross-section'].Set(faces= model.parts['Cross-section'].faces.getSequenceFromMask(( '[#4 ]'    , ), ), name='INSIDE_WALL_MIDDLE')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['INSIDE_WALL_MIDDLE'], sectionName='INSIDE_WALL_MIDDLE', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['INSIDE_WALL_SIDE']  , sectionName='INSIDE_WALL_SIDE'  , thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['OUTER_WALL']        , sectionName='OUTER_WALL'        , thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Impactor'].ReferencePoint(point=model.parts['Impactor'].InterestingPoint(model.parts['Impactor'].edges[1], CENTER))
model.parts['Impactor'].Set(name='IMPACTOR_PP', referencePoints=(model.parts['Impactor'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - SUPPORT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Support'].ReferencePoint(point=model.parts['Support'].InterestingPoint(model.parts['Support'].edges[1], CENTER))
model.parts['Support'].Set(name='SUPPORT_RP', referencePoints=(model.parts['Support'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Impactor'].Surface(name='Impactor', side2Faces=model.parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
model.parts['Support' ].Surface(name='Support' , side2Faces=model.parts['Support' ].faces.getSequenceFromMask(('[#1 ]', ), ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE ASSEMBLY
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
assembly = model.rootAssembly
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR PROFILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Cross-section', part=model.parts['Cross-section'])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR SUPPORT 1 #TODO Parameterize vectors
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Support-1', part=model.parts['Support'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-1', ))
assembly.translate(instanceList=('Support-1', ), vector=(0.0, 69.5, 52.5))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR SUPPORT 2 #TODO Parameterize vectors
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Support-2', part=model.parts['Support'])
assembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-2', ))
assembly.translate(instanceList=('Support-2', ), vector=(0.0, 69.5, 427.5))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR IMPACTOR #TODO Parameterize vectors
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
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='Load_amp', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_support1' , region=assembly.instances['Support-1' ].sets['SUPPORT_RP' ], u1=SET, u2=SET  , u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_support_2', region=assembly.instances['Support-2' ].sets['SUPPORT_RP' ], u1=SET, u2=SET  , u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_impactor' , region=assembly.instances['Impactor-1'].sets['IMPACTOR_PP'], u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='Load_amp', createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=None, name='Load', region=assembly.instances['Impactor-1'].sets['IMPACTOR_PP'], v1=UNSET, v2=VELOCITY, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE CONTACT PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact_properties = model.ContactProperty('Interaction')
contact_properties.TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((FRICTION_COEFFICIENT, ), ), temperatureDependency=OFF)
contact_properties.NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE GENERAL CONTACT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact = model.ContactExp(createStepName='Load', name='Interaction')
contact.includedPairs.setValuesInStep(stepName='Load', useAllstar=ON)
contact.contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'Interaction'), ), stepName='Load')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE FIELD AND HISTORY OUTPUTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=100, variables=('MISES', 'PEEQ', 'U', 'SDV', 'STATUS'))
model.HistoryOutputRequest(createStepName='Load', name='F-D', numIntervals=100, rebar=EXCLUDE, region=assembly.allInstances['Impactor-1'].sets['IMPACTOR_PP'], sectionPoints=DEFAULT, variables=('U2', 'RF2'))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=ELEMENT_SIZE)
model.parts['Cross-section'].generateMesh()
model.rootAssembly.regenerate()
model.rootAssembly.regenerate()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
job = mdb.Job(model='BENDING', name=input_name.format(MODEL))
job.writeInput(consistencyChecking=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN INPUT FILE AND INCLUDE THE MATERIAL CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
fp = open(input_name.format(MODEL)+'.inp','r')
lines = fp.read()
fp.close()
lines=lines.replace('*Material, name=C28_INSIDE_WALL_SIDE\n','')
lines=lines.replace('*Material, name=C28_INSIDE_WALL_MIDDLE\n','')
lines=lines.replace('*Material, name=C28_OUTER_WALL','*include,input={}'.format(mat_card_file.format(MODEL)))

fp = open(input_name.format(MODEL)+'.inp','w')
fp.write(lines)
fp.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN MATERIAL CARD FILE AND UPDATE PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
fp = open('mat_parameter.inc','r')
lines = fp.read()
fp.close()
lines=lines.replace('<SIGMA0>',str(SIGMA0))
lines=lines.replace('<E0>',str(E0))
lines=lines.replace('<OUTER_WALL_TICKNESS>',str(OUTER_WALL_TICKNESS))
lines=lines.replace('<INSIDE_WALL_SIDE_TICKNESS>',str(INSIDE_WALL_SIDE_TICKNESS))
lines=lines.replace('<INSIDE_WALL_MIDDLE_TICKNESS>',str(INSIDE_WALL_MIDDLE_TICKNESS))

fp = open(mat_card_file.format(MODEL),'w')
fp.write(lines)