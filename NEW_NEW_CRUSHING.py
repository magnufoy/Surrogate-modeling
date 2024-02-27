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
#input_name = 'CRUSHING_{}'
#mat_name = 'C28'
#mat_card_file = 'C28_{}.inp'
#
#try:
 # E0     = float(sys.argv[-1])
 # SIGMA0 = float(sys.argv[-2])
  #
 # WIDTH  = float(sys.argv[-3])
#  HEIGHT = float(sys.argv[-4])
  #
#  T_MIDDLE_INNER = float(sys.argv[-5])
#  T_SIDE_INNER   = float(sys.argv[-6])
#  T_OUTER        = float(sys.argv[-7])
#  #
#  MODEL          = int(sys.argv[-8])
#except:
#  exit() 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DEFINE VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
HEIGHT_MIDDLE_INNER = 43.6
L = 430.0
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
VELOCITY  = -1500.0
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
model.Material(name='C28_OUTER')
model.Material(name='C28_INNER_SIDE')
model.Material(name='C28_INNER_MIDDLE')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_OUTER', name='Outer_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=2.7, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_INNER_SIDE', name='Side_inner_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=2.0, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='C28_INNER_MIDDLE', name='Inner_middle_wall', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT, thickness=1.5, thicknessField='', thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)



CROSS_SECTION = mdb.models['CRUSHING'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
CROSS_SECTION.Line(point1=(0.0, 0.0), point2=(0.0, 21.8))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[2])
CROSS_SECTION.Line(point1=(0.0, 21.8), point2=(0.0, 37.95))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[3])
CROSS_SECTION.ParallelConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[2], entity2=CROSS_SECTION.geometry[3])
CROSS_SECTION.Line(point1=(0.0, 37.95), point2=(53.95, 37.95))
CROSS_SECTION.HorizontalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[4])
CROSS_SECTION.PerpendicularConstraint(addUndoState=False, entity1=CROSS_SECTION.geometry[3], entity2=CROSS_SECTION.geometry[4])
CROSS_SECTION.Line(point1=(63.95, 0.0), point2=(63.95, 27.95))
CROSS_SECTION.VerticalConstraint(addUndoState=False, entity=CROSS_SECTION.geometry[5])
CROSS_SECTION.FilletByRadius(curve1=CROSS_SECTION.geometry[4], curve2=CROSS_SECTION.geometry[5], nearPoint1=(45.4165077209473, 37.7963790893555), nearPoint2=(64.2001495361328, 18.3933868408203), radius=10.0)
mdb.models['CRUSHING'].Part(dimensionality=THREE_D, name='Cross-section', type=DEFORMABLE_BODY)
mdb.models['CRUSHING'].parts['Cross-section'].BaseShellExtrude(depth=430.0, sketch=CROSS_SECTION)
del CROSS_SECTION


mdb.models['CRUSHING'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=YZPLANE)
mdb.models['CRUSHING'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=XZPLANE)


mdb.models['CRUSHING'].parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[2])
mdb.models['CRUSHING'].parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[3])

# CREATE LINE TO DEVIDE INNER-MIDDLE AND INNER-SIDE
mdb.models['CRUSHING'].ConstrainedSketch(gridSpacing=21.83, name='__profile__', sheetSize=873.29, transform=mdb.models['CRUSHING'].parts['Cross-section'].MakeSketchTransform(sketchPlane=mdb.models['CRUSHING'].parts['Cross-section'].faces[10], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[5], sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['CRUSHING'].parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['CRUSHING'].sketches['__profile__'])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-21.8, 215.0), point2=(-21.8, -215.0))
mdb.models['CRUSHING'].sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[16])
mdb.models['CRUSHING'].sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=mdb.models['CRUSHING'].sketches['__profile__'].geometry[12], entity2=mdb.models['CRUSHING'].sketches['__profile__'].geometry[16])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(21.8, 215.0), point2=(21.8, -215.0))
mdb.models['CRUSHING'].sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[17])
mdb.models['CRUSHING'].sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=mdb.models['CRUSHING'].sketches['__profile__'].geometry[10], entity2=mdb.models['CRUSHING'].sketches['__profile__'].geometry[17])
mdb.models['CRUSHING'].parts['Cross-section'].PartitionFaceBySketch(faces=mdb.models['CRUSHING'].parts['Cross-section'].faces.getSequenceFromMask(('[#400 ]', ), ), sketch=mdb.models['CRUSHING'].sketches['__profile__'], sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[5])
del mdb.models['CRUSHING'].sketches['__profile__']

