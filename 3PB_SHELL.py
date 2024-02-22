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



model = mdb.models(name='Model-1')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE EMPTY MATERIAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

model.ConstrainedSketch(name='__profile__', sheetSize=200.0)
model.sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, 21.8))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[2])
model.sketches['__profile__'].Line(point1=(0.0, 21.8), point2=(
    0.0, 37.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=model.sketches['__profile__'].geometry[2], 
    entity2=model.sketches['__profile__'].geometry[3])
model.sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, -21.8))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[4])
model.sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=model.sketches['__profile__'].geometry[2], 
    entity2=model.sketches['__profile__'].geometry[4])
model.sketches['__profile__'].Line(point1=(0.0, -21.8), point2=
    (0.0, -37.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[5])
model.sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=model.sketches['__profile__'].geometry[4], 
    entity2=model.sketches['__profile__'].geometry[5])
model.sketches['__profile__'].Line(point1=(0.0, 37.95), point2=
    (53.95, 37.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[6])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[3], entity2=
    model.sketches['__profile__'].geometry[6])
model.sketches['__profile__'].Line(point1=(0.0, 37.95), point2=
    (-53.95, 37.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[7])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[3], entity2=
    model.sketches['__profile__'].geometry[7])
model.sketches['__profile__'].Line(point1=(0.0, -37.95), 
    point2=(53.95, -37.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[8])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[5], entity2=
    model.sketches['__profile__'].geometry[8])
model.sketches['__profile__'].Line(point1=(0.0, -37.95), 
    point2=(-53.95, -37.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[9])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[5], entity2=
    model.sketches['__profile__'].geometry[9])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    -53.95, -34.95), point1=(-53.95, -37.95))
model.sketches['__profile__'].Line(point1=(-53.95, -34.95), 
    point2=(-56.95, -34.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[11])
model.sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].vertices[10], entity2=
    model.sketches['__profile__'].geometry[10])
model.sketches['__profile__'].breakCurve(curve1=
    model.sketches['__profile__'].geometry[10], curve2=
    model.sketches['__profile__'].geometry[11], point1=(
    -52.8506393432617, -32.0841178894043), point2=(-55.0026931762695, 
    -34.9176025390625))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[12], ))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].constraints[37], ))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[11], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    -53.95, 34.95), point1=(-53.95, 37.95))
model.sketches['__profile__'].Line(point1=(-53.95, 34.95), 
    point2=(-56.95, 34.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[15])
model.sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].vertices[12], entity2=
    model.sketches['__profile__'].geometry[14])
model.sketches['__profile__'].breakCurve(curve1=
    model.sketches['__profile__'].geometry[14], curve2=
    model.sketches['__profile__'].geometry[15], point1=(
    -55.7310485839844, 33.0573425292969), point2=(-55.4055557250977, 
    34.6818466186523))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[17], ))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[15], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    53.95, 34.95), point1=(53.95, 37.95))
model.sketches['__profile__'].Line(point1=(53.95, 34.95), 
    point2=(56.95, 34.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[19])
model.sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].vertices[14], entity2=
    model.sketches['__profile__'].geometry[18])
model.sketches['__profile__'].breakCurve(curve1=
    model.sketches['__profile__'].geometry[18], curve2=
    model.sketches['__profile__'].geometry[19], point1=(
    55.1857604980469, 32.6559982299805), point2=(55.2821464538574, 
    34.9650039672852))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[20], ))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[19], ))
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    53.95, -34.95), point1=(53.95, -37.95))
model.sketches['__profile__'].Line(point1=(53.95, -34.95), 
    point2=(56.95, -34.95))
model.sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    model.sketches['__profile__'].geometry[23])
model.sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].vertices[16], entity2=
    model.sketches['__profile__'].geometry[22])
model.sketches['__profile__'].breakCurve(curve1=
    model.sketches['__profile__'].geometry[22], curve2=
    model.sketches['__profile__'].geometry[23], point1=(
    56.3024559020996, -36.884765625), point2=(55.1151924133301, 
    -35.2687149047852))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[25], ))
model.sketches['__profile__'].delete(objectList=(
    model.sketches['__profile__'].geometry[23], ))
