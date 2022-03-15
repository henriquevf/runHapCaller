#runHapCaller.py
#Creates a bash script with the commands required to run GATK's Haplotype Caller
#Developed by Henrique V. Figueiró
#Contact: henriquevf@gmail.com

#Edit the parameter to your needs

import os

path = "/path/to/bam_files" #Path to the bam files
reference = "/path/to/reference" #Path to the reference
dirs = os.listdir(path)

for files in dirs:
    if files.endswith(".bam"):
        print("gatk --java-options \"-Xmx32g\" HaplotypeCaller -R " + reference + " -I " + files + "-O " + files.split(".")[0] + ".g.vcf.gz -ERC GVCF")