# CREATE CUT 1
mdb.models['CRUSHING'].ConstrainedSketch(gridSpacing=25.02, name='__profile__', sheetSize=1000.98, transform=mdb.models['CRUSHING'].parts['Cross-section'].MakeSketchTransform(sketchPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[28], sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['CRUSHING'].parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['CRUSHING'].sketches['__profile__'])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-215.0, 0.0), point2=(-205.085, -63.95))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-205.085, -63.95), point2=(-215.0, -63.95))
mdb.models['CRUSHING'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[3])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-215.0, -63.95), point2=(-224.915, 0.0))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-224.915, 0.0), point2=(-215.0, 63.95))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-215.0, 63.95), point2=(-205.085, 63.95))
mdb.models['CRUSHING'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[6])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(-205.085, 63.95), point2=(-215.0, 0.0))
mdb.models['CRUSHING'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=OFF, sketch=mdb.models['CRUSHING'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[28])
del mdb.models['CRUSHING'].sketches['__profile__']

# CREATE CUT 2
mdb.models['CRUSHING'].ConstrainedSketch(gridSpacing=25.02, name='__profile__', sheetSize=1000.98, transform=mdb.models['CRUSHING'].parts['Cross-section'].MakeSketchTransform(sketchPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[41], sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['CRUSHING'].parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['CRUSHING'].sketches['__profile__'])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(205.085, -63.95), point2=(215.0, 0.0))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(215.0, 0.0), point2=(205.085, 63.95))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(205.085, 63.95), point2=(215.0, 63.95))
mdb.models['CRUSHING'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[6])
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(215.0, 63.95), point2=(224.915, 0.0))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(224.915, 0.0), point2=(215.0, -63.95))
mdb.models['CRUSHING'].sketches['__profile__'].Line(point1=(215.0, -63.95), point2=(205.085, -63.95))
mdb.models['CRUSHING'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['CRUSHING'].sketches['__profile__'].geometry[9])
mdb.models['CRUSHING'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON, sketch=mdb.models['CRUSHING'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['CRUSHING'].parts['Cross-section'].datums[3], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['CRUSHING'].parts['Cross-section'].edges[41])
del mdb.models['CRUSHING'].sketches['__profile__']

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SETS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].Set(edges=model.parts['Cross-section'].edges.getSequenceFromMask(('[#40a24400 #512 ]', ), ), name='CLAMPED')
model.parts['Cross-section'].Set(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#1fff ]', ), ), name='Whole')
model.parts['Cross-section'].Set(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#80 ]', ), ), name='Inner_middle')
model.parts['Cross-section'].Set(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#3 ]', ), ), name='Side_inner')
model.parts['Cross-section'].Set(faces=model.parts['Cross-section'].faces.getSequenceFromMask(('[#1f7c ]', ), ), name='Outer')



#TODO Antar dette er for impactor?
model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
model.sketches['__profile__'].Line(point1=(-100.0, 0.0), point2=(100.0, 0.0))
model.sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[2])
model.Part(dimensionality=THREE_D, name='Plate_impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Plate_impactor'].AnalyticRigidSurfExtrude(depth=1.0, sketch=model.sketches['__profile__'])
del model.sketches['__profile__']

model.parts['Plate_impactor'].features['3D Analytic rigid shell-1'].setValues(depth=200.0)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ASSIGN SECTION CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Inner_middle'], sectionName='Inner_middle_wall', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Side_inner'], sectionName='Side_inner_wall', thicknessAssignment=FROM_SECTION)
model.parts['Cross-section'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=model.parts['Cross-section'].sets['Outer'], sectionName='Outer_wall', thicknessAssignment=FROM_SECTION)





