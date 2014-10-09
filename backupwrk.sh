#!/bin/bash
p=$PWD;
cd ..;
tar cvf ./contBlock.tar ./contBlock;
gzip -f ./contBlock.tar;
scp ./contBlock.tar.gz nemo@nemor.cz:/raid/home/nemo/00_imp_data_rep_nemo/SKOLA2/BI-ADS;
cd $p;