model.sketches['__profile__'].Line(point1=(56.95, 34.95), 
    point2=(56.95, -34.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[26])
model.sketches['__profile__'].TangentConstraint(addUndoState=
    False, entity1=model.sketches['__profile__'].geometry[21], 
    entity2=model.sketches['__profile__'].geometry[26])
model.sketches['__profile__'].Line(point1=(-56.95, 34.95), 
    point2=(-56.95, -34.95))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[27])
model.sketches['__profile__'].TangentConstraint(addUndoState=
    False, entity1=model.sketches['__profile__'].geometry[16], 
    entity2=model.sketches['__profile__'].geometry[27])

model.Part(dimensionality=THREE_D, name='Profile_shell', type=
    DEFORMABLE_BODY)
model.parts['Profile_shell'].BaseShellExtrude(depth=480.0, 
    sketch=model.sketches['__profile__'])
del model.sketches['__profile__']


model.ConstrainedSketch(gridSpacing=24.29, name='__profile__', 
    sheetSize=971.92, transform=
    model.parts['Profile_shell'].MakeSketchTransform(
    sketchPlane=model.parts['Profile_shell'].faces[0], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=model.parts['Profile_shell'].edges[6], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 240.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    model.sketches['__profile__'])
model.sketches['__profile__'].Line(point1=(-21.8, -240.0), 
    point2=(-21.8, 240.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[16])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[4], entity2=
    model.sketches['__profile__'].geometry[16])
model.sketches['__profile__'].Line(point1=(21.8, 240.0), 
    point2=(0.0, -240.0))
model.sketches['__profile__'].undo()
model.sketches['__profile__'].Line(point1=(21.8, -240.0), 
    point2=(21.8, -47.8779907226562))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[17])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[6], entity2=
    model.sketches['__profile__'].geometry[17])
model.sketches['__profile__'].undo()
model.sketches['__profile__'].Line(point1=(21.8, -240.0), 
    point2=(-558.67, 230.755))
model.sketches['__profile__'].undo()
model.sketches['__profile__'].Line(point1=(21.8, -240.0), 
    point2=(21.8, 240.0))
model.sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=model.sketches['__profile__'].geometry[17])
model.sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    model.sketches['__profile__'].geometry[6], entity2=
    model.sketches['__profile__'].geometry[17])


model.parts['Profile_shell'].PartitionFaceBySketch(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#1 ]', ), ), sketch=model.sketches['__profile__'], 
    sketchUpEdge=model.parts['Profile_shell'].edges[6])
del model.sketches['__profile__']


model.parts['Profile_shell'].Set(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#2 ]', ), ), name='Middle_inner_wall')
model.parts['Profile_shell'].Set(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#5 ]', ), ), name='Side_inner_wall')
model.parts['Profile_shell'].Set(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#1fe8 ]', ), ), name='Thick_wall')
model.ConstrainedSketch(gridSpacing=24.46, name='__profile__', 
    sheetSize=978.57, transform=
    model.parts['Profile_shell'].MakeSketchTransform(
    sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=model.parts['Profile_shell'].edges[16], 
    sketchOrientation=RIGHT, origin=(-56.95, 0.0, 240.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    model.sketches['__profile__'])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    37.95, -40.0), point1=(19.95, -20.05))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=
    OFF, sketch=model.sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    model.parts['Profile_shell'].faces[5], sketchPlaneSide=
    SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[16])
del model.sketches['__profile__']


model.ConstrainedSketch(gridSpacing=24.25, name='__profile__', 
    sheetSize=970.12, transform=
    model.parts['Profile_shell'].MakeSketchTransform(
    sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=model.parts['Profile_shell'].edges[17], 
    sketchOrientation=RIGHT, origin=(-56.95, -0.744097, 241.19493)))
model.parts['Profile_shell'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    model.sketches['__profile__'])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    38.694097, -41.19493), point1=(20.694097, -21.24493))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=
    OFF, sketch=model.sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    model.parts['Profile_shell'].faces[5], sketchPlaneSide=
    SIDE1, sketchUpEdge=model.parts['Profile_shell'].edges[17])
del model.sketches['__profile__']


model.ConstrainedSketch(gridSpacing=24.25, name='__profile__', 
    sheetSize=970.12, transform=
    model.parts['Profile_shell'].MakeSketchTransform(
    sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=model.parts['Profile_shell'].edges[31], 
    sketchOrientation=RIGHT, origin=(-56.95, -0.744097, 241.19493)))
