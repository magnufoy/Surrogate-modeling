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
import numpy as np
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE INPUT FILE NAMES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
input_name    = 'CRUSHING_{}'
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

HEIGHT_DIFFERENCE         = 0.5

LENGTH                    = 430.0

HALF_HEIGHT               = (HEIGHT - OUTER_WALL_TICKNESS)/2
HALF_HEIGHT_CENTER        = HALF_HEIGHT + HEIGHT_DIFFERENCE
HALF_WIDTH                = (WIDTH - OUTER_WALL_TICKNESS)/2

HEIGHT_INSIDE_WALL_SIDE   = 13.45
HEIGHT_INSIDE_WALL_MIDDLE = HALF_HEIGHT_CENTER - HEIGHT_INSIDE_WALL_SIDE

RADIUS                    = 10.0

CUT_DEPTH                 = 9.915

LENGHT_IMPACTOR           = 200.0
DEPTH_IMPACTOR            = 1.0
GAP_IMPACTOR              = -1
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
VELOCITY  = 1500.0
TIME      = 0.05
TIME_RAMP = TIME/10.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MODEL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='CRUSHING')
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
model.parts['Cross-section'].PartitionFaceBySketch(faces=model.parts['Cross-section'].faces.findAt(( 0, 0, 0),), sketch=LINE, sketchUpEdge=model.parts['Cross-section'].edges[5])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CUT 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CUT_1= model.ConstrainedSketch(gridSpacing=25.02, name='cut_1', sheetSize=1000.98, transform=model.parts['Cross-section'].MakeSketchTransform(sketchPlane=model.parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[28], sketchOrientation=LEFT, origin=(0.0, 0.0, LENGTH/2)))
model.parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=CUT_1)
CUT_1.Line(point1=(LENGTH/2 - CUT_DEPTH, -HALF_WIDTH), point2=(            LENGTH/2,         0.0))
CUT_1.Line(point1=(            LENGTH/2,         0.0), point2=(LENGTH/2 - CUT_DEPTH,  HALF_WIDTH))
CUT_1.Line(point1=(LENGTH/2 - CUT_DEPTH,  HALF_WIDTH), point2=(            LENGTH/2,  HALF_WIDTH))
CUT_1.Line(point1=(            LENGTH/2,  HALF_WIDTH), point2=(LENGTH/2 + CUT_DEPTH,         0.0))
CUT_1.Line(point1=(LENGTH/2 + CUT_DEPTH,         0.0), point2=(            LENGTH/2, -HALF_WIDTH))
CUT_1.Line(point1=(            LENGTH/2, -HALF_WIDTH), point2=(LENGTH/2 - CUT_DEPTH, -HALF_WIDTH))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXTRUDE CUT 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].CutExtrude(flipExtrudeDirection=OFF, sketch=CUT_1, sketchOrientation=LEFT, sketchPlane=model.parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[28])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CUT 2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
CUT_2 = model.ConstrainedSketch(gridSpacing=25.02, name='cut_2', sheetSize=1000.98, transform=model.parts['Cross-section'].MakeSketchTransform(sketchPlane=model.parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[41], sketchOrientation=RIGHT, origin=(0.0, 0.0, LENGTH/2)))
model.parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=CUT_2)
CUT_2.Line(point1=(LENGTH/2 - CUT_DEPTH, -HALF_WIDTH), point2=(            LENGTH/2,         0.0))
CUT_2.Line(point1=(            LENGTH/2,         0.0), point2=(LENGTH/2 - CUT_DEPTH,  HALF_WIDTH))
CUT_2.Line(point1=(LENGTH/2 - CUT_DEPTH,  HALF_WIDTH), point2=(            LENGTH/2,  HALF_WIDTH))
CUT_2.Line(point1=(            LENGTH/2,  HALF_WIDTH), point2=(LENGTH/2 + CUT_DEPTH,         0.0))
CUT_2.Line(point1=(LENGTH/2 + CUT_DEPTH,         0.0), point2=(            LENGTH/2, -HALF_WIDTH))
CUT_2.Line(point1=(            LENGTH/2, -HALF_WIDTH), point2=(LENGTH/2 - CUT_DEPTH, -HALF_WIDTH))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXTRUDE CUT 2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON, sketch=CUT_2, sketchOrientation=RIGHT, sketchPlane=model.parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Cross-section'].edges[41])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
IMPACTOR = model.ConstrainedSketch(name='IMPACTOR', sheetSize=200)
IMPACTOR.Line(point1=(-LENGHT_IMPACTOR/2, 0.0), point2=(LENGHT_IMPACTOR/2, 0.0)) 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='Plate_impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Plate_impactor'].AnalyticRigidSurfExtrude(depth = DEPTH_IMPACTOR, sketch=IMPACTOR)
model.parts['Plate_impactor'].features['3D Analytic rigid shell-1'].setValues(depth=LENGHT_IMPACTOR) 
model.parts['Plate_impactor'].regenerate() # Fra Benjamin for  vise hele platen
model.rootAssembly.regenerate() # Fra Benjamin for  vise hele platen
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INSIDE WALL SIDE
faces_inside_wall_side = model.parts['Cross-section'].faces.findAt((( 0,    HEIGHT_INSIDE_WALL_MIDDLE + HEIGHT_INSIDE_WALL_SIDE/2, 0),),
                                                                   (( 0,    HEIGHT_INSIDE_WALL_MIDDLE + HEIGHT_INSIDE_WALL_SIDE/2, LENGTH),),
                                                                   (( 0, -(HEIGHT_INSIDE_WALL_MIDDLE + HEIGHT_INSIDE_WALL_SIDE/2), 0),),)
