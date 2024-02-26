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
input_name = 'CRUSHING_{}'
mat_name = 'C28'
mat_card_file = 'C28_{}.inp'
#
try:
  E0     = float(sys.argv[-1])
  SIGMA0 = float(sys.argv[-2])
  #
  WIDTH  = float(sys.argv[-3])
  HEIGHT = float(sys.argv[-4])
  #
  T_MIDDLE_INNER = float(sys.argv[-5])
  T_SIDE_INNER   = float(sys.argv[-6])
  T_OUTER        = float(sys.argv[-7])
  #
  MODEL          = int(sys.argv[-8])
except:
  exit() 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
HEIGHT_MIDDLE_INNER = 43.6
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
model = mdb.Model(modelType=STANDARD_EXPLICIT, name='CRUSHING')
try:
   del mdb.models['Model-1']
except:
   pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR CROSS-SECTION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

CROSS_SECTION = model.ConstrainedSketch(name='CROSS_SECTION', sheetSize=200.0)
model.sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.0, HEIGHT_MIDDLE_INNER/2))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[2])
model.sketches['__profile__'].Line(point1=(0.0, HEIGHT_MIDDLE_INNER/2), point2=(0.0, 37.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[2], entity2=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.0, -HEIGHT_MIDDLE_INNER/2))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[4])
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[2], entity2=model.sketches['__profile__'].geometry[4])
model.sketches['__profile__'].Line(point1=(0.0, -HEIGHT_MIDDLE_INNER/2), point2=(0.0, -37.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[5])
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[4], entity2=model.sketches['__profile__'].geometry[5])
model.sketches['__profile__'].Line(point1=(0.0, 37.95), point2=(53.95, 37.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[6])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[3], entity2=model.sketches['__profile__'].geometry[6])
model.sketches['__profile__'].Line(point1=(0.0, 37.95), point2=(-53.95, 37.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[7])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[3], entity2=model.sketches['__profile__'].geometry[7])
model.sketches['__profile__'].Line(point1=(0.0, -37.95), point2=(53.95, -37.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[8])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[5], entity2=model.sketches['__profile__'].geometry[8])
model.sketches['__profile__'].Line(point1=(0.0, -37.95), point2=(-53.95, -37.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[9])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[5], entity2=model.sketches['__profile__'].geometry[9])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(-53.95, 34.95), point1=(-53.95, 37.95))
model.sketches['__profile__'].Line(point1=(-53.95, 34.95), point2=(-56.95, 34.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[11])
model.sketches['__profile__'].CoincidentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].vertices[10], entity2=model.sketches['__profile__'].geometry[10])
model.sketches['__profile__'].breakCurve(curve1=model.sketches['__profile__'].geometry[10], curve2=model.sketches['__profile__'].geometry[11], point1=(-54.6662406921387, 32.6842269897461), point2=(-55.3110313415527, 35.0740623474121))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[13], ))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[11], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(-53.95, -34.95), point1=(-53.95, -37.95))
model.sketches['__profile__'].Line(point1=(-53.95, -34.95), point2=(-56.95, -34.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[15])
model.sketches['__profile__'].CoincidentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].vertices[12], entity2=model.sketches['__profile__'].geometry[14])
model.sketches['__profile__'].breakCurve(curve1=model.sketches['__profile__'].geometry[14], curve2=model.sketches['__profile__'].geometry[15], point1=(-56.834587097168, -37.5181121826172), point2=(-55.2094573974609, -35.3890113830566))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[16], ))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[15], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(53.95, 34.95), point1=(53.95, 37.95))
model.sketches['__profile__'].Line(point1=(53.95, 34.95), point2=(56.95, 34.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[19])
model.sketches['__profile__'].CoincidentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].vertices[14], entity2=model.sketches['__profile__'].geometry[18])
model.sketches['__profile__'].breakCurve(curve1=model.sketches['__profile__'].geometry[18], curve2=model.sketches['__profile__'].geometry[19], point1=(54.4764976501465, 31.5016136169434), point2=(54.9246559143066, 34.8566970825195))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[20], ))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[19], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(53.95, -34.95), point1=(53.95, -37.95))
model.sketches['__profile__'].Line(point1=(53.95, -34.95), point2=(56.95, -34.95))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[23])
model.sketches['__profile__'].CoincidentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].vertices[16], entity2=model.sketches['__profile__'].geometry[22])
model.sketches['__profile__'].breakCurve(curve1=model.sketches['__profile__'].geometry[22], curve2=model.sketches['__profile__'].geometry[23], point1=(52.1236839294434, -32.133056640625), point2=(55.2607917785645, -35.1526260375977))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[25], ))
model.sketches['__profile__'].delete(objectList=(model.sketches['__profile__'].geometry[23], ))
model.sketches['__profile__'].Line(point1=(56.95, 34.95), point2=(56.95, -34.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[26])
model.sketches['__profile__'].TangentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[21], entity2=model.sketches['__profile__'].geometry[26])
model.sketches['__profile__'].Line(point1=(-56.95, 34.95), point2=(-56.95, -34.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[27])
model.sketches['__profile__'].TangentConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[12], entity2=model.sketches['__profile__'].geometry[27])
model.Part(dimensionality=THREE_D, name='Profile_shell', type=DEFORMABLE_BODY)
model.parts['Profile_shell'].BaseShellExtrude(depth=430.0, sketch=model.sketches['__profile__'])
del model.sketches['__profile__']
model.ConstrainedSketch(gridSpacing=21.75, name='__profile__', sheetSize=870.05, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[1], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[11], sketchOrientation=RIGHT, origin=(-26.975, 37.95, 215.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=model.sketches['__profile__'])
model.sketches['__profile__'].Line(point1=(-26.975, 215.0), point2=(-80.93, 205.085))
model.sketches['__profile__'].Line(point1=(-26.975, 215.0), point2=(26.98, 205.09))
del model.sketches['__profile__']
model.ConstrainedSketch(gridSpacing=21.75, name='__profile__', sheetSize=870.05, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[1], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[12], sketchOrientation=RIGHT, origin=(-26.975, 37.95, 215.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=model.sketches['__profile__'])
model.sketches['__profile__'].Spot(point=(-205.085, 80.93))
model.sketches['__profile__'].Line(point1=(-215.0, 26.975), point2=(-205.085, 80.93))
model.sketches['__profile__'].Line(point1=(-205.085, 80.93), point2=(-201.297025135253, 101.543230844662))
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[13], entity2=model.sketches['__profile__'].geometry[14])
model.sketches['__profile__'].Line(point1=(-215.0, 26.975), point2=(-215.0, 100.27607879648))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[15])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[2], entity2=model.sketches['__profile__'].geometry[15])
model.sketches['__profile__'].Line(point1=(-215.0, 100.27607879648), point2=(-201.297025135253, 101.543230844662))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=ON, sketch=model.sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=model.parts['Profile_shell'].faces[1], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[12])
del model.sketches['__profile__']
model.ConstrainedSketch(gridSpacing=21.66, name='__profile__', sheetSize=866.74, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[2], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[14], sketchOrientation=RIGHT, origin=(-26.975, 37.95, 215.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=model.sketches['__profile__'])
model.sketches['__profile__'].Line(point1=(-26.975, -215.0), point2=(26.98, -205.085))
model.sketches['__profile__'].Line(point1=(26.98, -205.085), point2=(92.0550000007823, -193.126541562275))
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[13], entity2=model.sketches['__profile__'].geometry[14])
model.sketches['__profile__'].Line(point1=(92.0550000007823, -193.126541562275), point2=(92.0550000007823, -220.851257324219))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[15])
model.sketches['__profile__'].Line(point1=(92.0550000007823, -220.851257324219), point2=(26.975, -215.0))
model.sketches['__profile__'].Line(point1=(26.975, -215.0), point2=(-26.975, -215.0))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[17])
model.sketches['__profile__'].ParallelConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[7], entity2=model.sketches['__profile__'].geometry[17])
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=ON, sketch=model.sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=model.parts['Profile_shell'].faces[2], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[14])
del model.sketches['__profile__']
model.ConstrainedSketch(gridSpacing=21.99, name='__profile__', sheetSize=879.93, transform=model.parts['Profile_shell'].MakeSketchTransform(sketchPlane=model.parts['Profile_shell'].faces[5], sketchPlaneSide=SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[23], sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=model.sketches['__profile__'])
model.sketches['__profile__'].Line(point1=(-HEIGHT_MIDDLE_INNER/2, 215.0), point2=(-HEIGHT_MIDDLE_INNER/2, -215.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[16])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[4], entity2=model.sketches['__profile__'].geometry[16])
model.sketches['__profile__'].Line(point1=(HEIGHT_MIDDLE_INNER/2, 215.0), point2=(HEIGHT_MIDDLE_INNER/2, -215.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[17])
model.sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=model.sketches['__profile__'].geometry[11], entity2=model.sketches['__profile__'].geometry[17])
model.parts['Profile_shell'].PartitionFaceBySketch(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#20 ]', ), ), sketch=model.sketches['__profile__'], sketchUpEdge=model.parts['Profile_shell'].edges[23])
del model.sketches['__profile__']
model.parts['Profile_shell'].Set(edges=model.parts['Profile_shell'].edges.getSequenceFromMask(('[#40a24400 #512 ]', ), ), name='CLAMPED')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#1fff ]', ), ), name='Whole')
model.Material(name='C28')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Inner_middle_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=1.5, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Side_inner_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=2.0, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28', name='Outer_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=2.7, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#80 ]', ), ), name='Inner_middle')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#3 ]', ), ), name='Side_inner')
model.parts['Profile_shell'].Set(faces=model.parts['Profile_shell'].faces.getSequenceFromMask(('[#1f7c ]', ), ), name='Outer')
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Inner_middle'], sectionName='Inner_middle_wall', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Side_inner'], sectionName='Side_inner_wall', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Profile_shell'].sets['Outer'], sectionName='Outer_wall', thicknessAssignment=FROM_SECTION)
model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
model.sketches['__profile__'].Line(point1=(-100.0, 0.0), point2=(100.0, 0.0))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[2])
model.Part(dimensionality=THREE_D, name='Plate_impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Plate_impactor'].AnalyticRigidSurfExtrude(depth=1.0, sketch=model.sketches['__profile__'])
del model.sketches['__profile__']
model.parts['Plate_impactor'].features['3D Analytic rigid shell-1'].setValues(depth=200.0)
model.parts['Plate_impactor'].regenerate()
model.parts['Plate_impactor'].ReferencePoint(point=model.parts['Plate_impactor'].InterestingPoint(model.parts['Plate_impactor'].edges[1], MIDDLE))
model.parts['Plate_impactor'].Set(name='Impactor_rp', referencePoints=(model.parts['Plate_impactor'].referencePoints[2], ))
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
model.rootAssembly.Instance(dependent=ON, name='Profile_shell-1', part=model.parts['Profile_shell'])
model.rootAssembly.Instance(dependent=ON, name='Plate_impactor-1', part=model.parts['Plate_impactor'])
model.rootAssembly.rotate(angle=90.0, axisDirection=(1.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Plate_impactor-1', ))
model.rootAssembly.translate(instanceList=('Plate_impactor-1', ), vector=(0.0, 0.0, 431.0))
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='Load', previous='Initial', timePeriod=0.5)
model.SmoothStepAmplitude(data=((0.0, 0.0), (0.01, 1.0)), name='Load_amp', timeSpan=STEP)
model.steps['Load'].setValues(improvedDtMethod=ON, timePeriod=0.05)
model.HistoryOutputRequest(createStepName='Load', name='F-D', numIntervals=100, rebar=EXCLUDE, region=model.rootAssembly.allInstances['Plate_impactor-1'].sets['Impactor_rp'], sectionPoints=DEFAULT, variables=('U3', 'RF3'))
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Profile_clamped', region=model.rootAssembly.instances['Profile_shell-1'].sets['CLAMPED'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_impactor', region=model.rootAssembly.instances['Plate_impactor-1'].sets['Impactor_rp'], u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=UNSET)
model.VelocityBC(amplitude='Load_amp', createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-3', region=model.rootAssembly.instances['Plate_impactor-1'].sets['Impactor_rp'], v1=UNSET, v2=UNSET, v3=-1500.0, vr1=UNSET, vr2=UNSET, vr3=UNSET)
model.ContactProperty('Interaction')
model.interactionProperties['Interaction'].NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
model.interactionProperties['Interaction'].TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((0.05, ), ), temperatureDependency=OFF)
model.ContactExp(createStepName='Load', name='Interaction')
model.interactions['Interaction'].includedPairs.setValuesInStep(stepName='Load', useAllstar=ON)
model.interactions['Interaction'].contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'Interaction'), ), stepName='Load')
model.parts['Plate_impactor'].Surface(name='Surf-1', side1Faces=model.parts['Plate_impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
model.rootAssembly.regenerate()
model.fieldOutputRequests['F-Output-1'].setValues(variables=('MISES', 'PEEQ', 'LE', 'U', 'SDV', 'STATUS'))
