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


CROSS_SECTION = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
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
CROSS_SECTION.FilletByRadius(curve1=CROSS_SECTION.geometry[4], curve2=CROSS_SECTION.geometry[5], nearPoint1=(53.7953643798828, 37.7188262939453), nearPoint2=(64.2597961425781, 28.1494750976562), radius=10.0)
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Cross-section', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Cross-section'].BaseShellExtrude(depth=430.0, sketch=CROSS_SECTION)
del CROSS_SECTION

mdb.models['Model-1'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=XZPLANE)
mdb.models['Model-1'].parts['Cross-section'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=YZPLANE)

mdb.models['Model-1'].parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=mdb.models['Model-1'].parts['Cross-section'].datums[3])
mdb.models['Model-1'].parts['Cross-section'].Mirror(keepOriginal=ON, mirrorPlane=mdb.models['Model-1'].parts['Cross-section'].datums[4])

# CREATE LINE TO DEVIDE INNER-MIDDLE AND INNER-SIDE
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=21.83, name='__profile__', sheetSize=873.29, transform=mdb.models['Model-1'].parts['Cross-section'].MakeSketchTransform(sketchPlane=mdb.models['Model-1'].parts['Cross-section'].faces[10], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[38], sketchOrientation=RIGHT, origin=(0.0, 0.0, 215.0)))
mdb.models['Model-1'].parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, 21.8), point2=(215.0, 21.8))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[14], entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, -21.8), point2=(215.0, -21.8))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].parts['Cross-section'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Cross-section'].faces.getSequenceFromMask(('[#400 ]', ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[38])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(gridSpacing=21.99, name='__profile__', sheetSize=879.93, transform=mdb.models['Model-1'].parts['Cross-section'].MakeSketchTransform(sketchPlane=mdb.models['Model-1'].parts['Cross-section'].faces[6], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[24], sketchOrientation=RIGHT, origin=(-26.975, 37.95, 215.0)))
mdb.models['Model-1'].parts['Cross-section'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, -26.975), point2=(-205.085, -90.925))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-205.085, -90.925), point2=(-215.0, -90.925))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, -90.925), point2=(-224.917, -26.975))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-224.917, -26.975), point2=(-215.0, 36.975))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-215.0, 36.975), point2=(-205.085, 36.975))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-205.085, 36.975), point2=(-215.0, -26.975))
mdb.models['Model-1'].parts['Cross-section'].CutExtrude(flipExtrudeDirection=ON, sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, sketchPlane=mdb.models['Model-1'].parts['Cross-section'].faces[6], sketchPlaneSide=SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['Cross-section'].edges[24])
del mdb.models['Model-1'].sketches['__profile__']
