#write functions here, don't add input('') statements here!
# A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. 
# For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. 
# The tax for the acre assessed at $6000 will be $43.20.Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax

# Functions:

# get_assessment_value with parameter value
#60 percent?
def get_assessment_value(value):
    return value * 0.6
# get_tax_assessed with parameter assessment value
# The property tax is then 72¢ for each $100 of the assessment value.
def get_tax_assessed(assessment_value):
    return (assessment_value / 100) * 72