model.parts['Profile_shell'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    model.sketches['__profile__'])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    -38.694097, 41.19493), point1=(-35.694097, 14.4928233415358))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=ON
    , sketch=model.sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    model.parts['Profile_shell'].edges[31])
del model.sketches['__profile__']
del model.parts['Profile_shell'].features['Cut extrude-2']


model.parts['Profile_shell'].deleteFeatures(('Cut extrude-1', 
    'Cut extrude-3'))
model.ConstrainedSketch(gridSpacing=24.46, name='__profile__', 
    sheetSize=978.57, transform=
    model.parts['Profile_shell'].MakeSketchTransform(
    sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=model.parts['Profile_shell'].edges[16], 
    sketchOrientation=RIGHT, origin=(-56.95, 0.0, 240.0)))
model.parts['Profile_shell'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    model.sketches['__profile__'])
model.sketches['__profile__'].CircleByCenterPerimeter(center=(
    37.95, -40.0), point1=(19.95, -20.05))
model.parts['Profile_shell'].CutExtrude(flipExtrudeDirection=ON
    , sketch=model.sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=model.parts['Profile_shell'].faces[5], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    model.parts['Profile_shell'].edges[16])
del model.sketches['__profile__']


model.Material(name='C28')
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='C28', name='Middle_inner', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=1.5, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='C28', name='Side_inner', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=2.0, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
model.HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='C28', name='Outer', nodalThicknessField=
    '', numIntPts=5, poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=
    GRADIENT, thickness=2.7, thicknessField='', thicknessModulus=None, 
    thicknessType=UNIFORM, useDensity=OFF)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    model.parts['Profile_shell'].sets['Middle_inner_wall'], 
    sectionName='Middle_inner', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    model.parts['Profile_shell'].sets['Side_inner_wall'], 
    sectionName='Side_inner', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    model.parts['Profile_shell'].sets['Thick_wall'], 
    sectionName='Outer', thicknessAssignment=FROM_SECTION)
model.parts['Profile_shell'].Set(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#3fa67 ]', ), ), name='Thick_wall')
model.parts['Profile_shell'].Set(faces=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#3fe67 ]', ), ), name='Thick_wall')
#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
SUPPORT_PROFILE = model.ConstrainedSketch(name='SUPPORT_PROFILE', sheetSize=200.0)
SUPPORT_PROFILE.ConstructionLine(point1=(0.0,  -100.0), point2=(0.0, 100.0))
SUPPORT_PROFILE.FixedConstraint(entity=SUPPORT_PROFILE.geometry[2])
SUPPORT_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0))
SUPPORT_PROFILE.VerticalConstraint(addUndoState=False, entity=model.sketches['__profile__'].geometry[3])
#--------------------------------------------------------------------------------------------------------
# MAKE PART FOR IMPACTOR
#--------------------------------------------------------------------------------------------------------
impactor_part = model.Part(dimensionality=THREE_D, name='Impactor', type=ANALYTIC_RIGID_SURFACE)
model.parts['Impactor'].AnalyticRigidSurfRevolve(sketch=model.sketches['__profile__'])

#--------------------------------------------------------------------------------------------------------
# CREATE SKETCH FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
IMPACTOR_PROFILE = model.ConstrainedSketch(name='IMPACTOR_PROFILE', sheetSize=200.0)
IMPACTOR_PROFILE.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
IMPACTOR_PROFILE.FixedConstraint(entity=IMPACTOR_PROFILE.geometry[2])
IMPACTOR_PROFILE.Line(point1=(30.0, -100.0), point2=(30.0, 100.0))
IMPACTOR_PROFILE.VerticalConstraint(addUndoState=False, entity=IMPACTOR_PROFILE.geometry[3])
#--------------------------------------------------------------------------------------------------------
# MAKE PART FOR SUPPORT
#--------------------------------------------------------------------------------------------------------
support_part = model.Part(dimensionality=THREE_D, name='Support', type=ANALYTIC_RIGID_SURFACE)
model.parts['Support'].AnalyticRigidSurfRevolve(sketch=SUPPORT_PROFILE)