model.parts['Cross-section'].Set(faces=faces_inside_wall_side, name='INSIDE_WALL_SIDE'  )

# INSIDE WALL MIDDLE
faces_inside_wall_middle = model.parts['Cross-section'].faces.findAt((( 0, 0, 0),),)
model.parts['Cross-section'].Set(faces=faces_inside_wall_middle, name='INSIDE_WALL_MIDDLE')

# WHOLE
faces_whole = model.parts['Cross-section'].faces.getByBoundingBox(xMin = -HALF_WIDTH, yMin= -HALF_HEIGHT_CENTER, zMin = 0,
                                                                  xMax =HALF_WIDTH, yMax =  HALF_HEIGHT_CENTER, zMax = LENGTH)
model.parts['Cross-section'].Set(faces=faces_whole, name='WHOLE')

#OUTER
model.parts['Cross-section'].SetByBoolean(name ='OUTER_WALL', operation=DIFFERENCE,
                                                                   sets=(model.parts['Cross-section'].sets['WHOLE'],
                                                                         model.parts['Cross-section'].sets['INSIDE_WALL_MIDDLE'],
                                                                         model.parts['Cross-section'].sets['INSIDE_WALL_SIDE'],))

#CLAMPED
edges_clamp = model.parts['Cross-section'].edges.getByBoundingBox(xMin = -HALF_WIDTH, yMin= -HALF_HEIGHT_CENTER, zMin = LENGTH,
                                                                  xMax =HALF_WIDTH, yMax =  HALF_HEIGHT_CENTER, zMax = LENGTH)
