age = int(raw_input("How old are you? "))
height = float(raw_input("How tall are you in m? "))
weight = int(raw_input("How much do you weigh in lbs? "))

print "So, you're %r old, %r m tall and %r lbs heavy." % (age, height, weight)

BMI = (((weight/2.20426)/height)/1.75)
print ("You're BMI is %s" % round(BMI,1))