#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE REFERENCE POINT - IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Plate_impactor'].ReferencePoint(point=model.parts['Plate_impactor'].InterestingPoint(model.parts['Plate_impactor'].edges[1], MIDDLE))
model.parts['Plate_impactor'].Set(name='Impactor_rp', referencePoints=(model.parts['Plate_impactor'].referencePoints[2], ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SURFACES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Plate_impactor'].Surface(name='Surf-1', side1Faces=model.parts['Plate_impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE ASSEMBLY
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.rootAssembly.DatumCsysByDefault(CARTESIAN)
assembly = model.rootAssembly
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR PROFILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='__profile__-1', part=model.parts['Cross-section'])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INSTANCE FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
assembly.Instance(dependent=ON, name='Plate_impactor-1', part=model.parts['Plate_impactor'])
assembly.rotate(angle=90.0, axisDirection=(1.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Plate_impactor-1', ))
assembly.translate(instanceList=('Plate_impactor-1', ), vector=(0.0, 0.0, 0.0))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE STEP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='Load', previous='Initial', timePeriod=TIME)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE SMOOTH AMPLITUDE CURVE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.SmoothStepAmplitude(data=((0.0, 0.0), (TIME_RAMP, 1.0)), name='Load_amp', timeSpan=STEP)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TODO Hva er dette?
model.steps['Load'].setValues(improvedDtMethod=ON, timePeriod=0.05)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INITIAL BOUNDARY CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_profile', region=assembly.instances['__profile__-1'].sets['CLAMPED'], u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', localCsys=None, name='Clamp_impactor', region=assembly.instances['Plate_impactor-1'].sets['Impactor_rp'], u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=UNSET)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE LOADING CONDITIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.VelocityBC(amplitude='Load_amp', createStepName='Load', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-3', region=assembly.instances['Plate_impactor-1'].sets['Impactor_rp'], v1=UNSET, v2=UNSET, v3=VELOCITY, vr1=UNSET, vr2=UNSET, vr3=UNSET)
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
model.fieldOutputRequests['F-Output-1'].setValues(variables=('MISES', 'PEEQ', 'LE', 'U', 'SDV', 'STATUS'))
model.HistoryOutputRequest(createStepName='Load', name='F-D', numIntervals=100, rebar=EXCLUDE, region=assembly.allInstances['Plate_impactor-1'].sets['Impactor_rp'], sectionPoints=DEFAULT, variables=('U3', 'RF3'))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE MESH
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
model.parts['Cross-section'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=ELEMENT_SIZE)
model.parts['Cross-section'].generateMesh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE INPUT FILE
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#job = mdb.Job(model='CRUSHING', name=input_name.format(MODEL))
#job.writeInput(consistencyChecking=OFF)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN INPUT FILE AND INCLUDE THE MATERIAL CARD
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#fp = open(input_name.format(MODEL)+'.inp','r')
#lines = fp.read()
#fp.close()
#lines=lines.replace('*Material, name=C28_INNER_SIDE\n','')
#lines=lines.replace('*Material, name=C28_INNER_MIDDLE\n','')
#lines=lines.replace('*Material, name=C28_OUTER','*include,input={}'.format(mat_card_file.format(MODEL)))
#fp = open(input_name.format(MODEL)+'.inp','w')
#fp.write(lines)
#fp.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPEN MATERIAL CARD FILE AND UPDATE PROPERTIES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#fp = open('mat_parameter.inc','r')
#lines = fp.read()
#fp.close()
#lines=lines.replace('<SIGMA0>',str(SIGMA0))
#lines=lines.replace('<E0>',str(E0))
#lines=lines.replace('<THICK_OUTER>',str(T_OUTER))
#fp.close()
#lines=lines.replace('<THICK_INNER_SIDE>',str(T_SIDE_INNER))
#lines=lines.replace('<THICK_INNER_MIDDLE>',str(T_MIDDLE_INNER))
#fp = open(mat_card_file.format(MODEL),'w')
#fp.write(lines)