model.parts['Cross-section'].Set(edges= edges_clamp, name='CLAMPED')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['INSIDE_WALL_MIDDLE'], sectionName='INSIDE_WALL_MIDDLE', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['INSIDE_WALL_SIDE'], sectionName='INSIDE_WALL_SIDE', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['OUTER_WALL'], sectionName='OUTER_WALL', thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Plate_impactor'].ReferencePoint(point=model.parts['Plate_impactor'].InterestingPoint(model.parts['Plate_impactor'].edges[1], MIDDLE))
model.parts['Plate_impactor'].Set(name='IMPACTOR_RP', referencePoints=(model.parts['Plate_impactor'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Plate_impactor'].Surface(name='Plate_impactor', side1Faces=model.parts['Plate_impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
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
# CREATE INSTANCE FOR IMPACTOR 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='IMPACTOR-1', part=model.parts['Plate_impactor'])
assembly.rotate(angle=90.0, axisDirection=(1.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('IMPACTOR-1', ))
assembly.translate(instanceList=('IMPACTOR-1', ), vector=(0.0, 0.0, GAP_IMPACTOR)) 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE STEP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='loading', previous='Initial', timePeriod=TIME)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SMOOTH AMPLITUDE CURVE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='Load_amp', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TSIZE TIMESTEP
model.steps['loading'].setValues(improvedDtMethod=ON, timePeriod=TIME)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_cross-section', region=assembly.instances['Cross-section'].sets['CLAMPED'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_impactor', region=assembly.instances['IMPACTOR-1'].sets['IMPACTOR_RP'], u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE loading' CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='Load_amp', createStepName='loading', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-3', region=assembly.instances['IMPACTOR-1'].sets['IMPACTOR_RP'], v1=UNSET, v2=UNSET, v3=VELOCITY, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE CONTACT PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact_properties = model.ContactProperty('Interaction')
contact_properties.TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((FRICTION_COEFFICIENT, ), ), temperatureDependency=OFF)
contact_properties.NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE GENERAL CONTACT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
contact = model.ContactExp(createStepName='loading', name='Interaction')
contact.includedPairs.setValuesInStep(stepName='loading', useAllstar=ON)
contact.contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'Interaction'), ), stepName='loading')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE FIELD AND HISTORY OUTPUTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=2, variables=('MISES', 'PEEQ', 'LE', 'U', 'SDV', 'STATUS'))
model.HistoryOutputRequest(createStepName='loading', name='F-D', numIntervals=1000, rebar=EXCLUDE, region=assembly.allInstances['IMPACTOR-1'].sets['IMPACTOR_RP'], sectionPoints=DEFAULT, variables=('U3', 'RF3'))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=ELEMENT_SIZE)
model.parts['Cross-section'].generateMesh()
model.rootAssembly.regenerate()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
job = mdb.Job(model='CRUSHING', name=input_name.format(MODEL))
job.writeInput(consistencyChecking=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE A LIST WITH ELEMENT LABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
OUTER_WALL_elements = model.rootAssembly.instances['Cross-section'].sets['OUTER_WALL'].elements
OUTER_WALL_element_labels = [element.label for element in OUTER_WALL_elements]
length_OUTER_WALL_element_labels= len(OUTER_WALL_element_labels)

INSIDE_WALL_SIDE_elements = model.rootAssembly.instances['Cross-section'].sets['INSIDE_WALL_SIDE'].elements
INSIDE_WALL_SIDE_element_labels = [element.label for element in INSIDE_WALL_SIDE_elements]
length_INSIDE_WALL_SIDE_element_labels= len(INSIDE_WALL_SIDE_element_labels)

INSIDE_WALL_MIDDLE_elements = model.rootAssembly.instances['Cross-section'].sets['INSIDE_WALL_MIDDLE'].elements
INSIDE_WALL_MIDDLE_element_labels = [element.label for element in INSIDE_WALL_MIDDLE_elements]
length_INSIDE_WALL_MIDDLE_element_labels= len(INSIDE_WALL_MIDDLE_element_labels)

OUTER_WALL_mean = 2.7
OUTER_WALL_std_dev = 1

INSIDE_WALL_SIDE_mean = 1.7
INSIDE_WALL_SIDE_std_dev = 1

INSIDE_WALL_MIDDLE_mean = 1.2
INSIDE_WALL_MIDDLE_std_dev = 1

OUTER_WALL_values = np.random.normal(OUTER_WALL_mean, OUTER_WALL_std_dev, length_OUTER_WALL_element_labels)
INSIDE_WALL_SIDE_values = np.random.normal(INSIDE_WALL_SIDE_mean, INSIDE_WALL_SIDE_std_dev, length_INSIDE_WALL_SIDE_element_labels)
INSIDE_WALL_MIDDLE_values = np.random.normal(INSIDE_WALL_MIDDLE_mean, INSIDE_WALL_MIDDLE_std_dev, length_INSIDE_WALL_MIDDLE_element_labels)

fp = open(input_name.format(MODEL)+'.inp','r')
lines = fp.read()
fp.close()

lines = lines.replace(OUTER_WALL_TICKNESS + ', 5\n', '')
lines = lines.replace(INSIDE_WALL_MIDDLE_TICKNESS + ', 5\n', '')
lines = lines.replace(INSIDE_WALL_SIDE_TICKNESS + ', 5\n', '')

lines = lines.replace("*Shell Section, elset=OUTER_WALL, material=C28_OUTER_WALL\n", "*SHELL SECTION, ELSET=ELEMENT_SET, MATERIAL=C28, SHELL THICKNESS=OUTER_DISTRIBUTION_THICKNESS\n               1.,        5\n*DISTRIBUTION TABLE, NAME=OUTER_DISTRIBUTION_TABLE_THICKNESS\nLENGTH,\n*DISTRIBUTION, LOCATION=ELEMENT, TABLE=OUTER_DISTRIBUTION_TABLE_THICKNESS, NAME=OUTER_DISTRIBUTION_THICKNESS\n        ,               1.\n replace me")
for i in range(length_OUTER_WALL_element_labels):
   lines = lines.replace('replace me', str(OUTER_WALL_element_labels[i]) + ',' + str(OUTER_WALL_values[i]) + '\n' + 'replace me')
lines = lines.replace('replace me', '')

lines = lines.replace("*Shell Section, elset=INSIDE_WALL_SIDE, material=C28_INSIDE_WALL_SIDE\n", "*SHELL SECTION, ELSET=ELEMENT_SET, MATERIAL=C28, SHELL THICKNESS=INSIDE_WALL_SIDE_DISTRIBUTION_THICKNESS\n               1.,        5\n*DISTRIBUTION TABLE, NAME=INSIDE_WALL_SIDE_DISTRIBUTION_TABLE_THICKNESS\nLENGTH,\n*DISTRIBUTION, LOCATION=ELEMENT, TABLE=INSIDE_WALL_SIDE_DISTRIBUTION_TABLE_THICKNESS, NAME=INSIDE_WALL_SIDE_DISTRIBUTION_THICKNESS\n        ,               1.\n replace me")
for i in range(length_INSIDE_WALL_SIDE_element_labels):
   lines = lines.replace('replace me', str(INSIDE_WALL_SIDE_element_labels[i]) + ',' + str(INSIDE_WALL_SIDE_values[i]) + '\n' + 'replace me')
lines = lines.replace('replace me', '')

lines = lines.replace("*Shell Section, elset=INSIDE_WALL_MIDDLE, material=C28_INSIDE_WALL_MIDDLE\n", "*SHELL SECTION, ELSET=ELEMENT_SET, MATERIAL=C28, SHELL THICKNESS=INSIDE_WALL_MIDDLE_DISTRIBUTION_THICKNESS\n               1.,        5\n*DISTRIBUTION TABLE, NAME=INSIDE_WALL_MIDDLE_DISTRIBUTION_TABLE_THICKNESS\nLENGTH,\n*DISTRIBUTION, LOCATION=ELEMENT, TABLE=INSIDE_WALL_MIDDLE_DISTRIBUTION_TABLE_THICKNESS, NAME=INSIDE_WALL_MIDDLE_DISTRIBUTION_THICKNESS\n        ,               1.\n replace me")
for i in range(length_INSIDE_WALL_MIDDLE_element_labels):
   lines = lines.replace('replace me', str(INSIDE_WALL_MIDDLE_element_labels[i]) + ',' + str(INSIDE_WALL_MIDDLE_values[i]) + '\n' + 'replace me')
lines = lines.replace('replace me', '')

fp = open(input_name.format(MODEL)+'.inp','w')
fp.write(lines)
fp.close()
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