#!/bin/bash
p=$PWD;
cd ..;
tar cvf ./siteBlock.tar ./siteBlock;
gzip -f ./siteBlock.tar;
scp ./siteBlock.tar.gz nemo@nemor.cz:/raid/home/nemo/00_imp_data_rep_nemo/SKOLA2/BI-ADS;
cd $p;
