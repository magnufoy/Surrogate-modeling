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
from connectorBehavior import*
import numpy as np
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE INPUT FILE NAMES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
input_name    = 'CRUSHING_MODEL' # input file name
mat_name      = 'AA6060'         # material name
mat_card_file = 'mat.inc'        # input file with material card
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE SIZE OF THE EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
WIDTH    = 80.0
THICK    = 3.0
LENGTH   = 350.0
OFFSET   = 0.1
ANGLE    = 4.0
TRIGGER  = (WIDTH-THICK)/2.0*np.tan(np.deg2rad(6.0))
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
VELOCITY  = 15000.0
TIME      = 0.01
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
model.Material(name='AA6060')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='AA6060', name='AA6060', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=3.0, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR EXTRUSION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
sketch = model.ConstrainedSketch(name='PROFILE_SKETCH', sheetSize=200.0)
sketch.rectangle(point1=(-(WIDTH-THICK)/2.0, -(WIDTH-THICK)/2.0), point2=((WIDTH-THICK)/2.0, (WIDTH-THICK)/2.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR EXTRUSION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part = model.Part(dimensionality=THREE_D, name='PROFILE', type=DEFORMABLE_BODY)
part.BaseShellExtrude(depth=LENGTH, sketch=sketch)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TRIGGER ON 1ST SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
face = part.faces.findAt((               0., -(WIDTH-THICK)/2.0, LENGTH/2.0),)
edge = part.edges.findAt(((WIDTH-THICK)/2.0, -(WIDTH-THICK)/2.0, LENGTH/2.0),)
#sketch = model.ConstrainedSketch(gridSpacing=18.06, name='CUT_1', sheetSize=722.49, transform=part.MakeSketchTransform(sketchPlane=face, sketchPlaneSide=SIDE1, sketchUpEdge=edge, sketchOrientation=RIGHT, origin=(0.0, -(WIDTH-THICK)/2.0, LENGTH/2.0)))
sketch = model.ConstrainedSketch(gridSpacing=18.06, name='CUT_1', sheetSize=722.49, transform=part.MakeSketchTransform(sketchPlane=face, sketchPlaneSide=SIDE1, sketchUpEdge=edge, sketchOrientation=RIGHT, origin=(0.0, -(WIDTH-THICK)/2.0,         0.0)))
part.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=sketch)
sketch.Line(point1=(-(WIDTH-THICK)/2.0, LENGTH-TRIGGER), point2=(0.0, LENGTH))
sketch.Line(point1=(       0.0,   LENGTH), point2=((WIDTH-THICK)/2.0, LENGTH-TRIGGER))
part.PartitionFaceBySketch(faces=face, sketch=sketch, sketchUpEdge=edge)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TRIGGER ON 2ND SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
face = part.faces.findAt(((WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),)
edge = part.edges.findAt(((WIDTH-THICK)/2.0,  (WIDTH-THICK)/2.0, LENGTH/2.0),)
sketch = model.ConstrainedSketch(gridSpacing=18.39, name='CUT_2', sheetSize=735.66, transform=part.MakeSketchTransform(sketchPlane=face, sketchPlaneSide=SIDE1, sketchUpEdge=edge, sketchOrientation=RIGHT, origin=((WIDTH-THICK)/2.0, 0.0,         0.0)))
part.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=sketch)
sketch.Line(point1=(-(WIDTH-THICK)/2.0, LENGTH-TRIGGER), point2=((WIDTH-THICK)/2.0, LENGTH-TRIGGER))
part.PartitionFaceBySketch(faces=face, sketch=sketch, sketchUpEdge=edge)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TRIGGER ON 3RD SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
face = part.faces.findAt((                0.,  (WIDTH-THICK)/2.0, LENGTH/2.0),)
edge = part.edges.findAt((-(WIDTH-THICK)/2.0,  (WIDTH-THICK)/2.0, LENGTH/2.0),)
sketch = model.ConstrainedSketch(gridSpacing=18.39, name='CUT_3', sheetSize=735.66, transform=part.MakeSketchTransform(sketchPlane=face, sketchPlaneSide=SIDE1, sketchUpEdge=edge, sketchOrientation=RIGHT, origin=(0.0,  (WIDTH-THICK)/2.0,         0.0)))
part.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=sketch)
sketch.Line(point1=(-(WIDTH-THICK)/2.0, LENGTH-TRIGGER), point2=(0.0, LENGTH))
sketch.Line(point1=(       0.0,   LENGTH), point2=((WIDTH-THICK)/2.0, LENGTH-TRIGGER))
part.PartitionFaceBySketch(faces=face, sketch=sketch, sketchUpEdge=edge)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TRIGGER ON 4TH SIDE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
face = part.faces.findAt((-(WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),)
edge = part.edges.findAt((-(WIDTH-THICK)/2.0, -(WIDTH-THICK)/2.0, LENGTH/2.0),)
sketch = model.ConstrainedSketch(gridSpacing=18.39, name='CUT_4', sheetSize=735.66, transform=part.MakeSketchTransform(sketchPlane=face, sketchPlaneSide=SIDE1, sketchUpEdge=edge, sketchOrientation=RIGHT, origin=(-(WIDTH-THICK)/2.0, 0.0,         0.0)))
part.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=sketch)
sketch.Line(point1=(-(WIDTH-THICK)/2.0, LENGTH-TRIGGER), point2=((WIDTH-THICK)/2.0, LENGTH-TRIGGER))
part.PartitionFaceBySketch(faces=face, sketch=sketch, sketchUpEdge=edge)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# REMOVE UNNECESSARY FACES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
faces = [part.faces.findAt(( (WIDTH-THICK)/2.0-1.0,  (WIDTH-THICK)/2.0, LENGTH-1.0),),
         part.faces.findAt((-(WIDTH-THICK)/2.0+1.0,  (WIDTH-THICK)/2.0, LENGTH-1.0),),
         part.faces.findAt(( (WIDTH-THICK)/2.0-1.0, -(WIDTH-THICK)/2.0, LENGTH-1.0),),
         part.faces.findAt((-(WIDTH-THICK)/2.0+1.0, -(WIDTH-THICK)/2.0, LENGTH-1.0),),
         part.faces.findAt(( (WIDTH-THICK)/2.0,                 0., LENGTH-1.0),),
         part.faces.findAt((-(WIDTH-THICK)/2.0,                 0., LENGTH-1.0),)]
