import sys
#print(1,2,3,4,5,sep=",",end="[end]\n",file=sys.stdout)
#print("str")
#du = input("입력:")
#print(du)
print("{du1} : {du2} - {du3}".format(du1="first",du2="second",du3="third"))
du={"du1":"first","du2":"second","du3":"third"}
print("{0[du1]} {0[du2]}".format(du))