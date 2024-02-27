# -*- coding: mbcs -*-
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
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, 21.8))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 21.8), point2=(
    0.0, 37.95))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[2], 
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 37.95), point2=
    (53.95, 37.95))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(63.95, 0.0), point2=
    (63.95, 27.95))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], nearPoint1=(
    45.4165077209473, 37.7963790893555), nearPoint2=(64.2001495361328, 
    18.3933868408203), radius=10.0)
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Cross-section', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Cross-section'].BaseShellExtrude(depth=430.0, 
    sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=
    0.0, principalPlane=YZPLANE)
mdb.models['Model-1'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=
    0.0, principalPlane=XZPLANE)
mdb.models['Model-1'].parts['Cross-section'].Mirror(keepOriginal=ON, 
    mirrorPlane=mdb.models['Model-1'].parts['Cross-section'].datums[2])
mdb.models['Model-1'].parts['Cross-section'].Mirror(keepOriginal=ON, 
    mirrorPlane=mdb.models['Model-1'].parts['Cross-section'].datums[3])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=21.83, name='__profile__', 
    sheetSize=873.29, transform=
    mdb.models['Model-1'].parts['Cross-section'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Cross-section'].faces[10], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[5], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['Model-1'].parts['Cross-section'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-21.8, 215.0), 
    point2=(-21.8, -215.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(21.8, 215.0), 
    point2=(21.8, -215.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].parts['Cross-section'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Cross-section'].faces.getSequenceFromMask((
    '[#400 ]', ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[5])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=25.02, name='__profile__', 
    sheetSize=1000.98, transform=
    mdb.models['Model-1'].parts['Cross-section'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Cross-section'].datums[3], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[28], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['Model-1'].parts['Cross-section'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, 0.0), 
    point2=(-205.085, -63.95))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-205.085, -63.95), 
    point2=(-215.0, -63.95))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, -63.95), 
    point2=(-224.915, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-224.915, 0.0), 
    point2=(-215.0, 63.95))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, 63.95), 
    point2=(-205.085, 63.95))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-205.085, 63.95), 
    point2=(-215.0, 0.0))
mdb.models['Model-1'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=
    OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    mdb.models['Model-1'].parts['Cross-section'].datums[3], sketchPlaneSide=
    SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[28])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=25.02, name='__profile__', 
    sheetSize=1000.98, transform=
    mdb.models['Model-1'].parts['Cross-section'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Cross-section'].datums[3], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[41], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['Model-1'].parts['Cross-section'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(212.67, 0.0), 
    point2=(-131.355, 200.16))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(205.085, -63.95), 
    point2=(215.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(215.0, 0.0), point2=
    (205.085, 63.95))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(205.085, 63.95), 
    point2=(215.0, 63.95))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(215.0, 63.95), 
    point2=(224.915, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(224.915, 0.0), 
    point2=(215.0, -63.95))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(215.0, -63.95), 
    point2=(205.085, -63.95))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON
    , sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['Model-1'].parts['Cross-section'].datums[3], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['Model-1'].parts['Cross-section'].edges[41])
del mdb.models['Model-1'].sketches['__profile__']
# Save by ben00 on 2024_02_27-14.56.36; build 2022 2021_09_15-19.57.30 176069
