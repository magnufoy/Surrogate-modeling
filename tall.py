fil = open('haterbodoglimt.txt','w')
fil.write( 'sample,outer_wall_tickness,inside_wall_side_tickness,inside_wall_middle_tickness,height,width,sigma0,youngs')
for i in range(1,3):
   fil.write('\n'+ str(i)+',2.7,2.0,1.5,75.9,127.9,267.1,70000')
fil.close