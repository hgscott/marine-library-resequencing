# Marine Library Resequencing

To use the helper functions, add the package to your $PYTHONPATH.

To find out what is included in $PYTHONPATH, run the following code in python:
```{python}
import sys
print(sys.path)
```

To add the directory to you $PYTHONPATH permanently, add the following line to your ~/.profile file.
```{bash}
export PYTHONPATH=$PYTHONPATH:/projectnb/hfsp/Challenge21/helen/marine-library-resequencing/helper_functions
```

## To Joseline
So, my code sucks, and I would suggest figuring out how to get the gene names for the SNPs using a pre-existing tool. A few I saw that looked promising were:
- vcf-annotater: https://github.com/rpetit3/vcf-annotator
- SnpEff: http://pcingola.github.io/SnpEff/

I've already installed vcf-annotater so the only thing you would have to do is download GenBank files to use it.

To use vcf-annotater:
1. Go to the directory where I cloned it (you can copy this or move it where it is easier): ```cd /projectnb/hfsp/Challenge21/helen/vcf-annotator```
2. Load the python3 module ```module load python3```
3. To test it you can run: ```python3 vcf-annotator.py --version``` which should print out something like "vcf-annotator.py 0.5", or do a test on an example VCF that comes with it by doing ```
3. To test it you can run: ```python3 vcf-annotator.py --version``` which should print out something like "vcf-annotator.py 0.5", or do a test on an example VCF that comes with it by doing ```python3 vcf-annotator.py example-data/example.vcf example-data/example.gb```- heads-up this will print the vcf straight to your screen.

You can probably add the vcf-annotator.py file to your python path so that you can run the file from a different directory without typing the whole path but I haven't done that yet.

The website says that it should be able to do one of our VCFs in about 10 sec. so this will be SO MUCH BETTER than my script. 



