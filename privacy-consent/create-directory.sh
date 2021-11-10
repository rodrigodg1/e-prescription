#!/bin/bash



mkdir prescription-files
mkdir encrypted-prescription-files

mkdir -p report/{memory-evaluation,execution-time-evaluation}
mkdir -p separate-prescription-data/{diagnosis,medication,personal_ID}


cd separate-prescription-data/
cd diagnosis/
mkdir encrypted/

cd ..

cd medication/
mkdir encrypted/

cd ..

cd personal_ID/
mkdir encrypted/