model.parts['Impactor'].ReferencePoint(point=model.parts['Impactor'].InterestingPoint(model.parts['Impactor'].edges[1], CENTER))
model.parts['Support'].ReferencePoint(point=model.parts['Support'].InterestingPoint(model.parts['Support'].edges[1], CENTER))

model.parts['Impactor'].Set(name='Impactor_RP', referencePoints=(model.parts['Impactor'].referencePoints[2], ))
model.parts['Support'].Set(name='Support_RP', referencePoints=(model.parts['Support'].referencePoints[2], ))

model.parts['Impactor'].Surface(name='Impactor', side2Faces=model.parts['Impactor'].faces.getSequenceFromMask(('[#1 ]', ), ))
model.parts['Support'].Surface(name='Support', side2Faces=model.parts['Support'].faces.getSequenceFromMask(('[#1 ]', ), ))

model.rootAssembly.DatumCsysByDefault(CARTESIAN)
model.rootAssembly.Instance(dependent=ON, name=
    'Profile_shell-1', part=model.parts['Profile_shell'])
model.rootAssembly.Instance(dependent=ON, name='Support-1', 
    part=model.parts['Support'])
model.rootAssembly.Instance(dependent=ON, name='Support-2', 
    part=model.parts['Support'])
model.rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 
    1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-2', ))
model.rootAssembly.translate(instanceList=('Support-2', ), 
    vector=(0.0, 69.5, 427.5))
model.rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 
    1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Support-1', ))
model.rootAssembly.translate(instanceList=('Support-1', ), 
    vector=(0.0, 69.5, 52.5))
model.rootAssembly.Instance(dependent=ON, name='Impactor-1', 
    part=model.parts['Impactor'])
model.rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 
    1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Impactor-1', ))
model.rootAssembly.translate(instanceList=('Impactor-1', ), 
    vector=(0.0, -69.5, 240.0))
model.ExplicitDynamicsStep(improvedDtMethod=ON, name='Load', 
    previous='Initial', timePeriod=0.05)
model.SmoothStepAmplitude(data=((0.0, 0.0), (0.01, 1.0)), name=
    'Amp-1', timeSpan=STEP)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'Clamp_support1', region=
    model.rootAssembly.instances['Support-1'].sets['Support_RP']
    , u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'Clamp_support_2', region=
    model.rootAssembly.instances['Support-2'].sets['Support_RP']
    , u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'Clamp_impactor', region=
    model.rootAssembly.instances['Impactor-1'].sets['Impactor_RP']
    , u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
model.VelocityBC(amplitude='Amp-1', createStepName='Load', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Load', 
    region=
    model.rootAssembly.instances['Impactor-1'].sets['Impactor_RP']
    , v1=UNSET, v2=700.0, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
model.ContactProperty('Int_prop')
model.interactionProperties['Int_prop'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.05, ), ), temperatureDependency=OFF)
model.interactionProperties['Int_prop'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
model.ContactExp(createStepName='Load', name='Interaction')
model.interactions['Interaction'].includedPairs.setValuesInStep(
    stepName='Load', useAllstar=ON)
model.interactions['Interaction'].contactPropertyAssignments.appendInStep(
    assignments=((GLOBAL, SELF, 'Int_prop'), ), stepName='Load')
model.HistoryOutputRequest(createStepName='Load', name='F-D', 
    numIntervals=100, rebar=EXCLUDE, region=
    model.rootAssembly.allInstances['Impactor-1'].sets['Impactor_RP']
    , sectionPoints=DEFAULT, variables=('U2', 'RF2'))
model.fieldOutputRequests['F-Output-1'].setValues(numIntervals=
    100, variables=('MISES', 'PEEQ', 'U', 'SDV', 'STATUS'))
model.parts['Profile_shell'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=24.0)
model.parts['Profile_shell'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.1)
model.parts['Profile_shell'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=5.0)
model.parts['Profile_shell'].setElementType(elemTypes=(
    ElemType(elemCode=S4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT), ElemType(elemCode=S3, elemLibrary=STANDARD)), 
    regions=(
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#3ffff ]', ), ), ))
model.parts['Profile_shell'].setMeshControls(regions=
    model.parts['Profile_shell'].faces.getSequenceFromMask((
    '[#37efe ]', ), ), technique=STRUCTURED)
model.parts['Profile_shell'].generateMesh()
model.rootAssembly.regenerate()
