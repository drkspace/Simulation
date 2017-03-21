from random import random, randint
import csv


class family_name(object):
	

	def __init__(self, number):
		self.number=number

	

class generation(object):
	
	def __init__(self, number_of_families,chance_to_marry, average_number_of_offspring):
		
		self.number_of_families=number_of_families
		self.families=[]
		self.chance_to_marry=chance_to_marry
		self.average_number_of_offspring=average_number_of_offspring
		

	def generate_family_names(self):
	
		for i in range(self.number_of_families):
		
			self.families.append(family_name(i))	
		
def run_generation(generation):


	couples=[]
	for i in generation.families:
		
		if random() < generation.chance_to_marry:
		
			rand_num = randint(0,len(generation.families)-1)

			if i is not generation.families[rand_num]:

                            couples.append([i,generation.families[rand_num]])

                            del i
			
                            del generation.families[rand_num]

                    
                else:
                    del i

        for i in couples:

            if randint(0,1)==1:
                i[1].number=i[0].number
            else:
                i[0].number=i[1].number

        families=[]
        for i in couples:

            num_of_children=randint(0,2*generation.average_number_of_offspring)

            
            for k in range(num_of_children):
                
                families.append(family_name(i[0].number))

        generation.families=families
            
        return generation

def count(alist,num):

    cnt=0
    for i in alist:
        if i.number==num:
            cnt+=1
    return cnt
	
def find_percentage(alist,number_of_families):

    numbers=[]
    for i in alist:
        if i.number not in numbers:
            numbers.append(i.number)

    print "Number of uniqe last names left: {}".format(len(numbers))
##    numbers.sort()

    percentages=[]
    for i in range(number_of_families):
        percentages.append(count(alist,i)*100/float(len(alist)))

    return percentages
    
            
def print_list(alist):
    for i in alist:
        print "Family {}: {}%".format(i[0],i[1])


def writer(alist,gen_num):
    with open("names.csv","a") as csvfile:
        writer=csv.writer(csvfile,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
        writer.writerow([gen_num,alist])
def main():

        

	max_generations=25

	generations=[]

	gen=generation(10000,0.75,3)

	gen.generate_family_names()

	generations.append(gen)

        with open("names.csv","w") as csvfile:
            awriter=csv.writer(csvfile,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
            awriter.writerow(["Generation",range(gen.number_of_families)])

        writer(find_percentage(gen.families, gen.number_of_families),0)
        for i in range(max_generations):

            print "Running Generation {} of {}".format(i+1,max_generations)
            gen=run_generation(gen)
            generations.append(gen)
            writer(find_percentage(gen.families, gen.number_of_families),i+1)
            
        
        #print_list(find_percentage(gen.families))
        print len(gen.families)


if __name__=="__main__":
    main()