part.RemoveFaces(deleteCells=False, faceList=faces)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Whole
faces = part.faces.findAt((( (WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),),
                          ((-(WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),),
                          ((               0.0,  (WIDTH-THICK)/2.0, LENGTH/2.0),),
                          ((               0.0, -(WIDTH-THICK)/2.0, LENGTH/2.0),))
part.Set(faces=faces, name='elements')
# Clamp
edges = part.edges.findAt((( (WIDTH-THICK)/2.0,                0.0, 0.0),),
                          ((-(WIDTH-THICK)/2.0,                0.0, 0.0),),
                          ((               0.0,  (WIDTH-THICK)/2.0, 0.0),),
                          ((               0.0, -(WIDTH-THICK)/2.0, 0.0),))
part.Set(edges=edges, name='CLAMP')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=part.sets['elements'], sectionName='AA6060', thicknessAssignment=FROM_SECTION)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
part.seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=Le)
face = part.faces.findAt((                0.,  (WIDTH-THICK)/2.0, LENGTH/2.0),)
part.setMeshControls(elemShape=QUAD, regions=(face,), technique=STRUCTURED)
face = part.faces.findAt((                0., -(WIDTH-THICK)/2.0, LENGTH/2.0),)
part.setMeshControls(elemShape=QUAD, regions=(face,), technique=STRUCTURED)
face = part.faces.findAt(( (WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),)
part.setMeshControls(elemShape=QUAD, regions=(face,), technique=STRUCTURED)
face = part.faces.findAt((-(WIDTH-THICK)/2.0,                0.0, LENGTH/2.0),)
part.setMeshControls(elemShape=QUAD, regions=(face,), technique=STRUCTURED)
part.generateMesh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR THE IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
sketch = model.ConstrainedSketch(name='IMPACTOR_SKETCH', sheetSize=200.0)
sketch.Line(point1=(-200.0, 0.0), point2=(200.0, 0.0))
sketch.HorizontalConstraint(addUndoState=False, entity=sketch.geometry[2])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.Part(dimensionality=THREE_D, name='IMPACTOR', type=ANALYTIC_RIGID_SURFACE)
model.parts['IMPACTOR'].AnalyticRigidSurfExtrude(depth=400.0, sketch=sketch)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['IMPACTOR'].ReferencePoint(point=model.parts['IMPACTOR'].InterestingPoint(model.parts['IMPACTOR'].edges[1], MIDDLE))
nreference = model.parts['IMPACTOR'].referencePoints.keys()[0]
model.parts['IMPACTOR'].Set(name='REFPT', referencePoints=(model.parts['IMPACTOR'].referencePoints[nreference], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACE FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
faces = model.parts['IMPACTOR'].faces.findAt((( 0.0, 0,    0),),)
model.parts['IMPACTOR'].Surface(name='IMPACTOR', side2Faces= faces)
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
assembly.rotate(angle=90.0, axisDirection=(1.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('IMPACTOR-1', ))
assembly.translate(instanceList=('IMPACTOR-1', ), vector=(0.0, 0.0, LENGTH+OFFSET))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SMOOTH AMPLITUDE CURVE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='loading_curve', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE STEP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=OFF, name='loading', previous='Initial', timePeriod=TIME,timeIncrementationMethod=AUTOMATIC_EBE)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='CLAMP', region=assembly.instances['PROFILE-1'].sets['CLAMP'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='BCload', region=assembly.instances['IMPACTOR-1'].sets['REFPT'], u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='loading_curve', createStepName='loading', distributionType=UNIFORM, fieldName='', localCsys=None, name='load', region=assembly.instances['IMPACTOR-1'].sets['REFPT'], v1=UNSET, v2=UNSET, v3=-VELOCITY, vr1=UNSET, vr2=UNSET, vr3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE FIELD AND HISTORY OUTPUTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=100, variables=('S', 'PEEQ', 'U', 'SDV'))
model.HistoryOutputRequest(createStepName='loading', name='force_displacement', numIntervals=1000, rebar=EXCLUDE, region=assembly.allInstances['IMPACTOR-1'].sets['REFPT'], sectionPoints=DEFAULT, variables=('U3', 'RF3'))
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
Job = mdb.Job(model='CRUSHING', name=input_name)
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